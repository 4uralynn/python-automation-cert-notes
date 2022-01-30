Bash Scripting
==============

Begin bash scripts with `#!/bin/bash` and name them with the `.sh` extension. 
Like in C++, lines can be ended with `;` and condensed together (see below).


```console

#!/bin/bash

echo "Starting at: $(date)"; echo 

echo "UPTIME"; uptime; echo

echo "FREE"; free; echo

echo "WHO"; who; echo 

echo "Finishing at: $(date)"

```

**Variables** can be defined and used like this:

```console

example=hello
echo $example

```

To *define* a variable, just type it out with an equal sign (no spaces!). And to *execute* the vaiable, remember to add a '$' sign to the beginning.

*See the bash script:* ***example.sh***


## Globs (splat)

The `*` and `?` in bash are called 'globs'. They are the *most common* globs. These are characters that allow us to create sequences of filenames.
Specifically, the `*` is a wildcard character that stands in for any amount of characters, and the `?` stands in as one wildcard character. See below.

```console
echo *.md
#result: bashscripting.md shellinteraction.md

echo ??????????ing.md
#result: bashscripting.md

```

## Conditionals

Conditionals are based on the exit values of commands. For instance, an exit value of '0' means success. Starting the conditional block with `if`, you should end it with `fi`


```console

#!/bin/bash

if grep "127.0.0.1" /etc/hosts; then
	echo "Everything ok"
else
	echo "ERROR! 127.0.0.1 is not in /etc/hosts"
fi

```

Running *example2.sh*, you should get the following result:

```console

127.0.0.1       localhost
Everything ok

```

The `test` command evaluates the conditions received on exit to verify that there is an exit status of 0 when the conditions are true, and 1 when they are false. You can also use brackets with spaces in place of the *test* command: `if [ brackets ]; then`
