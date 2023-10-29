import subprocess
import sys

if __name__ == "__main__":
    subprocess.run(["python", "explainer-dashboard.py", "&"]) 
    subprocess.run(["streamlit", "run", "main.py", "&"]) 
