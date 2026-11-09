# Assignment 6: Exception Handling in Python

## 📌 Project Overview

This project is part of **TuteDude's Python Programming Assignment 6: Exception Handling**.

The objective of this assignment is to develop simple and safe Python programs that handle unexpected user inputs, invalid operations, and runtime errors using Python's exception-handling mechanism.

The assignment demonstrates how to use `try`, `except`, `else`, `finally`, and `raise` to make programs more reliable and user-friendly.

## 🎯 Objectives

* Understand Python exception handling.
* Handle invalid user inputs using `try-except`.
* Handle multiple exceptions using multiple `except` blocks.
* Use the `else` block when no exception occurs.
* Use the `finally` block to execute code regardless of success or failure.
* Raise exceptions using the `raise` keyword.
* Handle common exceptions such as `ValueError`, `ZeroDivisionError`, `TypeError`, `FileNotFoundError`, and `PermissionError`.
* Build simple real-world programs using exception handling.

## 🛠️ Technologies Used

* **Programming Language:** Python 3
* **Code Editor:** Visual Studio Code (VS Code)
* **Terminal:** VS Code Integrated Terminal
* **Version Control:** Git and GitHub (optional)

## 📂 Project Structure

Create the following folder structure:

```text
Assignment6/
│
├── task1.py
├── task2.py
├── task3.py
├── task4.py
├── task5.py
└── README.md
```

### File Description

| File Name   | Description                                      |
| ----------- | ------------------------------------------------ |
| `task1.py`  | Safe Division Utility                            |
| `task2.py`  | Bill Calculator with Error Handling              |
| `task3.py`  | Custom Exception: Age Validator                  |
| `task4.py`  | File Reader with Exception Handling              |
| `task5.py`  | Mini Program: Safe Shopping Cart                 |
| `README.md` | Project documentation and execution instructions |

## 📝 Assignment Tasks

### Task 1: Safe Division Utility

**Objective:** Perform division safely while handling invalid inputs and division by zero.

**Features:**

* Accepts numerator and denominator from the user.
* Converts both inputs into floating-point numbers.
* Handles `ValueError` if the input is not a valid number.
* Handles `ZeroDivisionError` if the denominator is zero.
* Uses `else` to print the result when no exception occurs.
* Uses `finally` to print `Operation Complete`.

**Example Output:**

```text
Enter numerator: 10
Enter denominator: 2
Result: 5.0
Operation Complete
```

### Task 2: Bill Calculator with Error Handling

**Objective:** Calculate the total of valid product prices while skipping invalid items.

**Input List:**

```python
prices = [120, 350, 'abc', 500, -200, 800]
```

**Features:**

* Iterates through the product-price list.
* Adds only valid, non-negative numerical prices.
* Raises and handles `TypeError` for non-numeric values.
* Raises and handles `ValueError` for negative prices.
* Skips invalid items and continues processing.
* Prints the final running total.

**Expected Output:**

```text
Type Error: Price must be a number.
Value Error: Negative price not allowed
Running Total: 1770
```

### Task 3: Custom Exception — Age Validator

**Objective:** Validate a user's age and raise an exception when the age is outside the permitted range.

**Features:**

* Defines a function named `check_age(age)`.
* Accepts age as input from the user.
* Raises `ValueError` if age is less than 1 or greater than 120.
* Handles the exception using `try-except`.
* Displays a suitable error message.

**Example Output:**

```text
Enter your age: 150
Error: Age must be between 1 and 120
```

### Task 4: File Reader with Exception Handling

**Objective:** Read a text file safely while handling common file-access errors.

**Features:**

* Accepts a filename from the user.
* Attempts to open and read the file.
* Handles `FileNotFoundError` if the file does not exist.
* Handles `PermissionError` if access is denied.
* Prints the first three lines when reading succeeds.
* Uses `finally` to print `File operation attempted.`

**Example Output:**

```text
Enter filename: sample.txt
First 3 lines of the file:
This is line one.
This is line two.
This is line three.

File operation attempted.
```

**Note:** Create a text file named `sample.txt` in the same folder as `task4.py` to test successful file reading.

### Task 5: Mini Program — Safe Shopping Cart

**Objective:** Create a simple shopping-cart program that accepts valid prices and calculates the final bill.

**Features:**

* Creates an empty list named `cart`.
* Uses a loop to accept product prices.
* Stops accepting prices when the user enters `q`.
* Converts valid inputs into floating-point numbers.
* Handles invalid inputs using `ValueError`.
* Raises `ValueError` if the price is negative.
* Stores only valid, non-negative prices.
* Displays the total number of items and the total bill.

**Example Output:**

```text
Enter item price (or 'q' to quit): 100
Price added successfully.
Enter item price (or 'q' to quit): 250
Price added successfully.
Enter item price (or 'q' to quit): q

Total items: 2
Total bill: 350.0
```

## ⚙️ Requirements

Before running the programs, ensure that:

1. Python 3 is installed on your computer.
2. Visual Studio Code is installed.
3. The Python extension for VS Code is installed.
4. The assignment files are saved with the `.py` extension.

No external Python libraries are required.

## 🚀 How to Execute the Programs

### Step 1: Install Python

Download Python from the official website:

https://www.python.org/downloads/

During installation on Windows, select **Add Python to PATH** if that option is available.

### Step 2: Verify Python Installation

Open Command Prompt or the VS Code terminal and execute:

```bash
python --version
```

If the command is not recognized, try:

```bash
py --version
```

A Python 3 version should be displayed.

### Step 3: Open the Project in VS Code

1. Open Visual Studio Code.
2. Select **File → Open Folder**.
3. Select your `Assignment6` folder.
4. Create the five Python files and paste the corresponding task solutions into them.
5. Save each file using `Ctrl + S`.

### Step 4: Run a Program

Open the VS Code terminal using:

**Terminal → New Terminal**

Navigate to the project folder if necessary:

```bash
cd Assignment6
```

Run any task separately:

**Task 1 — Safe Division**

```bash
python task1.py
```

**Task 2 — Bill Calculator**

```bash
python task2.py
```

**Task 3 — Age Validator**

```bash
python task3.py
```

**Task 4 — File Reader**

```bash
python task4.py
```

**Task 5 — Shopping Cart**

```bash
python task5.py
```

On Windows, if `python` does not work, use `py` instead. For example:

```bash
py task1.py
```

### Step 5: Test the Programs

Try both valid and invalid inputs to verify that exception handling works correctly.

| Task   | Test Case             | Expected Behavior                 |
| ------ | --------------------- | --------------------------------- |
| Task 1 | `10` and `2`          | Displays `5.0`                    |
| Task 1 | Denominator `0`       | Handles `ZeroDivisionError`       |
| Task 1 | Enter `abc`           | Handles `ValueError`              |
| Task 2 | List contains `'abc'` | Skips the invalid item            |
| Task 2 | List contains `-200`  | Rejects the negative price        |
| Task 3 | Age `25`              | Displays valid age                |
| Task 3 | Age `150`             | Displays an age validation error  |
| Task 4 | Existing text file    | Displays the first three lines    |
| Task 4 | Missing text file     | Handles `FileNotFoundError`       |
| Task 5 | Price `100`           | Adds the price to the cart        |
| Task 5 | Price `-50`           | Rejects the negative price        |
| Task 5 | Input `q`             | Stops input and displays the bill |

## 📚 Concepts Learned

### 1. `try`

Contains code that may generate an exception.

### 2. `except`

Handles an exception and prevents the program from terminating unexpectedly.

### 3. Multiple `except` Blocks

Allow a program to handle different types of exceptions separately.

### 4. `else`

Executes only when the associated `try` block completes without an exception.

### 5. `finally`

Executes whether an exception occurs or not, making it useful for operations that must always be performed.

### 6. `raise`

Manually generates an exception when a condition is invalid.

### 7. Common Exceptions

* `ValueError`: A value has an inappropriate format or is outside an allowed range.
* `ZeroDivisionError`: Division by zero is attempted.
* `TypeError`: An operation receives an inappropriate type.
* `FileNotFoundError`: The requested file cannot be found.
* `PermissionError`: The operation is not permitted because of access restrictions.

## ✅ Conclusion

This assignment demonstrates how Python exception handling can make programs safer, more reliable, and easier to use.

By completing these five tasks, I practised handling invalid inputs, validating data, managing runtime errors, and ensuring that programs continue processing when recoverable errors occur.

The assignment strengthened my understanding of Python's exception-handling mechanisms and their practical applications in everyday programming.

---

**Assignment:** 6 — Exception Handling

