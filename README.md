# Password Strength Checker

A simple Python-based tool for analyzing password strength using basic security rules.

This project was built as a beginner cybersecurity-focused Python project to practice string handling, loops, conditions, Boolean flags, and basic password analysis.

## Features

* Checks password length
* Detects numbers
* Detects uppercase characters
* Detects lowercase characters
* Detects special characters
* Calculates a password score
* Classifies password strength as:

  * Weak
  * Medium
  * Strong

## Password Requirements

The checker looks for:

| Requirement                     | Score |
| ------------------------------- | ----: |
| At least 8 characters           |    +2 |
| Contains a number               |    +2 |
| Contains an uppercase character |    +2 |
| Contains a lowercase character  |    +2 |
| Contains a special character    |    +2 |

Maximum score: **10/10**

## Example

```text
---------------------------------------------
A Simple Code for Checking Password Strength
You password must have least 8 Chracter You Can Use: a-A , 0-9 , $@!
---------------------------------------------

Enter your password: Hello123!

Password Analysis
---------------------------------------------
Number Character: OK
Uppercase Character: OK
Lowercase Character: OK
Special Character: OK

Strength: STRONG
Password: Hello123!
Score: 10/10
```

## How It Works

The program analyzes the password character by character.

For each character, it checks whether it is:

* A number using `isdigit()`
* An uppercase letter using `isupper()`
* A lowercase letter using `islower()`
* A special character using the `in` operator

Boolean flags are used to keep track of which requirements have been found.

Example:

```python
has_number = False

for character in password:
    if character.isdigit():
        has_number = True
```

Once the password has been analyzed, the program calculates the final score.

## Installation

Clone the repository:

```bash
git clone https://github.com/Lowsignal-Code/Password-Strength-Checker.git
```

Move into the project directory:

```bash
cd Password-Strength-Checker
```

Run the program:

```bash
python password_checker.py
```

## Requirements

* Python 3.x
* No external libraries are required.

## Project Structure

```text
Password-Strength-Checker/
│
├── password_checker.py
└── README.md
```

## What I Practiced

This project helped me practice:

* Variables
* `input()`
* `len()`
* `if / elif / else`
* `while` loops
* `for` loops
* Boolean values
* Flag variables
* String methods
* `isdigit()`
* `isupper()`
* `islower()`
* The `in` operator
* f-strings
* Basic program logic

## Future Improvements

Possible improvements for future versions:

* Add better password strength scoring
* Add password generation
* Hide password input
* Add common-password detection
* Improve the command-line interface
* Split the project into multiple Python modules
* Add automated tests
* Add password entropy estimation

## Disclaimer

This project is intended for educational purposes.

It is a basic password analysis tool and should not be considered a complete password security solution.

## Author

**Daniyal**

Built as part of my journey learning Python and cybersecurity.
