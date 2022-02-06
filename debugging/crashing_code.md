Code That Crashes
=================

When fixing *someone else's code*, there can be thousands of lines to read through. So it is best
to:
  1. Read the **comments**.
  2. Implement **testing** modules to try to understand the code and it's errors better.
  3. **Start at the affected function** and work your way out.
  4. If it is in a programming language you do not yet know, you may still be able to **figure out enough to fix the error**.
  5. It is best to **develop these skills before they are necessary**, look a program you use and have access to the code (or use GitHub) and read until you understand what the code is doing.


## Segmentation Faults (C++ and other low-level languages)

When an application crashes, it is usefult to have a core file for the crash. So we would need to
**tell the OS that we want to generate a core file** by typing `ulimit -c unlimited`. The **-c** flag
and **'unlimited** option state that we want to generate a ***core file*** with *no size limit*. This
will produce a file named `core`.

In order to **read the core file**, we will use the **gdb debugger**, with the **-c** flag, the **core**
file name, and the **name of the executable** with the error:  `gdb -c core example`.

  + Once verifying the location of the segmentation fault, use the `backtrace` command to see the full **backtrace of the functions that caused the crash**. 
  + Use the `up` command to **move to the calling function** in the backtrace. 
  + **Get more context** for the code that failed by calling the `list` command. This will show the lines surrounding the line that caused the issue.
  + The `print` *command in gdb* can be used to print the value of a variable at crash.


## Exception Crashes in Python (and other high-level languages)

When the *Traceback* of an exception doesn't give enough information, use Python debugger **pdb3** along
with the **script name** and any other **parameters** included: `pdb3 script.py necessary_file.csv`

  + Run through the script line by line using the `next` command, or use the `continue` command to run the script until it crashes.
  + Use the `print()` function to show the value of variables at the crash.

 






