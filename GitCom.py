import subprocess

subprocess.run(['git', 'add', '-A'])
print("Hello, please enter your commit message below:")
comMsg = input()
subprocess.run(['git', 'commit', '-m','"'+comMsg+'"'])
subprocess.run (['git', 'push'])

# https://github.com/C-Lyngbjerg/PythonA2021