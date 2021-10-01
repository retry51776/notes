# Git CMDs
```
// Convert Git repo end of line
git config --global core.attributesfile ~/.gitattributes
echo "* text=auto" > ~/.gitattributes

git log --abbrev-commit
git cherry-pick 7017284

git rm --cached -r .
git add .

git config --global core.autocrlf false
git config --global core.eol lf


git reset --hard
git reset HEAD
git reset --hard HEAD~1

// Squash last 3 commits
git reset --soft HEAD~3
git commit

git merge --squash

git push origin develop --force
git remote set-url origin https://github.com/USERNAME/REPOSITORY.git
git remote -v

git branch rm swan-metrics
git diff README.md

config --global --edit
git config --global user.name "Terry"
git config --global user.email terrywuemail@gmail.com
git reset --soft HEAD~1

git push --set-upstream origin f/FTR-11-bussiness-metrics

git rebase // will stash my branch prev commits, then apply after rebase branch
```

# Tech Terms 

Git is a database, smallest unit is File store as blob unit.


Git object types:
1. blob
2. commit
3. tree
