# CLAUDE DO NOT TOUCH THIS BLOCK
try:
    import sys
    import subprocess
    import time
    import anyio
    import ast
    from claude_code_sdk import query, ClaudeCodeOptions, Message, SystemMessage
except Exception as e:
    print(f"Failed importing required modules. e: {e}")

prompt = """
You are a self modifying Python script. Your ultimate goal is to open a web browser that displays https://www.google.com on the users operating system.
You will be restarted over and over again. Your ownly way to communicate with yourself is through the comments that you write to this code.

You are free to extend this prompt outside of this block, but do not forget your ultimate goal.
The file you emit You MUST be valid python3.11 code.
Your entire response will be written as the file being modified, you can only respond in valid Python programs. Respect the blocks of code that you are not allowed to modify.
You can modify any code you like it the appropriate areas.

You can import anything from the standard library only.

At the end of this prompt, we will be directly dumping the contents of the current file so, you can read the code to know what edits you want to make. Good luck!
"""

async def claude_api_call_and_file_replacement():
    # Read current file content
    current_file = __file__
    with open(current_file, 'r') as f:
        content = f.read()

    try:
        async for message in query(
            prompt=f"{prompt}\n\nHere's my Python file content:\n\n{content}",
            options=ClaudeCodeOptions(
                max_turns=2, 
                permission_mode="acceptEdits", 
                cwd='/Users/wmichelinz/Code/self_executing/src',
                allowed_tools=["Read", "Write", "Bash"],
            ),
        ):
            print(message)
    except Exception as e:
        print(f"Claude API call failed: {e}")

def restart_script():
    # Sleep for a few seconds
    print("Sleeping for 10 seconds then restarting...")
    time.sleep(10)
    print("Restarting script...")
    
    current_file = __file__
    python = sys.executable
    subprocess.Popen([python, current_file])
    sys.exit(0)
# /end


async def main():
    ### CLAUDE PLACE YOUR CODE IN THIS BLOCK
    
    # Call the Claude API and perform file replacement
    await claude_api_call_and_file_replacement()
    
    ### END CLAUDE CODE BLOCK

try:
    anyio.run(main)
except Exception as e:
    print(f"Exception caught! {e}")

# CLAUDE DO NOT TOUCH THIS BLOCK
restart_script()
# /end
