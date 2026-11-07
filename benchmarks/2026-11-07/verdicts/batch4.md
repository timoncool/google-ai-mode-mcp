########## QUESTION q16 ##########
Question: How do I undo the last git commit but keep its changes staged?
Reference answer: git reset --soft HEAD~1 (HEAD^): moves HEAD back, index and working tree unchanged, so the changes stay staged.
Reference source: https://git-scm.com/docs/git-reset

=== OUTPUT C39 ===
The answer is `git reset --soft HEAD~1`. Several sources agree on it. It moves HEAD back one commit and leaves that commit's changes in the staging area, so you can edit and re-commit right away. The commands below are from the sources and are not reproduced text.

```bash
git reset --soft HEAD~1
git commit -m "Corrected commit message"
```

Other options from the results:

- **Unstage instead:** plain `git reset HEAD~1` (the default `--mixed` mode) keeps your files but leaves nothing staged.
- **Pushed commits:** if others already have the commit, `git revert HEAD` adds a new commit that reverses it rather than rewriting history.
- **Discarding changes:** `--hard` removes the changes entirely, so avoid it unless you truly want them gone.

Sources: coreui.io, deployhq.com (FAQ), adamj.eu, coddy.tech, and leyaa.ai.

Sources:
1. https://coreui.io/answers/how-to-undo-the-last-commit-in-git/
2. https://www.deployhq.com/git/faqs/undo-last-git-commit.md
3. https://www.deployhq.com/git/faqs/undo-last-git-commit
4. https://adamj.eu/tech/2022/11/02/git-how-to-undo-commits/
5. https://coddy.tech/git-commands/git-undo-last-commit
6. https://leyaa.ai/codefly/learn/git/qna/how-to-undo-last-commit-in-git
7. https://leyaa.ai/codefly/learn/git/qna/how-to-undo-commit-but-keep-changes
=== END OF OUTPUT C39 ===

=== OUTPUT G67 ===
To undo your most recent commit while keeping all of its changes staged, run **`git reset --soft HEAD~1`**. [1]

This command moves your branch pointer back by one commit (`HEAD~1`) without modifying your staging area (index) or working directory. [2]

-   **`--soft`:** Preserves your changes in the staging area so they are ready to be re-committed immediately.
    
-   **`HEAD~1`:** Targets the single commit right before your current `HEAD` (change `1` to `2` or `3` to undo multiple commits).
    
-   **Verify Status:** Run `git status` afterward to confirm your modified files appear in green under "Changes to be committed". [3]
    

### Important Caveats

-   **Local vs. Pushed Commits:** Only use `git reset` on local commits that have not been pushed to a shared remote branch, as it rewrites commit history. (If you already pushed it, use `git revert HEAD` instead, or note that you will need `git push --force-with-lease` on a personal branch). [4]
    
-   **Just Fixing a Typo or Missing File:** If you only want to tweak the commit message or add a forgotten file to the last commit, running `git commit --amend` is a faster shortcut. [2]
    

For more details on reset modes, see the [GitLab Undo Documentation](https://docs.gitlab.com/topics/git/undo/).

If you have already pushed this commit to a remote branch or need to undo a commit from earlier in your history, let me know **how your branch is set up** and I can walk you through the safest command to use.

Sources:
1. https://github.com/orgs/community/discussions/169763
2. https://coddy.tech/git-commands/git-undo-last-commit
3. https://jtemporal.com/undoing-the-last-commit-and-reusing-the-message/
4. https://dev.to/yeahiasarker/how-to-undo-a-git-commit-without-losing-your-work-2anc
5. https://docs.gitlab.com/topics/git/undo/
=== END OF OUTPUT G67 ===

=== OUTPUT M47 ===
Title: How to un-commit last un-pushed git commit without losing the changes
URL: https://stackoverflow.com/questions/19859486/how-to-un-commit-last-un-pushed-git-commit-without-losing-the-changes
Published: N/A
Author: N/A
Highlights:
There are a lot of ways to do so, for example:

in case you have not pushed the commit publicly yet:

git reset HEAD~1 --soft 

That's it, your commit changes will be in your working directory, whereas the LAST commit will be removed from your current branch. See git reset man

In case you did push publicly (on a branch called 'master'):

git checkout -b MyCommit //save your commit in a separate branch just in case (so you don't have to dig it from reflog in case you screw up :) )

revert commit normally and push 

git checkout master
git revert a8172f36 #hash of the commit you want to destroy
# this introduces a new commit (say, it's hash is 86b48ba) which removes changes, introduced in the commit in question (but those changes are still visible in the history)
git push origin master

now if you want to have those changes as you local changes in your working copy ("so that your local copy keeps the changes made in that commit") - just revert the revert commit with --no-commit option:

git revert --no-commit 86b48ba (hash of the revert commit).

---

Title: Resetting, Checking Out & Reverting | Atlassian Git Tutorial
URL: https://www.atlassian.com/git/tutorials/resetting-checking-out-and-reverting
Published: N/A
Author: N/A
Highlights:
### Undo public commits with revert

Reverting undoes a commit by creating a new commit. This is a safe way to undo changes, as it has no chance of re-writing the commit history. For example, the following command will figure out the changes contained in the 2nd to last commit, create a new commit undoing those changes, and tack the new commit onto the existing project.

```
1git checkout hotfix git revert HEAD~2
```

This can be visualized as the following:

Contrast this with `git reset`, which does alter the existing commit history. For this reason, `git revert` should be used to undo changes on a public branch, and `git reset` should be reserved for undoing changes on a private branch.

You can also think of `git revert` as a tool for undoing committed changes, while `git reset HEAD` is for undoing uncommitted changes.

Like `git checkout`, `git revert` has the potential to overwrite files in the working directory, so it will ask you to commit or stash changes that would be lost during the revert operation.

...

When invoked with a file path, `git reset` updates the staged snapshot to match the version from the specified commit. For example, this command will fetch the version of `foo.py` in the 2nd-to-last commit and stage it for the next commit:

...

1git reset HEAD~2 foo.py
```

As with the commit-level version of `git reset`, this is more commonly used with `HEAD` rather than an arbitrary commit. Running `git reset HEAD foo.py` will unstage `foo.py`. The changes it contains will still be present in the working directory.

---

Title: Undo Git Commit | How do you undo your last Git commit?
URL: https://www.gitkraken.com/learn/git/problems/undo-git-commit
Published: N/A
Author: N/A
Highlights:
To undo a Git commit after you’ve performed another action in GitKraken, you will have to use the Git reset feature. Simply right-click on the commit from the central graph and select Reset -> Soft to keep all of the changes, or Reset -> Hard to discard the changes, if you’re sure you won’t need them again in the future.

...

## How do you Git undo your last commit and keep changes? 

If you want to undo your last Git commit but keep the changes, a soft Git reset will do the trick. Using the `--soft` flag will ensure that the changes in undone revisions are preserved. You can find these changes as uncommitted local modifications in your working copy after you perform a soft Git reset. If you’re using the GitKraken CLI, you can simply type: 

`$  git reset --soft HEAD~1`

Git reset should be used with care. Let’s say, for example, that you travel back in time to a commit far back in your history; all of the commits you passed along the way may now end up in a dangling state where they exist, but nothing references them. And if you perform a “hard” reset, you risk losing work that wasn’t backed up properly. You should only perform a hard Git reset if you are positive you don’t need those changes anymore. 

`$  git reset --hard HEAD~1`

As a Git best practice, you should always avoid doing anything that requires a force push, which will rewrite the history of your main branch(es).

---

Title: Undo changes in your Git repo - Azure Repos | Microsoft Learn
URL: https://learn.microsoft.com/en-us/azure/devops/repos/git/undo?view=azure-devops
Published: N/A
Author: Battle-born
Highlights:
## Discard uncommitted changes to a file

If you've made changes to a file but haven't committed those changes, you can use Git checkout to quickly discard the changes and revert the file to its last committed version.

Git `checkout` can also revert a file to any committed version, when you specify the commit ID.

Warning

If there's a chance you might want to reapply the changes that Git `checkout` would discard, consider stashing those changes instead.

...

Visual Studio supports discarding uncommitted changes to a file by reverting the file to its last committed version.

In the Git Changes window, identify the file with the changes that you want to discard. If the file is in the Staged Changes section, right-click it and choose Unstage. Unstaged files show up in the Changes section.

If the file is in the Changes section, right-click it and choose Undo Changes to discard all changes to the file since the last commit.

...

You can use the Git `checkout` command to discard uncommitted changes to a file by reverting the file to its last committed version:

```console
git checkout <file>

...

For example, `git checkout README.md` discards uncommitted changes to the `README.md` file.

...

## Revert a branch to a prior state

You can revert a branch to a prior state by using Git reset to reset the branch to a previous commit. Git `reset` affects all files in all branch folders.

Git `reset` has a few options. The default option is to revert the branch to a previous commit, but retain all the subsequent changes as uncommitted changes. Another option is to revert a branch to a previous commit by discarding all changes to all branch files since that commit.

Warning

Don't reset a branch to a commit prior to the last commit if the last commit has been pushed and shared with others. Doing so will result in your local branch history no longer matching the remote branch history. For shared branches, see Undo the changes made by a shared commit.

...

1. From the menu bar, choose Git > View Branch History to open the History tab for the current branch.
2. In the History tab for the current branch, right-click the commit you want to reset, and then choose Reset > Delete Changes (--hard) to reset the branch to the selected commit and delete all changes to all branch files since that commit. Or, choose Reset > Keep Changes (--mixed) to reset the branch to the selected commit and retain all subsequent changes as unstaged changes.

...

# Git Command Line

You can use Git `reset` to revert a branch to its state in a previous commit. The Git `reset` command can be used with various flags:

- The `--hard` flag tells Git to reset the branch to the specified commit, and to discard all subsequent changes. Be careful with this option since you can lose work using it.
- The `--mixed` flag tells Git to reset the branch to the specified commit, but to keep all subsequent changes as unstaged changes. This option is the default.
- The `--soft` flag tells Git to reset the branch to the specified commit, but to keep all subsequent changes as staged and unstaged changes per their previous state.

A common use of Git `reset` is with the `--hard` option to discard all uncommitted changes in all files since the last commit:

```console
git reset --hard

```

...

You can undo the changes made by a commit by using Git revert to create a new commit that reverses those changes. Git `revert` doesn't delete the original commit. This approach is suitable for undoing the changes made by a shared commit because Git `revert` won't alter the previous commit history, and so local and remote branch histories continue to match.

---

Title: How to Undo the Last Git Commit
URL: https://techearl.com/git-undo-last-commit
Published: 2026-06-01T03:45:15.000Z
Author: Ishan Karunaratne
Highlights:
To undo your last Git commit but keep all the changes staged, run `git reset --soft HEAD~1`. The commit disappears, your files are untouched, and everything is staged ready to recommit. That single command covers the most common case. Which command you actually want depends on two questions: do you want to keep the changes or throw them away, and have you already pushed the commit.

Here is the short version before the detail:

```bash
# Undo the commit, keep changes staged (most common)
git reset --soft HEAD~1

# Undo the commit, keep changes but unstage them
git reset --mixed HEAD~1   # or just: git reset HEAD~1

# Undo the commit AND throw the changes away (destructive)
git reset --hard HEAD~1

# Just fix the last commit's message or add a forgotten file
git commit --amend

# Undo a commit you already pushed (safe for shared branches)
git revert HEAD
```

git reset --soft HEAD~1 removes the commit but keeps your changes staged.

...

## The one rule that decides everything: have you pushed?

There are two families of "undo" in Git, and the only thing that decides which family you can safely use is whether the commit has left your machine.

- Not pushed yet (local only): you can rewrite history freely. `reset` and `amend` are fine. They edit the commit graph as if the bad commit never existed.
- Already pushed to a shared branch: do not rewrite history. Other people may have pulled that commit. Use `revert`, which creates a new commit that undoes the changes, leaving the original in place.

Rewriting a commit that someone else has already pulled is how you end up with the divergent-branches mess and force-push arguments. If the commit is on `main` (or any branch a teammate tracks) and it has been pushed, reach for `revert`. Everything else in this article is for commits that are still local.

## Keep the changes: `git reset --soft HEAD~1`

This is the command most people actually want. It removes the last commit from history but leaves your working tree and the staging area exactly as they were. The changes from that commit are now staged, waiting for you to commit again.

```bash
git reset --soft HEAD~1
```

`HEAD~1` means "one commit before the current HEAD", so this moves the branch pointer back by one commit. Use it when you committed too early, picked a bad commit message, or want to fold a couple of commits together by recommitting. After running it, `git status` shows your changes staged in green:

```text
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   src/app.js
```

Recommit when you are ready:

```bash
git commit -m "A better message this time"
```

## Keep the changes but unstage them: `git reset --mixed HEAD~1`

`--mixed` is the default mode of `git reset`, so `git reset HEAD~1` does the same thing. It removes the last commit and keeps your file changes, but it unstages them. The edits are still in your working tree; they just are not in the staging area anymore.

```bash
git reset --mixed HEAD~1
# identical to:
git reset HEAD~1
```

Reach for this when you want to re-stage selectively, splitting one fat commit into several smaller ones, for example. After the reset, `git status` shows the changes as unstaged ("Changes not staged for commit"), and you re-add the pieces you want with `git add`. If the difference between staged and unstaged is fuzzy, the Git staging area explained breaks down exactly what `git add` does and why the index sits between your files and a commit.

## Throw the changes away: `git reset --hard HEAD~1`

`--hard` is the destructive one. It removes the last commit and discards the changes from your working tree and staging area. After this, the work in that commit is gone from your normal view of the repo.

```bash
git reset --hard HEAD~1
```

Only use this when you are certain you want to lose the work, for example a commit full of debugging junk you never want to see again. There is one safety net: a reset moves a branch pointer, and Git keeps a log of every place HEAD has been. If you run `--hard` and panic, you can usually get the commit back from the reflog for a while (the dangling commit lives until garbage collection). I wrote a full walkthrough of that recovery in recover lost commits with git reflog. For discarding uncommitted edits rather than a whole commit, see how to discard local changes in Git.

...

Sometimes you do not want to undo the commit at all. You typed a typo in the message, or you forgot to stage one file.

...

Fix the message:

```bash
git commit --amend -m "The corrected commit message"
```

...

## Already pushed it? Use `git revert`

If the commit is already on a shared remote, do not rewrite it. `git revert` creates a brand-new commit that is the inverse of the one you name, so history stays intact and everyone's clones reconcile cleanly on the next pull.

```bash
git revert HEAD
```

Git opens an editor with a prefilled message like `Revert "the original subject"`; save and close it (or pass `--no-edit` to accept the default). You then push the new revert commit like any other commit. The bad change is undone for everyone, and the original commit is still in the log as a record of what happened. For the full comparison of these two approaches and the decision tree, I have a dedicated piece: git reset vs git revert: when to use each.

...

| Situation | Command | Keeps changes? | Rewrites history? |
| --- | --- | --- | --- |
| Committed too early, want to recommit | `git reset --soft HEAD~1` | Yes, staged | Yes (local only) |
| Want to re-stage selectively | `git reset HEAD~1` | Yes, unstaged | Yes (local only) |
| Commit was pure junk, drop it | `git reset --hard HEAD~1` | No, discarded | Yes (local only) |
| Just a bad message or a missing file | `git commit --amend` | Yes | Yes (local only) |
| Commit is already pushed and shared | `git revert HEAD` | New inverse commit | No, adds a commit |

The pattern is consistent: `reset` and `amend` edit local history and are off-limits once a commit is shared; `revert` adds a new commit and is the only safe choice for anything that has been pushed. When you are working

...

To undo the last three local commits but keep all their combined changes staged:

...

git reset --soft HEAD~3

---

Title: Can I delete (or undo) a git commit but keep the changes?
URL: https://stackoverflow.com/questions/15772134/can-i-delete-or-undo-a-git-commit-but-keep-the-changes
Published: N/A
Author: N/A
Highlights:
It's as simple as this:
git reset HEAD^

Note: some shells treat ^ as a special character (for example some Windows shells or ZSH with globbing enabled), so you may have to quote "HEAD^" or use HEAD~1 in those cases.
git reset without a --hard or --soft moves your HEAD to point to the specified commit, without changing any files. HEAD^ refers to the (first) parent commit of your current commit, which in your case is the commit before the temporary one.
Note that another option is to carry on as normal, and then at the next commit point instead run:
git commit --amend [-m … etc]

which will instead edit the most recent commit, having the same effect as above.
Note that this (as with nearly every git answer) can cause problems if you've already pushed the bad commit to a place where someone else may have pulled it from. Try to avoid that

...

There are two ways of handling this. Which is easier depends on your situation.
Reset
If the commit you want to get rid of was the last commit, and you have not done any additional work you can simply use git-reset
git reset HEAD^

Takes your branch back to the commit just before your current HEAD. However, it doesn't actually change the files in your working tree. As a result, the changes that were in that commit show up as modified - its like an 'uncommit' command. In fact, I have an alias to do just that.
git config --global alias.uncommit 'reset HEAD^'

Then you can just used git uncommit in the future to back up one commit.
Squashing
Squashing a commit means combining two or more commits into one. I do this quite often. In your case you have a half done feature commited, and then you would finish it off and commit again with the proper, permanent commit message.
git rebase -i <ref>

I say above because I want to make it clear this could be any number of commits back. Run git log and find the commit you want to get rid of, copy its SHA1 and use it in place of <ref>. Git will take you into interactive rebase mode. It will show all the commits between your current state and whatever you put in place of <ref>. So if <ref> is 10 commits ago, it will show you all 10 commits.
In front of each commit, it will have the word pick. Find the commit you want to get rid of and change it from pick to fixup or squash. Using fixup simply discards that commits message and merges the changes into its immediate predecessor in the list. The squash keyword does the same thing, but allows you to edit the commit message of the newly combined commit.
Note that the commits will be re-committed in the order they show up on the list when you exit the editor. So if you made a temporary commit, then did other work on the same branch, and completed the feature in a later commit, then using rebase would allow you to re-sort the commits and squash them.
WARNING:
Rebasing modifies history - DONT do this to any commits you have already shared with other developers.
Stashing
In the future, to avoid this problem consider using git stash to temporarily store uncommitted work.
git stash save 'some message'

This will store your current changes off to the side in your stash list. Above is the most explicit version of the stash command, allowing for a comment to describe what you are stashing. You can also simply run git stash and nothing else, but no message will be stored.
You can browse your stash list with...
git stash list

This will show you all your stashes, what branches they were done on, and the message and at the beginning of each line, and identifier for that stash which looks like this stash@{#} where # is its position in the array of stashes.
To restore a stash (which can be done on any branch, regardless of where the stash was originally created) you simply run...
git stash apply stash@{#}

---

Title: Reverting changes - Learn Git
URL: https://devdojo.com/guide/git/reverting-changes
Published: N/A
Author: N/A
Highlights:
As with everything, there are multiple ways to do a specific thing. But what I would usually do in this case I want to undo my latest commit and then commit my new changes is the following.

- Let's say that you made some changes and you committed the changes:

```
git commit -m "Committing the wrong changes"

```

- After that if you run `git log`, you will see the history of everything that has been committed to a repository.
- To undo the last commit, just run the following:

```
git reset --soft HEAD~1

```

The above command will reset back with 1 point.

Note: the above would undo your commit, but it would keep your code changes if you would like to get rid of the changes as well, you need to do a hard reset: `git reset --hard HEAD~1`

- After that, make your new changes
- Once you are done with the changes, run `git add` to add any of the files that you would like to be included in the next commit:

```
git add .

```

- Then use `git commit` as normal to commit your new changes:

```
git commit -m "Your new commit message"

```

- After that, you could again check your history by running:

```
git log

```

Here's a screenshot of the process:

Another approach would be to use `git revert COMMIT_ID` instead.

---

Title: Git Reset: --soft vs --mixed vs --hard, HEAD~1 | Coddy
URL: https://coddy.tech/git-commands/git-reset
Published: 2026-07-02T03:16:05.000Z
Author: N/A
Highlights:
`git reset` moves the current branch to a different commit and, depending on the mode, updates the staging area (index) and working tree to match. The three modes differ only in how far that update reaches: `--soft` moves the branch and stops, `--mixed` (the default) also resets the staging area, and `--hard` also overwrites your working files.

Because `--hard` discards uncommitted work, know which mode you want before you run it. On commits you've already pushed, prefer git revert instead. Try these safely in the terminal playground - a real shell in your browser.

git reset moves HEAD back to an earlier commit; the commits after it leave the branch but stay recoverable via the reflog.

## The three modes

| Mode | Moves branch | Resets staging | Resets working tree |
| --- | --- | --- | --- |
| `--soft` | Yes | No | No |
| `--mixed` (default) | Yes | Yes | No |
| `--hard` | Yes | Yes | Yes |

## Syntax

| Command | What it does |
| --- | --- |
| `git reset --soft HEAD~1` | Undo last commit, keep changes staged |
| `git reset HEAD~1` | Undo last commit, keep changes unstaged |
| `git reset --hard HEAD~1` | Undo last commit, discard changes |
| `git reset ` | Unstage a file (keep its changes) |
| `git reset --hard origin/main` | Force local branch to match the remote |

...

What is the difference between --soft, --mixed, and --hard?

All three move your branch pointer to the target commit; they differ in what else they touch. `--soft` changes nothing else, so your changes stay staged. `--mixed` (the default) also clears the staging area, so changes become unstaged but stay in your files. `--hard` also overwrites your working tree to match the target commit, discarding uncommitted changes.

How do I unstage a file with git reset?

Run `git reset ` (for example `git reset README.md`), or `git reset` with no path to unstage everything. This removes the file from the staging area but keeps your edits in the working tree. In newer Git you can also use `git restore --staged `, which does the same thing more explicitly.

Is git reset --hard reversible?

Not from the working tree - `--hard` discards uncommitted changes permanently. However, committed work you reset away can usually be recovered: run git reflog to find the commit's hash, then `git reset --hard ` (or create a branch at it). Uncommitted changes that were never staged or committed can't be recovered, so use `--hard` carefully.

...

What does git reset --soft HEAD~1 do?

It undoes the last commit but keeps everything that commit changed staged. `HEAD~1` means one commit before the current one, so the branch moves back one step while the staging area and working tree stay as they are. It is the quickest way to redo a commit: fix the files or the message, then commit again. See git undo last commit for the other options.

---

Title: Git Undoing Changes &amp; Debugging | Web Development | CodePath Guides
URL: https://guides.codepath.org/webdev/Git-Undoing-Changes-%26-Debugging
Published: N/A
Author: N/A
Highlights:
### Unstaging changes

If you’ve staged changes but haven’t committed them:

```
# Unstage a specific file
$ git reset HEAD file.txt

# Unstage all staged changes
$ git reset HEAD

# In Git 2.23+, the newer syntax is:
$ git restore --staged file.txt

...

$ git revert a1b2c3d

# Revert the last commit

...

# Soft reset: Move HEAD but keep changes staged

...

> ⚠️ Warning: Hard reset is destructive! It permanently discards any uncommitted changes to tracked files, staged or not. The commits you reset past are removed from the branch too; they can usually still be recovered through the reflog, but only until Git expires those reflog entries (by default after 30 days for entries whose commits are no longer reachable from the branch). Use with extreme caution.

---

Title: Undoing Changes | Luca Nerlich - Tech Documentation
URL: https://lucanerlich.com/git/beginners-guide/undoing-changes/
Published: N/A
Author: N/A
Highlights:
`git reset` moves the current branch pointer to a different commit. It is more powerful than `git restore` because it affects the commit history, not just individual files.

Git reset has three modes, controlling what happens to the staging area and working tree after the branch pointer moves:

| Mode | Branch pointer | Staging area | Working tree | Use when |
| --- | --- | --- | --- | --- |
| `--soft` | Moved | Unchanged (staged) | Unchanged | Keep changes staged, ready to recommit |
| `--mixed` | Moved | Reset to target | Unchanged | Keep changes in working tree (default mode) |
| `--hard` | Moved | Reset to target | Reset to target | Permanently discard all changes |

### `--soft`: undo commit, keep changes staged​

git reset --soft HEAD~1 

The last commit is gone from the history, but all the changes it contained are back in the staging area, ready to be committed again (perhaps with a different message or after adding more files).

Useful for: "I committed too early - I have more to add to this commit."

git reset --soft HEAD~1 

# Make more changes 

git add additional-file.js 

git commit -m "feat(auth): complete login flow with remember-me" 

### `--mixed`: undo commit, keep changes unstaged (default)​

git reset HEAD~1 

# or explicitly: 

git reset --mixed HEAD~1 

The last commit is gone, and its changes are back in your working tree but not staged. You can review them, modify them, and re-add selectively.

Useful for: "I want to split this commit into multiple smaller commits."

git reset HEAD~1 

git add src/auth.js 

git commit -m "feat(auth): add login endpoint" 

git add src/session.js 

git commit -m "feat(session): add session management" 

### `--hard`: undo commit, discard changes permanently​

git reset --hard HEAD~1 

The last commit is gone and all changes in it are permanently discarded from your working tree and staging area. This is the most destructive form of reset.

Useful for: "This whole commit was a mistake - throw it away completely."

# Go back 3 commits and discard everything since then 

git reset --hard HEAD~3 

# Reset to match remote (discard ALL local commits not on origin) 

git reset --hard origin/main 

> Warning: `git reset --hard` discards changes with no easy recovery path. The only way back is via `git reflog` (see below). Never run `--hard` on a shared branch.

...

It never rewrites history - it adds to it. This makes it safe to use on shared branches.
=== END OF OUTPUT M47 ===


########## QUESTION q17 ##########
Question: Как в Linux узнать, какой процесс слушает порт 8080?
Reference answer: ss -ltnp | grep :8080 (sudo for other users' processes); alternatives lsof -i :8080 or netstat -tlnp.
Reference source: https://man7.org/linux/man-pages/man8/ss.8.html

=== OUTPUT A33 ===
Самый быстрый способ — команда `ss`, а для порта 8080 есть несколько вариантов:

- **ss (рекомендуется на современных системах).** Чтобы вывести все слушающие TCP-порты с владеющим процессом, используйте sudo ss -tlnp. Чтобы отфильтровать только порт 8080: `sudo ss -tlnp | grep :8080`. В выводе процесс показывается в виде имени и PID.
- **lsof.** Команда `sudo lsof -i :8080` показывает процесс, который использует порт. Список слушающих TCP-портов можно получить командой lsof -nP -iTCP -sTCP:LISTEN.
- **fuser.** Для поиска процесса на порту 8080 используйте fuser 8080/tcp, который выведет PID. Чтобы получить подробности, можно передать PID в ps: ps -p $(fuser 8080/tcp) -ww.
- **netstat (устаревший).** Команда netstat -ltnp | grep ':8080' делает то же самое, но netstat считается устаревшим на современных дистрибутивах, хотя во многих системах ещё доступен.

Если утилит нет, установите их через пакетный менеджер: пакеты называются `iproute2` (для ss), `lsof` и `psmisc` (для fuser). Для остановки найденного процесса используйте `kill <PID>`, а если он не реагирует, `kill -9 <PID>`. Учтите, что без `sudo` вы не увидите процессы других пользователей.

Sources:
1. https://linuxconfig.org/linux-what-process-is-listening-on-a-port
2. https://www.cyberciti.biz/faq/find-linux-what-running-on-port-80-command/
3. https://odoowebhook.aryng.com/trending-stories/find-process-using-port-linux-command-guide-1767649024
4. https://www.safaribooksonline.com/library/view/squid-proxy-server/9781849513906/ch12s05.html
5. https://dev.to/nyxtom/why-is-port-8080-already-in-use-and-what-else-is-running-using-lsof-to-navigate-your-system-567e
6. https://sumguy.pages.dev/finding-the-pid-of-a-process-using-a-specific-port-in-linux
7. https://adminschoice.com/check-open-ports-linux/
=== END OF OUTPUT A33 ===

=== OUTPUT X78 ===
**Самый быстрый способ узнать, какой процесс занимает порт 8080 в Linux — использовать встроенную утилиту `ss` с правами суперпользователя****.** Без `sudo` система скроет имя и PID процессов, запущенных от имени других пользователей или `root`. [1]

-   **`ss` (рекомендуемый современный инструмент):**
    
    bash
    
    ```
    sudo ss -tulpn | grep :8080
    ```
    
    Используйте код с осторожностью.
    
    В колонке `users` отобразится имя программы и её идентификатор (например, `users:(("node",pid=41207,fd=19))`). Подробнее о замене устаревших утилит на `ss` можно прочитать в разборе [hip-hosting](https://hip.hosting/ru/blog/ss-instead-of-netstat).
    
-   **`lsof` (показывает открытые файлы и сетевые сокеты):**
    
    bash
    
    ```
    sudo lsof -i :8080
    ```
    
    Используйте код с осторожностью.
    
    Утилита выведет таблицу с именем команды (`COMMAND`), идентификатором (`PID`) и владельцем процесса (`USER`). [3]
    
-   **`fuser` (возвращает только PID процесса):**
    
    bash
    
    ```
    sudo fuser 8080/tcp
    ```
    
    Используйте код с осторожностью.
    
    Узнать имя процесса по полученному номеру можно командой `ps -p <PID> -o comm=`. [4]
    
-   **`netstat` (классический инструмент из пакета `net-tools`):**
    
    bash
    
    ```
    sudo netstat -tulpn | grep :8080
    ```
    
    Используйте код с осторожностью.
    
    В некоторых современных дистрибутивах и минимальных контейнерах утилита отсутствует по умолчанию и требует установки пакета `net-tools`. [1]
    

### Расшифровка флагов для `ss` и `netstat`

-   **`-t`** — показать только TCP-соединения.
    
-   **`-u`** — показать UDP-соединения.
    
-   **`-l`** — вывести только прослушиваемые (listening) порты.
    
-   **`-p`** — отобразить имя программы и PID процесса.
    
-   **`-n`** — выводить номера портов цифрами, не преобразуя их в названия служб. [5]
    

Детальный разбор работы с ошибкой занятого порта (`Address already in use`) доступен в статье на [Хабре](https://habr.com/ru/companies/netologyru/articles/1077578/).

Если процесс уже найден и его нужно завершить или перезапустить, я могу подсказать команды для **безопасной остановки службы** (через `systemctl` или `kill`). Помочь с этим?

Sources:
1. https://habr.com/ru/companies/netologyru/articles/1077578/
2. https://hip.hosting/ru/blog/ss-instead-of-netstat
3. https://1cloud.ru/help/linux/kak_uznat_kakoj_komponent_ispolzuet_tcp_port_80
4. https://blog.sedicomm.com/2017/11/09/3-sposoba-uznat-kakoj-protsess-proslushivaet-opredelennyj-port/
5. https://doc.macroscop.com/qna/configure/what-proc-using-port.htm
=== END OF OUTPUT X78 ===

=== OUTPUT A82 ===
Title: How to Find Which Process Is Using a Port in Linux | Linuxize
URL: https://linuxize.com/post/how-to-find-which-process-is-using-a-port/
Published: 2026-07-25T05:30:00.000Z
Author: Dejan Panovski
Highlights:
If you need an inventory of every service accepting connections instead of one specific port, see the guide on checking listening ports in Linux . The addresses `127.0.0.1:8080` and `0.0.0.0:8080` also collide. Binding to all interfaces includes the loopback address .

## Quick Reference #

For printable quick references, see the ss cheatsheet , lsof cheatsheet , and netstat cheatsheet .

| Task | Command |
| --- | --- |
| Find a TCP listener with ss | `sudo ss -ltnp 'sport = :80'` |
| Find a UDP socket with ss | `sudo ss -lunp 'sport = :53'` |
| Find a TCP listener with lsof | `sudo lsof -nP -iTCP:80 -sTCP:LISTEN` |
| List every socket on a port with lsof | `sudo lsof -i :80` |
| Find processes with fuser | `sudo fuser -v 80/tcp` |
| Find a TCP listener with netstat | `sudo netstat -ltnp | grep ':80 '` |
| Inspect a process | `ps -fp PID` |
| Stop an unmanaged process | `sudo kill PID` |
| Send SIGTERM with fuser | `sudo fuser -k -TERM 80/tcp` |

## Finding the Process with ss #

The `ss` command is the standard choice on current Linux distributions. It comes from the `iproute2` package and supports filters that match an exact port without piping the output through another command.

 Terminal

```bash
sudo ss -ltnp 'sport = :80'
```

```output
State     Recv-Q    Send-Q       Local Address:Port        Peer Address:Port    Process
LISTEN    0         511                0.0.0.0:80               0.0.0.0:*        users:(("nginx",pid=479731,fd=5),("nginx",pid=479730,fd=5))
LISTEN    0         511                   [::]:80                  [::]:*        users:(("nginx",pid=479731,fd=6),("nginx",pid=479730,fd=6))
```

Run the command with `sudo` so `ss` can show process details for sockets owned by other users. The options provide the following information:

- `-l` - Show only listening sockets.
- `-t` - Show TCP sockets.
- `-n` - Print numeric port numbers instead of resolving service names.
- `-p` - Show the process that owns each socket.

The `sport = :80` expression matches local port 80 exactly, so it does not also return ports such as 8080. In the output above, `nginx` holds the port. The `Process` column lists two process IDs because the master process, `479730`, opened the socket and passed it to its worker, `479731`. Either PID leads you back to the same service. The two rows show that `nginx` listens on both IPv4 and IPv6.

UDP sockets do not use the TCP `LISTEN` state. To check a UDP port, replace `-t` with `-u`. For example, the following command identifies the process bound to UDP port 53:

 Terminal

```bash
sudo ss -lunp 'sport = :53'

...

## Finding the Process with lsof #

The `lsof` command lists open files, including network sockets. Use numeric output and restrict the result to TCP listeners on the port:

```bash
sudo lsof -nP -iTCP:80 -sTCP:LISTEN
```

```output
COMMAND    PID     USER FD   TYPE  DEVICE SIZE/OFF NODE NAME
nginx   479730     root 5u  IPv4 1021072      0t0  TCP *:80 (LISTEN)
nginx   479730     root 6u  IPv6 1021073      0t0  TCP *:80 (LISTEN)
nginx   479731 www-data 5u  IPv4 1021072      0t0  TCP *:80 (LISTEN)
nginx   479731 www-data 6u  IPv6 1021073      0t0  TCP *:80 (LISTEN)
```

The `-nP` options prevent hostname and service-name lookups, while `-iTCP:80` selects TCP port 80 and `-sTCP:LISTEN` excludes established connections. The output reports the command, PID, user, and file descriptor. Here `lsof` gives you the same two `nginx` processes that `ss` reported, each listed once for IPv4 and once for IPv6, and it also shows the user each one runs as, which is useful when a master process drops privileges for its workers.

You will often see a shorter form that matches every socket on the port, whatever its protocol or state:

```bash
sudo lsof -i :80
```

```output
COMMAND    PID     USER FD   TYPE  DEVICE SIZE/OFF NODE NAME

...

nginx   479731 www-data 6u  IPv6 1021073      0t0  TCP *:http (LISTEN)

...

Without `-P`, `lsof` translates the port number to its service name, so the `NAME` column shows `*:http`, not `*:80`. The short form also lists established connections. It matches port 80 on either end of a connection, so an outgoing download from `apt` or a browser shows up next to the server. Add `-sTCP:LISTEN` to keep only the listening sockets.

...

## Finding the Process with fuser #

When you want a PID without the full socket table, `fuser` provides a short command. Pass the port number followed by the protocol:

```bash
sudo fuser 80/tcp
```

```output
80/tcp:              479730 479731
```

You get the PID list and nothing else, which makes the plain form easy to pass to another command. To include the user, access type, and command name, add the `-v` option:

```bash
sudo fuser -v 80/tcp
```

```output
                     USER        PID ACCESS COMMAND
80/tcp:              root      479730 F.... nginx
                     www-data  479731 F.... nginx
```

The port appears once on the first row, and every process below it belongs to that same port. The `ACCESS` column describes how each process uses the socket, where `F` marks it as open for writing.

You must specify `tcp` or `udp` because the same numeric port can be used by both protocols.

## Finding the Process with netstat #

On older systems you may still find `netstat` , part of the `net-tools` package. Use it as a fallback when `ss` is not available:

```bash
sudo netstat -ltnp | grep ':80 '
```

```output
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      479730/nginx: maste
tcp6       0      0 :::80                   :::*                    LISTEN      479730/nginx: maste
```

The last column ties PID `479730` to the `nginx` master process. `netstat` cuts the PID and program name to a fixed width, so the name here ends at `nginx: maste`. Unlike `ss` and `lsof`, it reports a single process per socket rather than the whole group. The space after `:80` in the filter prevents it from matching a longer port number such as 8080. For a UDP port, use `-lunp` instead of `-ltnp`.

...

Once you have the PID, confirm what started the process before stopping it. The following `ps` command shows the full command and its parent PID:

```bash
ps -fp 479730
```

```output
UID          PID    PPID  C STIME TTY          TIME CMD
root      479730       1  0 20:58 ?        00:00:00 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
```

A service manager or container runtime may own the process. In that case, stop it through its manager so it does not immediately start again. To find the systemd unit that manages a PID, ask `ps` for it:

```bash
ps -o unit= -p 479730
```

```output
nginx.service
```

...

## Confirming the Port Is Free #

Run the same `ss` query after stopping the process:

```bash
sudo ss -ltnp 'sport = :80'
```

If no socket row appears below the header, nothing is listening on TCP port 80 in the current network namespace. If you changed a service configuration instead of stopping it, start the service again and check the new port with the same command.

---

Title: Найти открытый порт. Поиск процессов по открытому порту
URL: https://onedev.net/post/992
Published: 2020-05-13T19:11:54.000Z
Author: N/A
Highlights:
Проверка открытых портов и поиск связанных процессов (слушающих порт).

Показать список всех открытых портов: 

```
lsof -i -P -n | grep LISTEN
netstat -anltup | grep "LISTEN"
ss -tulpn | grep LISTEN

```

Опции netstat

```
-a  All sockets
-n  Show port number only, don't try to resolve the service name
-l  Listening sockets (only services which are listening on some port)
-t  TCP ports
-u  UDP ports
-p  Program name

```

## Команда lsof

Проверить порт утилитой lsof:

```
lsof -i:8010
```

```
COMMAND    PID USER   FD   TYPE  DEVICE SIZE/OFF NODE NAME
php     167457 user    3u  IPv6 2362403      0t0  TCP localhost:8010 (LISTEN)
```

Получить PID процессов слушающих порт утилитой lsof: 

```
lsof -t -i:8080

```

```
145395
150643
```

Убить процессы слушающие порт:

```
lsof -t -i:8086 | xargs kill -9  # Способ 1
kill -9 $(lsof -t -i:8080)       # Способ 2

```

...

```

...

8010/tcp:            167457

---

Title: How can I kill a process running on particular port in Linux?
URL: https://stackoverflow.com/questions/11583562/how-can-i-kill-a-process-running-on-particular-port-in-linux
Published: N/A
Author: N/A
Highlights:
Use the command
sudo netstat -plten | grep java

I used grep java as the tomcat process uses java as its processes.
It will show the list of processes with port number and process id:
tcp6 0 0 :::8080 :::* LISTEN
1000 30070621 16085/java

The number before /java is a process id. Now use the kill command to kill the process:
kill -9 16085

-9 implies the process will be killed forcefully.

...

The command fuser 8080/tcp will print the PID of the process bound to that port.
And the command fuser -k 8080/tcp will kill that process.
It works on Linux only. More universal is use of lsof -i4 (or 6 for IPv6).
General form:
# List the TCP process bound to port PORT
fuser PORT/tcp

# Example: list the TCP process bound to port 8080
fuser 8080/tcp

# List the UDP process bound to port PORT
fuser PORT/udp

# Example: list the UDP process bound to port 8080
fuser 8080/udp

---

Title: Как узнать, какой процесс занял порт?
URL: https://doc.macroscop.com/qna/configure/what-proc-using-port.htm
Published: N/A
Author: N/A
Highlights:
## На ОС Linux🔗

Чтобы узнать, какой процесс занял порт, используйте один из следующих способов:

### Способ 1: Использование утилиты lsof🔗

Примечание

При отсутствии утилиты lsof установите её, следуя инструкции:

1. Запустите терминал.
2. Введите команду:

```
sudo apt install lsof

```
3. Проверьте наличие установленного пакета с помощью команды:

```
lsof --version

```

Для проверки процесса, который занимает порт, выполните следующие шаги:

1. Запустите терминал.
2. Введите команду:

```
sudo lsof -i :<номер_порта>

```

Пример команды для порта 8080:

```
sudo lsof -i :8080

```

В выводе отобразится информация о процессе (имя, идентификатор и т.д.), который занимает указанный порт.

### Способ 2: Использование утилиты ss🔗

Примечание

При отсутствии утилиты ss установите её из пакета iproute2, следуя инструкции:

1. Запустите терминал.
2. Введите команду:

```
sudo apt install iproute2

```
3. Проверьте наличие установленного пакета с помощью команды:

```
dpkg -S iproute2

```

Для проверки процесса, который занимает порт, выполните следующие шаги:

1. Запустите терминал.
2. Введите команду:

```
sudo ss -tlnp | grep :<номер_порта>

```

Обозначения опции -tlnp:

- -t: только TCP.
- -l: только слушающие (listening) порты.
- -n: показывать числовые порты (без преобразования в имена).
- -p: показать процесс (PID и имя).

Пример команды для порта 8080:

```
sudo ss -tlnp | grep :8080

```

### Способ 3: Использование утилиты netstat🔗

Примечание

При отсутствии утилиты netstat установите её из пакета net-tools, следуя инструкции:

1. Запустите терминал.
2. Введите команду:

```
sudo apt install net-tools

```
3. Проверьте наличие установленного пакета с помощью команды:

```
netstat --version

```

Для проверки процесса, который занимает порт, выполните следующие шаги:

1. Запустите терминал.
2. Введите команду:

```
sudo netstat -tlnp | grep :<номер_порта>

```

Обозначения опции -tlnp:

- -t: только TCP.
- -l: только слушающие (listening) порты.
- -n: показывать числовые порты (без преобразования в имена).
- -p: показать процесс (PID и имя).

Пример команды для порта 8080:

```
sudo netstat -tlnp | grep :8080

```

---

Title: Which Process Is Using That Port? Mapping a Listening Port to a PID on Linux – BackendSide Blog
URL: https://backendside.com/blog/2026/07/29/find-process-using-port-linux/
Published: 2026-07-29T00:00:00.000Z
Author: N/A
Highlights:
## The short answer

On any reasonably modern distribution, this is the whole trick:

```
sudo ss -ltnp
```

That lists every TCP socket in the LISTEN state, without resolving names, with the owning process attached. Output looks like this:

```
State   Recv-Q  Send-Q   Local Address:Port   Peer Address:Port  Process
LISTEN  0       128            0.0.0.0:22          0.0.0.0:*      users:(("sshd",pid=811,fd=3))
LISTEN  0       511            0.0.0.0:80          0.0.0.0:*      users:(("nginx",pid=1187,fd=6),("nginx",pid=1186,fd=6))
LISTEN  0       4096         127.0.0.1:3306        0.0.0.0:*      users:(("mariadbd",pid=942,fd=25))
LISTEN  0       4096                  *:8080               *:*    users:(("backendsidemon",pid=1502,fd=9))
```

The last column is the answer. `users:(("nginx",pid=1187,fd=6))` means: the process named `nginx`, PID 1187, is holding this socket on file descriptor 6. Port 80 shows two entries because a master process and a worker both hold the listening descriptor—that is normal for pre-forking servers.

To look at one port instead of all of them, use a filter rather than piping to `grep`—it avoids matching the port number in some other column:

```
sudo ss -ltnp 'sport = :8080'
```

### The flags, decoded

| Flag | What it does | Why you want it |
| --- | --- | --- |
| `-t` / `-u` | TCP / UDP sockets | Filters out the pile of Unix domain sockets |
| `-l` | Listening sockets only | A server binding a port is what you are hunting |
| `-n` | Numeric — no name resolution | Shows `:8080`, not `:http-alt`; also much faster |
| `-p` | Show the owning process | The entire point — needs root for other users’ processes |
| `-a` | All sockets, not just listening | Use when chasing an established connection instead |
| `-e` | Extended info, including the socket inode | The escape hatch when `-p` gives you nothing |

## Why you almost always need sudo

Run `ss -ltnp` without root and the Process column will be blank for everything you do not own. The kernel only lets you map a socket back to a PID if the process is yours or you have `CAP_NET_ADMIN`. This trips people up constantly: the port is clearly listed as LISTEN, the process field is empty, and it looks like a ghost. It is not a ghost—it is a permissions problem. Add `sudo` and try again before you go any further.

...

### 1. `lsof` — the most readable output

`lsof` treats sockets as what they are on Linux: open files. Ask it which files match an internet address:

```
sudo lsof -i :8080 -sTCP:LISTEN -P -n

COMMAND          PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
backendsidemon  1502  root    9u  IPv6  28841      0t0  TCP *:8080 (LISTEN)
```

`-P` and `-n` keep ports and addresses numeric, and `-sTCP:LISTEN` drops established connections so you only see the binding process. For scripting, `-t` prints bare PIDs and nothing else:

```
sudo lsof -t -i :8080 -sTCP:LISTEN
1502
```

### 2. `fuser` — fastest when you only want the PID

```
sudo fuser 8080/tcp
8080/tcp:             1502

sudo fuser -v 8080/tcp
                     USER        PID ACCESS COMMAND
8080/tcp:            root       1502 F....  backendsidemon
```

`fuser` also has `-k`, which kills whatever it finds. It is genuinely useful and genuinely dangerous—`sudo fuser -k 8080/tcp` will happily terminate a production database if that is what answered. Always run it without `-k` first and read the output.

### 3. `netstat` — the one in every old runbook

```
sudo netstat -tulpn | grep ':8080'
tcp6  0  0 :::8080   :::*   LISTEN   1502/backendsidemon
```

`netstat` comes from the deprecated `net-tools` package and is not installed by default on most current distributions. It reads `/proc/net/tcp` by walking every process’s file descriptors, which is noticeably slow on a busy machine. Learn `ss`; keep `netstat` for the servers you inherited.

## From PID to the whole story

A PID and a process name are rarely the end of the investigation—”python3″ or “java” tells you nothing. Once you have the number, `/proc` gives you everything else:

```
# Full command line, owner, parent, and how long it has been up
ps -p 1502 -o pid,ppid,user,etime,cmd

# The actual binary on disk (survives a renamed process)
sudo ls -l /proc/1502/exe

# Its working directory - often reveals which deployment it belongs to
sudo ls -l /proc/1502/cwd

# The raw argv, NUL-separated
sudo tr '' ' ' < /proc/1502/cmdline; echo

# Which systemd unit or container owns it
cat /proc/1502/cgroup
systemctl status 1502
```

That last one is the most useful and the least known: `systemctl status ` resolves a PID to its owning unit, so you find out that port 8080 belongs to `backendsidemon.service` and can stop it properly instead of killing it.

### The manual method: socket inodes

If `-p` gives you nothing and you have already ruled out permissions, you can do the mapping by hand. Every socket has an inode number, and every process holding it has a symlink to `socket:[inode]` in its file-descriptor directory:

```
$ sudo ss -ltne 'sport = :8080'
LISTEN 0 4096 *:8080 *:*  ino:28841 sk:3 cgroup:/system.slice/backendsidemon.service

$ sudo find /proc/[0-9]*/fd -lname 'socket:[28841]' 2>/dev/null
/proc/1502/fd/9
```

The path contains the PID. This is exactly what `ss`, `lsof` and `netstat` do internally—it is worth seeing once, because it explains why these tools need root and why they get slow on machines with tens of thousands of open descriptors.

...

### The owner is systemd itself

With socket activation, systemd holds the listening socket and only starts the real service when the first connection arrives. Until then the port genuinely belongs to PID 1. `systemctl list-sockets` shows every such socket and the unit it will hand off to.

---

Title: Какой процесс слушает порт в Linux
URL: https://blog.sedicomm.com/2017/11/09/3-sposoba-uznat-kakoj-protsess-proslushivaet-opredelennyj-port/
Published: 2017-11-09T10:58:09.000Z
Author: Егор Мирошниченко
Highlights:
## Использование команд netstat и ss

Утилита `netstat` — инструмент командной строки Linux, предназначенный для отображения информации о сетевых соединениях, интерфейсах, прослушиваемых портах и других данных, связанных с сетью.

Вы можете использовать эту утилиту, чтобы найти процесс, прослушивающий определенный порт в ОС Linux. Для этого следует применить следующую команду:

sudo netstat -ltnp | grep -w ': '

Где:

- `-l` — параметр, который указывает `netstat` отображать только прослушиваемые порты;
- `-t` — параметр, который указывает отображать только порты TCP;
- `-n` — опция, определяющая, что должны быть показаны IP-адреса и номера портов;
- `-p` — опция, показывающая идентификатор процесса (PID) и название программы, связанной с каждым портом;
- `|` — конвейер, который используется для перенаправления вывода одной команды в качестве ввода другой;
- `grep -w ': '` — команда, которая ищет точное совпадение с шаблоном, указанным в качестве ее аргумента.

Для примера узнаем, какой процесс прослушивает порт 80:

sudo netstat -ltnp | grep -w ':80'

На скриншоте выше видно, что веб-cервер Apache прослушивает порт 80.

Утилита `ss` (от англ. Socket Statistics) предназначена для отображения подробной статистики о сокетах. Она имеет ряд преимуществ перед `netstat`: работает быстрее и предоставляет более подробную информацию о состоянии сети.

Команды `ss` и `netstat` имеют похожий набор опций. Поэтому, чтобы определить программу, прослушивающую порт, с помощью `ss`, используйте следующую команду:

sudo ss -tulpn | grep -w ': '

Где `-u` — параметр, который указывает отображать UDP-порты.

Давайте узнаем, какой процесс прослушивает порт 80:

sudo ss -tulpn | grep -w ':80'

На скриншоте выше видно, что утилита `ss`, в отличие от `netstat`, отображает идентификаторы не только родительских процессов, но и дочерних.

...

Команда `fuser` применяется для определения процессов, которые используют определенные файлы / каталоги или прослушивают сетевые порты.

Вы можете узнать процесс, прослушивающий определенный порт, выполнив приведенную ниже команду:

sudo fuser / 

Где:

- ` ` — номер сетевого порта;
- ` ` — тип сетевого протокола, связанного с портом (TCP или UDP).

Например, узнаем, какой процесс прослушивает TCP-порт 80:

---

Title: Проверка и поиск занятых портов в Linux | База знаний PlanetaHost
URL: https://wiki.planetahost.ru/books/os-i-po/page/proverka-i-poisk-zaniatyx-portov-v-linux
Published: N/A
Author: N/A
Highlights:
### Определение процесса, использующего порт

Чтобы увидеть, какой процесс использует конкретный порт, выполните:

```bash
sudo ss -tulpn
```

Пример:

В выводе отображаются:

- имя процесса;
- PID процесса;
- файловый дескриптор.

### Проверка конкретного порта

Например, необходимо узнать, используется ли порт 10050.

```bash
sudo ss -tulpn | grep :10050
```

Если команда ничего не вернула, значит данный порт в настоящий момент не используется.

---

Title: How to Kill Port 8080 on Linux (Ubuntu, Debian, Fedora) | portrm
URL: https://portrm.dev/guides/kill-port-8080-linux/
Published: N/A
Author: N/A
Highlights:
## Quick fix: portrm

```
$ ptrm fix 8080
  Port 8080 in use
  java (PID 19432) - Spring Boot
  SAFE - development server
  Killed PID 19432. Port 8080 is free.
```

...

## Method 1: ss (socket statistics)

`ss` is the modern replacement for `netstat`, pre-installed on all modern Linux distributions:

```
$ ss -tlnp | grep :8080
LISTEN  0  100  *:8080  *:*  users:(("java",pid=19432,fd=56))

$ kill -9 19432
```

## Method 2: fuser (one-liner)

`fuser` is the simplest way. The `-k` flag kills the process automatically:

```
# Find and kill in one command
$ fuser -k 8080/tcp
8080/tcp:  19432

# Just find (without killing)
$ fuser 8080/tcp
8080/tcp:  19432
```

...

java   19432 dev    56u  IPv6 0x...  0t0     

...

## Method 4: /proc filesystem

On Linux, you can inspect sockets directly without installing anything:

```
# Find the inode for port 8080 (hex 1F90)
$ grep '1F90' /proc/net/tcp
  0: 00000000:1F90 00000000:0000 0A 00000000:00000000 ...

# Or use the portrm approach for human-readable output
$ ptrm 8080
```

---

Title: Netstat в Linux: как узнать открытые порты и соединения — FixPedia
URL: https://fixpedia.ru/guides/linux/netstat-command
Published: N/A
Author: FixPedia Team
Highlights:
### Шаг 2: Просмотрите все активные соединения и слушающие порты

Запустите основную, самую информативную команду:

```bash
sudo netstat -tulpn

```

Что вы увидите и как читать вывод:

```text
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      1234/sshd
tcp6       0      0 :::80                   :::*                    LISTEN      5678/nginx: master
udp        0      0 127.0.0.1:323           0.0.0.0:*                          901/chronyd

```

- Proto: Протокол (`tcp`, `udp`, `tcp6`, `udp6`).
- Local Address: Локальный адрес и порт. `0.0.0.0:22` — сервис слушает на всех IPv4-интерфейсах порт 22. `:::80` — на всех IPv6-интерфейсах порт 80.
- Foreign Address: Удалённый адрес и порт. `0.0.0.0:*` или `*:*` означает, что соединение не с конкретным удалённым хостом (состояние LISTEN).
- State: Состояние соединения. Для слушающих портов — `LISTEN`. Для активных соединений — `ESTABLISHED`, `TIME_WAIT` и др.
- PID/Program name: Идентификатор процесса (PID) и имя программы, которая владеет сокетом. Ключевая колонка для диагностики.

### Шаг 3: Отфильтруйте вывод по протоколу или порту

Полный вывод (`-tulpn`) может быть очень объёмным. Фильтрация с помощью `grep` сузит результаты.

Показать только TCP-соединения (игнорируя слушающие порты):

```bash
sudo netstat -tn

```

Показать только UDP-соединения:

```bash
sudo netstat -un

```

Найти все записи, связанные с портом 80 (HTTP) или 443 (HTTPS):

```bash
sudo netstat -tulpn | grep -E ':80|:443'

```

Найти процесс, слушающий конкретный порт (например, 3306 MySQL):

```bash
sudo netstat -tulpn | grep ':3306'

```

Вывод будет содержать одну строку с PID и именем программы (например, `mysqld`).

Найти все соединения с конкретным удалённым IP-адресом:

```bash
sudo netstat -tn | grep '192.168.1.100'

```

...

Для выхода нажмите `Ctrl+C`.

### Шаг 5: Определите, какой процесс использует конкретный порт (практический пример)

Задача: Порт 8080 занят, но неизвестно каким приложением. Нужно найти и, возможно, остановить этот процесс.

1. Найдите процесс:

```bash
sudo netstat -tulpn | grep ':8080'

```

 Пример вывода: `tcp 0 0 0.0.0.0:8080 0.0.0.0:* LISTEN 4321/java`
2. Проанализируйте: Процесс с PID `4321` и именем `java` слушает порт 8080 на всех интерфейсах.
3. (Опционально) Получите больше информации о процессе:

```bash
ps aux | grep 4321
# или
sudo lsof -i :8080

```
4. Если это нежелательный процесс, его можно остановить: `sudo kill 4321` (мягко) или `sudo kill -9 4321` (принудительно).

## Проверка результата

- Успешное выполнение: Команда `sudo netstat -tulpn` выводит таблицу с колонками `Proto`, `Local Address`, `State`, `PID/Program name`. Вы видите список всех слушающих портов и активных соединений.
- Практический результат: Вы можете по имени процесса (`PID/Program name`) однозначно связать порт с конкретным сервисом (nginx, mysql, sshd, docker-proxy и т.д.). Вы можете отфильтровать вывод и найти информацию по нужному вам порту или IP.
- Критерий завершения: Вы смогли ответить на вопрос "Какая программа использует порт X?" или "Какие соединения сейчас активны?" с помощью `netstat`.

---

Title: How to know what program is listening on a given port?
URL: https://askubuntu.com/questions/278448/how-to-know-what-program-is-listening-on-a-given-port
Published: N/A
Author: N/A
Highlights:
Open your terminal and type as 

lsof -i :8000

that command will list you the application used by that port with PID.
(If no results run via sudo since your might have no permission to certain processes.)

For example, with port 8000 (python3 -m http.server):

$ lsof -i :8000
COMMAND PID USER FD TYPE DEVICE SIZE/OFF NODE NAME
python3 3269 user 3u IPv4 1783216 0t0 TCP *:8000 (LISTEN)

And port 22 (SSH):

$ sudo lsof -i :22
COMMAND PID USER FD TYPE DEVICE SIZE/OFF NODE NAME
sshd 998 root 3u IPv4 1442116 0t0 TCP *:ssh (LISTEN)
sshd 998 root 4u IPv6 1442118 0t0 TCP *:ssh (LISTEN)

Hope that helps.

...

You can use netstat to see which process is listening on which port.

You can use this command to have a full detail :

sudo netstat -peanut

if you need to know exactly which one is listening on port 8000 you can use this :

sudo netstat -peanut | grep ":8000 "

There is no process that can hide from netstat.

...

$ lsof -i :8000
COMMAND PID USER FD TYPE DEVICE SIZE/OFF NODE NAME
squid3 1289 proxy 15u IPv6 14810490 0t0 TCP *:8000 (LISTEN)

$ ps -fp 1289
UID PID PPID C STIME TTY TIME CMD
proxy 1289 1 0 09:48 ? 00:00:00 /usr/sbin/squid3 -N -f /etc/squid-deb-proxy/squid-deb-proxy.conf

I can see right there that squid is the process, but it is actualy my squid-deb-proxy that is taking up the port.
=== END OF OUTPUT A82 ===


########## QUESTION q18 ##########
Question: Python: how to read a large file line by line without loading it into memory?
Reference answer: with open(path) as f: for line in f: ... — iterating the file object is memory efficient.
Reference source: https://docs.python.org/3/tutorial/inputoutput.html

=== OUTPUT C15 ===
**Iterate directly over the file object using a `for` loop inside a `with` statement.** Python file objects act as lazy iterators, reading one buffered line at a time so memory usage stays constant regardless of file size. [1]

Use the built-in `open()` function with a context manager to ensure the file closes automatically: [2]

python

```
with open("large_file.txt", "r", encoding="utf-8") as file:
    for line in file:
        # Process one line at a time (use line.strip() to remove '\n')
        print(line.strip())
```

Используйте код с осторожностью.

### Reusable Generator Pattern

If you need to pass the line stream through a data pipeline, wrap the loop in a generator function using `yield`: [3]

python

```
def read_lines(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            yield line.strip()

for clean_line in read_lines("large_file.txt"):
    process(clean_line)
```

Используйте код с осторожностью.

### Key Details & Pitfalls

-   **Avoid `.read()` and `.readlines()`:** Both methods load the entire file into RAM at once, which triggers a `MemoryError` on multi-gigabyte files. [4]
    
-   **Do not accumulate results in a list:** Appending every processed line to a list (`results.append(line)`) still fills up memory. Write outputs directly to a new file or database inside the loop.
    
-   **Custom buffer size:** Python automatically buffers disk reads in small chunks, but you can adjust the buffer size (in bytes) via the `buffering` parameter in Python's open() documentation (e.g., `open("large_file.txt", "r", buffering=1024*1024)` for a 1 MB buffer). [4]
    
-   **Structured formats:** For massive structured files, use streaming parsers like Python's built-in `csv.reader` (which wraps the file iterator directly) or [ijson](https://pypi.org/project/ijson/) for incremental JSON parsing. [4]
    

If you're working with a specific file format (such as **CSV**, **JSON**, or **compressed `.gz` logs**) or need to **filter and write** the output efficiently, let me know and I can share a tailored snippet.

Sources:
1. https://medium.com/@akaashhazarika/processing-multi-gigabyte-files-in-python-without-crashing-94fd39adc21e
2. https://www.geeksforgeeks.org/python/read-a-file-line-by-line-in-python/
3. https://www.youtube.com/watch?v=8a6dWenA8Hs
4. https://blog.devgenius.io/10-ways-to-work-with-large-files-in-python-effortlessly-handle-gigabytes-of-data-aeef19bc0429
5. https://pypi.org/project/ijson/
6. https://aitapri.com/interview-questions/python/read-large-file-line-by-line
=== END OF OUTPUT C15 ===

=== OUTPUT V44 ===
The standard answer is to iterate over the file object directly. Python yields one line at a time, so memory use stays roughly constant regardless of file size.

- **Default pattern:** Iterating directly over a file object is the simplest, safest, and most efficient way to read a file line by line. A common form is `with open(path, encoding="utf-8") as f: for line in f: ...`, and a file object is already an iterator.
- **Why it scales:** Python reads a single line, processes it, and moves on to the next, so the whole file never sits in memory. The sources say line-by-line iteration keeps memory usage constant.
- **Line numbers:** Wrap the file in `enumerate(f, start=1)` to get a counter alongside each line without a manual variable.
- **Manual control:** `readline()` returns one line per call and returns an empty string at end of file. It suits cases where reading must be conditional, such as stopping once a condition is met.
- **What to avoid:** `readlines()` reads the entire file into memory and returns a list of lines, so it is unsuitable for large files.
- **Encoding:** Specify the encoding explicitly, such as UTF-8, and use `"rb"` for binary data.

These points come from DataCamp tutorials, which are a single source family rather than independent references. The core advice matches standard Python practice.

Sources:
1. https://www.datacamp.com/tutorial/python-read-file-line-by-line
2. https://www.datacamp.com/th/tutorial/python-read-file-line-by-line
3. https://www.datacamp.com/nl/tutorial/python-read-file-line-by-line
4. https://www.datacamp.com/ja/tutorial/python-read-file-line-by-line
5. https://www.datacamp.com/ko/tutorial/python-read-file-line-by-line
6. https://www.datacamp.com/zh/tutorial/python-read-file-line-by-line
7. https://www.datacamp.com/hi/tutorial/python-read-file-line-by-line
=== END OF OUTPUT V44 ===

=== OUTPUT I23 ===
Title: How can I read large text files line by line, without loading them into memory?
URL: https://stackoverflow.com/questions/6475328/how-can-i-read-large-text-files-line-by-line-without-loading-them-into-memory
Published: N/A
Author: N/A
Highlights:
### Answer by John La Rooy (score: 451 [ACCEPTED])

Use a for loop on a file object to read it line-by-line. Use with open(...) to let a context manager ensure that the file is closed after reading:
with open("log.txt") as infile:
 for line in infile:
 print(line)

### Answer by Keith (score: 81)

All you need to do is use the file object as an iterator.

for line in open("log.txt"):
 do_something_with(line)

Even better is using context manager in recent Python versions.

with open("log.txt") as fileobject:
 for line in fileobject:
 do_something_with(line)

This will automatically close the file as well.

...

You are better off using an iterator instead.
Relevant: fileinput — Iterate over lines from multiple input streams.
From the docs:
import fileinput
for line in fileinput.input("filename", encoding="utf-8"):
 process(line)

This will avoid copying the whole file into memory at once.

...

An old school approach:

fh = open(file_name, 'rt')
line = fh.readline()
while line:
 # do stuff with line
 line = fh.readline()
fh.close()

...

with open('filename','r',buffering=100000) as f:
 for line in f:

...

Here's what you do if you dont have newlines in the file:
with open('large_text.txt') as f:
 while True:
 c = f.read(1024)
 if not c:
 break
 print(c,end='')

...

How about this?
Divide your file into chunks and then read it line by line, because when you read a file, your operating system will cache the next line. If you are reading the file line by line, you are not making efficient use of the cached information. 

Instead, divide the file into chunks and load the whole chunk into memory and then do your processing.

---

Title: How to Read a File Line by Line in Python
URL: https://www.datacamp.com/tutorial/python-read-file-line-by-line
Published: N/A
Author: N/A
Highlights:
## The Recommended Way to Read a File Line by Line in Python

If you remember just one pattern from this article, make it this one. In most situations, iterating directly over a file object is the simplest, safest, and most efficient way to read a file line by line, and it’s the approach you’ll see most often in real Python code.

At a basic level, a file object in Python is already an iterator. That means you can loop over it directly and get one line at a time:

```
with open("example.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line)

```

Explain code Powered by

This does exactly what it looks like. Python opens the file and yields each line one by one as the loop runs. There’s no manual indexing, no extra function calls, and no hidden complexity.

One of the biggest advantages of this approach is memory efficiency. Python does not load the entire file into memory. Instead, it reads a single line, processes it, and moves on to the next. That makes this pattern safe even for very large files, such as logs or raw data exports.

It’s also the most Pythonic solution. Iterating directly over a file object is clear, readable, and immediately understandable to anyone familiar with Python. That matters as scripts grow or when other people need to read your code later.

Because of these benefits, this should be your default choice unless you have a very specific reason to do something else. It automatically handles large files, scales well as file sizes grow, and avoids unnecessary memory usage—all without adding extra complexity.

...

When Python reads a file line by line, each line usually ends with a newline character (`\n`). That newline is part of the line itself, not something Python adds later. 

For example, a file that looks like this:

```
apple
banana
cherry

```

Explain code Powered by

...

### Cleaning lines for processing

The most common solution is to strip whitespace before using each line:

```
with open("data.txt", encoding="utf-8") as file:
    for line in file:
        clean_line = line.strip()
        print(clean_line)

```

Explain code Powered by

The `strip()` method removes leading and trailing whitespace, including spaces, tabs, and newline characters. This is usually what you want when:

- Comparing lines to expected values
- Converting strings to numbers
- Building structured data from file contents

...

The `readline()` method reads a single line each time it’s called. When the file is exhausted, it returns an empty string:

...

print(line.strip())

...

## Why readlines() Is Usually a Bad Idea for Large Files

The `readlines()` method reads the entire file into memory and returns a list of lines:

```
with open("example.txt", encoding="utf-8") as file:
    lines = file.readlines()

```

Explain code Powered by

This works for small files—but it doesn’t scale.

Because the entire file is loaded at once:

- Memory usage grows with file size
- Large files can slow your program or crash it
- Problems often appear only in production

### When readlines() is acceptable

It’s reasonable when:

- The file is guaranteed to be small
- You truly need all lines at once
- The size is predictable and bounded

Otherwise, iterating line by line is almost always the better choice.

## Common Mistakes When Reading Files Line by Line

Most issues come from a few small oversights:

- Forgetting to close files → Use `with`
- Loading entire files unintentionally → Avoid `read()` and `readlines()`
- Ignoring encodings → Specify UTF-8 explicitly
- Confusing text and binary modes → Use `"r"` for text, `"rb"` for binary

Once you’re aware of these, they’re easy to avoid.

---

Title: io — Core tools for working with streams — Python 3.15.2 documentation
URL: https://docs.python.org/3/library/io.html
Published: N/A
Author: N/A
Highlights:
### Text I/O¶

Text I/O expects and produces `str` objects. This means that whenever the backing store is natively made of bytes (such as in the case of a file), encoding and decoding of data is made transparently as well as optional translation of platform-specific newline characters.

The easiest way to create a text stream is with `open()`, optionally specifying an encoding:

```
f = open("myfile.txt", "r", encoding="utf-8")

```

In-memory text streams are also available as `StringIO` objects:

```
f = io.StringIO("some initial text data")

```

When working with a non-blocking stream, be aware that read operations on text I/O objects might raise a `BlockingIOError` if the stream cannot perform the operation immediately.

...

### Binary I/O¶

Binary I/O (also called buffered I/O) expects bytes-like objects and produces `bytes` objects. No encoding, decoding, or newline translation is performed. This category of streams can be used for all kinds of non-text data, and also when manual control over the handling of text data is desired.

The easiest way to create a binary stream is with `open()` with `'b'` in the mode string:

```
f = open("myfile.jpg", "rb")

```

In-memory binary streams are also available as `BytesIO` objects:

```
f = io.BytesIO(b"some initial binary data: \x00\x01")

```

...

Raw I/O (also called unbuffered I/O) is generally used as a low-level building-block for binary and text streams; it is rarely useful to directly manipulate a raw stream from user code. Nevertheless, you can create a raw stream by opening a file in binary mode with buffering disabled:

```
f = open("myfile.jpg", "rb", buffering=0)

...

readline(size=-1, /)¶
: Read and return one line from the stream. If size is specified, at most size bytes will be read.

The line terminator is always `b'\n'` for binary files; for text files, the newline argument to `open()` can be used to select the line terminator(s) recognized.

readlines(hint=-1, /)¶
: Read and return a list of lines from the stream. hint can be specified to control the number of lines read: no more lines will be read if the total size (in bytes/characters) of all lines so far exceeds hint.

hint values of `0` or less, as well as `None`, are treated as no hint.

Note that it’s already possible to iterate on file objects using `for
line in file: ...` without calling `file.readlines()`.

...

class io. BufferedReader(raw, buffer_size= DEFAULT_BUFFER_SIZE)¶
: A buffered binary stream providing higher-level access to a readable, non seekable `RawIOBase` raw binary stream. It inherits from `BufferedIOBase`.

When reading data from this object, a larger amount of data may be requested from the underlying raw stream, and kept in an internal buffer. The buffered data can then be returned directly on subsequent reads.

The constructor creates a `BufferedReader` for the given readable raw stream and buffer_size. If buffer_size is omitted, `DEFAULT_BUFFER_SIZE` is used.

...

class io. StringIO(initial_value='', newline='\n')¶
: A text stream using an in-memory text buffer. It inherits from `TextIOBase`.

The text buffer is discarded when the `close()` method is called.

The initial value of the buffer can be set by providing initial_value. If newline translation is enabled, newlines will be encoded as if by `write()`. The stream is positioned at the start of the buffer which emulates opening an existing file in a `w+` mode, making it ready for an immediate write from the beginning or for a write that would overwrite the initial value. To emulate opening a file in an `a+` mode ready for appending, use `f.seek(0, io.SEEK_END)` to reposition the stream at the end of the buffer.

...

getvalue()¶
: Return a `str` containing the entire contents of the buffer. Newlines are decoded as if by `read()`, although the stream position is not changed.

Example usage:

```
import io

output = io.StringIO()
output.write('First line.\n')
print('Second line.', file=output)

# Retrieve file contents -- this will be
# 'First line.\nSecond line.\n'
contents = output.getvalue()

# Close object and discard memory buffer --
# .getvalue() will now raise an exception.
output.close()

...

By reading and writing only large chunks of data even when the user asks for a single byte, buffered I/O hides any inefficiency in calling and executing the operating system’s unbuffered I/O routines. The gain depends on the OS and the kind of I/O which is performed. For example, on some modern OSes such as Linux, unbuffered disk I/O can be as fast as buffered I/O. The bottom line, however, is that buffered I/O offers predictable performance regardless of the platform and the backing device. Therefore, it is almost always preferable to use buffered I/O rather than unbuffered I/O for binary data.

...

Text I/O over a binary storage (such as a file) is significantly slower than binary I/O over the same storage, because it requires conversions between unicode and binary data using a character codec. This can become noticeable handling huge amounts of text data like large log files. Also, `tell()` and `seek()` are both quite slow due to the reconstruction algorithm used.

---

Title: MemoryError when trying to load 5GB text file
URL: https://stackoverflow.com/questions/26032287/memoryerror-when-trying-to-load-5gb-text-file
Published: 2014-09-25T06:46:31.000Z
Author: N/A
Highlights:
The best way for you to handle large files would be -

```
with open('../file.txt', 'r') as f:
    for line in f:
        # do stuff

```

`readlines()` would error because you are trying to load too large a file directly into the memory. The above code will automatically close your file once you are done processing on it.

...

If you want to process lines in the file, you should rather use:

```
for line in file:
    # do something with the line

```

It will read the file line by line, instead of reading it all to the RAM at once.

---

Title: Files and Input/Output — Textbook of Python
URL: https://www.textbookofpython.com/chapter/files-and-io.html
Published: N/A
Author: Dr Chris Paton
Highlights:
Python provides several ways to read a file's contents:

```python
with open("notes.txt") as f:
    # Read the entire file as a single string
    content = f.read()

with open("notes.txt") as f:
    # Read one line at a time
    first_line = f.readline()
    second_line = f.readline()

with open("notes.txt") as f:
    # Read all lines into a list
    lines = f.readlines()
    print(lines)    # Output: ['line one\n', 'line two\n', 'line three\n']

```

The most Pythonic approach is to iterate over the file object directly. This reads one line at a time and is memory-efficient even for enormous files:

```python
with open("notes.txt") as f:
    for line in f:
        print(line.strip())    # strip() removes the trailing newline

```

This is the pattern you should reach for by default. It is clean, it is efficient, and it communicates intent clearly.

---

Title: When should I ever use file.read() or file.readlines()?
URL: https://stackoverflow.com/questions/38105507/when-should-i-ever-use-file-read-or-file-readlines
Published: N/A
Author: N/A
Highlights:
The short answer to your question is that each of these three methods of reading bits of a file have different use cases. As noted above, f.read() reads the file as an individual string, and so allows relatively easy file-wide manipulations, such as a file-wide regex search or substitution.
f.readline() reads a single line of the file, allowing the user to parse a single line without necessarily reading the entire file. Using f.readline() also allows easier application of logic in reading the file than a complete line by line iteration, such as when a file changes format partway through.
Using the syntax for line in f: allows the user to iterate over the file line by line as noted in the question.
(As noted in the other answer, this documentation is a very good read):
https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects
Note:
It was previously claimed that f.readline() could be used to skip a line during a for loop iteration. However, this doesn't work in Python 2.7, and is perhaps a questionable practice, so this claim has been removed.

---

Title: Processing large files using python | Oxford Protein Informatics Group
URL: https://www.blopig.com/blog/2016/08/processing-large-files-using-python/
Published: 2016-08-10T15:43:25.000Z
Author: Author Alistair Martin View all posts
Highlights:
My first big data tip for python is learning how to break your files into smaller units (or chunks) in a manner that you can make use of multiple processors. Let’s start with the simplest way to read a file in python.

```

with open("input.txt") as f:
    data = f.readlines()
    for line in data:
        process(line)

```

This mistake made above, with regards to big data, is that it reads all the data into RAM before attempting to process it line by line. This is likely the simplest way to cause the memory to overflow and an error raised. Let’s fix this by reading the data in line by line, so that only a single line is stored in the RAM at any given time.

```

with open("input.txt") as f:
    for line in f:
        process(line)

```

This is a big improvement, namely it doesn’t crash when fed a big file (though also it’s shorter!). Next we should attempt to speed this up a bit by making use of all these otherwise idle cores.

```

import multiprocessing as mp

#init objects
pool = mp.Pool(cores)
jobs = []

#create jobs
with open("input.txt") as f:
    for line in f:
        jobs.append( pool.apply_async(process,(line)) )

#wait for all jobs to finish
for job in jobs:
    job.get()

#clean up
pool.close()

...

While the above is now making use of all those cores, it sadly runs into memory problems once again. We specifically use apply_async function so that the pool isn’t blocked while each line processes. However, in doing so, all the data is read into memory once again; this time stored as individual lines associated with each job, waiting inline to be processed. As such, the memory will again overflow. Ideally the method will only read the line into memory when it is its turn to be processed.

```

import multiprocessing as mp

def process_wrapper(lineID):
    with open("input.txt") as f:
        for i,line in enumerate(f):
            if i != lineID:
                continue
            else:
                process(line)
                break

#init objects
pool = mp.Pool(cores)
jobs = []

#create jobs
with open("input.txt") as f:
    for ID,line in enumerate(f):
        jobs.append( pool.apply_async(process_wrapper,(ID)) )

#wait for all jobs to finish
for job in jobs:
    job.get()

#clean up
pool.close()

```

Above we’ve now changed the function fed to pool of workers to include opening the file, locating the specified line, reading it into memory, and then processing it. The only input now stored for each job spawned is the line number, thereby preventing the memory overflow. Sadly, the overhead involved in having to locate the line by reading iteratively through the file for each job is untenable, getting progressively more time consuming as you get further into the file. To avoid this we can use the seek function of file objects which skips you to a particular location within a file. Combining with the tell function, which returns the current location within a file, gives:

```

import multiprocessing as mp

def process_wrapper(lineByte):
    with open("input.txt") as f:
        f.seek(lineByte)
        line = f.readline()
        process(line)

#init objects
pool = mp.Pool(cores)
jobs = []

#create jobs
with open("input.txt") as f:
    nextLineByte = f.tell()
    for line in f:
        jobs.append( pool.apply_async(process_wrapper,(nextLineByte)) )
        nextLineByte = f.tell()

#wait for all jobs to finish
for job in jobs:
    job.get()

#clean up
pool.close()

```

Using seek we can move directly to the correct part of the file, whereupon we read a line into the memory and process it. We have to be careful to correctly handle the first and last lines, but otherwise this does exactly what we set out, namely using all the cores to process a given file while not overflowing the memory.

I’ll finish this post with a slight upgrade to the above as there is a reasonable amount of overhead associated with opening and closing the file for each individual line. If we process multiple lines of the file at a time as a chunk, we can reduce these operations. The biggest technicality when doing this is noting that when you jump to a location in a file, you are likely not located at the start of a line. For a simple file, as in this example, this just means you need to call readline, which reads to next newline character. More complex file types likely require additional code to locate a suitable location to start/end a chunk.

---

Title: How to read large text files in Python? - GeeksforGeeks
URL: https://www.geeksforgeeks.org/python/how-to-read-large-text-files-in-python/
Published: N/A
Author: N/A
Highlights:
To read large text files in Python, we can use the file object as an iterator to iterate over the file and perform the required task. Since the iterator just iterates over the entire file and does not require any additional data structure for data storage, the memory consumed is less comparatively. Also, the iterator does not perform expensive operations like appending hence it is time-efficient as well. Files are iterable in Python hence it is advisable to use iterators.

...

Here, the only difference is that we will use the iterator of a file object. The open() function wraps the entire file into a file object. After that, we use an iterator to get the lines in the file object. We open the file in a 'with' block as it automatically closes the file as soon as the entire block executes.

```
import time

start = time.time()
count = 0
with open("sample.txt") as file:
    for line in file:
       print(line)
       count = count + 1
end =  time.time()
print("Execution time in seconds: ",(end-start))
print("No of lines printed: ",count)

---

Title: Files larger than memory · Python, from Zero, for AI
URL: https://addaly.com/learn/python-for-ai/streaming-large-files
Published: N/A
Author: N/A
Highlights:
The file is the same size in all four. What differs is how much of it exists as Python objects at once: a dict with five short keys is 300 to 400 bytes for maybe 60 bytes of data. Looping over the file object holds one line, whatever the file size, which is why it is the only one that still works at 40 GB.

...

## The line that kills the process

Python Copy Python code

```
data = open("events.jsonl").read()          # a 6 GB string
rows = list(csv.DictReader(f))              # 40 million dictionaries
```

Both load the whole file into memory. On a laptop with 8 GB of RAM the first raises `MemoryError` if you are lucky, and if you are not, the operating system starts swapping and the machine becomes unusable for ten minutes.

A Python object costs far more than the bytes it represents. A dictionary with five short string keys is roughly 300 to 400 bytes; the same row in the file might be 60. Loading a 1 GB CSV into a list of dictionaries can need 6 to 8 GB.

## Files are already iterators

Python Copy Python code

```
with open("events.jsonl", encoding="utf-8") as f:
    for line in f:
        record = json.loads(line)
        process(record)
```

This holds one line at a time. The file object reads a buffer from disk, hands you lines, and discards them as you go. It works identically for a 2 KB file and a 200 GB one, and it is the default way to read text in Python for exactly that reason.

`csv.DictReader` and `csv.reader` stream the same way, as long as you do not wrap them in `list()`.

## Write your own streaming step with `yield`

Python Copy Python code

```
def parse_events(path):
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                yield json.loads(line)

def large_orders(events, threshold):
    for e in events:
        if e.get("amount", 0) > threshold:
            yield e

for order in large_orders(parse_events(path), 10_000):
    print(order["id"])
```

A function containing `yield` is a generator: calling it produces an object that does nothing until you loop over it, and then produces one value at a time. Nothing above holds more than one record in memory, and the three stages read as a pipeline. The generators lesson in the last module takes the mechanism apart; this is the use you will reach for first.

Two properties to know now. A generator is single-use: loop over it twice and the second loop sees nothing, with no error. And the work happens while you consume it, so an exception from line 4 million surfaces in the middle of your loop rather than at the call.

...

## Peeking at the first few

Python Copy Python code

```
from itertools import islice

with open(path, encoding="utf-8") as f:
    for line in islice(f, 5):
        print(line[:200])
```

`islice` takes the first n items of any iterator without reading the rest. This is how you inspect the shape of a 40 GB file in a fraction of a second, and it is the right first move on any file you have not seen before. On the command line, `head -5 file.jsonl` does the same thing.

---

Title: (10/27/20) Methods, iterables, and generators for reading files — Analytics and Integrative Machine Learning
URL: https://ncar.github.io/aiml-utils/generators.html
Published: N/A
Author: N/A
Highlights:
Reading files like this shouldn’t be a problem for file sizes up to ~1G. But sometimes we have no choice and have to work with large files (sometimes hundreds of gigs). As a result the readlines operation can take a very long time. Furthermore, if the file is too large to load into memory, python will throw the error MemoryError and your program will terminate with error.

We frequently encounter large datafiles at NCAR. What can we do about it?

Reading and processing one line at a time would solve this problem. We could even process an “infinitely” large file, which means any file that’s too large to load fully into memory.

This kind of file reading is called lazy reading.

## The Python Generator¶

There is a special tool in the python toolbox that easily enables lazy reading called a generator. The generator object is built on top of python’s Iterator object class, but I will cover them in reverse below.

```
def generator_loader(fn):
    with open(fn, "r") as fid:
        for line in fid:
            yield line.strip("\n").split(" ")[-1]

```

We’ve replaced the return with something new named \(\color{green}{\textbf{yield}}\). This chunk of code looks similar to the method_loader!

Test it.

```
for processed_line in generator_loader(fn):
    print(processed_line)
    break # Stop early, I don't need to print 1,000,000 lines!

```

It behaves similarly when in use as compared to the method variant presented above. The big difference is that the generator version is more memory efficient because, through \(\color{green}{\textbf{yield}}\), lines are read into memory one at a time, returned, released, …, until reaching the end of the file (EOF).

That is to say \(\color{green}{\textbf{yield}}\) returns more than once, whereas \(\color{green}{\textbf{return}}\) in a method signals the end (in terms of memory usage, as it is freed and the method is exited).

Generators work nicely with serialized data … you may have dumped data using the pickle library before. The pickle library allows you to do that for the entire file, all in one go, or line-by-line as the example below illustrates:

```
import pickle

```

```
fn_pkl = "generators/test_data.pkl"

...

with open(fn, "wb") as fid:

...

yield pickle.load(fid) # Iteration over .load

...

Fortunatly, there is a generalized version of yield, \(\color{green}{\textbf{yield from}}\) for these siuations:

```
def load_from_pickle(fn):
    with open(fn, "rb") as fid:
        yield from pickle.load(fid)

...

```

...

continue

...

## When should I use a generator rather than a method?¶

There are lots of scenerios, in addition to data loading! Note that in the first method example above, a list was returned. Do you need all elements of the list, all at the same time? If the answer is no, then you want to try to use a generator if that file is large in size!

With generators one tries to balance the time spent performing operations with/on the data with memory utilization. Using them will often be determined by how your program is designed to run and utilize resources. If you are presented with a significant memory bottleneck, generators are very often the way to go. However if your program does not have said memory issue, using a generator might result in the program running significantly slower.

As you use generators more and more in your work-flow, you will learn to apply them when they are needed and when to avoid them when they do not offer any benefit over using methods.
=== END OF OUTPUT I23 ===


########## QUESTION q19 ##########
Question: Как с помощью ffmpeg сделать GIF из видео с частотой 10 кадров в секунду и шириной 480 пикселей?
Reference answer: Filters fps=10,scale=480:-1 (flags=lanczos); for quality two passes with palettegen and paletteuse.
Reference source: http://blog.pkh.me/p/21-high-quality-gif-with-ffmpeg.html

=== OUTPUT I63 ===
Чтобы создать GIF-анимацию с частотой **10 кадров в секунду** и шириной **480 пикселей** через [FFmpeg](https://ffmpeg.org/), лучше всего использовать метод генерации индивидуальной цветовой палитры — это избавит картинку от зернистости и искажения цветов. [2]

Выполните в терминале или командной строке следующую команду:

bash

```
ffmpeg -i input.mp4 -vf "fps=10,scale=480:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" output.gif
```

Используйте код с осторожностью.

**Что делают параметры этой команды:**

-   **`-i input.mp4`** — путь к исходному видеофайлу.
    
-   **`fps=10`** — задает частоту 10 кадров в секунду.
    
-   **`scale=480:-1:flags=lanczos`** — устанавливает ширину 480 пикселей. Значение `-1` автоматически вычисляет высоту с сохранением пропорций видео, а алгоритм `lanczos` обеспечивает высокую четкость при уменьшении.
    
-   **`split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse`** — анализирует видео, создает оптимальную 256-цветную палитру и применяет ее при сборке GIF.
    
-   **`output.gif`** — имя итогового файла. [3]
    

* * *

### Быстрый способ (в одну простую строку)

Если качество цветопередачи не критично и нужна максимально простая команда без генерации палитры:

bash

```
ffmpeg -i input.mp4 -vf "fps=10,scale=480:-1:flags=lanczos" output.gif
```

Используйте код с осторожностью.

### Полезные дополнения

-   **Вырезать конкретный фрагмент:** добавьте параметры `-ss` (время начала) и `-t` (длительность в секундах) перед `-i`. Например, чтобы взять 5 секунд начиная с 12-й секунды:
    
    bash
    
    ```
    ffmpeg -ss 00:00:12 -t 5 -i input.mp4 -vf "fps=10,scale=480:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" output.gif
    ```
    
    Используйте код с осторожностью.
    
-   **Уменьшить вес файла:** можно ограничить количество цветов в палитре до 128 или 64 (например, `palettegen=max_colors=128`). [2]
    

Нужно ли дополнительно **обрезать видео по времени**, **уменьшить размер итогового файла** или **убрать зацикливание** анимации? Подскажу, какие флаги добавить в команду.

Sources:
1. https://ffmpeg.org/
2. https://fora-soft.ru/kursy/video-encoding/containers-and-pipeline/ffmpeg-shpargalka-dlya-razrabotchika
3. https://www.mux.com/articles/create-gifs-from-video-clips-with-ffmpeg
4. https://www.reddit.com/r/ffmpeg/comments/1lpcq4l/convert_a_video_to_fast_gif_using_ffmpeg_tutorial/?tl=ru
=== END OF OUTPUT I63 ===

=== OUTPUT A96 ===
Чтобы сделать GIF с частотой 10 кадров в секунду и шириной 480 пикселей, используйте фильтры `fps` и `scale`. Один из найденных источников показывает такой же подход: fps=10,scale=360:-1 задаёт частоту и ширину, а при высоте `-1` сохраняются пропорции.

**Команда в один проход** (с палитрой для лучшего качества):

```
ffmpeg -i input.mp4 -vf "fps=10,scale=480:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" output.gif
```

Здесь `flags=lanczos` задаёт алгоритм масштабирования, а палитра строится из самого видео. Один источник отмечает, что для большинства GIF 10–15 fps дают хороший баланс между плавностью движения и размером файла.

**Вариант в два шага** (тот же результат, но палитру можно посмотреть отдельно):

```
ffmpeg -i input.mp4 -vf "fps=10,scale=480:-1:flags=lanczos,palettegen" palette.png
ffmpeg -i input.mp4 -i palette.png -filter_complex "fps=10,scale=480:-1:flags=lanczos[x];[x][1:v]paletteuse" output.gif
```

**Выбор фрагмента:** чтобы взять только часть видео, добавьте `-ss` (начало) и `-t` (длительность), например `-ss 00:00:10 -t 00:00:05` (5 секунд, начиная с 10-й). Ещё один источник советует не делать GIF длиннее 5 секунд, чтобы файл оставался небольшим.

Результаты поиска не проверялись на актуальность версий ffmpeg. Палитры и фильтр `paletteuse` доступны начиная с версии 2.6.

Sources:
1. https://www.cincopa.com/learn/creating-gifs-from-videos-using-ffmpeg
2. https://gist.github.com/RhinoLu/93dc463d037d2d7c5887b38c933ab801
3. https://www.mux.com/articles/create-gifs-from-video-clips-with-ffmpeg
4. https://creatomate.com/blog/how-to-make-a-gif-from-a-video-using-ffmpeg
5. https://bannerbear.com/blog/how-to-make-a-gif-from-a-video-using-ffmpeg
6. https://cloudinary.com/guides/image-formats/ffmpeg-mp4-to-gif
7. https://kiwix.ounapuu.ee/content/superuser.com_en_all_2023-11/questions/556029/how-do-i-convert-a-video-to-gif-using-ffmpeg-with-reasonable-quality
=== END OF OUTPUT A96 ===

=== OUTPUT V65 ===
Title: Working with GIFs: Convert Video to GIF and Optimize for the Web
URL: https://www.ffmpeg.media/articles/working-with-gifs-convert-optimize
Published: 2024-09-10T00:00:00.000Z
Author: N/A
Highlights:
## Basic Video to GIF Conversion

`# Simple conversion (may be large)
ffmpeg -i input.mp4 -vf "fps=10,scale=480:-1:flags=lanczos" output.gif

# Better quality with custom palette (two-pass)
ffmpeg -i input.mp4 -vf "fps=10,scale=480:-1:flags=lanczos,palettegen" palette.png
ffmpeg -i input.mp4 -i palette.png -lavfi "fps=10,scale=480:-1:flags=lanczos[x];[x][1:v]paletteuse" output.gif`

The two-pass approach generates a palette that matches your content, avoiding the generic 256-color web palette and giving you better visual quality.

---

Title: How to Convert a Video to GIF: Free, Small, Sharp
URL: https://quickveed.com/blogs/how-to-convert-video-to-gif
Published: 2026-10-05T17:39:24.000Z
Author: Ijharul Islam
Highlights:
## Method 2: Convert a video to GIF with FFmpeg

FFmpeg, the free command-line tool, makes high-quality GIFs with two filters: palettegen builds the best 256 colours for your clip, and paletteuse applies them. This one-line command takes 4 seconds starting at 0:05, at 10 fps and 480 px wide:

`ffmpeg -ss 5 -t 4 -i input.mp4 -vf "fps=10,scale=480:-1:flags=lanczos,split[a][b];[a]palettegen[p];[b][p]paletteuse" -loop 0 output.gif`

| Part | What it does |
| --- | --- |
| `-ss 5 -t 4` | Start at 5 seconds, take 4 seconds |
| `fps=10` | 10 frames per second |
| `scale=480:-1:flags=lanczos` | 480 px wide, height in proportion, sharp scaling |
| `palettegen` / `paletteuse` | Build and apply a 256-colour palette for this clip |
| `-loop 0` | Loop forever (use -1 for no loop) |

Without the palette step, FFmpeg uses a generic palette and the GIF looks blotchy. For a smaller file, add `paletteuse=dither=bayer:bayer_scale=3`, which uses a pattern dither that compresses better.

---

Title: How to make GIFs with FFMPEG
URL: https://engineering.giphy.com/how-to-make-gifs-with-ffmpeg/
Published: N/A
Author: N/A
Highlights:
While the above generally works with most content, you may be interested to learn that GIFs support widely varying frame rates or frame delays that when converted to a video format without transformation, can trip up certain video players. If I were to use the previous command to convert my contrived and not very useful as a countdown example,`321.gif`, the VLC player on my Mac has trouble playing that mp4. Don’t worry, I still love you VLC. If your particular application might be sensitive to such issues, you can try the following command:

```

bash
$ ffmpeg -i 321.gif -filter_complex "[0:v] fps=15" -vsync 0 -f mp4 -pix_fmt yuv420p 321.mp4

...

This here is how you specify a filter graph. Filters process raw video or audio based on the name of the filter and the arguments specified. You can read more here.

...

This specifies that we will be using the first video stream fed to FFmpeg as input to this section of the filter. If you had a file with multiple video streams, or you put two inputs in the command you could imagine selecting the second video stream with`[1:v]`, or the

...

```

fps=15

```

This is the fps or “frames per second” or “framerate” filter. If you don’t want to lose any visual content, I suggest you set the value to the nominal framerate of the input, so the inverse of the minimum frame delay.

```

-vsync 0

```

This vsync flag tells ffmpeg to not modify the timing of the frames as they come from the decoder. This should keep your weird gif timing intact.

...

So that was nice, one-liner FFmpeg command to convert video to high quality GIF clip. But there’s still a problem. Our GIF is still too big. Unfortunately GIFs aren’t well suited to being 1080p even if they are 2.5 seconds long. Let’s fix that with this next command:

```

bash
$ ffmpeg -ss 61.0 -t 2.5 -i StickAround.mp4 -filter_complex "[0:v] fps=12,scale=480:-1,split [a][b];[a] palettegen [p];[b][p] paletteuse" SmallerStickAround.gif

```

Most of the above is pretty familiar. We just have a couple of new additions to the filter graph.

```

-filter_complex "[0:v] fps=12,scale=w=480:h=-1,split [a][b];[a] palettegen [p];[b][p] paletteuse"

```

Let’s look at that first stage.

```

[0:v] fps=12,scale=480:-1,split [a][b];

```

Our split filter from before has a couple of new friends – fps and scale. I’ve separated them with commas, which you can do with filters that accept a single input and output. We’ve seen fps before. It changes the frame rate. In this case it took a 24 fps input video and halved the framerate to`12` as you can see. I think 12 fps is high enough for this content and gets our file size down, but decide for yourself. The next filter in line here is scale, which resizes its input video. The scale filter needs two parameters, width and height, and they can look a little odd. To complicate matters they can take several forms. Here’s how I’ve written it:

```

scale=w=480:h=-1

```

I could also be more explicit:

```

scale=width=480:height=-1

```

How about a third option if that wasn’t confusing enough:

```

scale=480:-1

```

Any way you write it, I’ve specified that I want to scale the input video to width 480 pixels and I want the height to be -1 pixels. Nah – that ain’t right.`-1` has a special significance to the scale filter. It means I want the filter to maintain the aspect ratio or proportions of the video while resizing the other dimension I specified.

...

`-2` has a similar meaning to`-1` in the scale filter. It means to stay as close to the aspect ratio but round to an even number. This is important for many video codecs which require even dimensions, such as H.264. It doesn’t matter for GIFs.

...

If you’re changing the frame rate and resizing/scaling your video, resize before increasing the framerate or resize after decreasing the framerate. Your machine won’t have to resize as many frames – saving you time and processing power.

---

Title: Make a GIF From a Video on Windows (Free) | MCSA Guru
URL: https://mcsaguru.com/make-gif-from-video-windows-free
Published: 2026-06-25T08:00:00.000Z
Author: MCSA Guru Team
Highlights:
## The quick (lower quality) way#

A one-liner works, but expect a generic palette and a chunky file:

```
ffmpeg -i input.mp4 -vf "fps=12,scale=480:-1" output.gif
```

- `fps=12` drops the frame rate to keep the size down.
- `scale=480:-1` sets width to 480px and height automatically.

This is fine for a rough GIF. For anything you’ll actually share, use the palette method.

## The right way: build a palette first#

This is a two-step process that gives GIFs their clean colors. First, generate a palette tailored to the clip:

```
ffmpeg -i input.mp4 -vf "fps=12,scale=480:-1,palettegen" palette.png
```

Then apply that palette while creating the GIF:

```
ffmpeg -i input.mp4 -i palette.png -lavfi "fps=12,scale=480:-1,paletteuse" output.gif
```

The difference is obvious — smoother gradients, accurate colors, far less banding. The two `fps` and `scale` values must match between the steps.

Match the filters in both passes

Whatever `fps` and `scale` you use in `palettegen` must be repeated in `paletteuse`, otherwise the palette won’t fit the frames it’s applied to. Keep the two commands side by side and change both together.

## Make a GIF from just part of the video#

Most GIFs are a few seconds. Use `-ss` (start time) and `-t` (duration) to grab a segment. Generate the palette and the GIF from the same window:

```
ffmpeg -ss 5 -t 3 -i input.mp4 -vf "fps=12,scale=480:-1,palettegen" palette.png
ffmpeg -ss 5 -t 3 -i input.mp4 -i palette.png -lavfi "fps=12,scale=480:-1,paletteuse" output.gif
```

This takes a 3-second clip starting at the 5-second mark.

## Control the file size#

GIF gets big fast. The three levers:

#### Keeping GIFs small

| fps=10-15 | Lower frame rate — biggest, easiest saving |
| --- | --- |
| scale=480:-1 | Smaller width — 320-480px is plenty |
| -t 2-4 | Keep it short |
| palettegen + paletteuse | Better quality at the same size |

A 480px-wide, 12 fps, 3-second GIF with a palette usually looks great and stays a reasonable size. Push resolution or length up and the file balloons.

---

Title: skills/ffmpeg-ops/references/images-gif.md
URL: https://github.com/0xdarkmatter/claude-mods/blob/main/skills/ffmpeg-ops/references/images-gif.md
Published: N/A
Author: N/A
Highlights:
## GIF (the palettegen discipline)

GIF is 256 colors with no partial transparency; quality is *entirely* about the
palette and dithering:

```bash
# single-pass via split (fps and scale BEFORE palettegen — palette should be
# computed on the frames that will actually be in the GIF):
ffmpeg -ss 5 -to 8 -i in.mp4 -filter_complex \
  "fps=12,scale=480:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=128[p];[s1][p]paletteuse=dither=bayer:bayer_scale=4" \
  out.gif
```

Size levers, in order of impact: duration → dimensions → fps (8–15 is plenty) →
max_colors → dither (`bayer` smallest, `floyd_steinberg`/`sierra2_4a` prettiest).
`palettegen=stat_mode=diff` helps when only a small region moves.
**Modern check first:** most "GIF" destinations (Slack, GitHub, web) accept MP4 or
animated WebP at a tenth the size — `-c:v libwebp -loop 0 -quality 80 out.webp`.

---

Title: Convert Video to GIF on Mac with FFmpeg: Palettegen Guide
URL: https://rottenwifi.com/how-to-convert-video-to-an-optimized-gif-on-macos-with-ffmpeg/
Published: 2026-10-09T20:15:38.000Z
Author: RottenWiFi Team
Highlights:
## Convert a trimmed video with a two-pass palette workflow

This example takes a three-second excerpt beginning at five seconds, outputs 12 frames per second, and scales the video to 480 pixels wide while preserving its aspect ratio. Replace `input.mp4` with your video’s filename, and adjust the time and size for your clip.

1. Generate a palette from the same excerpt and scaled frames you plan to encode:

```
ffmpeg -ss 5 -t 3 -i input.mp4 
  -vf "fps=12,scale=480:-1:flags=lanczos,palettegen" 
  palette.png
```
2. Apply that palette to the matching excerpt and write a looping GIF:

```
ffmpeg -ss 5 -t 3 -i input.mp4 -i palette.png 
  -lavfi "fps=12,scale=480:-1:flags=lanczos[x];[x][1:v]paletteuse" 
  -loop 0 output.gif
```
3. Open `output.gif` and check both its appearance and file size. If you change the excerpt, frame rate, or scaling, use the same frame selection and scaling in both commands so the palette corresponds to the frames in the GIF.

...

## Choose settings for the destination

GIF size and appearance depend mainly on how long the clip is, how many frames it contains, and how many pixels each frame has. There is no single setting that minimizes size while preserving every detail, so compare the resulting file with the motion and clarity you need.

- Duration: Keep only the essential action. A shorter excerpt contains fewer frames and generally produces less data.
- Frame rate: Lower rates reduce the number of frames and often the file size, but can make motion look choppy. Use the lowest rate that still communicates the action.
- Dimensions: In `scale=480:-1`, FFmpeg sets the width to 480 pixels and calculates the height proportionally. Reduce the width for a smaller display or file, but check that details remain readable.
- Palette:`palettegen` builds a palette from the video frames rather than relying on a generic fixed palette. FFmpeg documents a `max_colors` option; lowering it can reduce color detail.
- Dithering: Dithering changes how color transitions and texture are rendered. FFmpeg supports several methods, including Bayer, Floyd–Steinberg, Sierra, Atkinson, Burkes, and none; its documented default is `sierra2_4a`. Compare results on your clip for visible banding or distracting texture.

---

Title: media-os/skills/ffmpeg-frames-images/references/recipes.md at main · damionrashford/media-os · GitHub
URL: https://github.com/damionrashford/media-os/blob/main/skills/ffmpeg-frames-images/references/recipes.md
Published: N/A
Author: N/A
Highlights:
### 22. Baseline: palette + paletteuse (two passes)

```
ffmpeg -i in.mp4 -vf "fps=15,scale=480:-1:flags=lanczos,palettegen=max_colors=256" -y palette.png
ffmpeg -i in.mp4 -i palette.png \
  -lavfi "fps=15,scale=480:-1:flags=lanczos[x];[x][1:v]paletteuse=dither=bayer:bayer_scale=5" \
  -y out.gif
```

### 23. Tiny GIF (fps 10, width 320, fewer colors)

```
ffmpeg -i in.mp4 -vf "fps=10,scale=320:-1:flags=lanczos,palettegen=max_colors=128" -y p.png
ffmpeg -i in.mp4 -i p.png \
  -lavfi "fps=10,scale=320:-1:flags=lanczos[x];[x][1:v]paletteuse=dither=bayer:bayer_scale=5" \
  -y tiny.gif

...

### 25. Clip + GIF in one go (10s clip starting at 1:00)

```
ffmpeg -ss 60 -t 10 -i in.mp4 -vf "fps=15,scale=480:-1:flags=lanczos,palettegen" -y p.png
ffmpeg -ss 60 -t 10 -i in.mp4 -i p.png \
  -lavfi "fps=15,scale=480:-1:flags=lanczos[x];[x][1:v]paletteuse=dither=bayer:bayer_scale=5" \
  -y clip.gif
```

...

### GIF fps / size trade-off (480px wide, 10s clip)

| fps | approx size | smoothness |
| --- | --- | --- |
| 10 | 1.0x | Choppy |
| 15 | 1.4x | Web default |
| 20 | 1.8x | Smooth |
| 30 | 2.6x | Native |

---

Title: SilvioBaratto/video-rendering
URL: https://github.com/SilvioBaratto/video-rendering
Published: N/A
Author: N/A
Highlights:
### Command Line

```bash
# Convert images to video
video-render images ./frames/ -o output.mp4

# Convert images to GIF
video-render images ./frames/ -o output.gif --fps 15

# Convert video to GIF
video-render convert video.mp4 -o output.gif --fps 10 --width 480

# Check FFmpeg installation
video-render doctor

...

# Video to GIF
converter = GifConverter()
converter.convert("video.mp4", "output.gif", fps=10, width=480)

...

### `video-render convert`

Convert video to GIF with palette optimization.

```bash
video-render convert <VIDEO> -o <OUTPUT> [OPTIONS]
```

| Option | Default | Description |
|--------|---------|-------------|
| `-o, --output` | Required | Output GIF path |
| `--fps` | 10 | Output frames per second |
| `--width` | None | Resize width (maintains aspect ratio) |
| `--start` | None | Start time in seconds |
| `--duration` | None | Duration in seconds |

...

### GifConverter

```python
from video_rendering import GifConverter

converter = GifConverter()

# Basic usage
converter.convert("video.mp4", "output.gif")

# All options
converter.convert(
    input_path="video.mp4",
    output_path="output.gif",
    fps=10,
    width=480,
    start_time=5.0,
    duration=10.0,
    show_progress=True,
)

# Get video info
info = converter.get_video_info("video.mp4")
print(f"Duration: {info['duration']}s")
print(f"Resolution: {info['width']}x{info['height']}")

---

Title: Why a 5-Second GIF Can Be Bigger Than the Original Video (And How to Fix It) - DEV Community
URL: https://dev.to/webdev1/why-a-5-second-gif-can-be-bigger-than-the-original-video-and-how-to-fix-it-241n
Published: 2026-11-05T18:11:17.000Z
Author: Web Developer
Highlights:
Why a 5-Second GIF Can Be Bigger Than the Original Video (And How to Fix It) - DEV Community
Web Developer
Posted on Nov 5
# Why a 5-Second GIF Can Be Bigger Than the Original Video (And How to Fix It)
Have you ever converted a short video into a GIF, only to discover that the GIF is significantly larger than the original video?
It sounds ridiculous. A five-second animation with no audio should be smaller than a full video, right?
Not necessarily.
You can take a short MP4 file, convert just a few seconds into an animated GIF, and end up with a file that's several times larger than the source.
This is particularly noticeable when converting TikTok videos into GIFs for documentation, GitHub README files, blog posts, or reaction animations.
But there's a technical reason behind it, and fortunately, there are several ways to make GIF files smaller without completely destroying their visual quality.
Let's explore why this happens, how GIF compression works, and how to create better GIFs using FFmpeg or an online converter.
## 1. Why Are GIF Files So Large?
The answer lies in how video compression and GIF compression work.
Modern video formats such as MP4 (typically using H.264 or H.265) are designed to compress moving images efficiently.
Instead of independently storing every complete frame, modern video codecs can use information from previous and future frames to represent changes.
For example, imagine a video showing someone talking against a mostly static background.
The background barely changes between frames. A video codec can take advantage of that and avoid repeatedly encoding the same visual information.
GIF works differently.
Originally introduced in 1987, the GIF format wasn't designed for modern high-resolution video.
GIF uses LZW lossless compression for image data and can optimize unchanged regions between frames, but it doesn't have the sophisticated motion compensation used by modern video codecs.
It also supports a maximum of 256 colors per frame.
This creates two problems:
* GIF animations are often much larger than equivalent compressed videos.
* Complex scenes and color gradients can lose visual quality.
**The result?** A short GIF can easily consume more storage than a much longer MP4 video.
## 2. Three Factors That Determine GIF File Size
Before converting a video, it's important to understand what makes a GIF larger.
### Duration
This is usually the most important factor.
Every additional second means more frames need to be stored.
A three-second reaction animation is generally much easier to optimize than a 20-second clip.
For GIFs intended for documentation, social posts, or messaging, I recommend using the shortest possible segment that still communicates the intended action.
Often, three to five seconds is enough.
### Frame Rate (FPS)
FPS stands for frames per second.
Higher frame rates make animation smoother, but they also increase the number of frames stored in the file.
Consider a five-second animation:
|Frame Rate|Total Frames|
|5 FPS|25|
|10 FPS|50|
|15 FPS|75|
|20 FPS|100|
|25 FPS|125|
A GIF at 25 FPS contains 2.5 times as many frames as one at 10 FPS.
That doesn't mean its file size will be exactly 2.5 times larger, because compression efficiency varies, but the difference can be substantial.
For most reaction GIFs and simple demonstrations, 10–15 FPS is a reasonable starting point.
### Resolution
Resolution matters just as much.
A 720-pixel-wide animation contains considerably more pixel data than the same animation at 320 pixels wide.
For many purposes, a GIF doesn't need to preserve the original video's resolution.
Some useful starting points:
* **240px:** Small reactions and compact previews.
* **320px:** Messaging apps, comments, and lightweight animations.
* **480px:** Blog posts, documentation, and larger previews.
* **720px:** When additional detail is genuinely necessary.
For most web-based uses, 480px or less is a sensible starting point.
## 3. How to Create an Optimized GIF with FFmpeg
If you're a developer, FFmpeg offers excellent control over video-to-GIF conversion.
A basic command might look like this:
```
ffmpeg -i input.mp4 output.gif
```
This converts the video, but it doesn't give you much control over the resulting file size.
A better approach is to adjust the frame rate, resolution, and color palette.
### Step 1: Reduce the Frame Rate and Resolution
Try this:
```
ffmpeg -i input.mp4 \
  -vf "fps=12,scale=480:-1:flags=lanczos" \
  output.gif
```
Here's what happens:
* `fps=12` reduces the animation to 12 frames per second.
* `scale=480:-1` sets the width to 480 pixels while preserving the aspect ratio.
* `flags=lanczos` uses Lanczos image scaling for better resizing quality.
These settings can substantially reduce the amount of image data required.
However, there's another optimization worth considering.
### Step 2: Generate a Better Color Palette
GIF is limited to 256 colors per frame.
A generic color palette can produce unpleasant color banding, especially with gradients, shadows, and detailed backgrounds.
FFmpeg provides two useful filters:
* `palettegen` generates an optimized color palette from video frames.
* `paletteuse` applies that palette when creating the GIF.
Here's a more complete command:
```
ffmpeg -ss 00:00:12 -t 4 -i input.mp4 \
  -filter_complex \
  "[0:v]fps=12,scale=480:-1:flags=lanczos,split[a][b];[a]palettegen[p];[b][p]paletteuse=dither=sierra2_4a" \
  -loop 0 output.gif
```
Let's break down the important parts.
**`-ss 00:00:12`**
Starts processing at the 12-second mark.
**`-t 4`**
Extracts four seconds of video.
**`fps=12`**
Limits the animation to 12 frames per second.
**`scale=480:-1`**
Resizes the video while preserving its aspect ratio.
**`palettegen`**
Generates a color palette optimized for the selected clip.
**`paletteuse`**
Applies that palette to the output frames.
**`-loop 0`**
Makes the GIF loop indefinitely.
The optimized palette can improve perceived color quality, although it doesn't guarantee a smaller file in every case.
You should experiment with different frame rates and resolutions to find the right balance.
## 4. Converting TikTok Videos to GIFs Without FFmpeg
FFmpeg is powerful, but sometimes you don't want to download a video, open a terminal, and experiment with conversion settings.
Suppose you find a useful animation or funny moment in a TikTok video.
You only need four seconds of it for a presentation, forum post, or README.
The traditional workflow involves downloading the MP4, opening it in editing software or FFmpeg, trimming the desired segment, and exporting the GIF.
A browser-based converter can simplify this process.
One option is FromTik's TikTok to GIF Converter.
It lets you create an animated GIF directly from a public TikTok video URL.
The process is straightforward:
1. Copy the link to a public TikTok video.
2. Open the TikTok to GIF converter.
3. Paste the URL.
4. Select the exact beginning and end of the animation.
5. Choose the resolution and frame rate.
6. Preview the selected segment and generate the GIF.
The converter supports clips up to 30 seconds long, lets you adjust timing in 0.1-second increments, and offers frame rates between 5 and 25 FPS.
It also creates the animation without the moving TikTok watermark, provided the video can be accessed.
The useful part is that you can control the same three important factors we discussed earlier: duration, resolution, and frame rate.
You don't need to download and upload the original MP4 separately.
For quick conversions, this can be more convenient than setting up a manual FFmpeg workflow.
Of course, FFmpeg remains the better option when you need batch processing, custom filters, scripting, or more advanced encoding control.
## 5. GIF vs. MP4: Which Should Developers Use?
Here's something worth mentioning: **sometimes the best way to optimize a GIF is not to use GIF at all.**
Modern browsers support much more efficient video formats.
If you're building a website and need a looping animation, an MP4 or WebM video may be a better option.
For example:
```
<video autoplay loop muted playsinline>
  <source src="demo.webm" type="video/webm">
  <source src="demo.mp4" type="video/mp4">
</video>
```
This creates an automatically looping animation without requiring the GIF format.
The benefits can include:
* Smaller file sizes.
* Better color reproduction.
* Higher frame rates.
* Lower bandwidth consumption.
For a web application, documentation website, or product landing page, this is often the more efficient approach.
However, GIF still has advantages.
It is widely recognized, easy to embed in many platforms, and useful when video embedding isn't supported or is inconvenient.
### When GIF Makes Sense
Use GIF when:
* Creating short reaction animations.
* Sharing animations in environments that expect GIF files.
* Embedding lightweight visual demonstrations in supported Markdown platforms.
* Creating short, silent looping previews.
### When MP4 or WebM Makes Sense
Use video when:
* The animation is longer than a few seconds.
* Image quality matters.
* You need smooth motion at a high frame rate.
* Website performance and bandwidth are priorities.
The important thing is choosing the format based on where the animation will be used.
## 6. Practical Tips for Smaller GIFs
After experimenting with video-to-GIF conversion, I've found that a few basic principles make a significant difference.
**Trim before converting.**
Don't convert an entire 30-second video if you only need four seconds of animation.
**Start with 10–15 FPS.**
Increase the frame rate only if the animation looks noticeably worse without it.
**Avoid unnecessarily large resolutions.**
A 320px GIF might communicate exactly the same information as a 720px GIF.
**Use an optimized color palette.**
Especially for videos with complicated colors or gradients.
**Avoid excessive motion when possible.**
Scenes with rapid camera movement and constantly changing backgrounds can be harder to compress efficiently.
**Consider an alternative format.**
If you're embedding an animation on your own website, try MP4, WebM, or an appropriate animated image format before settling on GIF.
And most importantly, don't assume that a shorter animation automatically means a smaller file.
Always check the resulting file size.
## 7. A Note About Content Ownership
When converting TikTok videos or other online content, remember that being able to download or convert a video doesn't automatically give you permission to republish it.
For documentation, tutorials, and public projects, it's best to use your own recordings, appropriately licensed clips, or content you have permission to reuse.
Removing a watermark also doesn't remove the original creator's rights.
## Final Thoughts
GIF is a remarkably persistent format.
Despite being introduced decades ago, it's still widely used for reactions, tutorials, documentation, and short visual demonstrations.
But its compression technology wasn't designed for today's high-resolution videos.
That's why a five-second GIF can sometimes be larger than the entire MP4 it came from.
Fortunately, there are straightforward ways to improve the result.
If you want full control, **FFmpeg with palette generation, reduced resolution, and a sensible frame rate** is a great approach.
If you just want to turn a particular moment from a TikTok video into an animation, a browser-based converter can make the process considerably simpler.
Ultimately, the best GIF isn't necessarily the one with the highest resolution or the smoothest animation.
**It's the one that communicates the intended moment clearly, without wasting unnecessary bandwidth.**
*Have you ever encountered unexpectedly large GIF files? Do you prefer using FFmpeg, browser-based converters, or video formats for animations in your projects? I'd be interested to hear which approach works best for you.*

---

Title: Как мне конвертировать видео в GIF с использованием ffmpeg с приемлемым качеством?
URL: https://qastack.ru/superuser/556029/how-do-i-convert-a-video-to-gif-using-ffmpeg-with-reasonable-quality
Published: N/A
Author: N/A
Highlights:
```
ffmpeg -ss 30 -t 3 -i input.mp4 -vf "fps=10,scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 output.gif

```
...
вывода ( `-t 3`).
- Фильтр fps
...
, сохранив соотношение сторон.
- Фильтры palettegen и
=== END OF OUTPUT V65 ===


########## QUESTION q20 ##########
Question: How do I delete duplicate rows in PostgreSQL while keeping one row per group?
Reference answer: DELETE rows whose row_number() OVER (PARTITION BY dup columns ORDER BY id) > 1 (or compare ctid); keeps the lowest id.
Reference source: https://wiki.postgresql.org/wiki/Deleting_duplicates

=== OUTPUT X20 ===
**The cleanest way to delete duplicate rows in PostgreSQL while keeping one per group is by using a Common Table Expression (CTE) with the `ROW_NUMBER()` window function****.** This approach partitions your data into duplicate groups, assigns a sequential number to each row, and deletes everything except the first row. [1]

If your table has a unique identifier (like a primary key `id`), partition by the duplicate columns and order by that ID to decide which row survives: [2]

sql

```
WITH ranked_rows AS (
    SELECT 
        id,
        ROW_NUMBER() OVER (
            PARTITION BY email, first_name  -- Columns that define a duplicate
            ORDER BY id ASC                 -- ASC keeps the oldest row; DESC keeps the newest
        ) AS row_num
    FROM users
)
DELETE FROM users
WHERE id IN (
    SELECT id 
    FROM ranked_rows 
    WHERE row_num > 1
);
```

Используйте код с осторожностью.

-   **Grouping (`PARTITION BY`):** List all columns that must match for rows to be considered duplicates.
    
-   **Tie-Breaking (`ORDER BY`):** Use `ASC` to keep the earliest record, or `DESC` (e.g., `ORDER BY created_at DESC`) to keep the most recent one. [3]
    

* * *

### 2\. Fallback Method: Tables Without a Unique ID (`ctid`)

If your table has completely identical rows with no primary key or unique column, use PostgreSQL's built-in physical row locator `ctid`: [4]

sql

```
WITH ranked_rows AS (
    SELECT 
        ctid,
        ROW_NUMBER() OVER (
            PARTITION BY email, first_name
            ORDER BY ctid
        ) AS row_num
    FROM users
)
DELETE FROM users
USING ranked_rows
WHERE users.ctid = ranked_rows.ctid
  AND ranked_rows.row_num > 1;
```

Используйте код с осторожностью.

-   **`ctid`:** Acts as a temporary unique physical address for each row during the query execution.
    
-   **`USING` clause:** Joins the CTE back to the target table so PostgreSQL knows which physical rows to remove. [4]
    

* * *

### Best Practices Before Deleting

-   **Preview first:** Run just the `SELECT` statement inside the CTE with `WHERE row_num > 1` to verify the exact rows slated for deletion.
    
-   **Wrap in a transaction:** Run your `DELETE` inside a `BEGIN; ... COMMIT;` block so you can run `ROLLBACK;` if the affected row count looks wrong.
    
-   **Prevent future duplicates:** Once cleaned up, add a `UNIQUE` constraint or unique index on the grouped columns so duplicates cannot be inserted again. [5]
    

If you'd like to tailor this query to your schema, let me know:

-   Your **table and column names**
-   Whether you want to keep the **oldest or newest** record (and which column tracks that)
-   Approximately **how many rows** are in the table

I can write the exact query for you or suggest a faster batching approach if your table has millions of rows.

Sources:
1. https://www.runxbuild.com/blog/sql-delete-duplicate-rows-but-keep-one/
2. https://builder.ai2sql.io/blog/how-to-delete-duplicate-rows-sql
3. https://www.instagram.com/reel/DR62GDugdzv/
4. https://dba.stackexchange.com/questions/138320/duplicate-rows-how-to-remove-one
5. https://www.youtube.com/watch?v=YmWqLenZoiM
=== END OF OUTPUT X20 ===

=== OUTPUT R23 ===
Title: Deleting duplicates - PostgreSQL wiki
URL: https://wiki.postgresql.org/wiki/Deleting_duplicates
Published: N/A
Author: N/A
Highlights:
A frequent question in IRC is how to delete rows that are duplicates over a set of columns, keeping only the one with the lowest ID. 

This query does that for all rows of tablename having the same column1, column2, and column3. 

```
DELETE FROM tablename
WHERE id IN (
    SELECT
        id
    FROM (
        SELECT
            id,
            row_number() OVER w as rnum
        FROM tablename
        WINDOW w AS (
            PARTITION BY column1, column2, column3
            ORDER BY id
        )

    ) t
WHERE t.rnum > 1);

```

Sometimes a timestamptz field is used instead of an ID field.

---

Title: How to Delete Duplicate Rows in PostgreSQL
URL: https://neon.com/postgresql/tutorial/how-to-delete-duplicate-rows-in-postgresql
Published: N/A
Author: N/A
Highlights:
## Deleting duplicate rows using DELETE USING statement

The following statement uses the `DELETE USING` statement to remove duplicate rows:

```
DELETE FROM
    basket a
        USING basket b
WHERE
    a.id < b.id
    AND a.fruit = b.fruit;
```

Copy

In this example, we joined the `basket` table to itself and checked if two different rows (a.id < b.id) have the same value in the `fruit` column.

The following query retrieves data from the `basket` table to verify the duplication removal:

```
SELECT
	id,
	fruit
FROM
	basket;
```

Copy

```
id | fruit
----+--------
  2 | apple
  5 | orange
  6 | banana
(3 rows)
```

Copy

The output indicates that the statement removes the duplicate rows with the lowest IDs and keeps the one with the highest id.

If you want to keep the duplicate rows with the lowest id, you need to flip the operator in the `WHERE` clause:

```
DELETE  FROM
    basket a
        USING basket b
WHERE
    a.id > b.id
    AND a.fruit = b.fruit;
```

Copy

To check whether the statement works correctly, let’s verify the data in the `basket` table:

```
SELECT
    id,
    fruit
FROM
    basket;
```

Copy

```
id | fruit
----+--------
  1 | apple
  3 | orange
  6 | banana
(3 rows)
```

Copy

The output indicates that duplicate rows with the lowest ids are retained.

## Deleting duplicate rows using subquery

The following statement uses a subquery to delete duplicate rows and keep the row with the lowest id.

```
DELETE FROM basket
WHERE id IN
    (SELECT id
    FROM
        (SELECT id,
         ROW_NUMBER() OVER( PARTITION BY fruit
        ORDER BY  id ) AS row_num
        FROM basket ) t
        WHERE t.row_num > 1 );
```

Copy

In this example, the subquery returned the duplicate rows except for the first row in the duplicate group. The outer `DELETE` statement deleted the duplicate rows returned by the subquery.

If you want to keep the duplicate row with the highest ID, just change the order in the subquery:

```
DELETE FROM basket
WHERE id IN
    (SELECT id
    FROM
        (SELECT id,
         ROW_NUMBER() OVER( PARTITION BY fruit
        ORDER BY  id DESC ) AS row_num
        FROM basket ) t
        WHERE t.row_num > 1 );
```

Copy

In case you want to delete duplicates based on values of multiple columns, here is the query template:

```
DELETE FROM table_name
WHERE id IN
    (SELECT id
    FROM
        (SELECT id,
         ROW_NUMBER() OVER( PARTITION BY column_1,
         column_2
        ORDER BY  id ) AS row_num
        FROM table_name ) t
        WHERE t.row_num > 1 );
```

Copy

In this case, the statement will delete all rows with duplicate values in the `column_1` and `column_2` columns.

## Deleting duplicate rows using an immediate table

To delete rows using an immediate table, you use the following steps:

1. Create a new table with the same structure as the one whose duplicate rows should be removed.
2. Insert distinct rows from the source table to the immediate table.
3. Drop the source table.
4. Rename the immediate table to the name of the source table.

The following illustrates the steps for removing duplicate rows from the `basket` table:

...

-- step 2

...

id
FROM basket;

-- step 3

...

-- step 4
ALTER TABLE basket_temp

---

Title: Remove only duplicates from specific Postgresql table
URL: https://stackoverflow.com/questions/54257538/remove-only-duplicates-from-specific-postgresql-table
Published: 2019-01-18T16:04:47.000Z
Author: Essex
Highlights:
I guess you have a `id` field.

```
delete from customer 
where id not in (
    select min(id)
    from customer
    group by email, first_name, last_name
)
```

The subquery finds the id of the rows you want to keep. Then you delete the other rows

---

Title: How to deduplicate rows in PostgreSQL
URL: https://clearcove.ca/2013/09/how-to-deduplicate-rows-in-postgresql/
Published: 2013-09-05T00:00:00.000Z
Author: N/A
Highlights:
Use the following query to keep only one row and delete all duplicates of that row.

Note: this is non-standard SQL and works only with PostgreSQL.

The following snippet finds all rows in the users table that have identical email and organization_id. It keeps the oldest of the rows (via users.id > u2.id) and deletes the newer duplicates.

```
DELETE FROM users USING users u2
 WHERE users.email = u2.email
 AND users.organization_id = u2.organization_id
 AND users.id > u2.id;
```

---

Title: How to remove duplicate entries in postgresql table?
URL: https://stackoverflow.com/questions/28763256/how-to-remove-duplicate-entries-in-postgresql-table
Published: 2015-02-27T10:49:14.000Z
Author: membersound
Highlights:
If you have rows that are complete duplicates (i.e., no way to distinguish one from the other), then you have two options. One is to use a built-in row identifier such as `ctid`:

```
DELETE FROM mytable USING mytable t
  WHERE mytable.id = t.id AND
        (mytable.modification < t.modification OR
         mytable.modification = t.modification AND mytable.ctid < t.ctid);
```

Or use a secondary table:

```
create table tokeep as
    select distinct on (t.id) t.*
    from mytable
    order by t.id, t.modification;

truncate table mytable;

insert into mytable
    select * from tokeep;
```

...

Use EXISTS to see if there are other rows with same id:

```
DELETE FROM mytable t
WHERE EXISTS (SELECT 1 from mytable
              WHERE id = t.id AND modification > t.modification);

---

Title: Delete Duplicate Rows in SQL — Keep One (PostgreSQL, MySQL, SQL Server) | Forgly
URL: https://forgly.dev/sql/delete-duplicate-rows
Published: N/A
Author: N/A
Highlights:
PostgreSQL, SQL Server, SQLite 3.25+ (window function) Copy

```
WITH ranked AS (
  SELECT id,
         ROW_NUMBER() OVER (
           PARTITION BY email ORDER BY id
         ) AS rn
  FROM users
)
DELETE FROM users
WHERE id IN (SELECT id FROM ranked WHERE rn > 1);
```

```
DELETE u FROM users u
JOIN users keep
  ON keep.email = u.email
 AND keep.id < u.id;
```

Joins each row to any earlier row with the same email and deletes the later ones, keeping the smallest id.

```
DELETE FROM users a
USING users b
WHERE a.id > b.id
  AND a.email = b.email;
```

## How to delete duplicate rows but keep one

Deleting duplicates means keeping one row per group (usually the lowest id) and removing the rest. To delete duplicate rows but keep one, the cleanest cross-dialect approach uses ROW_NUMBER(); MySQL can do it with a self-join.

## How it works

- ROW_NUMBER() numbers rows 1, 2, 3… within each PARTITION BY group, ordered so the row you keep gets number 1.
- Every row with rn > 1 is a duplicate to remove.
- ORDER BY id inside the window decides which copy survives — order by created_at to keep the newest, for example.

## Tip

Always run the SELECT version first to preview which rows would be deleted, then wrap the delete in a transaction.

...

Deleting duplicates means keeping one row per group (usually the lowest id) and removing the rest. To delete duplicate rows but keep one, the cleanest cross-dialect approach uses ROW_NUMBER(); MySQL can do it with a self-join. ROW_NUMBER() numbers rows 1, 2, 3… within each PARTITION BY group, ordered so the row you keep gets number 1. Every row with rn > 1 is a duplicate to remove. ORDER BY id inside the window decides which copy survives — order by created_at to keep the newest, for example.

---

Title: Detect and Remove Duplicate Rows in PostgreSQL Tables • ZeroExp
URL: https://zeroexp.dev/library/postgres-remove-duplicates
Published: N/A
Author: N/A
Highlights:
HAVING count(*) > 1 and removed by numbering rows within each group and deleting those after the first. In PostgreSQL 18.6, 20,000 contacts with 5,000 distinct emails lost 15,000 rows in one DELETE, and a unique index then refused a new copy.

...

------------

...

The table held 20,000 rows and 5,000 distinct emails. Grouping by the columns that define a duplicate, with `HAVING count(*) > 1`, listed the addresses that occur more than once; each of the first three appeared four times. The second query counted the rows that would be removed if one copy of each is kept: 15,000. That number is the figure to check before you delete anything. If it is larger than you expect, the definition of "duplicate" is wrong, for example because two people share an address or because the column is padded with spaces and case.

Decide the definition on purpose. Is `[email protected]` a duplicate of `[email protected]`? Group by `lower(trim(email))` if so, and see case insensitive lookups for the permanent fix. Which copy should survive? The oldest by `id` or `created_at` is the usual choice, because other tables may reference it; the newest may hold the most recent data. Check for references first, since a `DELETE` of a row referenced by a foreign key fails or cascades.

## Deleting the extras

Number the rows within each group of duplicates, ordered by the one to keep first, and delete everything numbered above 1:

Text Copy

```
begin;
BEGIN
delete from contacts c using (select id, row_number() over (partition by email order by id) rn from contacts) d where c.id = d.id and d.rn > 1;
DELETE 15000
select count(*) as rows_left from contacts;
 rows_left 
-----------
      5000
(1 row)

commit;
COMMIT
```

`row_number() OVER (PARTITION BY email ORDER BY id)` gives each copy a number starting at 1 for the lowest `id`. The `DELETE ... USING (subquery) d WHERE c.id = d.id AND d.rn > 1` removed 15,000 rows, and `rows_left` showed 5,000 before the `COMMIT`. Doing it inside `BEGIN` is the safety: if the count is wrong, `ROLLBACK` costs nothing. For a large table, the delete takes locks and writes WAL for 15,000 rows, which is quick here and an hour on a table of 100 million; then delete in batches by id range, and expect the table to need `VACUUM` afterwards, as table bloat explains.

Two alternatives exist. `DELETE FROM contacts WHERE id NOT IN (SELECT min(id) FROM contacts GROUP BY email)` is shorter and works, but `NOT IN` against a subquery that can contain a null returns no rows at all, and it is often slow. `DISTINCT ON` is the tool when you want to keep the newest: `CREATE TABLE contacts_clean AS SELECT DISTINCT ON (email) * FROM contacts ORDER BY email, created_at DESC`, then swap the tables, which avoids the delete entirely and is covered in DISTINCT ON.

...

Some tables have no primary key, and rows can be exact copies of each other, so no column tells them apart. PostgreSQL's physical row address, `ctid`, does:

...

```
create table nokey (a int, b text);
CREATE TABLE
insert into nokey select g % 3, 'x' from generate_series(1,9) g;
INSERT 0 9
delete from nokey where ctid in (select ctid from (select ctid, row_number() over (partition by a, b order by ctid) rn from nokey) s where rn > 1);
DELETE 6
select * from nokey order by a;
 a | b 
---+---
 0 | x
 1 | x
 2 | x
(3 rows)

...

The table `nokey` had nine rows over three groups of `(a, b)`. Numbering by `(a, b)` ordered by `ctid` and deleting `ctid` values numbered above 1 removed 6 and left one of each. The `ctid` is stable only within the statement and changes when a row is updated or the table is vacuumed, so run it in one statement and never store it. This is a repair tool for a table that should have had a key, and the next step is to add one: `ALTER TABLE nokey ADD COLUMN id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY`.

...

After the delete, verify three things. The count of distinct keys should be the same as before, 5,000 here; if it dropped, the definition of the key was wrong and the transaction should not have been committed. The foreign keys that point at the table should still be satisfied, which the database enforces for you unless the delete cascaded: look at the `ON DELETE` rule of every referencing constraint before running the statement, because `ON DELETE CASCADE` turns a duplicate cleanup into the loss of child rows that belonged to the extra copy. The ON DELETE CASCADE article lists the cases.

...

Deleting 75% of the rows leaves the file the same size, and the freed space is reused by later inserts but not returned to the operating system; `VACUUM` marks it reusable and only `VACUUM FULL` or a rewrite shrinks the file. If the table is going to stay small, a rewrite is worth it, and the SQL formatter helps when you keep the cleanup statements in a migration file where they must stay readable. Keep a record of what was removed: `CREATE TABLE contacts_removed AS SELECT * FROM contacts WHERE ...` before the delete, or `DELETE ...

...

If duplicates differ in a column that matters, deleting loses data: two contacts with the same email and different names and phone numbers need merging, not removal. If other tables point at the extra rows, repoint them to the survivor first with an `UPDATE`, then delete. If the duplicates come from a bug, fix the bug or the table refills. And if the same business record legitimately exists twice (the same customer in two shops), the key is wrong, not the data: make the unique constraint over the columns that define identity. The windowing functions are described in window functions, and the `DELETE ... USING` syntax in the DELETE reference.

---

Title: How to use the physical location of rows (ROWID) in a DELETE statement
URL: https://stackoverflow.com/questions/15026420/how-to-use-the-physical-location-of-rows-rowid-in-a-delete-statement
Published: 2013-02-22T14:28:47.000Z
Author: endrigoantonini
Highlights:
On PostgreSQL the physical location of the row is called CTID.

So if you want to view it use a QUERY like this:

```
SELECT CTID FROM table_name
```

To use it on a DELETE statement to remove the duplicated records use it like this:

```
DELETE FROM table_name WHERE CTID NOT IN (
  SELECT RECID FROM 
    (SELECT MIN(CTID) AS RECID, other_columns 
      FROM table_name GROUP BY other_columns) 
  a);
```

Remember that table\_name is the desired table and other\_columns are the columns that you want to use to filter that.

Ie:

```
DELETE FROM user_department WHERE CTID NOT IN (
  SELECT RECID FROM 
    (SELECT MIN(CTID) AS RECID, ud.user_id, ud.department_id
      FROM user_department ud GROUP BY ud.user_id, ud.department_id) 
  a);
```

...

Simply:

```
DELETE FROM tbl
WHERE  ctid NOT IN (
   SELECT min(ctid)
   FROM   tbl
   GROUP  BY $other_columns
   );
```

... where duplicates are defined by equality in `$other_columns`. 
There is no need to include columns from the `GROUP BY` clause in the `SELECT` list, so you don't need another subquery.

[The manual about `ctid`.](https://www.postgresql.org/docs/current/ddl-system-columns.html)

...

You should consider using `row_number()` if want to delete based on a unique id column(or a timestamp), since `ctid` alone is not always reliable when you want to only keep recent records etc.

```
WITH d 
     AS (SELECT ctid c, 
                row_number() 
                  OVER ( 
                    partition BY s 
                    ORDER BY id) rn 
         FROM   t) 
DELETE FROM t 
WHERE  ctid IN (SELECT c 
               FROM   d 
               WHERE  rn > 1)  ; 
```

---

Title: Delete duplicate rows from small table
URL: https://stackoverflow.com/questions/6583916/delete-duplicate-rows-from-small-table
Published: N/A
Author: N/A
Highlights:
### Answer by user330315 (score: 127 [ACCEPTED])

DELETE FROM dupes a
WHERE a.ctid <> (SELECT min(b.ctid)
 FROM dupes b
 WHERE a.key = b.key);

...

A faster solution is to:

find the first occurence of the duplicate,
then remove all rows that are not the first duplicate occurence.

This looks like the following:
DELETE FROM dups a USING (
 SELECT MIN(ctid) as ctid, key
 FROM dups 
 GROUP BY key HAVING COUNT(*) > 1
) b
WHERE a.key = b.key 
AND a.ctid <> b.ctid

Notice that whith this solution you don't have control over which row is kept.
Toy example
CREATE TABLE people (
 name varchar(50) NOT NULL,
 surname varchar(50) NOT NULL,
 age integer NOT NULL
);

INSERT INTO people (name, surname, age) VALUES 
 ('A.', 'Tom', 30),
 ('A.', 'Tom', 10),
 ('B.', 'Tom', 20),
 ('B', 'Chris', 20);

-- The inner command to find duplicates first occurences:
SELECT MIN(ctid) as ctid, name, surname
FROM people 
GROUP BY (name, surname) HAVING COUNT(*) > 1;

DELETE FROM people a USING (
 SELECT MIN(ctid) as ctid, name, surname
 FROM people 
 GROUP BY (name, surname) HAVING COUNT(*) > 1
) b
WHERE a.name = b.name
AND a.surname = b.surname
AND a.ctid <> b.ctid;

SELECT * FROM people;

The inner request outputs:

ctid
name
surname

(0,1)
A.
Tom

And the final request (after deletion) outputs:

...

surname
age

A.

...

Tom
20

...

EXISTS is simple and among the fastest for most data distributions:
DELETE FROM dupes d
WHERE EXISTS (
 SELECT FROM dupes
 WHERE key = d.key
 AND ctid < d.ctid
 );

From each set of duplicate rows (defined by identical key), this keeps the one row with the minimum ctid.
Careful with table inheritance or partitioning. Then there can be multiple physical tables involved and ctid is not unique within the scope. See:

How to delete duplicate rows without unique identifier

Result is identical to the currently accepted answer by a_horse. Just faster, because EXISTS can stop evaluating as soon as the first offending row is found, while the alternative with min() has to consider all rows per group to compute the minimum. Speed is of no concern to this question, but why not take it?
You may want to add a UNIQUE constraint after cleaning up, to prevent duplicates from creeping back in:
ALTER TABLE dupes ADD CONSTRAINT constraint_name_here UNIQUE (key);

...

If there is any other column defined UNIQUE NOT NULL column in the table (like a PRIMARY KEY) then, by all means, use it instead of ctid.
If key can be NULL and you only want one of those, too, use IS NOT DISTINCT FROM instead of =. See:

---

Title: Ezra's Research: Removing Duplicates From a Database
URL: http://ezrakilty.net/research/2005/12/removing_duplicates_from_a_dat.html
Published: 2005-12-06T00:00:00.000Z
Author: N/A
Highlights:
You've inserted multiple copies of the same data into a table. You want to get rid of all but one copy of each, and you want to keep the one with the lowest ID. You are using a DMBS with sub-selects, such as PostgreSQL.

You will do this:

```
select min(wine_id) as canonical from
        wine, (select distinct wine_name from wine) as names
        where wine.wine_name = names.wine_name
        group by names.wine_name;

```

If that looks right, you will proceed:

```
delete from wine where wine_id not in
    (select min(wine_id) as canonical from
        wine, (select distinct wine_name from wine) as names
        where wine.wine_name = names.wine_name
        group by names.wine_name);

```

More generally, if you have a table T with pkey T_ID and the desired data is unique on some column UNIQUE_COLUMN, it's:

```
select min(T_ID) as canonical from
        T, (select distinct UNIQUE_COLUMN from T) as equiv_classes
        where T.UNIQUE_COLUMN = equiv_classes.UNIQUE_COLUMN
        group by equiv_classes.UNIQUE_COLUMN;

```
=== END OF OUTPUT R23 ===

=== OUTPUT L91 ===
The search turned up three common approaches, all covered in PostgreSQL tutorials.

**1. Window function (ROW_NUMBER) subquery.** This is the most common pattern. Partition by the columns that define a duplicate, number the rows within each group, and delete everything numbered above 1. One tutorial shows the form: DELETE FROM basket WHERE id IN (SELECT id FROM (SELECT id, ROW_NUMBER() OVER( PARTITION BY fruit ORDER BY id ) AS row_num FROM basket ) t WHERE t.row_num > 1 );. Ordering by id ascending keeps the oldest row, and switching to descending keeps the newest. For multiple key columns, the partition list simply grows, as the statement will delete all rows with duplicate values in the column_1 and column_2 columns.

**2. DELETE ... USING self-join.** This compares rows against each other directly. Per one tutorial, the statement removes the duplicate rows with the lowest IDs and keeps the one with the highest id, and reversing the comparison operator keeps the lowest id instead.

**3. Table without a primary key.** A Postgres mailing-list reply suggests using the system column ctid in the CTE, partitioned by all the columns, and deleting rows where the row number exceeds 1. This is useful when there is no id to order by.

**Practical notes:** Run a `GROUP BY ... HAVING COUNT(*) > 1` query first to see what will be affected, and wrap the delete in a transaction so you can roll back. One guide also recommends a unique index afterward to prevent recurrence. Sources: the PostgreSQL Tutorial (postgresqltutorial.com), Neon's tutorial, GeeksforGeeks, and a pgsql-general mailing list thread.

Sources:
1. https://alibaba-cloud.medium.com/postgresql-data-deduplication-methods-1bf54eb267d5
2. https://proxy-dev.blitzz.co/proxy/123456/www.geeksforgeeks.org/postgresql/postgresql-deleting-duplicate-rows-using-subquery
3. https://neon.com/postgresql/postgresql-tutorial/how-to-delete-duplicate-rows-in-postgresql
4. https://www.postgresqltutorial.com/?p=3160
5. https://postgresql.org/message-id/CAPnRvGs1%2BuqWe1ny0jMJapYMNR%2Bi%3DjDvWRL4YwsgsUdAQFSNGg%40mail.gmail.com
6. https://neon.com/postgresql/tutorial/how-to-delete-duplicate-rows-in-postgresql
7. https://builder.ai2sql.io/blog/how-to-delete-duplicate-rows-sql
=== END OF OUTPUT L91 ===
