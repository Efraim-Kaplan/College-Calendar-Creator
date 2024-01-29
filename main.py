from icalendar import Calendar, Event
from datetime import datetime, timedelta
import csv
import re
import os
import logging


logging.basicConfig(filename='calendar_creator.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def read_csv(file_name):
    rows = []
    try:
        with open(file_name, "r") as f:
            csvreader = csv.DictReader(f)
            for row in csvreader:
                if 'exceptions.csv' in file_name:
                    if '-' in row['Dates']:
                        start_date, end_date = row['Dates'].split('-')
                        start_date = datetime.strptime(start_date.strip(), "%m/%d/%Y").date()
                        end_date = datetime.strptime(end_date.strip(), "%m/%d/%Y").date()
                        delta = timedelta(days=1)
                        while start_date <= end_date:
                            row_copy = row.copy()
                            row_copy['Date'] = start_date
                            rows.append(row_copy)
                            start_date += delta
                    else:
                        row['Date'] = datetime.strptime(row['Dates'].strip(), "%m/%d/%Y").date()
                        rows.append(row)
                else:
                    rows.append(row)
    except Exception as e:
        logging.error(f"Error reading {file_name}: {e}")
    return rows

def create_standard_week(courses):
    standard_week = {}
    for course in courses:
        days = course["Days"].split(", ")
        for day in days:
            day_abbr = day[:3]
            if day_abbr not in standard_week:
                standard_week[day_abbr] = []
            standard_week[day_abbr].append(course)
    return standard_week


def add_event_to_calendar(cal, course, date):
    event = Event()
    event.add("summary", f"{course['Course Code']} - {course['Course Title']}")
    event.add(
        "dtstart",
        datetime.combine(
            date, datetime.strptime(course["Start Time"], "%I:%M %p").time()
        ),
    )
    event.add(
        "dtend",
        datetime.combine(
            date, datetime.strptime(course["End Time"], "%I:%M %p").time()
        ),
    )
    event.add("location", course["Room"])
    if (course["Zoom Link"] != ""):
        event.add("description", f"Instructor: {course['Instructor']}\nZoom Link: {course['Zoom Link']}")
        logging.debug(f"Zoom link added to {course['Course Code']} event.")
    else:
        event.add("description", f"Instructor: {course['Instructor']}")
        logging.debug(f"No Zoom link found for {course['Course Code']} event.")
    cal.add_component(event)

def add_full_day_event_to_calendar(cal, date, description, summary):
    event = Event()
    event.add("summary", summary)
    event.add("dtstart", date)
    event.add("dtend", date + timedelta(days=1))
    event.add("description", f"Exception: {description}")
    event["dtstart"].params["VALUE"] = "DATE"
    event["dtend"].params["VALUE"] = "DATE"
    cal.add_component(event)

def main():
    courses = read_csv("courses.csv")
    exceptions = read_csv("exceptions.csv")

    standard_week = create_standard_week(courses)

    exception_cal = Calendar()

    start_dates = [datetime.strptime(course["Start Date"], "%m/%d/%Y").date() for course in courses]
    end_dates = [datetime.strptime(course["End Date"], "%m/%d/%Y").date() for course in courses]

    start_date = min(start_dates)
    end_date = max(end_dates)

    delta = timedelta(days=1)

    current_date = start_date

    course_cals = {}

    while current_date <= end_date:
        exception_day = next(
            (item for item in exceptions if item["Date"] == current_date), None
        )

        current_day_abbr = current_date.strftime("%a")

        if exception_day:
            if '(Conversion)' in exception_day["Description"]:
                logging.debug(f"Conversion day found: {current_date}")
                target_day_match = re.search(r'(\bMonday\b|\bTuesday\b|\bWednesday\b|\bThursday\b|\bFriday\b|\bSaturday\b|\bSunday\b) schedule', exception_day["Description"])
                logging.debug(f"Target day match: {target_day_match}")
                if target_day_match:
                    target_day_full = target_day_match.group()
                    target_day_abbr = target_day_full[:3]
                    logging.debug(f"Target day abbreviation: {target_day_abbr}")
                    if target_day_abbr in standard_week:
                        logging.debug(f"Using schedule of target day: {target_day_abbr}")
                        for course in standard_week[target_day_abbr]:
                            if course['Course Code'] not in course_cals:
                                course_cals[course['Course Code']] = Calendar()
                            add_event_to_calendar(course_cals[course['Course Code']], course, current_date)
                            add_full_day_event_to_calendar(
                                exception_cal,
                                current_date,
                                exception_day["Description"],
                                exception_day["Description"]
                            )
                    else:
                        logging.debug(f"No schedule found for target day: {target_day_abbr}")
                    logging.debug(f"Conversion day processed: {current_date}")

            else:
                add_full_day_event_to_calendar(
                    exception_cal,
                    current_date,
                    exception_day["Description"],
                    exception_day["Description"]
                )
        elif current_day_abbr in standard_week:
            for course in standard_week[current_day_abbr]:
                if course['Course Code'] not in course_cals:
                    course_cals[course['Course Code']] = Calendar()
                add_event_to_calendar(course_cals[course['Course Code']], course, current_date)

        current_date += delta

    output_folder = "output"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    combined_cal = Calendar()

    for course_code, cal in course_cals.items():
        for component in cal.walk():
            combined_cal.add_component(component)
        logging.debug(f"Calendar for {course_code} added to combined calendar.")

    for component in exception_cal.walk():
        combined_cal.add_component(component)
    logging.debug("Exceptions calendar added to combined calendar.")

    with open(os.path.join(output_folder, "combined_calendar.ics"), "wb") as f:
        f.write(combined_cal.to_ical())
    logging.debug(f"Combined calendar saved in {output_folder}.")

if __name__ == "__main__":
    main()
