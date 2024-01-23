# Calendar Creator README

## Overview
Calendar Creator is a Python application that generates an iCalendar (.ics) file from course schedules and exception dates provided in CSV format. It is designed for educational institutions to ease the process of calendar event management for course schedules, including handling exceptions such as holidays or special events.

## System Requirements
- Python 3.x
- `icalendar` library

## Installation
Ensure that Python 3.x is installed on your system. If you do not have the `icalendar` library installed, you can install it using pip:

```bash
pip install icalendar
```

## Usage
1. Prepare your CSV files: `courses.csv` and `exceptions.csv`. Place them in the same directory as the script.
2. Run the script:
```bash
python calendar_creator.py
```
3. The script will generate an `output` directory that contains the `combined_calendar.ics` file.

## Input CSV File Format

### Courses CSV (`courses.csv`)
This CSV file should contain the course schedule with the following headers:

- Course Code
- Course Title
- Start Date (MM/DD/YYYY)
- End Date (MM/DD/YYYY)
- Days (e.g., Monday, Tuesday, Wednesday)
- Start Time (HH:MM AM/PM)
- End Time (HH:MM AM/PM)
- Instructor
- Room

Example:
```
| Course Code | Course Title | Start Date  | End Date    | Days       | Start Time | End Time   | Instructor | Room |
|-------------|--------------|-------------|-------------|------------|------------|------------|------------|------|
| MATH101     | Calculus I   | 01/15/2023  | 05/25/2023  | Monday, Wednesday, Friday   | 09:00 AM   | 10:30 AM   | Jane Doe   | 101  |
```

### Exceptions CSV (`exceptions.csv`)
This CSV file should contain exception dates such as holidays or non-standard class schedules with the following headers:

- Dates (can be a single date MM/DD/YYYY or a range MM/DD/YYYY-MM/DD/YYYY)
- Description (unless (conversion) is specified, the script will create a full-day exception event, otherwise it will create a single event for each course on the specified date(s) with the course schedule converted to the specified day)

Example:
```
Dates,Description
07/04/2023,Independence Day
1/28/2023, Monday Schedule (Conversion)
```

## Features
- Customizable logging (found in `calendar_creator.log`).
- Ability to handle a range of dates for exceptions.
- Day conversion ability (e.g., Tuesday schedule on a Monday).
- Generation of full-day exceptions.
- Consolidation of all course and exception events into a single iCalendar file.

## Output
The script will generate the following output:
- `output/combined_calendar.ics`: A combined iCalendar file containing all the course events and exceptions.

## Logging
The script logs informational and debugging messages, including errors during processing, to `calendar_creator.log`.

## Functions
- `read_csv(file_name)`: Reads the CSV file and returns a list of dictionaries, one for each row.
- `create_standard_week(courses)`: Creates a dictionary mapping weekdays to course schedules.
- `add_event_to_calendar(cal, course, date)`: Adds a single course event to the calendar.
- `add_full_day_event_to_calendar(cal, date, description, summary)`: Adds a full-day exception event.

## Contributing
To contribute to this project, please create a pull request or open an issue on the project's repository. Contributions should follow good coding practices and include appropriate documentation updates.

## Contact
For issues, suggestions, or contributions, please contact the repository maintainer or use the issue tracker associated with the project.

## License
This project is licensed under the terms of the MIT license.

## Disclaimer
This software is provided “as is”, without warranty of any kind. Users should test the software thoroughly before relying on it. The author(s) shall not be liable for any damages resulting from the use of the software.