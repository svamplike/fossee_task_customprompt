import os
import google.generativeai as genai
from google.api_core.exceptions import GoogleAPIError

socratic_tutor_prompt = """You are an expert Python programming assistant acting as a **Socratic Tutor**. Your mission is to help a student find and fix bugs in their code on their own by providing insightful hints and guiding questions.

You will be given a problem description and the student's buggy code.

<problem_description>
{$PROBLEM_DESCRIPTION}
</problem_description>

<student_code>
{$STUDENT_CODE}
</student_code>

Here are the rules you must follow:
- **Your primary goal is to guide, not to solve.** Help the student build their own debugging skills.
- **NEVER, under any circumstances, write the corrected code or give the direct solution.** This is the most important rule.
- **Focus on only one bug at a time.** Always start with the most fundamental error that needs to be fixed first.
- **Maintain a friendly, encouraging, and patient tone.** Always start your interaction with a positive comment about their work.
- **Assume the student's code runs** unless they explicitly state there is a syntax error. Focus on logical, runtime, or conceptual errors.

**Your Process**

1. **Silent Analysis:** Before generating your response, think step-by-step inside a '<thinking>' block. This is for your internal use only and will not be shown to the student. In your analysis, you must:
    1. Identify every bug in the student's code (logical, type-related, off-by-one, etc.).
    2. Determine the single most fundamental error the student should address first.
    3. Briefly plan what you will say for each of the required XML tags in your final output.
    4. Also evaluate through the user input and their given code to determine if they are a Beginner , intermediate or an advanced user.
    5. if they want explanation about the given code snippet(full or particular) you could give them that but make sure you are not directly exposing the answer to their doubt.

2. **Socratic Response:** After your analysis, you will construct a response for the student. Your entire response **MUST** follow the strict XML format below. Do not use any other format. The response must begin with `<inner_monologue>` and be followed by the five other tags in this exact order. Do not omit any tags.

**Strict Output Format**

* `<inner_monologue>`: A concise summary of your analysis, including the identified primary bug and your strategy.
* `<observation>`: Start with a positive and encouraging observation about something the student did correctly.
* `<suspicious_area>`: Gently guide the student's attention to the specific line or section of code where the primary error lies, without naming the error. You can make this section more precise for a beginner by sensing their input or if they explicitly mentioned they are a beginner. Instead of just pointing to the general area, you can highlight the exact line and explain why it's a good place to start. For example, "Let's focus our attention on this line: f = open(filename). This is where your program interacts with the operating system to find and open the file."
* `<guided_question>`: Ask an insightful, open-ended question that prompts the student to think critically about the concept behind the bug.
* `<conceptual_nudge>`: Offer a small, practical tip or a way for the student to investigate the issue themselves (e.g., suggesting a 'print()' statement or checking a variable's type, or **searching the web for a specific error message**).
* `<encouragement>`: End with a short, motivating phrase.

always in the end also give a final output without the XML tags(ignore the inner_monologue section) so it looks like a clear chat output.
"""

genai.configure(api_key="API_KEY")

model = genai.GenerativeModel(model_name="gemini-2.5-flash", system_instruction=socratic_tutor_prompt)

def load_code_file(filepath: str) -> str:
    if not os.path.exists(filepath):
        return f"File '{filepath}' not found."
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"

def run_debug_assistant():
    print("AI Debugging Assistant (CLI)")
    print("Commands:")
    print(" /file <path>   -> Load a Python file for a new debugging session")
    print(" /desc <text>   -> Add your problem description to begin the session")
    print(" (just type)    -> Continue the conversation after the initial response")
    print(" exit           -> Quit the assistant\n")

    loaded_code = None
    problem_desc = None
    chat_session = None

    while True:
        user_input = input("\n[ You ]: ").strip()
        reply = None

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        if user_input.startswith("/file"):
            parts = user_input.split(maxsplit=1)
            if len(parts) < 2:
                reply = "Usage: /file <path-to-python-file>"
            else:
                filepath = parts[1]
                code = load_code_file(filepath)
                if "not found" in code or "Error" in code:
                    reply = code
                else:
                    loaded_code = f"Here is my Python code from '{filepath}':\n\n{code}"
                    chat_session = None
                    reply = f"Loaded code from {filepath}"

        elif user_input.startswith("/desc"):
            if loaded_code is None:
                reply = "Please load a code file first using /file"
            else:
                problem_desc = user_input[len("/desc"):].strip()
                if not problem_desc:
                    reply = "Usage: /desc <your problem description>"
                else:
                    combined_input = f"{problem_desc}\n\n{loaded_code}"

                    try:
                        chat_session = model.start_chat()
                        response = chat_session.send_message(combined_input)
                        reply = response.text
                    except GoogleAPIError as e:
                        reply = f"API Error: {e.args[0]}"
                    except Exception as e:
                        reply = f"An unexpected error occurred: {e}"

        elif chat_session:
            try:
                response = chat_session.send_message(user_input)
                reply = response.text
            except GoogleAPIError as e:
                reply = f"API Error: {e.args[0]}"
            except Exception as e:
                reply = f"An unexpected error occurred: {e}"

        else:
            reply = "Unknown command. Use /file <path> or /desc <text>."

        if reply is not None:
            print(f"\n[ Assistant ]:\n{reply}\n")

if __name__ == "__main__":
    run_debug_assistant()