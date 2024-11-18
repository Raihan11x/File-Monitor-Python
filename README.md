# File-Monitor-Python

A simple and effective file monitoring tool built in Python to track changes in directories and files. This tool allows users to monitor file modifications, additions, and deletions in real-time, making it useful for managing and tracking file changes within specific directories.

## Features

- Real-Time Monitoring: Get immediate feedback when a file is created, modified, or deleted.
- Customizable Paths: Configure the directories you want to monitor.
- Cross-Platform Compatibility: Works on Windows, macOS, and Linux.
- Lightweight and Efficient: Minimal resource consumption while monitoring files.

## Prerequisites

Ensure you have Python 3.x installed on your system. You can check your Python version by running:

Installation
Clone this repository:

bash
Copy code
git clone https://github.com/Raihan11x/File-Monitor-Python.git

Navigate to the project directory:

bash
Copy code
cd File-Monitor-Python
(Optional) Create and activate a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install required dependencies:

bash
Copy code
python file_monitor.py /path/to/directory
Command-Line Arguments
--path (optional): Specify the path you want to monitor. If no path is specified, it will default to the current directory.

Example:

bash
Copy code
python file_monitor.py --path "/home/user/documents"
Contributing
Contributions are welcome! Please fork this repository, make your changes, and submit a pull request. Make sure to follow the coding style used in the project.
