import subprocess
import os
import sys
import psutil
import time

INDICATOR_SCRIPT = '/home/kamlesh/p-runner/runner.py'

def is_running():
    for proc in psutil.process_iter(['name', 'cmdline']):
        if proc.info['name'] == 'python3' and INDICATOR_SCRIPT in proc.info['cmdline']:
            return True
    return False

def start():
    if not is_running():
        subprocess.Popen(['python3', INDICATOR_SCRIPT])
        print("Indicator started.")
    else:
        print("Indicator is already running.")

def stop():
    for proc in psutil.process_iter(['name', 'cmdline']):
        if proc.info['name'] == 'python3' and INDICATOR_SCRIPT in proc.info['cmdline']:
            proc.terminate()
            proc.wait()
            print("Indicator stopped.")
            return
    print("Indicator is not running.")

def restart():
    stop()
    time.sleep(1)  # Give it a moment to fully stop
    start()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 indicator_launcher.py [start|stop|restart]")
        sys.exit(1)

    action = sys.argv[1].lower()
    if action == 'start':
        start()
    elif action == 'stop':
        stop()
    elif action == 'restart':
        restart()
    else:
        print("Invalid action. Use 'start', 'stop', or 'restart'.")
        sys.exit(1)