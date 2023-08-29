# Academic Calendar Generator

## Table of Contents

1. [Overview](#overview)
2. [Dependencies](#dependencies)
3. [Input Files](#input-files)
    - [courses.csv](#coursescsv)
    - [exceptions.csv](#exceptionscsv)
4. [How it Works](#how-it-works)
5. [Running the Script](#running-the-script)

## Overview

This Python script generates an academic calendar in iCal format (.ics), which can be imported into various calendar applications. The script takes two CSV files as input: one for the course schedule and another for exceptions like holidays or special events.

## Dependencies

- `icalendar`: iCal file generation.
- `datetime`: Date-time manipulation.
- `csv`: Reading CSV files.
- `re`: Regular expression operations.

## Input Files

### `courses.csv`

This CSV should contain course details with the following columns:

- `Course Code`: e.g., "MATH101"
- `Course Title`: e.g., "Basic Mathematics"
- `Days`: e.g., "Mon, Wed"
- `Start Time`: e.g., "9:00 AM"
- `End Time`: e.g., "10:30 AM"
- `Start Date`: e.g., "1/10/2023"
- `End Date`: e.g., "5/20/2023"
- `Room`: e.g., "Room 101"
- `Instructor`: e.g., "John Doe"

### `exceptions.csv`

This CSV should list exception days:

- `Type`: e.g., "Closed", "Conversion"
- `Date`: e.g., "11/25/2023"
- `Description`: e.g., "Thanksgiving"

#### Formatting Conversion Days

For conversion days, the description must contain the target day to which the schedule will convert, encapsulated within parentheses. For example, for a conversion to a Monday schedule, the description might be "Conversion (Mon)".

## How it Works

1. **Data Import**: Reads both `courses.csv` and `exceptions.csv`.
2. **Week Setup**: Forms a standard week schedule.
3. **Calendar Loop**: Iterates through each day from start to end.
    - Checks for exceptions.
    - Processes exceptions or adds scheduled courses.
4. **iCal Export**: Outputs `your_calendar.ics`.

### Parsing Details

- **Conversion Days**: The script uses regular expressions to look for a three-letter day abbreviation in the "Description" field of the `exceptions.csv` for conversion days. Make sure to format these correctly for accurate conversions.

## Running the Script

To run the script, use the following command:

```bash
python your_script_name.py
```