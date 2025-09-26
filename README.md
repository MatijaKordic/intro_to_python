# Python Learning Repository

## Introduction

Welcome to this repository! This repository is designed to help you learn Python programming, with a focus on test-driven development (TDD). It contains a series of exercises and projects that gradually increase in difficulty, covering fundamental Python concepts and basic AI/ML.

The goal is to provide a structured and practical learning experience, enabling her to write clean, well-tested, and maintainable code.

## Goals
github
* Provide a structured learning path for Python.
* Introduce test-driven development (TDD) from the beginning.
* Build a portfolio of Python code.
* Prepare for basic AI/ML concepts.
* Foster good coding practices.

## Repository Structure

    exercises/        # Contains individual Python coding exercises
        exercise_1.py
        exercise_2.py
        ...
    tests/            # Contains pytest test files for the exercises
        test_exercises.py
    projects/         # (Future) For larger, more complex projects
    docs/             # (Future) For additional documentation
    README.md         # This file

## Getting Started

1.  **Prerequisites:**

    * Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/). It's recommended to use the latest stable version.
    * Git installed on your system. You can download it from [git-scm.com](https://git-scm.com/). Git is a version control system that helps track changes to the code.
    * A GitHub account. You can create one at [github.com](https://github.com/). This will be used to store the code and collaborate.
    * [VSCode](https://code.visualstudio.com/) installed on your system. VSCode is a popular code editor that we'll use.

2.  **Setup:**

    * Clone this repository to your local machine:

        \`\`\`bash
        git clone https://github.com/your-username/your-repository-name.git
        cd your-repository-name
        \`\`\`

        (Replace `your-username` and `your-repository-name` with the correct values. This command copies the repository to your computer, and the `cd` command changes the current directory to the repository folder.)

    * It's highly recommended to use a virtual environment to manage Python dependencies. This keeps the project's dependencies isolated from other Python projects.  We'll use `uv` for this. 
        
        \`\`\`bash
        make install
        \`\`\`
    
    * Activate the virtual environment:
        * On macOS and Linux:
        
            \`\`\`bash
            source .intro_venv/bin/activate
            \`\`\`
        * On Windows:
        
            \`\`\`bash
            .intro_venv\\Scripts\\activate
            \`\`\`
            
        (When the virtual environment is activated, your terminal prompt will change, showing the environment name, e.g., `(.venv) $`.)

    * **Set up VSCode:**
        * Open the repository folder in VSCode.
        * Install the "Python" extension from the VSCode Marketplace (search for "ms-python.python").
        * In VSCode, open the Command Palette (Shift+Ctrl+P or Shift+Cmd+P) and select "Python: Select Interpreter".  Choose the Python interpreter from your virtual environment (`.venv`).

3.  **Workflow:**

    * Each exercise is located in the `exercises/` directory (e.g., `exercise_1.py`).
    * For each exercise:

        * Write your Python code in the exercise file. Follow the instructions provided in the file comments.
        * Write corresponding tests in the `tests/test_exercises.py` file. Follow the existing test structure and use pytest's `assert` statements to check the expected behavior of your code.
        * Run the tests using pytest:
            * **In the terminal:**
                
                \`\`\`bash
                pytest
                \`\`\`
            * **In VSCode:**
                * Open the `tests/test_exercises.py` file.
                * VSCode should automatically detect the tests. You can run them by clicking the "Run Test" button that appears near the test functions or by using the VSCode testing sidebar.

        * Ensure all tests pass. If a test fails, review your code, fix the bug, and run the tests again. Repeat this until all tests pass.
        * Commit your changes:

            \`\`\`bash
            git add exercises/exercise_1.py tests/test_exercises.py  # Add the files you changed
            git commit -m "Complete exercise 1: Add greeting function and tests"
            \`\`\`

            (The `git add` command stages the changes for commit, and the `git commit` command saves the changes with a descriptive message. Write clear and concise commit messages.)
        * Push your changes to the repository:

            \`\`\`bash
            git push
            \`\`\`

            (This command uploads your committed changes to the GitHub repository.)
        * Create a pull request on GitHub. This notifies the repository owner (you) that the exercise is complete and ready for review.

## Exercises

The `exercises/` directory contains the following exercises:

* **Exercise 1: Greeting Function** (`exercises/exercise_1.py`)
    * Write a function that greets a person by name.
* **Exercise 2: Sum of Two Numbers** (`exercises/exercise_2.py`)
    * Write a function that calculates the sum of two numbers.
* **Exercise 3: Even or Odd Checker** (`exercises/exercise_3.py`)
    * Write a function that determines if a number is even or odd.
* **Exercise 4: Simple String Reverser** (`exercises/exercise_4.py`)
    * Write a function that reverses a string.
* **Exercise 5: Finding the Maximum of Two Numbers** (`exercises/exercise_5.py`)
    * Write a function that finds the maximum of two numbers.

## Testing

This repository uses [pytest](https://pytest.org/) for testing. pytest is a powerful and flexible testing framework that makes it easy to write and run tests.

To run the tests, make sure you have activated your virtual environment and installed pytest.  You can run the tests from the command line using:

\`\`\`bash
pytest
\`\`\`

Or, you can run them directly within VSCode, which provides a more integrated experience.

This repository follows the Test-Driven Development (TDD) workflow. Here's how it works:

1.  **Red:** First, you write a test for a small piece of functionality. This test should fail initially because you haven't implemented the functionality yet.
2.  **Green:** Then, you write the minimum amount of code necessary to make the test pass.
3.  **Refactor:** Finally, you can refactor your code to improve its structure, readability, and maintainability, while ensuring that the test continues to pass.

This process helps to ensure that your code is well-tested and that you are only writing code that is actually needed.

## Debugging in VSCode

VSCode provides excellent debugging capabilities for Python.  Here's how to use it:

1.  Set a breakpoint in your code by clicking in the left margin next to the line where you want the program to pause.
2.  In VSCode, go to the "Run and Debug" view (Ctrl+Shift+D or Cmd+Shift+D).
3.  Create a launch configuration (if you don't have one already) by clicking the gear icon.  VSCode will create a `launch.json` file.
4.  Ensure the `launch.json` configuration is set to run your Python file.
5.  Press the "Start Debugging" button (green arrow) or press F5.

VSCode will start your program in debug mode, and it will pause at your breakpoint. You can then step through the code, inspect variables, and understand how your program is executing.

## Contributing

* All pull requests are welcome. Contributions help improve the learning experience.
* Follow the workflow described above.
* Write clear and concise commit messages. This makes it easier to understand the history of the code.
* Ensure all tests pass before submitting a pull request. This ensures that the changes do not introduce any errors.

## Code of Conduct

Please follow the [Code of Conduct](CODE_OF_CONDUCT.md) in all interactions with this project. This helps to create a welcoming and respectful environment.

## License

This project is licensed under the [License Name] License. See the [LICENSE](LICENSE) file for more information.


## Most common bash commands to use in terminal

`pwd` -- This command logs the current directory I am located in the terminal. 
`cd` -- This command allows you to go from one to another directory. To go back type `cd ..`, you can also chain that with adding backslashes and doing `cd ../../..` to go several backwards. Also, you can use `tab` for auto completion of folder names.
`ls -a` -- Command that lists all folders and files in a directory.
`mkdir` -- Create a directory.
`touch` -- Create a file. 
`rm` -- Remove a file. Add `-r` for recursive when deleting a folder. Be careful, the files don't go to Recycle bin.