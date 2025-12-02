from dotenv import load_dotenv
from e2b_code_interpreter import Sandbox


def main():
    """
    Main function to demonstrate E2B sandbox usage.
    """
    load_dotenv()
    sbx = Sandbox.create()
    execution = sbx.run_code("print('Hello, By e2b.dev Runtime Sandbox - Code interpretation in progress...')")
    print(execution.logs)

    files = sbx.files.list("agentic/")
    print(files)

if __name__ == "__main__":
    main()
