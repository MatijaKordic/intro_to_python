# Python Learning Repository

## Introduction

Welcome to this repository! This repository is designed to help you learn Python programming, with a focus on test-driven development (TDD). It contains a series of exercises and projects that gradually increase in difficulty, covering fundamental Python concepts and basic AI/ML.

The goal is to provide a structured and practical learning experience, enabling her to write clean, well-tested, and maintainable code.

## Goals

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


## Working with Github

Minor things to keep on mind:

- We want to have small PRs that are targeting one addition (be it a feature, fix, etc.)
- You can have multiple PRs and branches running at the same time.
- Github is a version control tool, which means it literally stores all of the different versions of the repository through history. You could jump back to any point in repo history using commit hashes. This is why Semantic Versioning (SemVer) and Conventional Changelog (CC) help.

When you want to contribute to a Github Repository, first you need to fetch and pull the latest main branch and checkout to your new branch from there. Once the development of the code has been implemented and tested, you will add a commit using Commitizen and push to Github for a PR (pull request). There, you will have to have at least one reviewer. Once the PR has been approved, you will fetch the latest of your branch. Push these and merge your branch. In code:

```python
git fetch —-all
```

We are fetching to make sure tags and other branches are fetched too. Just good practice. Now run pull:

```python
git pull
```

Okay, so not is the time to checkout to your branch and apply your changes. Remember, we are working according to Semantic Versioning and using a Conventional Changelog that follows following commit categories:

- build: Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm)
- ci: Changes to our CI configuration files and scripts (example scopes: Travis, Circle, BrowserStack, SauceLabs)
- docs: Documentation only changes
- feat: A new feature
- fix: A bug fix
- perf: A code change that improves performance
- refactor: A code change that neither fixes a bug nor adds a feature
- style: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
- test: Adding missing tests or correcting existing tests

Now, Semantic Versioning (SemVer), it says we track in our Github versioning only the following three: feat, fix, and major corresponding to 0.0.0 where first digit is major and represents a breaking change (moving repo from research to production), second digit is minor (in conventional changelog (CC) it is feat or short of feature) and represents adding a new feature and last digit is patch (in CC fix) and represents fixing a bug in code. 

So, upfront you should know what you are solving with your branch and name your new branch accordingly with type_of_change/branch_name e.g. if you are adding a new feature for Azure Blog storage: feat/azure_connector like this:

```python
git checkout -b feat/azure_connector
```

The -b bit will automatically create and transfer you to the branch so you can start developing. Once you develop, run:

```python
git status
```

Now, you can see which files were changed, add the ones you want to commit with:

```python
git add file_name
```

Now, if you added all of your files, run:

```python
git commit -m "Descriptive and concise message."
```

Once the commit has passed, we run:

```python
git push
```

It will ask us to set the upstream branch (because our branch is still local) and just copy paste the code from the terminal for that. 

Once it is pushed, you can open a PR directly from terminal (you will be given a link there) or go to Github repo and open a PR there. Add a reviewer and wait for approval or required changes. Once the PR has been finally approved, pull the latest branch to your local. **Note: do not merge the pull request yet!** 

```python
git pull
```

Once the PR has been approved, we need to pull the changes (if any) and before merging on Github we will bump the version locally. Once bump is done, make sure to push the bumped changes to Github prior to merging the branch. 

```python
git checkout main/dev
git fetch --all
git pull
git checkout your_branch
git merge main/dev
```

The above git merge main will have you enter VIM to add a commit message on why the merge was done. VIM is an editing in-terminal tool. It has a specific set of commands:

- ENTER will allow you to start adding your commit message
- Add your commit message e.g.: Merge main to your_branch to make sure Commitizen is up to date before doing cz bump
- ESCAPE will get you out of the commit message
- Now, in order to save and exit VIM, do :wq

In case our change has been a feature, bug fix or major, the bump will bump the [CHANGELOG.md](http://CHANGELOG.md) and populate it with our commit message, and change the .cz.yaml and VERSION files accordingly. Do 

```python
git status
git push
```

Now, on Github just do the merge of the branch. On your local machine, make sure to switch to main and do the fetch and pull to make sure you are up to date. 

Don’t forget, minor changes per branch, you can have multiple branches at the same time. 

### Github Stash

Let’s imagine a situation where you have been working on some files on branch feat/add_this_feature but you are still unsure and don’t want to commit the files. Now, in case of new files, you can freely change the branch without having to worry about losing the work but in case of changing existing files, if you say want to jump to a branch fix/change_this_file you will have to either commit the files on feat/add_this_feature and switch to fix/change_this_file or you can use a git stash. A git stash command will stash the current version of the uncommitted changes you made on feat/add_this_feature and you will be able to jump back to fix/change_this_file do your coding and jump back to feat/add_this_feature and do git stash pop to get your stash back for working on it. 

### Github History Fix — Squashing

Developing on a branch is not always predictable so commits often mix and we want to have a commit per file. So, once you are done and the PR is approved, you can check the number of commits in your PR, for example it is 12. You can enter interactive rebasing and squash the commits. This means you can now instead of having numerous commits nicely present them file per file or fix/feat by fix/feat. 

To get the number of commits that differ from the branch you based from and the branch you are on: 

`git rebase -i origin/branch_base`   

This will rebase you to your branch_base so you can do squash and pick.

When rebasing, you have two options, mark the commits you don’t want as `s` for squash or `pick` for what goes to Github. Once done, do:

- esc
- :wq
- :wq (sometimes it will need to be done twice)

`git push origin my_branch --force`

That is it, this way you can organise your commits nicely. 

In case you squashed the wrong commits, you can always go back:

1. Make a recovery branch (just in case)

`git checkout -b recovery` 

1. Checkout back:

`git checkout my_branch` 

1. Find commit

`git reflog`

`git reset --hard commit_hash` 

`git rebase -i origin/branch_base`  

`git push origin my_branch --force`

### Adding files/dirs to .gitignore

When working with data/code within your repo, there will be, from time to time, certain files or whole directories that you would like to avoid being accidentally staged and committed to the repo (the dreaded `git add .`). In order to avoid this, you can always modify the `.gitignore` and add any file/directory to it, which will tell git that it should ignore this file and stop tracking it.

In case you have a file, you can just open the `.gitignore` and write: `foo.py` , if this file is in the root of the repo. If it is nested inside of other dirs, you will have to write the relative path from the root to that file: `foo/bar/baz.py`. In case that there is a whole directory that you’d like to be ignored, if it is in the root, you can just do: `foo/`, which will tell git to stop tracking that dir all together (same approach if the dir is nested should be followed as for the file).

Keep in my that `.gitignore` file is being tracked by git and that it is part of the git history, so if any changes are made and the file is saved, be mindful when staging and committing files. In general, `.gitignore` should be modified in such a way that it should “benefit” every single developer, not just a single person making changes in their repo. For example, if it is agreed that `data/` folder will be ignored, this should be true for everyone.