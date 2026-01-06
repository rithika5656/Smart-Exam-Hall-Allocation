# Smart Exam Hall Allocation

A simple Python application that automatically allocates students to exam halls and seats, reducing manual errors in exam seating arrangements.

## Features

- **Automatic Hall Allocation**: Assigns students to available exam halls
- **Gap Seating**: Implements alternate seating to prevent cheating
- **Web Interface**: Easy-to-use web UI for managing allocations
- **Allocation Summary**: View statistics and reports

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Logic**: Simple allocation algorithm with gap seating

## Installation

1. Clone the repository:
```bash
git clone https://github.com/rithika5656/Smart-Exam-Hall-Allocation.git
cd Smart-Exam-Hall-Allocation
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to `http://localhost:5000`

## Usage

1. Add exam halls with their seating capacity
2. Add student names or roll numbers
3. Click "Allocate" to automatically assign seats
4. View the allocation results and download reports

## Project Structure

```
Smart-Exam-Hall-Allocation/
├── app.py              # Flask web application
├── allocation.py       # Core allocation logic
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Web interface
└── README.md          # Documentation
```

## Why It's Innovative

- Eliminates manual seating arrangement errors
- Ensures fair gap seating to prevent malpractice
- Saves time for exam coordinators
- Easy to use with a simple web interface

## License

MIT License
