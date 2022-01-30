#!/bin/bash

for file in *.md; do
        name=$(basename "$file" .md)	#The 'basename' command returns a file name without the extension
	echo mv "$file" "$name.MD"	#Remove the 'echo' command, and the extensions will actually change
					#this is a good way to test-run the script (with 'echo')
done;
