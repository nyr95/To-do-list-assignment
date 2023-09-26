# To-do-list-assignment


A simple command-line To-Do List Manager written in Python. This program allows users to add, mark as completed, delete tasks, view tasks based on their completion status, and undo/redo actions.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Keyboard Interrupt Handling](#keyboard-interrupt-handling)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)

## Features

- Add new tasks with descriptions and optional due dates.
- Mark tasks as 'completed'.
- Delete tasks.
- View tasks: all, completed, or pending.
- Undo and redo actions using the Memento Pattern.
- Error handling and keyboard interrupt handling for a robust user experience.

## Requirements

- Python 3.x
- `datetime` module (usually included in Python standard library)
- 'sys' module (usually included in Python standard library)

## Usage

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/.git

2.Navigate to the project directory:

    ```bash
    Copy code
    cd todo-list-manager
3.Run the To-Do List assignment:

    ```bash
    Copy code
    python todo_manager.py
    Follow the on-screen menu to interact with the To-Do List Manager.

Keyboard Interrupt Handling
The program includes keyboard interrupt handling to gracefully exit the To-Do List Manager when a keyboard interrupt (e.g., Ctrl+C) is detected.

Error Handling
Error handling is implemented for various scenarios, including:

Invalid date format when adding a task with a due date.
Invalid menu choices.
Invalid filter types when viewing tasks.
Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix: git checkout -b feature/your-feature-name
Commit your changes: git commit -m "Add your feature"
Push to the branch: git push origin feature/your-feature-name
Create a pull request on GitHub.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Happy task management!
