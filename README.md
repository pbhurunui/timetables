# School Timetable Builder

A Python application for building and editing school timetables with automatic conflict detection.

## Features

- **Build Timetables**: Create comprehensive school timetables with subjects, teachers, classes, and time slots
- **Edit Timetables**: Modify and remove timetable entries as needed
- **Conflict Detection**: Automatically prevents scheduling conflicts for teachers and classes
- **Multiple Views**: View timetables by class, teacher, or see all entries
- **Validation**: Validate complete timetables to ensure no conflicts exist
- **Interactive CLI**: User-friendly command-line interface for all operations
- **Sample Data**: Quick start with pre-loaded sample data

## Installation

1. Clone the repository:
```bash
git clone https://github.com/pbhurunui/timetables.git
cd timetables
```

2. The application requires Python 3.7 or higher. No additional dependencies are needed.

## Usage

### Interactive Mode

Run the application in interactive mode to build and edit timetables:

```bash
python3 main.py
```

This will launch an interactive menu where you can:
1. Manage subjects (add and list)
2. Manage teachers (add and list)
3. Manage classes (add and list)
4. Build timetable entries
5. View timetables (by class, teacher, or all entries)
6. Edit timetable entries
7. Validate the timetable for conflicts
8. Load sample data for demonstration

### Demo Mode

To see a quick demonstration with pre-loaded sample data:

```bash
python3 main.py --demo
```

This will load sample subjects, teachers, classes, and timetable entries, then display example timetables.

## Core Concepts

### Subjects
Subjects represent the courses taught at the school (e.g., Mathematics, English, Science).

### Teachers
Teachers are assigned to teach specific subjects and have unique IDs.

### Classes
Classes (or grades) represent groups of students (e.g., Grade 9A, Grade 10B).

### Time Slots
Time slots define the periods in a school day with start and end times.

### Timetable Entries
Each entry represents a scheduled class session with:
- Day of the week (Monday-Friday)
- Time slot (period)
- Class
- Subject
- Teacher
- Room (optional)

### Conflict Detection
The application automatically prevents:
- **Teacher conflicts**: A teacher cannot be scheduled in two places at the same time
- **Class conflicts**: A class cannot have two subjects scheduled simultaneously

## Example Workflow

1. **Start the application**:
   ```bash
   python3 main.py
   ```

2. **Load sample data** (option 8) for quick start, or manually:
   - Add subjects (option 1)
   - Add teachers (option 2)
   - Add classes (option 3)

3. **Build timetable** (option 4):
   - Select class, day, period, subject, teacher, and room
   - The system will check for conflicts before adding

4. **View timetables** (option 5):
   - View by class to see a student's schedule
   - View by teacher to see a teacher's schedule

5. **Validate** (option 7):
   - Check the entire timetable for any conflicts

## Running Tests

The application includes comprehensive unit tests:

```bash
python3 -m unittest test_timetable.py -v
```

All tests should pass, validating:
- Data model creation
- Timetable operations (add, remove, query)
- Conflict detection
- Display functionality
- Validation

## Project Structure

```
timetables/
├── README.md           # This file
├── main.py            # CLI application entry point
├── timetable.py       # Core timetable data models and logic
├── test_timetable.py  # Unit tests
├── requirements.txt   # Python dependencies (none currently)
└── .gitignore        # Git ignore file
```

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is open source and available for educational purposes.
