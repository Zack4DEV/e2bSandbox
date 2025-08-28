from dotenv import load_dotenv
load_dotenv()
from e2b_code_interpreter import Sandbox

sbx = Sandbox.create()  
execution = sbx.run_code("print('Hello, By e2b.dev Runtime Sandbox - Code interpretation in progress...')") 
print(execution.logs)

files = sbx.files.list("agentic/")
print(files)
