Branching and Merging
=====================

**Branches** allow you to break off from the current working version and write new code that will not affect the *main branch's* current working version
until you decde to ***merge*** that branch. 

## Creating New Branches

Running `git branch` alone will show all branches. To create a new branch, just include the name of the branch in the command: `git branch name`
  + To switch to a branch, we can use `git checkout branch_name`
  + To both create a new branch and immediately switch to it, use `git checkout -b branch_name`

```console

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git branch
* master

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git branch new_feature

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git branch
* master
  new_feature

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git checkout new_feature
Switched to branch 'new_feature'

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git checkout -b even-better-feature
Switched to a new branch 'even-better-feature'

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ nano free_memory.py

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git add free_memory.py

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git commit -m 'Add an empty free_memory.py'
[even-better-feature 5786b28] Add an empty free_memory.py
 1 file changed, 6 insertions(+)
 create mode 100644 free_memory.py

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git log -2
commit 5786b286dddcd42d062690ba19fd67e92e07fb4c (HEAD -> even-better-feature)
Author: 4ura <4uralynn@protonmail.com>
Date:   Sun Jan 30 14:54:13 2022 -0800

    Add an empty free_memory.py

commit 5dfabe6c38feff5a0a280c7f2c31b4f4da420716 (new_feature, master)
Author: 4ura <4uralynn@protonmail.com>
Date:   Sun Jan 30 14:06:06 2022 -0800

    Revert "Add call to disk_full function."

    Reason for rollback: The disk_full function is undefined and tabbing is inconsistent.

    This reverts commit 53ae37566d109c4ba1ca0da150f254ec3b61c7fb.
 
```

**To delete** a branch, use the `-d` option: `git branch -d branch_name`


```console

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git branch -d new_feature
Deleted branch new_feature (was 5dfabe6).

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git branch
* even-better-feature
  master

```

*If you try to delete a branch with unmerged changes,* Git will notify you:

```console

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git branch -d even-better-feature
error: Cannot delete branch 'even-better-feature' checked out at '/home/user/Code/Python/learn_git/checks'
 
```

## Merging

Merging combines branch data and history using the `git merge` command. In order to do this, the current working version *HEAD* must 
be the **master** branch or the branch you want to merch your new branch into.

When the merge is completed, both branches are **pointing to the same commmit**.

```console

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git branch
  even-better-feature
* master

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git merge even-better-feature
Updating 5dfabe6..5786b28
Fast-forward
 free_memory.py | 6 ++++++
 1 file changed, 6 insertions(+)
 create mode 100644 free_memory.py

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git log -2
commit 5786b286dddcd42d062690ba19fd67e92e07fb4c (HEAD -> master, even-better-feature)
Author: 4ura <4uralynn@protonmail.com>
Date:   Sun Jan 30 14:54:13 2022 -0800

    Add an empty free_memory.py

commit 5dfabe6c38feff5a0a280c7f2c31b4f4da420716
Author: 4ura <4uralynn@protonmail.com>
Date:   Sun Jan 30 14:06:06 2022 -0800

    Revert "Add call to disk_full function."

    Reason for rollback: The disk_full function is undefined and tabbing is inconsistent.

    This reverts commit 53ae37566d109c4ba1ca0da150f254ec3b61c7fb.

```

A **Fast-Forward** merge is the algorithm used in the example *above*. Occurs when all the checked out branches are in the branch being merged. Whereas
a **Three-Way** merge occurs when the history of the merging branches diverges in some way. There isn't a nice linear path.

In the **three-way** merge, Git will attempt to merge the snapshops at the two branch tips with the most recent commit **before the divergence**.
If the changes are made in the same part of the same file, Git doesn't know how to resolve this, so it will result in a ***Merge Conflict***.

```console

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git commit -a -m 'Add comment to free_memory script.'
[master 097e3d3] Add comment to free_memory script.
 1 file changed, 1 insertion(+)

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git checkout even-better-feature
Switched to branch 'even-better-feature'

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ nano free_memory.py

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git commit -a -m 'Print everything is OK.'
[even-better-feature 76f47e4] Print everything is OK.
 1 file changed, 1 insertion(+)

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git checkout master
Switched to branch 'master'

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git merge even-better-feature
Auto-merging free_memory.py
CONFLICT (content): Merge conflict in free_memory.py
Automatic merge failed; fix conflicts and then commit the result.

```


## Resolving Merge Conflicts

The first step in dealing with *merge conflict* situation above is to use the command `git status` to get more information.

```console

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git status
On branch master
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   free_memory.py

no changes added to commit (use "git add" and/or "git commit -a")

```

Next, either abort the merge or fix the conflicts. **Open the conflicted file(s)** in a text editor. Git will have made note of the conflicts.
Make the changes necessary, choosing the appropriate changes to keep and/or delete. 
  + After fixing the file, use `git add file_name` 
  + Next run `git status` again, and **Git will tell you the current status of the merge**.
  + Use `git commit` to finalize the merge, when ready, and add the appropriate comments.

```console

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git add free_memory.py

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git status
On branch master
All conflicts fixed but you are still merging.
  (use "git commit" to conclude merge)

Changes to be committed:
        modified:   free_memory.py


┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git commit
[master c4fc6f4] Merge branch 'even-better-feature'


```

___

**NOTE:**

You can use the **git log** options `--graph` and `oneline`, to organize the history better for quick viewing. This is especially helpful with merge conflicts.

*See the example below:*

```console

┌──(user㉿linux)-[~/Code/Python/learn_git/checks]
└─$ git log --graph --oneline
*   c4fc6f4 (HEAD -> master) Merge branch 'even-better-feature'
|\
| * 76f47e4 (even-better-feature) Print everything is OK.
* | 097e3d3 Add comment to free_memory script.
|/
* 5786b28 Add an empty free_memory.py
* 5dfabe6 Revert "Add call to disk_full function."
* 53ae375 Add call to disk_full function.
* cee3c70 Add two new scripts
* 202cd1c Fixing typo in os.path.exists method within all_checks.py.
* f204005 Committing .gitignore file changes to fix typo.
* 9ae02de Adding ignore file to ignore ignorethis.py
* 038810e Comp_check file added
* 68ba6c7 Delete unneeded process file.
* c87e964 Adding example file to be deleted.
* 1249be7 Add a message when everything is ok.
* 3ddd2f3 Call check_reboot from main, exit with 1 on error.
* 4effa35 Added a check_reboot function
* d38fea3 Create empty all_checks.py file in the main directory.
 
```
___
