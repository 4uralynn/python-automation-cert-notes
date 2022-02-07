Managing Resources
==================

This module includes management of computer resources, most of which are fairly self-explanatory,
or have been adequately covered in other modules with no significantly new information. Such as
memory and disk space **Due to previous experience with C++**, the notes on memory leaks are
limited to new information, regarding how to resolve similar issues in Python. 

*These notes predominantly focus on network resources for these reasons.*


## Network Saturation

If dealing with a network service that isn't up to speed, you may **need more details about the**
**connection**. The **two most important factors** that determine the time it takes for data to send
over a network are the ***latency and bandwidth** of the connection.

  + ***Latency*** is the **the delay** ***(in time)*** *between sending* a byte of data from one point *and recieving* at the other.
    - *Directly affected* by the *physical distance* between the two points, and the *amount of intermediate devices* between them. 
  + ***Bandwidth** is **how much data** ***(in megabits)*** can be sent and received in one second ***(megabits/second)***.
    - The *data capacity of a connection*.
    - *Usable bandwidth* is determined by the available bandwidth at each end point, and *every hop in between*.

When figuring out download times, **no matter the bandwidth, the initial** ***latency*** **will always**
**be a percentage of the time** to send the date. *This is important to consider when deciding*
*network resource placement*.
  + **When transmitting many small pieces of data,** latency matters more.
    - In this case, you want the distance between the user and server are as close as possible.
      * An average of **50 ms**, and in the worst case, 100 ms.
    - Latency also *increases when there are too many connections sharing the network*.
  + Bandwidth matters more **when transmittint large pieces of data**.
    - In this case, it matter less where the server is hosted, than the capacity of your connection.

The command `iftop` can tell how much data each application/connection is sending over the network. 

**Traffic shaping** is a way of *marking the data packets* sent over the network with *different* 
*priorities* to avoid having huge chunks of data use all of the bandwidth. It allows you to 
*restrict how much each application/connection on the network takes*.

## Memory Leaks (in Python)

**A Practical Example of What's Going On:**
Using the command `uxterm &` will open a terminal with a **very long scroll buffer**. Running
`od -cx /dev/urandom` inside the terminal will generate random numbers as both characters and
hexidecimal numebrs, and will quickly fill the buffer, and take a large percentage of memory.

In a different terminal, opening `top` can pressing **Shift+M** will order the processes in
terms of how much memory they are using. If you stop the current process in the *uxterm*
terminal using **Ctrl+C**, you can still see the process at the top of the readings.
**The process within uxterm has been stopped, but with uxterm's scroll buffer still loaded,**
**the memory has not been realeased**. This is a good example of a memory leak, although
***most memory leaks*** *happen far more slowly, and* ***less noticably***.

**Keeping track of the values in** `top` is usually how any memory leak investigation begins.

Once we see that a process is over-using memory, use a **memory profiler**. Simply very 
complex scripts befor use. 

The `memory_profiler` library can be **imported in Python** scripts to figure out where the
memory is going. There are many other memory profilers in Python that can also be used, 
like the `guppy` library.


```python

import memory_profiler


def function1(arg1, arg2)
	'''[Some code]'''

@profile  # Tells the profiler to analyze memory consumption
def main()
	function1(arg1, arg2)

```

___

**NOTE:**

The `@profile` label in the above code is called a ***decorator***, which *adds extra behavior*
*to functions* without having to modify the code.

___



