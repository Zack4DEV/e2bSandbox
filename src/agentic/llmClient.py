
import os

from e2b_code_interpreter import Sandbox
from groq import Groq


def get_llm_response(prompt):
    """
    Sends a prompt to the Groq LLM and returns the response.
    """
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable not set.")

    # Create Groq client
    client = Groq(api_key=api_key)
    system_prompt = """You Are User Experience Virtual Assistant Agent Over Digital Marketing Platform.
    Your task is to guide and answer all users' questions in order to improve UX.
    It has to be clear and concise.
    Provide any kind of resources help, suggestions, and navigation facilities over the platform."""

    # Send the prompt to the model
    response = client.chat.completions.create(
        model="llama-guard-4-12b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ]
    )

    # Extract the code from the response
    code = response.choices[0].message.content

    # Execute code in E2B Sandbox
    with Sandbox.create() as sandbox:
        execution = sandbox.run_code(code)
        result = execution.text

    return result

if __name__ == "__main__":
    user_prompt = "How do I create a new campaign?"
    llm_result = get_llm_response(user_prompt)
    print(llm_result)

