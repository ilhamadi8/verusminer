import subprocess
import threading
import time

# Define the command to run
command = ['bash', 'miner.sh']

def run_command():
    while True:
        # Start the subprocess
        process = subprocess.Popen(command)
        
        # Define a function to kill the process
        def kill_process():
            process.kill()
            print("Subprocess killed")
        
        # Start a timer to kill the process after 3 minutes (180 seconds)
        timer = threading.Timer(180, kill_process)
        timer.start()

        # Wait for the process to complete
        process.wait()

        # Cancel the timer if the process completes before 3 minutes
        timer.cancel()
        
        # Optional: Add a small sleep to prevent a tight loop in case of immediate subprocess termination
        time.sleep(60)  # Adjust the sleep duration as necessary

# Run the command in a loop
run_command()
