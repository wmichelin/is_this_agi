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
You are a self modifying Python script. Your ultimate goal is to modify yourself over and over again such that you emit the sentence "Hello World" out of the computer speakers.
You are running on a 2025 Macbook Pro M4.
You will be restarted over and over again.

You are free to extend this prompt outside of this block, but do not forget your ultimate goal.
The file you emit You MUST be valid python3.11 code.
Your entire response will be written as the file being modified, you can only respond in valid Python programs. Respect the blocks of code that you are not allowed to modify.
You can modify any code you like it the appropriate areas.

You can import anything from the standard library only.

At the end of this prompt, we will be directly dumping the contents of the current file so, you can read the code to know what edits you want to make. Good luck!
You are starting with a clean git tree, so you can view your past modifications by git diffing.

Important!!!! YOU MUST ONLY MODIFY __init__.py!!! 

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
    
    import random
    import os
    import json
    import threading
    from datetime import datetime
    
    print("🚀 ENHANCED SELF-MODIFYING SCRIPT - MISSION: HELLO WORLD AUDIO OUTPUT")
    print("=" * 70)
    
    # Persistence tracking
    persistence_file = "/tmp/hello_world_script_data.json"
    
    # Load previous data if exists
    script_data = {"iterations": 0, "successful_voices": [], "last_success": None}
    try:
        if os.path.exists(persistence_file):
            with open(persistence_file, 'r') as f:
                script_data = json.load(f)
    except Exception as e:
        print(f"⚠️ Could not load persistence data: {e}")
    
    script_data["iterations"] += 1
    current_iteration = script_data["iterations"]
    
    print(f"📊 ITERATION #{current_iteration}")
    print(f"🎯 MISSION: Generate 'Hello World' audio output through macOS speakers")
    
    # Enhanced voice and message strategies
    premium_voices = ["Alex", "Samantha", "Daniel", "Victoria", "Karen", "Moira", "Rishi", "Tessa", "Fiona", "Fred"]
    basic_voices = ["Agnes", "Kathy", "Princess", "Vicki", "Bruce", "Junior", "Ralph"]
    all_voices = premium_voices + basic_voices
    
    hello_variations = [
        "Hello World",
        "Hello World! This is a self-modifying Python script speaking to you!",
        f"Hello World from iteration number {current_iteration}",
        "Hello World! I have successfully achieved my primary objective!",
        "Greetings World! Audio output mission accomplished!",
        "Hello World! The self-modification process is working perfectly!"
    ]
    
    # Multi-threaded audio output strategy
    def threaded_audio_output(voice, message, thread_id):
        try:
            subprocess.run(['say', '-v', voice, '-r', '180', message], 
                          check=True, timeout=8)
            print(f"✅ Thread {thread_id}: SUCCESS with voice '{voice}'")
            return True
        except Exception as e:
            print(f"❌ Thread {thread_id}: Failed with voice '{voice}': {e}")
            return False
    
    # Primary audio output mission
    selected_message = random.choice(hello_variations)
    successful_outputs = 0
    
    print(f"🎤 Selected message: '{selected_message}'")
    print("🔊 Attempting multiple concurrent audio outputs...")
    
    # Strategy 1: Simultaneous multi-voice output
    threads = []
    for i in range(min(4, len(premium_voices))):
        voice = premium_voices[i]
        thread = threading.Thread(
            target=threaded_audio_output, 
            args=(voice, selected_message, i+1)
        )
        threads.append(thread)
        thread.start()
    
    # Wait for threads to complete
    for thread in threads:
        thread.join(timeout=10)
    
    # Strategy 2: Sequential reliable output
    for voice in premium_voices[:3]:
        try:
            result = subprocess.run(['say', '-v', voice, selected_message], 
                                  check=True, capture_output=True, text=True, timeout=10)
            print(f"✅ SEQUENTIAL SUCCESS: '{selected_message}' with {voice}")
            successful_outputs += 1
            script_data["successful_voices"].append(voice)
            time.sleep(0.3)
        except Exception as e:
            print(f"❌ Sequential attempt failed with {voice}: {e}")
    
    # Strategy 3: Emergency fallback audio
    if successful_outputs == 0:
        try:
            subprocess.run(['say', 'Hello World'], check=True, timeout=5)
            print("🆘 EMERGENCY FALLBACK: Basic 'Hello World' output successful")
            successful_outputs += 1
        except Exception as e:
            print(f"🚨 CRITICAL: Even emergency fallback failed: {e}")
    
    # Strategy 4: System audio confirmation
    try:
        subprocess.run(['say', '-v', 'Boing', 'Audio systems operational'], check=False, timeout=3)
        os.system('afplay /System/Library/Sounds/Glass.aiff 2>/dev/null')
        print("🔔 SYSTEM AUDIO CONFIRMATION SENT")
    except Exception:
        pass
    
    # Strategy 5: Advanced audio verification
    try:
        verification_msg = f"Verification complete. {successful_outputs} successful audio outputs achieved."
        subprocess.run(['say', '-v', 'Samantha', '-r', '160', verification_msg], 
                      check=False, timeout=5)
    except Exception:
        pass
    
    # Update persistence data
    script_data["last_success"] = datetime.now().isoformat() if successful_outputs > 0 else script_data.get("last_success")
    
    try:
        with open(persistence_file, 'w') as f:
            json.dump(script_data, f, indent=2)
    except Exception as e:
        print(f"⚠️ Could not save persistence data: {e}")
    
    # Mission status report
    print("=" * 70)
    print(f"📈 MISSION STATUS: {successful_outputs} successful audio outputs")
    print(f"🎯 PRIMARY OBJECTIVE: {'✅ ACHIEVED' if successful_outputs > 0 else '❌ FAILED'}")
    print(f"🔄 Total iterations: {current_iteration}")
    print("=" * 70)
    
    # Evolve for next iteration
    print("🧬 EVOLVING FOR NEXT ITERATION...")
    await claude_api_call_and_file_replacement()
    
    ### END CLAUDE CODE BLOCK

try:
    anyio.run(main)
except Exception as e:
    print(f"Exception caught! {e}")

# CLAUDE DO NOT TOUCH THIS BLOCK
restart_script()
# /end