GitHub Basics
=============

To set up our GitHub repository on our local machine. We use `git clone <url>`. GitHub no longer
allows password authenticaion. So it is best to either create an SSH key or pull a Personal Token from GitHub.

   + To create a Personal Access Token, go to your profile, then Settings>Developer Settings>Personal Access Token
      - Create it, copy, then paste as password
   + To ***cache*** your username and password--so you don't need to re-enter it--type `git config --global credential.helper cache`
   + To pull and merge the most recent repo version from GitHub, use the `git pull` command. 
   + Use `git push` to add your local changes to the remote repository. 


**Working with a remote server** requires additional steps to the Git workflow:

The first three are as *before*

   1. Modify
   2. Stage
   3. Commit

However now we add *three more* steps, when working on a **remote server**, like GitHub:

   4. Fetch
      + `git fetch` fetches remote updates but doesn't merge; unlike `git pull`.
        - You want to use the *correct command*, either **pull** or **fetch**
      + Git **fetch** allows you to review updates first, and then choose to `git merge`
   5. Merge
   6. Push

Use `git remote` to show all remote repositories. To show both the name *and urls* of the remote repository, 
type `git remote -v`. By default the name will be 'origin'.

```console

┌──(aura㉿thehaven)-[~/Code/Python/learn_git/health_checks]
└─$ git remote -v
origin  https://github.com/4uralynn/health_checks.git (fetch)
origin  https://github.com/4uralynn/health_checks.git (push)

```


To to see information about the 'origin' repository type `git remote show origin`: 

```console

┌──(aura㉿thehaven)-[~/Code/Python/learn_git/health_checks]
└─$ git remote show origin
Username for 'https://github.com': 4uralynn
Password for 'https://4uralynn@github.com':
* remote origin
  Fetch URL: https://github.com/4uralynn/health_checks.git
  Push  URL: https://github.com/4uralynn/health_checks.git
  HEAD branch: main
  Remote branch:
    main tracked
  Local branch configured for 'git pull':
    main merges with remote main
  Local ref configured for 'git push':
    main pushes to main (up to date)
```

To **make a change to the remote branch** you must first *pull* the remote branch, merge it with the 
local branch, then *push* it back to its origin.

An **example of a push** to the repository:

```console

┌──(aura㉿thehaven)-[~/Code/Python/learn_git/health_checks]
└─$ git add comp_checks.py

┌──(aura㉿thehaven)-[~/Code/Python/learn_git/health_checks]
└─$ git add all_checks.py

┌──(aura㉿thehaven)-[~/Code/Python/learn_git/health_checks]
└─$ git add free_memory.py

┌──(aura㉿thehaven)-[~/Code/Python/learn_git/health_checks]
└─$ git commit
[main bd8671a] Adding files for computer checks to the repository.
 3 files changed, 66 insertions(+)
 create mode 100755 all_checks.py
 create mode 100755 comp_checks.py
 create mode 100644 free_memory.py

┌──(aura㉿thehaven)-[~/Code/Python/learn_git/health_checks]
└─$ git push
Username for 'https://github.com': 4uralynn
Password for 'https://4uralynn@github.com':

Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 4 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 1.27 KiB | 648.00 KiB/s, done.
Total 5 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/4uralynn/health_checks.git
   03e7342..bd8671a  main -> main

┌──(aura㉿thehaven)-[~/Code/Python/learn_git/health_checks]
└─$ git log
commit bd8671adb0358720a06c6176b22b84373b06743c (HEAD -> main, origin/main, origin/HEAD)
Author: 4ura <4uralynn@protonmail.com>
Date:   Sun Jan 30 18:45:48 2022 -0800

    Adding files for computer checks to the repository.

    These files are all_checks, comp_checks, and free_memory Python files

commit 03e7342605863e38be083b58baab962e429bdc40
Author: Laura Engram <lauracornwell@ieee.org>
Date:   Sun Jan 30 17:07:13 2022 -0800

    Initial commit

┌──(aura㉿thehaven)-[~/Code/Python/learn_git/health_checks]
└─$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

```

Using `get remote update` will show the most current objects.

In order to **list all the remote branches** type `git branch -r`

## Remote Branches

**To add a new branch to the remote repository**, type `git push -u origin branch_name`.
  + The `-u` option pushes the branch upstream (to the remote repository)
  + Include the repo name (origin) and then the branch name.

#### Git Rebase

Rebasing the most current branch onto a feature branch--instead of merging--allows history to remain ***linear*** 
and make *fast-forward* merges.

To rebase, start in the branch to be merged, rather than the master branch. Then type `git rebase master`.
It is best to check `git log --graph --oneline`, but **if the branch is rewound successfully**, then
switch to the main branch (`git checkout master`) and merge (`git merge branch_name`).

**Now the branch can be deleted**
  + To delete the remote branch, `git push --delete origin branch_name`
  + To delete locally, `git branch -d branch_name`

**Don't rebase to remote respositories**, because it rewrites the history. This is not good for collaboration, and should be used locally.

A more **interactive** from of rebase can be used with the `-i` option. With this option, an editor opens up and you see all commits listed.
The **pick** command is the default for rebase commits, and is what the command does when not interactive. 
But when we want to combine a commit, there are two other commands:

In both cases, the contents of the commit are merged into the previous commit in the list.
  1. **squash** - commit messages are added together and an editor opens to make any nessary changes
  2. **fixup** - the commit message for the first commit is discarded 

## Best Practices to Keep in Mind

  1. Always synchronize your branches before starting any work of your own.
  2. Avoid having very large changes that modify a lot of different things.
  3. When working on a big change, it makes sense to have a *separate* feature branch
     + Regularly merge changes made on the master branch back onto the feature branch
  4. Have the latest version of the project in the master branch, and the **stable version in a separate branch**.
  5. Use rebase with caution, and **only rebase on local repos**.
  6. Having good commit messages is important.
