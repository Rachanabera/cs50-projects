# To-Do List Manager
#### Video Demo: <https://youtube.com/shorts/ztXJRseRRCU?si=f55jOQAEz-MnCBrP>
#### Description:

The **To-Do List Manager** is a command-line based productivity application developed as the final project for **CS50’s Introduction to Programming with Python (CS50P)**. It enables users to organize and track their daily tasks efficiently, encouraging better time management and focus. The project demonstrates proficiency in Python fundamentals, including lists, dictionaries, conditionals, loops, and functions.

---

### 🧭 What This Project Does

The To-Do List Manager is a text-based program that allows users to:
- **Add** tasks to their list
- **View** all current tasks with their status (complete/incomplete)
- **Mark** tasks as complete
- **Delete** tasks that are no longer needed
- **Exit** the program when finished

Each task is stored as a dictionary inside a list with two attributes:
- `"task"`: A string describing the task.
- `"done"`: A boolean representing completion status.

---

### 🗂️ File Structure

- **`project.py`**
  This is the main executable file. It handles user input, prints menus, and calls appropriate functions. It contains:
  - `main()`: The program loop with options menu.
  - `add_task(tasks, task)`: Appends a new task.
  - `complete_task(tasks, index)`: Marks a task as complete.
  - `delete_task(tasks, index)`: Removes a task.
  - `view_tasks(tasks)`: Displays the current list with checkmarks.

- **(Optional) `test_project.py`**
  This file would contain unit tests written using `pytest` to validate task creation, deletion, and completion functions.
  *(Note: Add this file if you're planning to include testing in your submission.)*

---

### 💡 Design Philosophy

The application was designed with simplicity and clarity in mind, focusing on readability, modularity, and user interaction. Here's why:

- **Modular Design:** Each action is encapsulated in its own function to keep the code organized and reusable.
- **Data Representation:** A list of dictionaries was chosen to represent tasks, making it easy to manage task attributes.
- **User-Friendly CLI:** The command-line interface is clear and accessible even to non-technical users.

---

### 🔍 How It Works

Upon launching the script, the user is presented with a numbered menu. Based on the user’s input:
- The program performs actions on the `tasks` list.
- Task indices are adjusted so users can refer to them starting from 1, even though Python uses 0-based indexing.
- Visual feedback is provided using `✅` for completed tasks and `❌` for incomplete ones.

Example:
Buy groceries [❌]
Finish CS50P project [✅]

---

### ✅ Features Implemented

- [x] Add new tasks
- [x] View all tasks with status indicators
- [x] Mark tasks as complete
- [x] Delete existing tasks
- [x] Clean and interactive CLI

---

### 🌱 Future Improvements

This project can be extended with the following enhancements:
- **Persistent Storage**: Save and load tasks using text files, JSON, or databases.
- **Due Dates & Priorities**: Add deadlines and task urgency.
- **GUI Application**: Use `tkinter` or `PyQt` for a visual task management interface.
- **Authentication & Profiles**: Support multiple users with their own task lists.

---

### 🧪 Testing

Although the project doesn't yet include automated testing, functions have been designed for easy testability. A future version may include `pytest` tests for:
- Adding a task
- Completing a task
- Deleting a task
- Displaying the correct output

---

### 🧑‍💻 About Me

- **Name:** Rasna (Rachana)
- **GitHub:** [your-github-username]
- **CS50 edX Username:** [your-edX-username]
- **Course:** CS50P - Introduction to Programming with Python
- **Location:** Navi Mumbai, India
- **Date Submitted:** April 2025

---

This To-Do List Manager is a representation of my progress throughout the CS50P course. It showcases what I’ve learned and what I’m capable of building using Python. I’m proud of this journey and excited to keep building!

Thanks, CS50!


