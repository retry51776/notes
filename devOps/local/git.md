# Git
> Git is a database, smallest unit is File store as blob unit.

> build number generator is global (share across branches)
### Git object types:
1. blob
2. commit
3. tree

.git/hooks

## CMDs
```bash
git log --abbrev-commit
git log --graph --online --decorate
git cherry-pick 7017284
# Go back to previous branch
git checkout -

# Tag
git tag -l
git tag v1.0 -m "First Tag"
git push origin v1.0 

# Releases are a feature of GitHub
# semantic versioning pre-release 0.9.1-alpha or beta
git release create v1.0

# Git Flow
git flow init
git flow feature start xxxx
git flow feature finish xxxx // feature completed
git flow release start 0.2.0
git flow release finish 0.2.0
git flow hotfix start xxx_bug
git flow hotfix finish xxx_bug


git rm --cached -r .
git commit -am "Single line did add & commit"
git commit --amend -m "rename commit msg"

git reset --hard
git reset HEAD
git reset --hard HEAD~1

# Force sync with remote
git fetch origin
git reset --hard origin/your-branch 
git pull

# Squash last 3 commits
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

find . -name "*.pyc" -exec git rm -f "{}" \;
```

#### Config
```bash
# Convert Git repo end of line
git config --global core.attributesfile ~/.gitattributes
echo "* text=auto" > ~/.gitattributes

git config --global core.autocrlf false
git config --global core.eol lf

config --global --edit
git config --global user.name "Terry"
git config --global user.email terrywuemail@gmail.com

git clean -df
```

# CI / CD Pipeline
## Github Vars
```bash
GITHUB_REF
GITHUB_SHA // full sha
```

## Jenkin Vars
```bash
@echo off
echo GIT_COMMIT %GIT_COMMIT% 
echo GIT_BRANCH %GIT_BRANCH%
echo GIT_LOCAL_BRANCH %GIT_LOCAL_BRANCH%
echo GIT_PREVIOUS_COMMIT %GIT_PREVIOUS_COMMIT%
echo GIT_PREVIOUS_SUCCESSFUL_COMMIT %GIT_PREVIOUS_SUCCESSFUL_COMMIT%
echo GIT_URL %GIT_URL%
echo GIT_URL_N - %GIT_URL_N%
echo GIT_AUTHOR_NAME %GIT_AUTHOR_NAME%
echo GIT_COMMITTER_EMAIL %GIT_COMMITTER_EMAIL%

ARG git_commit
RUN echo $git_commit > /app/.githash
```

Language Server Index Format (LSIF) - `enable github or gitlab code intelligence`

## Gitlab CI
> Executor is defined at runner level `/etc/gitlab-runner/config.toml`

> deploy by gitlab-takeoff
```yml
#.gitlab-ci.yml

# Defined Job Orders, same stage will executed parallel
stages:
  - stage1
  - stage2
  - stage3

# Example Job 1
run_something:
	image: python:3.10
	before_script:
		- apt-get update && apt-install
  script:
    - python3 start.py
  # Optional Settings
  allow_failure: true
  # Optional Rules
  rules:
    # Rule [if, changes, exists]
    - if: '$CI_COMMIT_BRANCH != "master"'
      # when (should rename to then)
      when: never
    - when: on_success
  artifacts:



```
#### Gitlab System hooks
- push_events
- tag_push_events
- merge_request_events
- repository_update_events
- enable_ssl_verification


## Github Vs Bitbucket Vs Gitlab
- Github
	- `charge per repo`
	- `ruby on rail`
	- `github action`
	- `better text search`
- Bitbucket
  - `charge per user`
  - `written in python & django`
  - `better security record`
  - `plugin for Jira Integration`
- Gitlab
  - `self host`