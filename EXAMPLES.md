# School Timetable Application - Usage Examples

This document provides detailed examples of how to use the school timetable application.

## Quick Start

### Run Demo Mode
```bash
python3 main.py --demo
```

This loads sample data and displays example timetables for a class and a teacher.

### Run Interactive Mode
```bash
python3 main.py
```

## Example Workflows

### Workflow 1: Build a Complete Timetable from Scratch

1. **Start the application**
   ```bash
   python3 main.py
   ```

2. **Add Subjects** (Menu Option 1)
   - Add Subject → Code: MATH, Name: Mathematics
   - Add Subject → Code: ENG, Name: English
   - Add Subject → Code: SCI, Name: Science

3. **Add Teachers** (Menu Option 2)
   - Add Teacher → ID: T001, Name: Mr. Smith, Subjects: MATH
   - Add Teacher → ID: T002, Name: Ms. Johnson, Subjects: ENG
   - Add Teacher → ID: T003, Name: Dr. Brown, Subjects: SCI

4. **Add Classes** (Menu Option 3)
   - Add Class → ID: C1, Name: Grade 9A, Students: 25
   - Add Class → ID: C2, Name: Grade 9B, Students: 28

5. **Build Timetable Entries** (Menu Option 4)
   - Class: C1, Day: 0 (Monday), Period: 1, Subject: MATH, Teacher: T001, Room: R101
   - Class: C1, Day: 0 (Monday), Period: 2, Subject: ENG, Teacher: T002, Room: R101
   - Class: C2, Day: 0 (Monday), Period: 1, Subject: ENG, Teacher: T002, Room: R102
   - Class: C2, Day: 0 (Monday), Period: 2, Subject: MATH, Teacher: T001, Room: R102

6. **View Timetables** (Menu Option 5)
   - View Class Timetable → Enter class ID: C1
   - View Teacher Timetable → Enter teacher ID: T001

7. **Validate** (Menu Option 7)
   - Check for any scheduling conflicts

### Workflow 2: Using Sample Data for Quick Testing

1. **Start the application**
   ```bash
   python3 main.py
   ```

2. **Load Sample Data** (Menu Option 8)
   - This loads 5 subjects, 5 teachers, 3 classes, and 7 timetable entries

3. **View Timetables** (Menu Option 5)
   - View any class: C1, C2, or C3
   - View any teacher: T001, T002, T003, T004, or T005

### Workflow 3: Testing Conflict Detection

1. **Load sample data** (Menu Option 8)

2. **Try to add a conflicting entry** (Menu Option 4)
   - Class: C1, Day: 0 (Monday), Period: 1, Subject: SCI, Teacher: T003, Room: LAB1
   - Result: Conflict detected! Class C1 is already scheduled at this time

3. **Try another conflict**
   - Class: C3, Day: 0 (Monday), Period: 1, Subject: MATH, Teacher: T001, Room: R201
   - Result: Conflict detected! Teacher T001 is already scheduled at this time

## Command Reference

### Main Menu Options

| Option | Function | Description |
|--------|----------|-------------|
| 1 | Manage Subjects | Add new subjects or list existing ones |
| 2 | Manage Teachers | Add new teachers or list existing ones |
| 3 | Manage Classes | Add new classes or list existing ones |
| 4 | Build Timetable | Add new timetable entries with conflict checking |
| 5 | View Timetables | View timetables by class, teacher, or all entries |
| 6 | Edit Timetable | Remove timetable entries |
| 7 | Validate Timetable | Check for any scheduling conflicts |
| 8 | Load Sample Data | Load pre-defined sample data for testing |
| 9 | Exit | Exit the application |

### Day of Week Values

| Value | Day |
|-------|-----|
| 0 | Monday |
| 1 | Tuesday |
| 2 | Wednesday |
| 3 | Thursday |
| 4 | Friday |

### Default Time Slots (Periods)

| Period | Start Time | End Time |
|--------|------------|----------|
| 1 | 08:00 | 08:50 |
| 2 | 09:00 | 09:50 |
| 3 | 10:00 | 10:50 |
| 4 | 11:00 | 11:50 |
| 5 | 12:00 | 12:50 |
| 6 | 13:00 | 13:50 |
| 7 | 14:00 | 14:50 |

## Programmatic Usage

You can also use the timetable module directly in your Python code:

```python
from timetable import Timetable, Subject, Teacher, SchoolClass, TimeSlot, TimetableEntry, DayOfWeek

# Create a timetable
tt = Timetable()

# Add a subject
tt.add_subject(Subject("MATH", "Mathematics"))

# Add a teacher
tt.add_teacher(Teacher("T001", "Mr. Smith", ["MATH"]))

# Add a class
tt.add_class(SchoolClass("C1", "Grade 9A", 25))

# Add a time slot
tt.add_time_slot(TimeSlot(1, "08:00", "08:50"))

# Create and add an entry
entry = TimetableEntry(
    DayOfWeek.MONDAY,
    tt.time_slots[0],
    "C1",
    "MATH",
    "T001",
    "R101"
)

# Add entry (returns True if successful, False if conflict)
if tt.add_entry(entry):
    print("Entry added successfully!")
else:
    print("Conflict detected!")

# Display timetable
print(tt.display_class_timetable("C1"))

# Validate timetable
errors = tt.validate()
if not errors:
    print("Timetable is valid!")
```

## Tips and Best Practices

1. **Always load sample data first** when exploring the application to see how it works

2. **Use meaningful IDs** for teachers and classes (e.g., T001, C1) to make timetables easier to read

3. **Validate regularly** after adding multiple entries to catch conflicts early

4. **Room assignments are optional** - you can leave them blank if not needed

5. **Plan your schedule** before adding entries to minimize conflicts

6. **Start with fewer entries** and gradually build up the complete timetable

## Troubleshooting

### "Conflict detected" Error
This means either:
- The teacher is already scheduled at that time
- The class is already scheduled at that time

**Solution**: Choose a different time slot, teacher, or class.

### "Invalid input" Error
This means you entered data in the wrong format.

**Solution**: 
- Check that numeric inputs (day, period) are valid numbers
- Verify that IDs match existing subjects/teachers/classes

### No output when viewing timetables
This means there are no entries for that class or teacher yet.

**Solution**: Add some timetable entries first (Option 4) or load sample data (Option 8).

## Advanced Features

### Validation
The validate function checks for:
- Teacher conflicts (same teacher scheduled in multiple places at once)
- Class conflicts (same class scheduled for multiple subjects at once)

### Querying
You can query entries by:
- Class ID: `get_entries_for_class(class_id)`
- Teacher ID: `get_entries_for_teacher(teacher_id)`
- Day: `get_entries_for_day(day)`

### Display Formats
- **Class Timetable**: Shows all subjects for a class organized by day
- **Teacher Timetable**: Shows all classes taught by a teacher organized by day
- **All Entries**: Shows raw list of all timetable entries

## Support

For issues or questions, please open an issue on the GitHub repository.
