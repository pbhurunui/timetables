#!/usr/bin/env python3
"""
School Timetable Application CLI
Command-line interface for building and editing school timetables.
"""

import sys
from typing import Optional
from timetable import (
    Timetable, Subject, Teacher, SchoolClass, 
    TimeSlot, TimetableEntry, DayOfWeek
)


class TimetableCLI:
    """Command-line interface for the timetable application."""
    
    def __init__(self):
        self.timetable = Timetable()
        self.setup_default_time_slots()
        
    def setup_default_time_slots(self):
        """Setup default time slots for a school day."""
        default_slots = [
            TimeSlot(1, "08:00", "08:50"),
            TimeSlot(2, "09:00", "09:50"),
            TimeSlot(3, "10:00", "10:50"),
            TimeSlot(4, "11:00", "11:50"),
            TimeSlot(5, "12:00", "12:50"),
            TimeSlot(6, "13:00", "13:50"),
            TimeSlot(7, "14:00", "14:50"),
        ]
        for slot in default_slots:
            self.timetable.add_time_slot(slot)
            
    def run(self):
        """Main loop for the CLI."""
        print("=" * 70)
        print("School Timetable Builder")
        print("=" * 70)
        
        while True:
            print("\nMain Menu:")
            print("1. Manage Subjects")
            print("2. Manage Teachers")
            print("3. Manage Classes")
            print("4. Build Timetable")
            print("5. View Timetables")
            print("6. Edit Timetable")
            print("7. Validate Timetable")
            print("8. Load Sample Data")
            print("9. Exit")
            
            choice = input("\nEnter your choice (1-9): ").strip()
            
            if choice == "1":
                self.manage_subjects()
            elif choice == "2":
                self.manage_teachers()
            elif choice == "3":
                self.manage_classes()
            elif choice == "4":
                self.build_timetable()
            elif choice == "5":
                self.view_timetables()
            elif choice == "6":
                self.edit_timetable()
            elif choice == "7":
                self.validate_timetable()
            elif choice == "8":
                self.load_sample_data()
            elif choice == "9":
                print("\nExiting... Goodbye!")
                break
            else:
                print("\nInvalid choice. Please try again.")
                
    def manage_subjects(self):
        """Manage subjects menu."""
        while True:
            print("\n--- Manage Subjects ---")
            print("1. Add Subject")
            print("2. List Subjects")
            print("3. Back to Main Menu")
            
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if choice == "1":
                code = input("Enter subject code: ").strip()
                name = input("Enter subject name: ").strip()
                if code and name:
                    self.timetable.add_subject(Subject(code, name))
                    print(f"Subject '{name}' added successfully!")
                else:
                    print("Invalid input. Both code and name are required.")
            elif choice == "2":
                if self.timetable.subjects:
                    print("\nSubjects:")
                    for subject in self.timetable.subjects.values():
                        print(f"  - {subject}")
                else:
                    print("\nNo subjects added yet.")
            elif choice == "3":
                break
            else:
                print("Invalid choice.")
                
    def manage_teachers(self):
        """Manage teachers menu."""
        while True:
            print("\n--- Manage Teachers ---")
            print("1. Add Teacher")
            print("2. List Teachers")
            print("3. Back to Main Menu")
            
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if choice == "1":
                teacher_id = input("Enter teacher ID: ").strip()
                name = input("Enter teacher name: ").strip()
                if teacher_id and name:
                    subjects = input("Enter subject codes (comma-separated, optional): ").strip()
                    subject_list = [s.strip() for s in subjects.split(",")] if subjects else []
                    self.timetable.add_teacher(Teacher(teacher_id, name, subject_list))
                    print(f"Teacher '{name}' added successfully!")
                else:
                    print("Invalid input. Both ID and name are required.")
            elif choice == "2":
                if self.timetable.teachers:
                    print("\nTeachers:")
                    for teacher in self.timetable.teachers.values():
                        print(f"  - {teacher}")
                else:
                    print("\nNo teachers added yet.")
            elif choice == "3":
                break
            else:
                print("Invalid choice.")
                
    def manage_classes(self):
        """Manage classes menu."""
        while True:
            print("\n--- Manage Classes ---")
            print("1. Add Class")
            print("2. List Classes")
            print("3. Back to Main Menu")
            
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if choice == "1":
                class_id = input("Enter class ID: ").strip()
                name = input("Enter class name: ").strip()
                if class_id and name:
                    try:
                        students = int(input("Enter number of students: ").strip() or "0")
                        self.timetable.add_class(SchoolClass(class_id, name, students))
                        print(f"Class '{name}' added successfully!")
                    except ValueError:
                        print("Invalid number of students.")
                else:
                    print("Invalid input. Both ID and name are required.")
            elif choice == "2":
                if self.timetable.classes:
                    print("\nClasses:")
                    for school_class in self.timetable.classes.values():
                        print(f"  - {school_class}")
                else:
                    print("\nNo classes added yet.")
            elif choice == "3":
                break
            else:
                print("Invalid choice.")
                
    def build_timetable(self):
        """Build timetable entries."""
        print("\n--- Build Timetable Entry ---")
        
        if not self.timetable.classes:
            print("No classes available. Please add classes first.")
            return
        if not self.timetable.subjects:
            print("No subjects available. Please add subjects first.")
            return
        if not self.timetable.teachers:
            print("No teachers available. Please add teachers first.")
            return
            
        # Display options
        print("\nAvailable Classes:")
        for class_id, school_class in self.timetable.classes.items():
            print(f"  {class_id}: {school_class.name}")
            
        print("\nAvailable Days:")
        for day in DayOfWeek:
            print(f"  {day.value}: {day.name}")
            
        print("\nAvailable Periods:")
        for slot in self.timetable.time_slots:
            print(f"  {slot.period}: {slot.start_time}-{slot.end_time}")
            
        print("\nAvailable Subjects:")
        for code, subject in self.timetable.subjects.items():
            print(f"  {code}: {subject.name}")
            
        print("\nAvailable Teachers:")
        for teacher_id, teacher in self.timetable.teachers.items():
            print(f"  {teacher_id}: {teacher.name}")
            
        # Get input
        try:
            class_id = input("\nEnter class ID: ").strip()
            if class_id not in self.timetable.classes:
                print("Invalid class ID.")
                return
                
            day_num = int(input("Enter day (0-4): ").strip())
            day = DayOfWeek(day_num)
            
            period = int(input("Enter period (1-7): ").strip())
            time_slot = next((s for s in self.timetable.time_slots if s.period == period), None)
            if not time_slot:
                print("Invalid period.")
                return
                
            subject_code = input("Enter subject code: ").strip()
            if subject_code not in self.timetable.subjects:
                print("Invalid subject code.")
                return
                
            teacher_id = input("Enter teacher ID: ").strip()
            if teacher_id not in self.timetable.teachers:
                print("Invalid teacher ID.")
                return
                
            room = input("Enter room (optional): ").strip() or None
            
            # Create and add entry
            entry = TimetableEntry(day, time_slot, class_id, subject_code, teacher_id, room)
            
            if self.timetable.add_entry(entry):
                print("\nTimetable entry added successfully!")
            else:
                print("\nCannot add entry: Conflict detected!")
                print("Either the teacher or the class is already scheduled at this time.")
                
        except ValueError as e:
            print(f"Invalid input: {e}")
            
    def view_timetables(self):
        """View timetables menu."""
        while True:
            print("\n--- View Timetables ---")
            print("1. View Class Timetable")
            print("2. View Teacher Timetable")
            print("3. View All Entries")
            print("4. Back to Main Menu")
            
            choice = input("\nEnter your choice (1-4): ").strip()
            
            if choice == "1":
                class_id = input("Enter class ID: ").strip()
                if class_id in self.timetable.classes:
                    print(self.timetable.display_class_timetable(class_id))
                else:
                    print("Class not found.")
            elif choice == "2":
                teacher_id = input("Enter teacher ID: ").strip()
                if teacher_id in self.timetable.teachers:
                    print(self.timetable.display_teacher_timetable(teacher_id))
                else:
                    print("Teacher not found.")
            elif choice == "3":
                if self.timetable.entries:
                    print("\nAll Timetable Entries:")
                    for entry in self.timetable.entries:
                        print(f"  - {entry}")
                else:
                    print("\nNo timetable entries yet.")
            elif choice == "4":
                break
            else:
                print("Invalid choice.")
                
    def edit_timetable(self):
        """Edit/remove timetable entries."""
        print("\n--- Edit Timetable ---")
        
        if not self.timetable.entries:
            print("No timetable entries to edit.")
            return
            
        print("\nCurrent Entries:")
        for i, entry in enumerate(self.timetable.entries, 1):
            print(f"{i}. {entry}")
            
        print("\n1. Remove an entry")
        print("2. Back to Main Menu")
        
        choice = input("\nEnter your choice (1-2): ").strip()
        
        if choice == "1":
            try:
                class_id = input("Enter class ID: ").strip()
                day_num = int(input("Enter day (0-4): ").strip())
                day = DayOfWeek(day_num)
                period = int(input("Enter period: ").strip())
                
                if self.timetable.remove_entry(day, period, class_id):
                    print("Entry removed successfully!")
                else:
                    print("Entry not found.")
            except (ValueError, KeyError) as e:
                print(f"Invalid input: {e}")
                
    def validate_timetable(self):
        """Validate the timetable for conflicts."""
        print("\n--- Validate Timetable ---")
        errors = self.timetable.validate()
        
        if errors:
            print("\nValidation Errors Found:")
            for error in errors:
                print(f"  - {error}")
        else:
            print("\nTimetable is valid! No conflicts found.")
            
    def load_sample_data(self):
        """Load sample data for demonstration."""
        print("\n--- Loading Sample Data ---")
        
        # Add subjects
        subjects = [
            Subject("MATH", "Mathematics"),
            Subject("ENG", "English"),
            Subject("SCI", "Science"),
            Subject("HIST", "History"),
            Subject("PE", "Physical Education"),
        ]
        for subject in subjects:
            self.timetable.add_subject(subject)
            
        # Add teachers
        teachers = [
            Teacher("T001", "Mr. Smith", ["MATH"]),
            Teacher("T002", "Ms. Johnson", ["ENG"]),
            Teacher("T003", "Dr. Brown", ["SCI"]),
            Teacher("T004", "Mrs. Davis", ["HIST"]),
            Teacher("T005", "Coach Wilson", ["PE"]),
        ]
        for teacher in teachers:
            self.timetable.add_teacher(teacher)
            
        # Add classes
        classes = [
            SchoolClass("C1", "Grade 9A", 25),
            SchoolClass("C2", "Grade 9B", 28),
            SchoolClass("C3", "Grade 10A", 24),
        ]
        for school_class in classes:
            self.timetable.add_class(school_class)
            
        # Add some sample timetable entries
        sample_entries = [
            # Grade 9A - Monday
            TimetableEntry(DayOfWeek.MONDAY, self.timetable.time_slots[0], "C1", "MATH", "T001", "R101"),
            TimetableEntry(DayOfWeek.MONDAY, self.timetable.time_slots[1], "C1", "ENG", "T002", "R101"),
            TimetableEntry(DayOfWeek.MONDAY, self.timetable.time_slots[2], "C1", "SCI", "T003", "LAB1"),
            # Grade 9B - Monday
            TimetableEntry(DayOfWeek.MONDAY, self.timetable.time_slots[0], "C2", "ENG", "T002", "R102"),
            TimetableEntry(DayOfWeek.MONDAY, self.timetable.time_slots[1], "C2", "MATH", "T001", "R102"),
            # Grade 10A - Monday
            TimetableEntry(DayOfWeek.MONDAY, self.timetable.time_slots[0], "C3", "HIST", "T004", "R201"),
            TimetableEntry(DayOfWeek.MONDAY, self.timetable.time_slots[1], "C3", "PE", "T005", "GYM"),
        ]
        
        for entry in sample_entries:
            self.timetable.add_entry(entry)
            
        print("Sample data loaded successfully!")
        print(f"  - {len(subjects)} subjects")
        print(f"  - {len(teachers)} teachers")
        print(f"  - {len(classes)} classes")
        print(f"  - {len(sample_entries)} timetable entries")


def main():
    """Main entry point for the application."""
    cli = TimetableCLI()
    
    # Check if running in interactive mode
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        # Load sample data and display
        cli.load_sample_data()
        print("\n" + "=" * 70)
        print("Sample Timetable for Grade 9A:")
        print(cli.timetable.display_class_timetable("C1"))
        print("\n" + "=" * 70)
        print("Sample Timetable for Mr. Smith:")
        print(cli.timetable.display_teacher_timetable("T001"))
    else:
        # Run interactive CLI
        try:
            cli.run()
        except KeyboardInterrupt:
            print("\n\nInterrupted. Exiting...")
        except Exception as e:
            print(f"\nError: {e}")
            sys.exit(1)


if __name__ == "__main__":
    main()
