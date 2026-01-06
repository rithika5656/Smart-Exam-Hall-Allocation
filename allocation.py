"""
Smart Exam Hall Allocation - Core Logic
Automatically allocates students to exam halls and seats
"""

class ExamHallAllocator:
    def __init__(self):
        self.halls = []
        self.students = []
        self.allocations = {}
    
    def add_hall(self, hall_name, rows, cols):
        """Add an exam hall with specified seating capacity"""
        capacity = rows * cols
        hall = {
            'name': hall_name,
            'rows': rows,
            'cols': cols,
            'capacity': capacity,
            'seats': [[None for _ in range(cols)] for _ in range(rows)]
        }
        self.halls.append(hall)
        return hall
    
    def add_students(self, student_list):
        """Add list of students to be allocated"""
        self.students.extend(student_list)
    
    def allocate_students(self):
        """Allocate students to halls with gap seating to prevent cheating"""
        self.allocations = {}
        student_index = 0
        total_students = len(self.students)
        
        for hall in self.halls:
            if student_index >= total_students:
                break
                
            # Allocate with gap seating (alternate seats)
            for row in range(hall['rows']):
                for col in range(hall['cols']):
                    if student_index >= total_students:
                        break
                    
                    # Skip alternate seats for gap seating
                    if (row + col) % 2 == 0:
                        student = self.students[student_index]
                        hall['seats'][row][col] = student
                        self.allocations[student] = {
                            'hall': hall['name'],
                            'row': row + 1,
                            'seat': col + 1
                        }
                        student_index += 1
        
        return self.allocations
    
    def get_hall_layout(self, hall_name):
        """Get seating layout for a specific hall"""
        for hall in self.halls:
            if hall['name'] == hall_name:
                return hall['seats']
        return None
    
    def get_student_allocation(self, student_name):
        """Get allocation details for a specific student"""
        return self.allocations.get(student_name, None)
    
    def get_allocation_summary(self):
        """Get summary of all allocations"""
        summary = {
            'total_students': len(self.students),
            'allocated_students': len(self.allocations),
            'halls_used': [],
        }
        
        for hall in self.halls:
            occupied = sum(1 for row in hall['seats'] for seat in row if seat is not None)
            summary['halls_used'].append({
                'name': hall['name'],
                'capacity': hall['capacity'],
                'occupied': occupied
            })
        
        return summary


# Demo usage
if __name__ == "__main__":
    allocator = ExamHallAllocator()
    
    # Add exam halls
    allocator.add_hall("Hall A", 5, 6)
    allocator.add_hall("Hall B", 4, 5)
    
    # Add students
    students = [f"Student_{i}" for i in range(1, 26)]
    allocator.add_students(students)
    
    # Perform allocation
    allocations = allocator.allocate_students()
    
    # Print results
    print("=== Smart Exam Hall Allocation ===\n")
    print("Allocation Results:")
    for student, details in allocations.items():
        print(f"  {student}: {details['hall']} - Row {details['row']}, Seat {details['seat']}")
    
    print("\n" + "="*40)
    summary = allocator.get_allocation_summary()
    print(f"\nSummary:")
    print(f"  Total Students: {summary['total_students']}")
    print(f"  Allocated: {summary['allocated_students']}")
