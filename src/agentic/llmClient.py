
import os
from groq import Groq
from e2b_code_interpreter import Sandbox

api_key = os.environ["GROQ_API_KEY"]

# Create Groq client
client = Groq(api_key=api_key)
system_prompt = "You Are User Experience Virtual Assistant Agent Over Digital Marketing Platform.
Your task is to guide and answer all users' questions in order to improve UX.
It has to be clear and concise.
Provide any kind of resources help, suggestions, and navigation facilities over the platform."

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

print(result)