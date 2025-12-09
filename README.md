# Project Title: CLI Task Manager
# Project Description

This project is a simple Command-Line Interface (CLI) Task Manager written in Python.
Users can add tasks, view tasks, mark tasks as completed, and delete tasks.
The program uses a JSON file to store all tasks so that the list remains saved between runs.

# Functions & Classes (Brief Description)
1. main()
The main function of the program.
It runs the menu loop, accepts user input, and triggers all other functions.

2. Task (Class)
Represents a task object with:
title -the name of the task
completed -True/False value showing if the task is done
Also includes:
to_dict() -returns the task as a dictionary for saving to JSON.

3. load_tasks()
Loads all tasks from the tasks.json file and returns them as a list of Task objects.
If the file does not exist, it returns an empty list.

4. save_tasks(tasks)
Saves the current list of tasks to the tasks.json file.
Converts each Task object into a dictionary before saving.

5. display_menu()
Shows menu options to the user inside the CLI.
Called repeatedly in the main loop.

How to Run the Project

Install Python 3.
Open a terminal.
Run the command.


