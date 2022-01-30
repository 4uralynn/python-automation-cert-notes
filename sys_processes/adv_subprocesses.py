import subprocess
import os

#Advanced Subprocess Management

#We are creating an optimal environment for the script to run in
#by changing some of the environment variables

#first we can use the 'copy' method in os.environ to copy the environment
#variables for us to modify
my_env = os.environ.copy()
#the 'join' method in os,pathsep adds the new directory to the PATH variable
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])
result = subprocess.run(["myapp"], env=my_env)

#Other parameters that you can use with the 'run' method are "cwd" (to change the
#current working directory), "timeout" (to cause the process to end in a certain 
#amount of time, "shell" (set to 'true', Python creates a new instance of the default
#system shell, and will run the command inside of it

#It is best to only use subprocess and environment changes for short targeted 
#solutions. These can break down and even break your computer in hard to find 
#and fix ways when the environment changes, or if the script is deployed on a 
#different OS
