"""
Smart Exam Hall Allocation - Web Application
Flask-based web interface for exam hall allocation
"""

from flask import Flask, render_template, request, jsonify
from allocation import ExamHallAllocator

app = Flask(__name__)
allocator = ExamHallAllocator()

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/add_hall', methods=['POST'])
def add_hall():
    """Add a new exam hall"""
    data = request.json
    hall_name = data.get('name')
    rows = int(data.get('rows', 5))
    cols = int(data.get('cols', 6))
    
    hall = allocator.add_hall(hall_name, rows, cols)
    return jsonify({
        'success': True,
        'message': f'Hall "{hall_name}" added with capacity {hall["capacity"]}',
        'hall': {
            'name': hall['name'],
            'rows': hall['rows'],
            'cols': hall['cols'],
            'capacity': hall['capacity']
        }
    })

@app.route('/add_students', methods=['POST'])
def add_students():
    """Add students to be allocated"""
    data = request.json
    students = data.get('students', [])
    
    if isinstance(students, str):
        students = [s.strip() for s in students.split(',') if s.strip()]
    
    allocator.add_students(students)
    return jsonify({
        'success': True,
        'message': f'{len(students)} students added',
        'total_students': len(allocator.students)
    })

@app.route('/allocate', methods=['POST'])
def allocate():
    """Perform student allocation"""
    if not allocator.halls:
        return jsonify({
            'success': False,
            'message': 'No halls available. Please add halls first.'
        })
    
    if not allocator.students:
        return jsonify({
            'success': False,
            'message': 'No students to allocate. Please add students first.'
        })
    
    allocations = allocator.allocate_students()
    summary = allocator.get_allocation_summary()
    
    return jsonify({
        'success': True,
        'allocations': allocations,
        'summary': summary
    })

@app.route('/get_layout/<hall_name>')
def get_layout(hall_name):
    """Get seating layout for a specific hall"""
    layout = allocator.get_hall_layout(hall_name)
    if layout:
        return jsonify({'success': True, 'layout': layout})
    return jsonify({'success': False, 'message': 'Hall not found'})

@app.route('/search_student/<student_name>')
def search_student(student_name):
    """Search for a student's allocation"""
    allocation = allocator.get_student_allocation(student_name)
    if allocation:
        return jsonify({'success': True, 'allocation': allocation})
    return jsonify({'success': False, 'message': 'Student not found'})

@app.route('/reset', methods=['POST'])
def reset():
    """Reset all data"""
    global allocator
    allocator = ExamHallAllocator()
    return jsonify({'success': True, 'message': 'All data reset'})

@app.route('/get_status')
def get_status():
    """Get current status"""
    return jsonify({
        'halls': len(allocator.halls),
        'students': len(allocator.students),
        'allocated': len(allocator.allocations)
    })

if __name__ == '__main__':
    print("Starting Smart Exam Hall Allocation System...")
    print("Open http://localhost:5000 in your browser")
    app.run(debug=True, port=5000)
