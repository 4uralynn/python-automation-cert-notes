Getting Started with Git
========================

These are the *bash commands* used to add **modified** files to **staging**, and then **commit**:
*(relevant results will be listed in comments below the commands)*

```console

git config --global user.email "4uralynn@protonmail.com"
git config --global user.name "4ura"
git config -l
#user.email=4uralynn@protonmail.com
#user.name=4ura
#core.repositoryformatversion=0
#core.filemode=true
#core.bare=false
#core.logallrefupdates=true
git init	#initializes current directory as repository
git add connect.sh	#adds the file to staging (to commit)
git add log.txt
git add mullmanage.py
git add ststuscheck.sh
git add statuscheck.sh
git add to_bin
git commit
#[master (root-commit) 1031e63] Add initial files for mullvad manager: connect.sh log.txt mullmanage.py statuscheck.sh /to_bin - Files in the to_bin folder (mullvad, vpnstatus), are to copy to the local /usr/bin/ directory.
# 6 files changed, 363 insertions(+)
# create mode 100755 connect.sh
# create mode 100644 log.txt
# create mode 100755 mullmanage.py
# create mode 100755 statuscheck.sh
# create mode 100755 to_bin/mullvad
# create mode 100755 to_bin/vpnstatus
git status
#On branch master
#nothing to commit, working tree clean
vim mullmanage.py
git status
#On branch master
#Changes to be committed:
#  (use "git restore --staged <file>..." to unstage)
#        modified:   mullmanage.py
#
git add mullmanage.py
git status
#On branch master
#Changes not staged for commit:
#  (use "git add <file>..." to update what will be committed)
#  (use "git restore <file>..." to discard changes in working directory)
#
#no changes added to commit (use "git add" and/or "git commit -a")git status
git commit -m 'Added newline characters to the end of status change messages printed to user'
#[master 0d4ccbb] Added newline characters to the end of status change messages printed to user
# 1 file changed, 3 insertions(+), 3 deletions(-)
git status
#On branch master
#nothing to commit, working tree clean

```

## Anatomy of a Commit Message

A good commit message:

  1. **Line 1:** less then 50 character, short description of what the changes are about
    + skip a line
  2. **Lines 2 - Last Line of message:** less  than 72 characters each, in neat paragraphs
    + Provide a detailed explanation of what is going with the change
    + Can reference bugs or issues fixed
    + Can provide references or links to more information, when relevent
  3. **Lines with leading '#':** Not apart of the message
    + provided as a reminder of what we are about to commit


___

NOTE:

The line limits are especially important for using the command `git log`.
Staying below the character limits will be sure the log is readable, since there is no line wrapping.

___ 

## Other Basic Options

Like the `-m` option, other options for **commit** allow us to process changes faster, or get more information.

  + The `-a` option allows you to skip staging
     - Example: `git commit -a -m "Call check_reboot from main, exit with 1 on error."`

