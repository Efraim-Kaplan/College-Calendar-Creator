# Calendar Creator README

## Overview
The Calendar Creator is a robust Python application tailored for educational institutions to streamline the creation of iCalendar (.ics) files, encapsulating comprehensive course schedules and exception dates. The application adeptly manages standard course events, exceptions such as holidays, and conversion days where a different schedule is to be followed.

## System Requirements
- Python 3.x
- `icalendar` Python library

## Installation
To ensure a smooth installation process, verify the presence of Python 3.x on your system. If not already installed, acquire the required `icalendar` library using the following command:

```bash
pip install icalendar
```

## Usage Instructions
1. Populate your CSV files, `courses.csv` for the course schedules and `exceptions.csv` for exception dates, adhering to the predefined formats.
2. Station these files in the same directory as the script for optimal performance.
3. Initiate the script execution using:

```bash
python calendar_creator.py
```

4. The application meticulously generates the `output` directory, which houses the collective `combined_calendar.ics` file.

## Input Data Structure

### Course Schedule CSV (`courses.csv`)
Structure the course schedule CSV with the following column headers:

- Course Code
- Course Title
- Start Date (in MM/DD/YYYY format)
- End Date (in MM/DD/YYYY format)
- Days (full weekdays such as Monday, Tuesday)
- Start Time (in HH:MM AM/PM format)
- End Time (in HH:MM AM/PM format)
- Instructor
- Room

Representative Example:
```
| Course Code | Course Title | Start Date  | End Date    | Days                  | Start Time | End Time   | Instructor | Room |
|-------------|--------------|-------------|-------------|-----------------------|------------|------------|------------|------|
| MATH101     | Calculus I   | 01/15/2023  | 05/25/2023  | Monday, Wednesday, Friday | 09:00 AM   | 10:30 AM   | Jane Doe   | 101  |
```

### Exception Dates CSV (`exceptions.csv`)
The exception dates CSV should encapsulate deviations such as holidays or special schedule events, under the following headers:

- Dates (either a single MM/DD/YYYY entry or a range denoted by MM/DD/YYYY-MM/DD/YYYY)
- Description (for full-day exceptions, a simple description suffices. When "(conversion)" appears, the script interprets this as an instruction for a schedule conversion to a specified day)

Exemplary Entry:
```
Dates,Description
07/04/2023,Independence Day
01/28/2023,Monday Schedule (Conversion)
```

## Feature Highlights
- Logs are custom-tailored for various verbosity levels, accessible within `calendar_creator.log`.
- Support for multiple dates within exception entries.
- Implements day conversion (e.g., a Tuesday adopting a Monday's schedule).
- Introduces full-day exceptions when required.
- Condenses all individual course and exception events into a singular, neat iCalendar file.

## Output Synopsis
Upon culmination, the application dispenses the output in the form of:
- `output/combined_calendar.ics`: The synthesized iCalendar file embedding both course occurrences and exceptions.

## Logging Insights
The application diligently records a broad gamut of messages, such as informational, debugging, and errors encountered during its operational lifecycle, into the `calendar_creator.log`.

## Functional Descriptors
- `read_csv(file_name)`: Intakes a CSV file, returning an assembly of row-wise dictionaries.
- `create_standard_week(courses)`: Engineering a day-to-course mapping dictionary from the input courses array.
- `add_event_to_calendar(cal, course, date)`: Methodology for registering a singular course event onto the calendar.
- `add_full_day_event_to_calendar(cal, date, description, summary)`: The apparatus for instituting a full-day exception event.

**Collaboration Protocol**

Contributions to the Calendar Creator project are welcome through pull requests and issue reporting.

**Communication Channel**

For inquiries regarding operational matters, innovative propositions, or potential contributions, kindly contact the repository maintainer. As an alternative, the project's issue tracker is available for more extensive dialogues.

**Licensing Details**

The Calendar Creator project is disseminated under an open-source license exclusively for personal utilization. Commercial entities are authorized to employ, adapt, and disseminate the software solely with explicit consent from the author.

**Disclaimer**

The Calendar Creator software is provided on an "as is" basis, without any form of warranty or assurance, either expressed or implied. Users are advised to perform comprehensive testing prior to deploying or relying upon the software in any critical capacity. Under no circumstances shall the authors be liable for any damages, losses, or liabilities incurred as a result of using or the inability to use the software.