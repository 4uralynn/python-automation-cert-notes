Advanced Bash Concepts
======================

## 'While' Loops
The syntax is slightly differnt for loops in bash than in python:

```console

#!/bin/bash

n=1
while [ $n -le 5 ]; do			# '-le' is >=
	echo "Iteration number $n"	#The loop begins with 'do'
	((n+=1))			#Double parentheses tells the shell you will perform arithmetic with a variable
done					#the loop ends with 'done'

```

See *while.sh* for example. Run with `./while.sh ./rando.py`. Look at both scripts and see how the bash script compares to this one.


## 'For' Loops

```console

#!/bin/bash

for fruit in peach orange apple; do 	#loops begins with do
	echo "I like $fruit!"

done					#ends with done

```

See *for.sh* to see an example of using bash for loop to change extensions in a directory


## Advanced Command Interaction


---

NOTE:

You can find the system log file in `/var/log/syslog`

---

Look at the last 10 lines of the system log.

```console

tail /var/log/syslog

```

If we wanted to find out which events were being logged the most: We first need to extract the part of the line with the actual event without the date and time.
We can do this with the **cut** command. The **-d** parameter says to uses a *' '* as a delimiter. The *-f5-* tells it to print field 5 and everything afterwards.

```console

tail /var/log/syslog | cut -d ' '  -f5- 

```

We can pipe this information to find out the lines repeated the most:

```console

cut -d' ' -f5- /var/log/syslog | sort | uniq -c | sort -n | head

```

See *toploglines.sh* for a full example, utilizing a for loop.

Bash scripts are wonderful, and powerful. But when they begin to be too complex, it probably would be better to write a **Python** script. Also, bash scripts work fine on Linux, but if you need it to operate on multiple platforms, **Python** would be the better choice. System commands, redirecting, and pipes are powerful with bash script. And in other instances, use whichever you are most comfortable with.
