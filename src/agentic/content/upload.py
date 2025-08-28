from e2b_code_interpreter import Sandbox

sbx = Sandbox.create()

with open("../snippet.py", "rb") as file:
	sbx.files.write("/src/agentic/content/threads/suggestion", file)
return "Upload complete"
