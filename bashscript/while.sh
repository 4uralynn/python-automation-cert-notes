
#!/bin/bash

n=0
command=$1 #same as sys.argv[1]
while ! $command && [ $n -le 5 ]; do 	#similar the to markdown example script, but we are including the argument as a condition
        sleep $n
        ((n=n+1))
	echo "Retry #$n"
done;

