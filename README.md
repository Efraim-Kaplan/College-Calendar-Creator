# Academic Calendar Generator Documentation

## Table of Contents

1. [Overview](#overview)
2. [Dependencies](#dependencies)
3. [Input Files](#input-files)
4. [Script Structure and Functions](#script-structure-and-functions)
5. [Running the Script](#running-the-script)
6. [Output](#output)
7. [Logging](#logging)

## Overview

This Python script generates a comprehensive academic calendar in iCal format (.ics), suitable for importing into various calendar applications. It efficiently processes course schedules and exceptions (like holidays or special events), handling complex scenarios like date ranges and schedule conversions.

## Dependencies

- `icalendar`: For creating iCal format files.
- `datetime`: For date and time operations.
- `csv`: To read CSV input files.
- `re`: For regular expression operations.
- `os`: For directory and file operations.
- `logging`: For logging script activities and issues.

## Input Files

### `courses.csv`

Contains details for each course with columns like `Course Code`, `Course Title`, `Days`, `Start Time`, `End Time`, `Start Date`, `End Date`, `Room`, and `Instructor`.

### `exceptions.csv`

Lists exceptions with `Type`, `Dates` (single or range), and `Description`. Conversion days should include the target day within the description (e.g., "Conversion to Monday schedule").

## Script Structure and Functions

- **`read_csv(file_name)`:** Reads CSV files and processes date ranges in `exceptions.csv`.
- **`create_standard_week(courses)`:** Forms a standard week schedule from course data.
- **`add_event_to_calendar(cal, course, date)`:** Adds individual course events to the calendar.
- **`add_full_day_event_to_calendar(cal, date, description, summary)`:** Adds full-day events for exceptions.
- **`main()`:** Orchestrates the calendar creation process, handling standard courses and exceptions, including conversion days, and outputs the final combined calendar.

### Calendar Creation Process

1. **Data Import:** Reads `courses.csv` and `exceptions.csv`.
2. **Standard Week Setup:** Forms a weekly schedule template.
3. **Exception Handling:** Processes exceptions, including conversion days.
4. **Calendar Assembly:** Compiles individual course calendars and the exceptions calendar into a combined calendar.
5. **File Output:** Saves the combined calendar in iCal format.

## Running the Script

To execute the script, run:

```bash
python your_script_name.py
```

## Output

- The script generates an `output` directory containing the `combined_calendar.ics` file, which integrates all course schedules and exceptions.
- Individual calendars for each course are also created and integrated into the combined calendar.

## Logging

- The script logs all major steps and issues in `calendar_creator.log`, aiding in troubleshooting and ensuring transparency in the process.

This documentation should provide clear guidance on the usage and inner workings of the Academic Calendar Generator script. Feel free to reach out if you encounter any issues or require further assistance.