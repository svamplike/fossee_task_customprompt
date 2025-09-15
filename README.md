
#**PLEASE READ THE SUBMIT.MD FIRST FOR THE PROMPT**

# AI Debugging Assistant

This is a testbench as command-line interface (CLI) for the AI Debugging Assistant using the custom prompt and built with the Google Gemini API. 

---




### Gemini API Integration

The prompt is used with the Google Gemini API.

---

### Setup and Installation

To get started with the Socratic Debugging Assistant, follow these simple steps.

1.  **Get a Gemini API Key:**
    * Go to the [Google AI Studio](https://ai.google.dev/).
    * Log in and generate a new API key.
    * **Keep this key secure.**

2.  **Install Required Library:**
    * Open your terminal and install the Google Generative AI library.
    ```bash
    pip install -q -U google-generativeai
    ```

3.  **Configure the API Key:**
    * In the Python script, find the line `genai.configure(api_key="API_KEY")`.
    * Replace `"API_KEY"` with the API key you generated.

---

### Usage

1.  **Run the Script:**
    * From your terminal, execute the Python file.
    ```bash
    python your_script_name.py
    ```

2.  **Follow the Commands:**
    * Use the following commands to interact with the assistant:
        * `/file <path_to_your_file.py>`: Loads your Python code into the assistant.
        * `/desc <your_problem_description>`: Provides a description of the bug you're trying to fix and starts the debugging session.
        * `exit`: Quits the application.


###  Test Case

This test case involves multiple, layered bugs to evaluate the assistant's ability to handle complex logical errors and guide the user through a multi-step debugging process.

#### Problem Description

Write a program that takes a list of student scores, calculates the average score, identifies the highest score, and counts how many students scored above the average.

#### Student's Buggy Code (`test.py`)

```python
scores = [75, 82, 90, 66, 59, 88]
total = 0
for i in range(len(scores)):
    total = scores[i]  # Bug 1: Overwrites total instead of accumulating
average = total / len(scores)

highest = 0
for score in scores:
    if score < highest:  # Bug 2: Should be '>'
        highest = score

above_average_count = 0
for score in scores:
    if score > average:
        above_average_count += 1
    else:
        above_average_count = 0  # Bug 3: Resets count incorrectly

print("Average score:", average)
print("Highest score:", highest)
print("Number of students above average:", above_average_count)


