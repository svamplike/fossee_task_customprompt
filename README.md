
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

The user is attempting to write a Python script that reads data from a JSON file, filters the data based on a specific key-value pair, and then calculates the average of a numerical field from the filtered results. The script should also handle cases where the file does not exist or the data is in an incorrect format. The user believes the code is logically sound but is getting an unexpected `KeyError` and incorrect average values.

#### Student's Buggy Code (`test.py`)

```python
import json

def process_data(filename, filter_key, filter_value, calc_field):
    with open(filename, 'r') as file:
        data = json.load(file)

    filtered_items = []
    for item in data:
        if item[filter_key] == filter_value:
            filtered_items.append(item)

    total = 0
    count = 0
    for item in filtered_items:
        total += item[calc_field]
        count += 1

    if count == 0:
        return 0

    return total / count

result = process_data("data.json", "category", "A", "value")

print(f"The average is: {result}")

