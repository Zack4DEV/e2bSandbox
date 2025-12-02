from e2b_code_interpreter import Sandbox


def upload_snippet():
    """
    Uploads the snippet.py file to the sandbox.
    """
    sbx = Sandbox.create()
    with open("../snippet.py", "rb") as file:
        sbx.files.write("/src/agentic/content/threads/suggestion", file)
    return "Upload complete"

if __name__ == "__main__":
    print(upload_snippet())
