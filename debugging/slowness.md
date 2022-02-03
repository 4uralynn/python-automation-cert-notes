Understanding Slowness
======================

Modern-day computers may seem like resources are *unlimited*, but if you open 
enough open appplications, the you will eventually run out of memory and the 
computer *will* slow. A good practice is to close any applications not 
currecntly needed.We may even need to look at applets, extensions, plugins, or 
other small programs. Closing browser tabs and documents can also help.

## Identifying the Bottleneck

To address slowness, the *general strategy* is to **identify the bottleneck**.

The bottleneck slowing down the computer could be:
  + CPU time
  + RAM
  + Video memory
  + Reading data from the disk
  + waiting for network data
  + transfering data from one drive/memory allocation to another

If we've closed or deleted things that were unnecessary and the comput is still
slow, look into other explanations:
  + Outdated or insufficient hardware
    - the `top` command in **Linux** shows how the processes are using CPU time or memory
    - In **Linux** you can use `iotop` and `iftop`, to see which processes are using the most disk space or network bandwith
    - **MacOS** has the *Activity Monitor* tool to monitor these resources, as well as energy
    - **Windows** operating systems have *Resource Monitor* and *Performance Monitor*

The first step is *always* to open up one of the above tools. Check whats going 
on and try to understand which resource is ***the bottleneck*** and why.

## Resource Interaction

When an application accesses data, the time spend retrieving it depends on where 
it is located.

Access Speeds, from fastest to slowest

  1. If it is a variable currently being used in a function, it is being accessed from the **CPU internal memory**
  2. If related to a running program, but not the currently executing function, the data will be in **RAM**
  3. Data in a file will be stored on local **disks**
  4. Reading information from **over a network** is the slowest, stored on remote disks, with added transmission speeds

It may be **better figure out if you can temporarily store data on disk** if 
consistently pulling data from the network.

Similarly, it may be better to store data in a ***cache*** to use **within processes memory**. 
A **cache** stores data in a form that's faster to access than it's original form/configuration.

  + A web proxy stores websites, images, or videos that are accessed often, so they don't need to download every time
  + A DNS server will *cache* websites to sent back to queries 
  + The OS caches as much information in RAM as possible, so it can be accessed quickly.
    - If the **RAM is filled up**, 
      * The OS will remove elements from the memory that are not currently in use, then if there is still not enough space...
      * The OS will cache parts of memory not currently in use on the hard disk, in a place called **swap** 

A **Memory Leak** is memory which is no longer needed, but is not getting 
released. While a computer may have too many applications open or may just 
not have enough RAM, one final issue to check for is the *memory leak*. A 
single program could have **memory leak, causing it to use up all the** 
**available memory**.

## Troubleshooting Slowness

**The first step is to ask WHEN** the computer is slow.
  + On start-up?
    - *Too many boot* applications.
  + After days of running?
    - Program in frozen state
    - Program auto-creating data, but does not *auto-delete* (code-fix or regular restart)
    - If log file, rotate out the log file.
  + If on network and program loads slowly
    - Make sure programs main directory is *local*
  + When reading to the hard disk (use OS utilities)
    - Hardware/drive errors
  + On website/Internet access
    - Malicious foreign program

 
## Monitoring Tools

Apache Benchmark tool can be used with command `ab`. This tool is useful for testing if
a website is *acting as expected*.

For example, to get the **average timeing of 500 requests**, type `ab -n 500 site.example.com/`

If the timing of the request is slow, you can ssh in and again use `top` to diagnose further.
When using the `top` command, the **load average* should be less than the amount of processors.

We can **change process priorities** in linux. The *lower the number*, the *higher* the priority.
Processes start with a priority of '0' *by default*, and range to '19'. We can change with the 
command `nice`, which will **start a process with a different priority**. The command `renice` 
will change the priority of a process that is ***already running***.

The `pidof` command receives a process name and returns all the PIDs, and we can use that in
loops as like the example: `for pid in $(pidof process_name); do renice 19 $pid; done` 

The command `ps ax` shows all running processes on the computer.

The `locate` command allows you to locate a file or directory on the disk.

The `killall` commant can utilize `killall -STOP` to send a stop signal but not kill the 
process completely. It can then utilize the `killall -CONT` to continue the process by name
or PID.
