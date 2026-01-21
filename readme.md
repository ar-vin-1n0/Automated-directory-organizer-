🗂️ Smart File Organizer (Phase 2 Final Project)

A Python-based automation tool that scans a directory (including subfolders), classifies files by extension, and safely organizes them into structured folders with professional logging and error handling.

This project is built using only Python Standard Library and demonstrates clean architecture, configuration-driven design, and real-world automation skills.

🚀 Features

📁 Recursive folder scanning (including subfolders)

🧠 Config-driven file classification

📂 Automatic folder creation

🔁 Overwrite-safe file moving (auto-renaming)

🧾 Professional logging (file + console)

❌ Graceful error handling

🔌 No external dependencies

🏗️ Project Architecture
smart-file-organizer/
│
├── config/
│   └── config.json
│
├── logs/
│   └── basic.log
│
├── organizer/
│   ├── __init__.py
│   ├── config_loader.py
│   ├── scanner.py
│   ├── classifier.py
│   ├── mover.py
│   └── logger.py
│
├── main.py
├── requirements.txt
└── README.md

⚙️ How It Works (High-Level Flow)
Load configuration
Initialize logger
Scan source folder recursively
For each file:
    Classify file by extension
    Move file to destination folder
    Log the result
Handle unexpected errors safely


main.py acts as the orchestrator
All business logic lives in isolated modules.

🧠 Design Principles Used

Separation of concerns

Fail early on invalid config

Config-driven behavior (no hardcoded paths)

Safe file operations

Readable, maintainable code

🧾 Example Log Output
| 2026-01-21 11:32:10 | INFO | Moved photo.jpg → images/ | main.py | 45 |
| 2026-01-21 11:32:12 | INFO | Moved report.pdf → docs/ | main.py | 45 |
| 2026-01-21 11:32:15 | ERROR | Failed to move locked.tmp | mover.py | 62 |

▶️ How to Run
1️⃣ Clone the repository
git clone https://github.com/your-username/smart-file-organizer.git
cd smart-file-organizer

2️⃣ Configure paths and categories

Edit:

config/config.json

3️⃣ Run the program
python main.py

📦 Requirements
# No external dependencies required
# Uses only Python Standard Library


Python version: 3.9+

🧪 Error Handling

Invalid or missing config → program stops early

File system errors → logged without crashing

Name conflicts → auto-renamed safely

🎯 What This Project Demonstrates

Real-world file automation

Clean modular architecture

Professional logging practices

Safe handling of OS operations

Readable, scalable Python code

This project is suitable for:

Automation roles

Python backend fundamentals

Internship / junior developer portfolios

🔮 Future Improvements

Dry-run mode

CLI arguments (--config, --dry-run)

File size/date-based classification

Unit tests

Packaging as a CLI tool

👤 Author

Aravind Raj |
Python Automation | Backend Fundamentals | Clean Code

📜 License

This project is open-source and available for learning and educational use.