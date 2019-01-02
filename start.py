import subprocess

cmd1 = "rcsoccersim"
cmd2 = "python base_client.py"

subprocess.call(cmd1.split())
subprocess.Popen(cmd2.split())
