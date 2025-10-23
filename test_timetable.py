"""
Unit tests for the school timetable application.
"""

import unittest
from timetable import (
    Timetable, Subject, Teacher, SchoolClass, 
    TimeSlot, TimetableEntry, DayOfWeek
)


class TestTimeSlot(unittest.TestCase):
    """Test cases for TimeSlot class."""
    
    def test_time_slot_creation(self):
        """Test creating a time slot."""
        slot = TimeSlot(1, "08:00", "08:50")
        self.assertEqual(slot.period, 1)
        self.assertEqual(slot.start_time, "08:00")
        self.assertEqual(slot.end_time, "08:50")
        
    def test_time_slot_string(self):
        """Test string representation of time slot."""
        slot = TimeSlot(2, "09:00", "09:50")
        self.assertEqual(str(slot), "Period 2 (09:00-09:50)")


class TestSubject(unittest.TestCase):
    """Test cases for Subject class."""
    
    def test_subject_creation(self):
        """Test creating a subject."""
        subject = Subject("MATH", "Mathematics")
        self.assertEqual(subject.code, "MATH")
        self.assertEqual(subject.name, "Mathematics")
        
    def test_subject_string(self):
        """Test string representation of subject."""
        subject = Subject("ENG", "English")
        self.assertEqual(str(subject), "ENG - English")


class TestTeacher(unittest.TestCase):
    """Test cases for Teacher class."""
    
    def test_teacher_creation(self):
        """Test creating a teacher."""
        teacher = Teacher("T001", "Mr. Smith", ["MATH", "SCI"])
        self.assertEqual(teacher.id, "T001")
        self.assertEqual(teacher.name, "Mr. Smith")
        self.assertEqual(teacher.subjects, ["MATH", "SCI"])
        
    def test_teacher_without_subjects(self):
        """Test creating a teacher without subjects."""
        teacher = Teacher("T002", "Ms. Johnson")
        self.assertEqual(teacher.subjects, [])


class TestSchoolClass(unittest.TestCase):
    """Test cases for SchoolClass class."""
    
    def test_class_creation(self):
        """Test creating a school class."""
        school_class = SchoolClass("C1", "Grade 9A", 25)
        self.assertEqual(school_class.id, "C1")
        self.assertEqual(school_class.name, "Grade 9A")
        self.assertEqual(school_class.students_count, 25)


class TestTimetable(unittest.TestCase):
    """Test cases for Timetable class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.timetable = Timetable()
        
        # Add subjects
        self.timetable.add_subject(Subject("MATH", "Mathematics"))
        self.timetable.add_subject(Subject("ENG", "English"))
        
        # Add teachers
        self.timetable.add_teacher(Teacher("T001", "Mr. Smith", ["MATH"]))
        self.timetable.add_teacher(Teacher("T002", "Ms. Johnson", ["ENG"]))
        
        # Add classes
        self.timetable.add_class(SchoolClass("C1", "Grade 9A", 25))
        self.timetable.add_class(SchoolClass("C2", "Grade 9B", 28))
        
        # Add time slots
        self.timetable.add_time_slot(TimeSlot(1, "08:00", "08:50"))
        self.timetable.add_time_slot(TimeSlot(2, "09:00", "09:50"))
        
    def test_add_subject(self):
        """Test adding a subject."""
        subject = Subject("SCI", "Science")
        self.timetable.add_subject(subject)
        self.assertIn("SCI", self.timetable.subjects)
        self.assertEqual(self.timetable.subjects["SCI"].name, "Science")
        
    def test_add_teacher(self):
        """Test adding a teacher."""
        teacher = Teacher("T003", "Dr. Brown", ["SCI"])
        self.timetable.add_teacher(teacher)
        self.assertIn("T003", self.timetable.teachers)
        self.assertEqual(self.timetable.teachers["T003"].name, "Dr. Brown")
        
    def test_add_class(self):
        """Test adding a class."""
        school_class = SchoolClass("C3", "Grade 10A", 24)
        self.timetable.add_class(school_class)
        self.assertIn("C3", self.timetable.classes)
        self.assertEqual(self.timetable.classes["C3"].name, "Grade 10A")
        
    def test_add_entry_success(self):
        """Test successfully adding a timetable entry."""
        entry = TimetableEntry(
            DayOfWeek.MONDAY,
            self.timetable.time_slots[0],
            "C1",
            "MATH",
            "T001",
            "R101"
        )
        result = self.timetable.add_entry(entry)
        self.assertTrue(result)
        self.assertEqual(len(self.timetable.entries), 1)
        
    def test_add_entry_teacher_conflict(self):
        """Test that adding an entry with teacher conflict fails."""
        # Add first entry
        entry1 = TimetableEntry(
            DayOfWeek.MONDAY,
            self.timetable.time_slots[0],
            "C1",
            "MATH",
            "T001",
            "R101"
        )
        self.timetable.add_entry(entry1)
        
        # Try to add conflicting entry (same teacher, same time)
        entry2 = TimetableEntry(
            DayOfWeek.MONDAY,
            self.timetable.time_slots[0],
            "C2",
            "MATH",
            "T001",
            "R102"
        )
        result = self.timetable.add_entry(entry2)
        self.assertFalse(result)
        self.assertEqual(len(self.timetable.entries), 1)
        
    def test_add_entry_class_conflict(self):
        """Test that adding an entry with class conflict fails."""
        # Add first entry
        entry1 = TimetableEntry(
            DayOfWeek.MONDAY,
            self.timetable.time_slots[0],
            "C1",
            "MATH",
            "T001",
            "R101"
        )
        self.timetable.add_entry(entry1)
        
        # Try to add conflicting entry (same class, same time)
        entry2 = TimetableEntry(
            DayOfWeek.MONDAY,
            self.timetable.time_slots[0],
            "C1",
            "ENG",
            "T002",
            "R101"
        )
        result = self.timetable.add_entry(entry2)
        self.assertFalse(result)
        self.assertEqual(len(self.timetable.entries), 1)
        
    def test_add_entry_no_conflict(self):
        """Test adding entries without conflicts."""
        entry1 = TimetableEntry(
            DayOfWeek.MONDAY,
            self.timetable.time_slots[0],
            "C1",
            "MATH",
            "T001",
            "R101"
        )
        entry2 = TimetableEntry(
            DayOfWeek.MONDAY,
            self.timetable.time_slots[1],
            "C1",
            "ENG",
            "T002",
            "R101"
        )
        
        result1 = self.timetable.add_entry(entry1)
        result2 = self.timetable.add_entry(entry2)
        
        self.assertTrue(result1)
        self.assertTrue(result2)
        self.assertEqual(len(self.timetable.entries), 2)
        
    def test_remove_entry(self):
        """Test removing a timetable entry."""
        entry = TimetableEntry(
            DayOfWeek.MONDAY,
            self.timetable.time_slots[0],
            "C1",
            "MATH",
            "T001",
            "R101"
        )
        self.timetable.add_entry(entry)
        
        result = self.timetable.remove_entry(DayOfWeek.MONDAY, 1, "C1")
        self.assertTrue(result)
        self.assertEqual(len(self.timetable.entries), 0)
        
    def test_remove_nonexistent_entry(self):
        """Test removing a non-existent entry."""
        result = self.timetable.remove_entry(DayOfWeek.MONDAY, 1, "C1")
        self.assertFalse(result)
        
    def test_get_entries_for_class(self):
        """Test getting entries for a specific class."""
        entry1 = TimetableEntry(
            DayOfWeek.MONDAY,
            self.timetable.time_slots[0],
            "C1",
            "MATH",
            "T001"
        )
        entry2 = TimetableEntry(
            DayOfWeek.MONDAY,
            self.timetable.time_slots[1],
            "C1",
            "ENG",
            "T002"
        )
        entry3 = TimetableEntry(
            DayOfWeek.MONDAY,
            self.timetable.time_slots[0],
            "C2",
            "ENG",
            "T002"
        )
        
        self.timetable.add_entry(entry1)
        self.timetable.add_entry(entry2)
        self.timetable.add_entry(entry3)
        
        c1_entries = self.timetable.get_entries_for_class("C1")
        self.assertEqual(len(c1_entries), 2)
        
    def test_get_entries_for_teacher(self):
        """Test getting entries for a specific teacher."""
        entry1 = TimetableEntry(
            DayOfWeek.MONDAY,
            self.timetable.time_slots[0],
            "C1",
            "MATH",
            "T001"
        )
        entry2 = TimetableEntry(
            DayOfWeek.MONDAY,
            self.timetable.time_slots[1],
            "C2",
            "MATH",
            "T001"
        )
        entry3 = TimetableEntry(
            DayOfWeek.MONDAY,
            self.timetable.time_slots[0],
            "C2",
            "ENG",
            "T002"
        )
        
        self.timetable.add_entry(entry1)
        self.timetable.add_entry(entry2)
        self.timetable.add_entry(entry3)
        
        t001_entries = self.timetable.get_entries_for_teacher("T001")
        self.assertEqual(len(t001_entries), 2)
        
    def test_get_entries_for_day(self):
        """Test getting entries for a specific day."""
        entry1 = TimetableEntry(
            DayOfWeek.MONDAY,
            self.timetable.time_slots[0],
            "C1",
            "MATH",
            "T001"
        )
        entry2 = TimetableEntry(
            DayOfWeek.TUESDAY,
            self.timetable.time_slots[0],
            "C1",
            "ENG",
            "T002"
        )
        
        self.timetable.add_entry(entry1)
        self.timetable.add_entry(entry2)
        
        monday_entries = self.timetable.get_entries_for_day(DayOfWeek.MONDAY)
        self.assertEqual(len(monday_entries), 1)
        self.assertEqual(monday_entries[0].day, DayOfWeek.MONDAY)
        
    def test_validate_valid_timetable(self):
        """Test validation of a valid timetable."""
        entry1 = TimetableEntry(
            DayOfWeek.MONDAY,
            self.timetable.time_slots[0],
            "C1",
            "MATH",
            "T001"
        )
        entry2 = TimetableEntry(
            DayOfWeek.MONDAY,
            self.timetable.time_slots[1],
            "C1",
            "ENG",
            "T002"
        )
        
        self.timetable.add_entry(entry1)
        self.timetable.add_entry(entry2)
        
        errors = self.timetable.validate()
        self.assertEqual(len(errors), 0)
        
    def test_display_class_timetable(self):
        """Test displaying a class timetable."""
        entry = TimetableEntry(
            DayOfWeek.MONDAY,
            self.timetable.time_slots[0],
            "C1",
            "MATH",
            "T001",
            "R101"
        )
        self.timetable.add_entry(entry)
        
        output = self.timetable.display_class_timetable("C1")
        self.assertIn("Grade 9A", output)
        self.assertIn("MONDAY", output)
        self.assertIn("Mathematics", output)
        
    def test_display_teacher_timetable(self):
        """Test displaying a teacher timetable."""
        entry = TimetableEntry(
            DayOfWeek.MONDAY,
            self.timetable.time_slots[0],
            "C1",
            "MATH",
            "T001",
            "R101"
        )
        self.timetable.add_entry(entry)
        
        output = self.timetable.display_teacher_timetable("T001")
        self.assertIn("Mr. Smith", output)
        self.assertIn("MONDAY", output)
        self.assertIn("Mathematics", output)


if __name__ == "__main__":
    unittest.main()
