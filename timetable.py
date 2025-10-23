"""
School Timetable Application
Core data models for managing school timetables.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Set
from enum import Enum


class DayOfWeek(Enum):
    """Days of the week for scheduling."""
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4


@dataclass
class TimeSlot:
    """Represents a time slot in the school day."""
    period: int
    start_time: str
    end_time: str
    
    def __str__(self):
        return f"Period {self.period} ({self.start_time}-{self.end_time})"


@dataclass
class Subject:
    """Represents a school subject."""
    code: str
    name: str
    
    def __str__(self):
        return f"{self.code} - {self.name}"


@dataclass
class Teacher:
    """Represents a teacher."""
    id: str
    name: str
    subjects: List[str] = field(default_factory=list)
    
    def __str__(self):
        return f"{self.name} ({self.id})"


@dataclass
class SchoolClass:
    """Represents a class/grade."""
    id: str
    name: str
    students_count: int = 0
    
    def __str__(self):
        return f"{self.name} ({self.students_count} students)"


@dataclass
class TimetableEntry:
    """Represents a single entry in the timetable."""
    day: DayOfWeek
    time_slot: TimeSlot
    class_id: str
    subject_code: str
    teacher_id: str
    room: Optional[str] = None
    
    def __str__(self):
        return (f"{self.day.name} {self.time_slot.period}: "
                f"{self.subject_code} - {self.teacher_id} in {self.room or 'TBA'}")


class Timetable:
    """Main timetable class that manages all scheduling."""
    
    def __init__(self):
        self.entries: List[TimetableEntry] = []
        self.subjects: Dict[str, Subject] = {}
        self.teachers: Dict[str, Teacher] = {}
        self.classes: Dict[str, SchoolClass] = {}
        self.time_slots: List[TimeSlot] = []
        
    def add_subject(self, subject: Subject) -> None:
        """Add a subject to the timetable."""
        self.subjects[subject.code] = subject
        
    def add_teacher(self, teacher: Teacher) -> None:
        """Add a teacher to the timetable."""
        self.teachers[teacher.id] = teacher
        
    def add_class(self, school_class: SchoolClass) -> None:
        """Add a class to the timetable."""
        self.classes[school_class.id] = school_class
        
    def add_time_slot(self, time_slot: TimeSlot) -> None:
        """Add a time slot to the timetable."""
        self.time_slots.append(time_slot)
        
    def add_entry(self, entry: TimetableEntry) -> bool:
        """
        Add an entry to the timetable if it doesn't create conflicts.
        Returns True if successful, False if there's a conflict.
        """
        if self.has_conflict(entry):
            return False
        self.entries.append(entry)
        return True
        
    def has_conflict(self, new_entry: TimetableEntry) -> bool:
        """
        Check if a new entry conflicts with existing entries.
        Conflicts occur when:
        - Same teacher is scheduled at the same time
        - Same class is scheduled at the same time
        """
        for entry in self.entries:
            if entry.day == new_entry.day and entry.time_slot.period == new_entry.time_slot.period:
                # Check teacher conflict
                if entry.teacher_id == new_entry.teacher_id:
                    return True
                # Check class conflict
                if entry.class_id == new_entry.class_id:
                    return True
        return False
        
    def remove_entry(self, day: DayOfWeek, period: int, class_id: str) -> bool:
        """Remove an entry from the timetable. Returns True if found and removed."""
        for i, entry in enumerate(self.entries):
            if (entry.day == day and 
                entry.time_slot.period == period and 
                entry.class_id == class_id):
                self.entries.pop(i)
                return True
        return False
        
    def get_entries_for_class(self, class_id: str) -> List[TimetableEntry]:
        """Get all timetable entries for a specific class."""
        return [entry for entry in self.entries if entry.class_id == class_id]
        
    def get_entries_for_teacher(self, teacher_id: str) -> List[TimetableEntry]:
        """Get all timetable entries for a specific teacher."""
        return [entry for entry in self.entries if entry.teacher_id == teacher_id]
        
    def get_entries_for_day(self, day: DayOfWeek) -> List[TimetableEntry]:
        """Get all timetable entries for a specific day."""
        return [entry for entry in self.entries if entry.day == day]
        
    def display_class_timetable(self, class_id: str) -> str:
        """Generate a formatted timetable display for a class."""
        if class_id not in self.classes:
            return f"Class {class_id} not found"
            
        entries = self.get_entries_for_class(class_id)
        if not entries:
            return f"No timetable entries for class {class_id}"
            
        # Sort entries by day and period
        entries.sort(key=lambda e: (e.day.value, e.time_slot.period))
        
        output = [f"\nTimetable for {self.classes[class_id].name}"]
        output.append("=" * 70)
        
        current_day = None
        for entry in entries:
            if current_day != entry.day:
                current_day = entry.day
                output.append(f"\n{entry.day.name}")
                output.append("-" * 70)
                
            subject_name = self.subjects.get(entry.subject_code, Subject(entry.subject_code, "Unknown")).name
            teacher_name = self.teachers.get(entry.teacher_id, Teacher(entry.teacher_id, "Unknown")).name
            room = entry.room or "TBA"
            
            output.append(f"  {entry.time_slot} | {subject_name:20} | {teacher_name:20} | Room: {room}")
            
        return "\n".join(output)
        
    def display_teacher_timetable(self, teacher_id: str) -> str:
        """Generate a formatted timetable display for a teacher."""
        if teacher_id not in self.teachers:
            return f"Teacher {teacher_id} not found"
            
        entries = self.get_entries_for_teacher(teacher_id)
        if not entries:
            return f"No timetable entries for teacher {teacher_id}"
            
        # Sort entries by day and period
        entries.sort(key=lambda e: (e.day.value, e.time_slot.period))
        
        output = [f"\nTimetable for {self.teachers[teacher_id].name}"]
        output.append("=" * 70)
        
        current_day = None
        for entry in entries:
            if current_day != entry.day:
                current_day = entry.day
                output.append(f"\n{entry.day.name}")
                output.append("-" * 70)
                
            subject_name = self.subjects.get(entry.subject_code, Subject(entry.subject_code, "Unknown")).name
            class_name = self.classes.get(entry.class_id, SchoolClass(entry.class_id, "Unknown")).name
            room = entry.room or "TBA"
            
            output.append(f"  {entry.time_slot} | {subject_name:20} | {class_name:20} | Room: {room}")
            
        return "\n".join(output)
        
    def validate(self) -> List[str]:
        """
        Validate the timetable for any issues.
        Returns a list of validation errors (empty if valid).
        """
        errors = []
        
        # Check for conflicts (shouldn't happen if add_entry is used properly)
        for i, entry1 in enumerate(self.entries):
            for entry2 in self.entries[i+1:]:
                if (entry1.day == entry2.day and 
                    entry1.time_slot.period == entry2.time_slot.period):
                    if entry1.teacher_id == entry2.teacher_id:
                        errors.append(
                            f"Teacher {entry1.teacher_id} has conflict on "
                            f"{entry1.day.name} period {entry1.time_slot.period}"
                        )
                    if entry1.class_id == entry2.class_id:
                        errors.append(
                            f"Class {entry1.class_id} has conflict on "
                            f"{entry1.day.name} period {entry1.time_slot.period}"
                        )
                        
        return errors
