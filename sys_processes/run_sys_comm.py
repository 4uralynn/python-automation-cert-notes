import subprocess

#Running System Commands

#The 'subprocess' method allows you to run commands, similar to using 'os.system{"ls -al")',
#But formatted into a list of strings, like the outputs from "sys.argv"

subprocess.run(["date"])
#Results:
#Tue Jan 18 12:10:56 AM PST 2022
#CompletedProcess(args=['date'], returncode=0)
subprocess.run(["sleep", "2"])
#Python is parent process, which implemented the child process (subprocess) 'sleep'
#until the two seconds of the sleep process specified were completed, nothing could be
#typed in Python. A parent process cannot continue until the child process completes
#subprocess input list is the same as the sys.argv outputs (a list of strings)

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.returncode)
#Result: 0
print(result.stdout)
#Results: b'8.8.8.8.in-addr.arpa domain name pointer dns.google.\n'
#The 'b' at the beginning communicates that this is a byte array, an unencoded string.
#In order to use the output string, we will have to use the 'decode' method
print(result.stdout.decode().split())

#In combination with the str 'split' method, we can create a list of strings with 'decode'
#You can capture the 'stdout' stream output, like above, and also do the same for
#other streams, like 'stderr'
