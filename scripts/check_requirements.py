import subprocess
import sys

result = subprocess.run([sys.executable, "-m", "pip_check_reqs.find_missing_reqs", "src"], capture_output=True, text=True)

if result.stdout:
    print(result.stdout)
if result.stderr:
    print(result.stderr)

if result.returncode != 0:
    print("Missing dependencies found!")
    raise SystemExit(1)

print("Requirements check passed.")