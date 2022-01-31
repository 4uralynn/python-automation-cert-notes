Getting More Information About Changes
======================================


There are options that can be used for `git log`, `git add`, and even other commands which can give us more information:

  + The `-p` option for `git log` gives us **patch** info for the commits.
    - Git will automatically use a paging tool, similar to using `| less` in the log. Press 'q' to quit.

```console

git log -p
commit 3ddd2f31552039e851f857c8a82b08ea85994d5c (HEAD -> master)
Author: 4ura <4uralynn@protonmail.com>
Date:   Sun Jan 30 11:02:33 2022 -0800

    Call check_reboot from main, exit with 1 on error.

diff --git a/all_checks.py b/all_checks.py
index fa8bb06..b4fcb57 100755
--- a/all_checks.py
+++ b/all_checks.py
@@ -1,12 +1,15 @@
 #!/usr/bin/env python3

 import os
+import sys

 def check_reboot():
     """Returns True if the computer has a pending reboot"""
     return os.path.exist("/run/reboot-required")

 def main():
-    pass
+    if check_reboot():
+        print("Pending reboot.")
+        sys.exit(1)

 main()

commit 4effa35a642ada64667b128d071986e478d238f4
Author: 4ura <4uralynn@protonmail.com>
Date:   Sat Jan 29 23:50:20 2022 -0800

    Added a check_reboot function

diff --git a/all_checks.py b/all_checks.py
index c0d03b3..fa8bb06 100755
--- a/all_checks.py
commit 3ddd2f31552039e851f857c8a82b08ea85994d5c (HEAD -> master)
Author: 4ura <4uralynn@protonmail.com>
Date:   Sun Jan 30 11:02:33 2022 -0800

    Call check_reboot from main, exit with 1 on error.

diff --git a/all_checks.py b/all_checks.py
index fa8bb06..b4fcb57 100755
--- a/all_checks.py
+++ b/all_checks.py
@@ -1,12 +1,15 @@
 #!/usr/bin/env python3

 import os
+import sys

 def check_reboot():
     """Returns True if the computer has a pending reboot"""
     return os.path.exist("/run/reboot-required")

 def main():
-    pass
+    if check_reboot():
+        print("Pending reboot.")
+        sys.exit(1)

 main()

commit 4effa35a642ada64667b128d071986e478d238f4
Author: 4ura <4uralynn@protonmail.com>
Date:   Sat Jan 29 23:50:20 2022 -0800

    Added a check_reboot function

diff --git a/all_checks.py b/all_checks.py
index c0d03b3..fa8bb06 100755
--- a/all_checks.py
+++ b/all_checks.py
@@ -1,5 +1,11 @@
 #!/usr/bin/env python3

+import os
+
+def check_reboot():
+    """Returns True if the computer has a pending reboot"""
+    return os.path.exist("/run/reboot-required")
+
 def main():
     pass


commit d38fea3c4072fc7fc3a26f53e0d1f9f03c0a4d2a
Author: 4ura <4uralynn@protonmail.com>
Date:   Sat Jan 29 23:44:28 2022 -0800

    Create empty all_checks.py file in the main directory.

diff --git a/all_checks.py b/all_checks.py
new file mode 100755
index 0000000..c0d03b3
--- /dev/null
+++ b/all_checks.py
@@ -0,0 +1,6 @@
+#!/usr/bin/env python3
+
+def main():
+    pass
+
+main()
(END)

```

  + Using `git log` in conjunction with `git show`, using the **show** command, shows information on a specific commit.
    - The format for this command, `git show commit_number` is utilized below, after looking up the numbers using `git log`:

```console

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git log
commit 3ddd2f31552039e851f857c8a82b08ea85994d5c (HEAD -> master)
Author: 4ura <4uralynn@protonmail.com>
Date:   Sun Jan 30 11:02:33 2022 -0800

    Call check_reboot from main, exit with 1 on error.

commit 4effa35a642ada64667b128d071986e478d238f4
Author: 4ura <4uralynn@protonmail.com>
Date:   Sat Jan 29 23:50:20 2022 -0800

    Added a check_reboot function

commit d38fea3c4072fc7fc3a26f53e0d1f9f03c0a4d2a
Author: 4ura <4uralynn@protonmail.com>
Date:   Sat Jan 29 23:44:28 2022 -0800

    Create empty all_checks.py file in the main directory.

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git show d38fea3c4072fc7fc3a26f53e0d1f9f03c0a4d2a
commit d38fea3c4072fc7fc3a26f53e0d1f9f03c0a4d2a
Author: 4ura <4uralynn@protonmail.com>
Date:   Sat Jan 29 23:44:28 2022 -0800

    Create empty all_checks.py file in the main directory.

diff --git a/all_checks.py b/all_checks.py
new file mode 100755
index 0000000..c0d03b3
--- /dev/null
+++ b/all_checks.py
@@ -0,0 +1,6 @@
+#!/usr/bin/env python3
+
+def main():
+    pass
+
+main()

```

  + The `--stats` option in will cause get log to show statistic for the commits, such as how many lines were changed.

```console

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git log --stat
commit 3ddd2f31552039e851f857c8a82b08ea85994d5c (HEAD -> master)
Author: 4ura <4uralynn@protonmail.com>
Date:   Sun Jan 30 11:02:33 2022 -0800

    Call check_reboot from main, exit with 1 on error.

 all_checks.py | 5 ++++-
 1 file changed, 4 insertions(+), 1 deletion(-)

commit 4effa35a642ada64667b128d071986e478d238f4
Author: 4ura <4uralynn@protonmail.com>
Date:   Sat Jan 29 23:50:20 2022 -0800

    Added a check_reboot function

 all_checks.py | 6 ++++++
 1 file changed, 6 insertions(+)

commit d38fea3c4072fc7fc3a26f53e0d1f9f03c0a4d2a
Author: 4ura <4uralynn@protonmail.com>
Date:   Sat Jan 29 23:44:28 2022 -0800

    Create empty all_checks.py file in the main directory.

 all_checks.py | 6 ++++++
 1 file changed, 6 insertions(+)

```

  + Using the `git diff` command allows us to track changes in non-committed, nonstaged files.
    - Adding the `--staged` option allows us to see changes that are staged. See example after next bullet point.

```console

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git diff
diff --git a/all_checks.py b/all_checks.py
index b4fcb57..63b8f5c 100755
--- a/all_checks.py
+++ b/all_checks.py
@@ -11,5 +11,7 @@ def main():
     if check_reboot():
         print("Pending reboot.")
         sys.exit(1)
+    print("Everything is OK.")
+    sys.exit(0)

 main() 

```

  + Adding the `-p` option to the `git add` command will allow us to see changes, before confirming that we want to stage them.
    - Also see example of `get diff --staged` below, after the choosing to stage the changes.
```console

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git add -p
diff --git a/all_checks.py b/all_checks.py
index b4fcb57..63b8f5c 100755
--- a/all_checks.py
+++ b/all_checks.py
@@ -11,5 +11,7 @@ def main():
     if check_reboot():
         print("Pending reboot.")
         sys.exit(1)
+    print("Everything is OK.")
+    sys.exit(0)

 main()
(1/1) Stage this hunk [y,n,q,a,d,e,?]? y


┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git diff --staged
diff --git a/all_checks.py b/all_checks.py
index b4fcb57..63b8f5c 100755
--- a/all_checks.py
+++ b/all_checks.py
@@ -11,5 +11,7 @@ def main():
     if check_reboot():
         print("Pending reboot.")
         sys.exit(1)
+    print("Everything is OK.")
+    sys.exit(0)

 main()

```

  + To either remove or rename a file, the options within git are the same as linux commands `git rm file_name`, and `git mv old_file new_file`
    - Remember: After using these options, the changes will be *staged*, and will need to be committed.

```console

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ ls
all_checks.py  comp_checks.py  process.py

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git rm process.py
rm 'process.py'

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        deleted:    process.py

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git commit -m 'Delete unneeded process file.'
[master 68ba6c7] Delete unneeded process file.
 1 file changed, 6 deletions(-)
 delete mode 100755 process.py


```

  + In order to **ignore** files or directories in the repo, we need to add it to a `.gitignore` file.
    - This **.gitignore** file must then be staged and committed as well.

```console

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ ls
all_checks.py  comp_checks.py  ignorethis.py

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ echo ignorthis.py > .gitignore

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git add .gitignore

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git commit -m 'Adding ignore file to ignore ignorethis.py'
[master 9ae02de] Adding ignore file to ignore ignorethis.py
 1 file changed, 1 insertion(+)
 create mode 100644 .gitignore

```


