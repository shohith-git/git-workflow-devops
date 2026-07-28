import platform
import socket

print("Git Workflow DevOps Demo")
print(f"Hostname: {socket.gethostname()}")
print(f"Operating System: {platform.system()}")
print(f"OS Version: {platform.release()}")