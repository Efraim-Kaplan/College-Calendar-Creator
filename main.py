from icalendar import Calendar, Event
from datetime import datetime, timedelta
import csv
import re
import os


def read_csv(file_name):
    rows = []
    try:
        with open(file_name, "r") as f:
            csvreader = csv.DictReader(f)
            for row in csvreader:
                rows.append(row)
    except Exception as e:
        print(f"Error reading {file_name}: {e}")
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
    event.add("description", f"Instructor: {course['Instructor']}")
    cal.add_component(event)


def add_full_day_event_to_calendar(cal, date, description, summary):
    event = Event()
    event.add("summary", summary)
    event.add("dtstart", date)
    event.add("dtend", date + timedelta(days=1))
    event.add("description", f"Exception: {description}")
    event["dtstart"].params["VALUE"] = "DATE"  # Set VALUE=DATE for all-day event
    event["dtend"].params["VALUE"] = "DATE"
    cal.add_component(event)


def main():
    courses = read_csv("courses.csv")
    exceptions = read_csv("exceptions.csv")

    for exception in exceptions:
        exception["Date"] = datetime.strptime(exception["Date"], "%m/%d/%Y").date()

    standard_week = create_standard_week(courses)

    # Separate Calendar object for exceptions
    exception_cal = Calendar()

    first_course_start_date_str = courses[0]["Start Date"]
    first_course_end_date_str = courses[0]["End Date"]

    start_date = datetime.strptime(first_course_start_date_str, "%m/%d/%Y").date()
    end_date = datetime.strptime(first_course_end_date_str, "%m/%d/%Y").date()

    delta = timedelta(days=1)

    current_date = start_date

    course_cals = {}  # Dictionary to hold Calendar objects for each course

    while current_date <= end_date:
        exception_day = next(
            (item for item in exceptions if item["Date"] == current_date), None
        )

        if exception_day:
            add_full_day_event_to_calendar(
                exception_cal,
                current_date,
                exception_day["Description"],
                exception_day["Type"]
            )
        else:
            day_abbr = current_date.strftime("%a")
            if day_abbr in standard_week:
                for course in standard_week[day_abbr]:
                    if course['Course Code'] not in course_cals:
                        course_cals[course['Course Code']] = Calendar()

                    add_event_to_calendar(course_cals[course['Course Code']], course, current_date)

        current_date += delta

    # Define the output folder name
    output_folder = "output"

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Save the individual course calendars
    for course_code, cal in course_cals.items():
        with open(os.path.join(output_folder, f"{course_code}_calendar.ics"), "wb") as f:
            f.write(cal.to_ical())
        print(f"Calendar for {course_code} saved in {output_folder}.")

    # Save the exceptions calendar
    with open(os.path.join(output_folder, "exceptions_calendar.ics"), "wb") as f:
        f.write(exception_cal.to_ical())
    print(f"Exceptions calendar saved in {output_folder}.")

if __name__ == "__main__":
    main()