import datetime
import os
import subprocess
import time

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(REPO_DIR, "activity_log.txt")

def run_cmd(cmd, cwd=REPO_DIR):
    result = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"[-] Command failed: {' '.join(cmd)}\nError: {result.stderr.strip()}")
    else:
        if result.stdout.strip():
            print(f"[+] {result.stdout.strip()}")
    return result.returncode == 0

def make_commits(count=3):
    run_cmd(["git", "config", "user.name", "gokulaan-07"])
    run_cmd(["git", "config", "user.email", "gokulaan9c@gmail.com"])
    
    for i in range(1, count + 1):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"Activity log update #{i}: {now}\n"
        
        with open(LOG_FILE, "a") as f:
            f.write(log_entry)
            
        print(f"[+] Updated log file with entry #{i}: {now}")
        
        run_cmd(["git", "add", "."])
        
        commit_msg = f"chore(activity): update log entry #{i} [{now}]"
        run_cmd(["git", "commit", "-m", commit_msg])
        
        time.sleep(1)

    print("[+] Pushing commits to GitHub...")
    if run_cmd(["git", "push", "-u", "origin", "main", "--force"]):
        print("[+] Successfully pushed commits to GitHub!")
    else:
        print("[-] Push failed. Please check git credentials.")

if __name__ == "__main__":
    make_commits(3)
