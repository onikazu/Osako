import subprocess

cmd1 = "rcsssserver"
cmd2 = "rcssmonitor"
cmd3 = "python base_client.py"

subprocess.Popen(cmd1.split())
subprocess.Popen(cmd2.split())
subprocess.Popen(cmd3.split())
