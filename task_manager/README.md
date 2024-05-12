# Task Manager Application

A Python-based Task Manager application employing the
'Model-View-Controller' pattern. It facilitates users to
effortlessly create, update, remove, or view tasks, deadlines,
priorities, and categories.

Please note that tasks do not get saved to a database - this is something that I am
currently working on 🚧

## Features

1. Create a new task: Easily add new tasks to your list
2. Update a task: Modify existing tasks as needed
3. Remove a task: Delete tasks that are no longer relevant
4. View a task: Display detailed information about a specific task
5. View deadlines: Check deadlines for tasks
6. View priorities: Prioritise tasks based on their importance
7. View categories: Organise tasks into different categories

## Getting started

1. Clone the repository to your local machine <br />
   `git clone`
2. Navigate to the project directory <br />
   `cd bootcamp_coding_tasks`
3. Open Visual Studio Code <br />
   `Code .`
4. Set up a virtual environment using `virtualenv` or `venv`

   Using venv

   Navigate to the project directory and run: <br />
   `python -m venv venv` <br />
   For Python 3.3 or newer: <br />
   `python3 -m venv venv`

   Using virtualenv

   `pip install virtualenv` <br />
   Navigate to the project directory and run: <br />
   `virtualenv venv`

5. Activate the virtual environment

   Using venv

   Windows <br />
   `venv\Scripts\activate`
   Unix\Mac <br />
   `source venv/bin/activate`

   Using virtualenv <br />

   Windows <br />
   `venv\Scripts\activate` <br />
   Unix\Mac <br />
   `source venv/bin/activate`

6. Ensure project dependencies are installed: <br />

```
- flake8==7.0.0
- mccabe==0.7.0
- pycodestyle==2.11.1
- pyflakes==3.2.0
```

7. Run the main script using: <br />
   `python src\main.py`
