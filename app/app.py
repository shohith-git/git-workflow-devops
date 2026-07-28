import platform
import socket
import getpass
from datetime import datetime

print("=" * 40)
print("Git Workflow DevOps Demo")
print("=" * 40)

print(f"Hostname        : {socket.gethostname()}")
print(f"Current User    : {getpass.getuser()}")
print(f"Operating System: {platform.system()}")
print(f"OS Version      : {platform.release()}")
print(f"Machine         : {platform.machine()}")
print(f"Python Version  : {platform.python_version()}")
print(f"Current Time    : {datetime.now()}")