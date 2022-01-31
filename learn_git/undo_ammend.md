Undoing and Ammending Changes
=============================

## Undoing *Before* Committing...

This is fairly self-explanatory. In the following example, the *check_reboot()* function is deleted 
from ***all_checks.py***. The script fails when executed, so we undo the change using `git checkout all_checks.py`
to *'checkout'* the current snapshot of the file ***BEFORE A FILE HAS BEEN STAGED***:

The **checkout** command allows you to undo any current, *unstaged* modifications and return to the current snapshot
of a file stored within Git.

```console

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ ./all_checks.py
Traceback (most recent call last):
  File "/home/user/Code/Python/learn_git/checks/./all_checks.py", line 13, in <module>
    main()
  File "/home/user/Code/Python/learn_git/checks/./all_checks.py", line 7, in main
    if check_reboot():
NameError: name 'check_reboot' is not defined

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   all_checks.py

no changes added to commit (use "git add" and/or "git commit -a")

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git checkout all_checks.py
Updated 1 path from the index

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git status
On branch master
nothing to commit, working tree clean

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ ./all_checks.py
Everything is OK.

```

**If a file has already been staged** and you wish to delete it, use the **reset** Git command. Using `git status` will tell you
the proper way to use **reset** on a file in the current staging area. This looks like `git reset HEAD file.name`

  + **Reset** is the counterpart to add. No example is provided since this is so self-explanatory, even within the **git status** command.

## Amending and Rollbacks *After* Committing

The *--amend* option will allow you to overwrite the previous commit after making changes, with `git commit --amend`.
  + You can update the commit message.
  + **DO NOT** use in a public repository. Only use locally, as it completely overwrites previous changes.

```console

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ touch auto-update.py

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ touch gather-info.sh

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ ls
all_checks.py  auto-update.py  comp_checks.py  gather-info.sh  ignorethis.py

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git add auto-update.py

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git commit -m 'Add two new scripts'
[master 980715f] Add two new scripts
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 auto-update.py

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git add gather-info.sh

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git commit --amend
[master cee3c70] Add two new scripts
 Date: Sun Jan 30 13:41:57 2022 -0800
 2 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 auto-update.py
 create mode 100644 gather-info.sh

```

**There are many ways** to process **rollbacks** in Git. We will begin and focus on the **revert** command.

**Revert** will perform the inverse of any changes performed from the earlier version. This allows the changes to be undone, while also
still keeping a history of the all the changes. It leaves a record of *everything* that happened.

```console

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git commit -a -m 'Add call to disk_full function.'
[master 53ae375] Add call to disk_full function.
 1 file changed, 3 insertions(+)

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ ./all_checks.py
  File "/home/user/Code/Python/learn_git/checks/./all_checks.py", line 16
    sys.exit(1)
TabError: inconsistent use of tabs and spaces in indentation

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git revert HEAD
[master 5dfabe6] Revert "Add call to disk_full function."
 1 file changed, 3 deletions(-)

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git log -p -2
commit 5dfabe6c38feff5a0a280c7f2c31b4f4da420716 (HEAD -> master)
Author: 4ura <4uralynn@protonmail.com>
Date:   Sun Jan 30 14:06:06 2022 -0800

    Revert "Add call to disk_full function."

    Reason for rollback: The disk_full function is undefined and tabbing is inconsistent.

    This reverts commit 53ae37566d109c4ba1ca0da150f254ec3b61c7fb.

diff --git a/all_checks.py b/all_checks.py
index d2f392d..3219864 100755
--- a/all_checks.py

    Reason for rollback: The disk_full function is undefined and tabbing is inconsistent.

    This reverts commit 53ae37566d109c4ba1ca0da150f254ec3b61c7fb.

diff --git a/all_checks.py b/all_checks.py
index d2f392d..3219864 100755
--- a/all_checks.py
commit 5dfabe6c38feff5a0a280c7f2c31b4f4da420716 (HEAD -> master)
Author: 4ura <4uralynn@protonmail.com>
Date:   Sun Jan 30 14:06:06 2022 -0800

    Revert "Add call to disk_full function."

    Reason for rollback: The disk_full function is undefined and tabbing is inconsistent.

    This reverts commit 53ae37566d109c4ba1ca0da150f254ec3b61c7fb.

diff --git a/all_checks.py b/all_checks.py
index d2f392d..3219864 100755
--- a/all_checks.py
index d2f392d..3219864 100755
--- a/all_checks.py
commit 5dfabe6c38feff5a0a280c7f2c31b4f4da420716 (HEAD -> master)
Author: 4ura <4uralynn@protonmail.com>
Date:   Sun Jan 30 14:06:06 2022 -0800

    Revert "Add call to disk_full function."

    Reason for rollback: The disk_full function is undefined and tabbing is inconsistent.

    This reverts commit 53ae37566d109c4ba1ca0da150f254ec3b61c7fb.

diff --git a/all_checks.py b/all_checks.py
index d2f392d..3219864 100755
--- a/all_checks.py
+++ b/all_checks.py
@@ -11,9 +11,6 @@ def main():
     if check_reboot():
         print("Pending reboot.")
         sys.exit(1)
-    if disk_full():
-        print("Disk full.")
-       sys.exit(1)
     print("Everything is OK.")
     sys.exit(0)


commit 53ae37566d109c4ba1ca0da150f254ec3b61c7fb
Author: 4ura <4uralynn@protonmail.com>
Date:   Sun Jan 30 14:04:59 2022 -0800

    Add call to disk_full function.

diff --git a/all_checks.py b/all_checks.py

```

## Identifying Commits for Rollbacks

Git uses *Commit IDs*, which are hashes created by a hashfunction implementing the *SHA1* algorithm. This ensures each commit is unique and identifiable.
This guarantees the consistency of our repository. Generally, especially locally, you **can use the first 4-8 characters of the hash** to identify the commit.

  + Instead of using `git revert HEAD` we can use the *commit ID* instead of the *HEAD* identifier (which is for the most current).
    - To revert commit number **cee3c70cc08a2c68f4f2e1d7594b97afabaea85b**, for instance, type `git revert cee3c70c` (generally, this will work given the first 4-8 characters of the hash) 


