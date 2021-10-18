# Git
## Config
```
// Convert Git repo end of line
git config --global core.attributesfile ~/.gitattributes
echo "* text=auto" > ~/.gitattributes

git config --global core.autocrlf false
git config --global core.eol lf

config --global --edit
git config --global user.name "Terry"
git config --global user.email terrywuemail@gmail.com

git clean -df
```
## CMDs
```
git log --abbrev-commit
git log --graph --online --decorate
git cherry-pick 7017284
# Go back to prevous branch
git checkout -

git rm --cached -r .
git commit -am "Single line did add & commit"
git commit --amend -m "rename commit msg"

git reset --hard
git reset HEAD
git reset --hard HEAD~1

// Squash last 3 commits
git reset --soft HEAD~3
git commit

git merge --squash

# If you are brave
git push origin develop --force
git remote set-url origin https://github.com/USERNAME/REPOSITORY.git
git remote -v


git push --set-upstream origin branch_b
git branch rm branch_a
git diff README.md

git reset --soft HEAD~1

git rebase // will stash my branch prev commits, then apply after rebase branch
```

# Tech Terms 

Git is a database, smallest unit is File store as blob unit.


Git object types:
1. blob
2. commit
3. tree

.git/hooks