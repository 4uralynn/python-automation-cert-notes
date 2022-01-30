Linux Shell
===========

# Redirecting Streams

The process of redirecting inputs, outputs, or errors to a different destination


```console
#To redirect program output and write to a new file...
ls > new_file.txt
cat new_file.txt
#The result should be a list of directories

#To redirect program output and APPEND to the file (instead of rewriting)...
ls >> new_file.txt
cat new_file.txt
#The result should be the first list, and a second afterwards

#To redirect what is input into a program from the keyboard to a file input...
someprogram < new_file.txt
#only information up until the first newline character will be input.

#To redirect an error message to a file...
cp nonexistant_file copied_file 2> errors.txt

```


## Pipes and Pipelines

**Pipes** connect the output of one program to the input of another in order to pass data
between programs.


```console
#EXAMPLE:
ls -al | less
#Less is a paging program for the terminal, which will display the output of 'ls -al' (directories 
#and info) a page at a time

#Another example:
cat spider.txt | tr ' ' '\n' | sort | uniq -c | sprt -nr | head
#Results (Putting each word in its own separate line):
#	7 the
#	3 up
#	3 spider
#	3 and
#	2 rain
#	2 itsy
#	2 climbed
#	2 came
#	2 bitsy
#	1 waterspout

#tr 	- 	(translate) takes the character ' ' and changes it to '\n'
#sort 	- 	sorts result alphabetically (-nr sorts numerically, in reverse order)
#uniq 	-	displays each result once (-c numbers each original occurance)
#head	-	prints the first 10 lines to stdout
```

# Signalling Processes

**Signals** are tokens delivered to running programs to indicate a desired action

```console
ping htto://www.google.com
#Pushing 'Ctrl-C'is a termination signal called 'SIGINT' causing a process to end cleanly
#Pushing 'Ctrl-Z' is stop signal called 'SIGSTOP'
#Typing 'fg' causes a stopped process to run again.

#Typing 'kill' causes a program to terminate, called 'SIGTERM' -- you must use the PID on a different terminal
ps ax | grep ping
#Returns PID
kill #PID#
```



