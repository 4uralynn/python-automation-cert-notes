Complexity in Slowness
======================

There are a lot of subtleties to slowness, within the system itself and whatever code is written.
Issues and solutions can both become very complex.

## Writing Efficient Code

When writing your code, you need to try **use the right data structures for the correct situation.**
Looking at the `list` and `dict` data structures in Python makes this easier to understand.

The **list** data structure uses indexing for *direct access* to data stored within, if we
know which index the data is stored in. But if we have to search for a specific data and we
don't know the index, we have to iterate through the whole list. In this case the `dict`
is more efficient since you can use keys to access the data. The order of the keys do not
matter.

You should also avoid **expensive** loops. For instance, if a file needs to be opened and read,
open it before the loop and read the contents into a dictionary (`dict`). Then the loop only
need to be accessed once.

___

**NOTE:**

Using the `time` command, we can measure a script's speed: `time ./script.py`

The outputs return as **real**, **user**, and **sys**. Where **real** is the amount of 
*actual* time spent to execute the commad, **user** is the time spent doing operations in
the user space, and **sys** is the amount of time doing *system-level* operations.

___

## Profilers

We can use **profilers** to get information about what is going on with a script. Profilers
for Python include the ***pprofile3*** profiler. We can use this in conjunction with 
**kcachegrind** (a graphical interface for profiler output):

```console

pprofile3 -f callgrind -o profile.out ./script.py
#the '-f' option tells the file format to be used, which is 'callgrind' in this case
#the '-o' option tells to name the output, in this case as 'profile.out'

#Then call kcachegrind to view the output:
kcachegrind profile.out

```

This can tell us things like how many times each function is called.

## Parallel Operations (Concurrency)

**Parallel operations** are when more than one process is carried out at the same time, and
this can be as simple as calling having the OS call your script multiple times. This is also
called ***concurrency***, and is an entire branch of Computer Scince.

**In Python, parallel operations can be done by importing** the `threading` or `asyncio`
modules. ***Threads*** run *parallel tasks* inside a process. Different programming languages
implement threading in different ways.

If a script is **CPU-bonnd** instead of **I/O -bound**, it may be advantageous to spit threads
into multiple processes, so as you take advantage of multiple CPUs.

When doing operations in parallel, the system may end up taking more time to switch back
and forth between CPUs, disks, and ultimately processes, that it isn't worth being done in 
parallel. *We need to take this into account when writing the code.*


## Growing in Complexity

As programs grow in complexity and usage, the systems become more complex as well.

This is seen in going form a script using a *CSV file*, migrating to utilizing *SQLite files*, and
then using a *database server for multiple files*. If the service becomes popular, it may not be
fast enough for all queries, and may then utilize a *caching service like **memcached***, to keep
the most commonly used results in RAM. Or another caching service like *varnish*, or utilize a
*load balancer* and/or an array of *virtual machines*.

Having a good monitering infrastructure is very important to find bottlenecks in **very large and**
**complex systems**. 

Database server queries can work much faster with *indexes*, but also too many indexes can become
very slow when adding or modifying indexes. Caching the queries can help, as well as modifying the
code to work on a distributed system.

#Using Threads in Python

Importing the `futures` submodule from the `concurrent` module gives us a very simple way to use
Python *threads*.

An **executor** is necessary to run things in parallel. This is *the process that's in charge of*
*distributing the work among different workers*. The **futures** module uses a couple of different
executors, *one for using threads*, and another *for using processes*. In this example, the
`ProcessPoolExecutor()` is used, but there is also the `ThreadPoolExecutor()`


```python

from concurrent import futures

def function1(arg1, arg2)
        print("This is {}".format(arg1))
        return arg2

def function2(arg3, arg4)
        print("We have both {} and {}".format(arg3, arg4))
        return 0

executor = furtures.ProcessPoolExecutor()

def main():
	i = 1
        while i < 21:
#instead of calling the function normally, input it and it's arguments into ProcessPoolExecutor().submit
		executor.submit(function1, arg1, arg2)
		i += 1
#the executor runs the tasks in parallel, using threads.
	print('Waiting for all threads to finish.')
#the 'shutdown' function waits until all threads in the pool are finished, and then shuts down the executor.
	executor.shutdown()
	return 0

```

Using *processes* instead of *threads*, we are making more use of the CPU's. The speed can be a lot faster
in specific applications.
