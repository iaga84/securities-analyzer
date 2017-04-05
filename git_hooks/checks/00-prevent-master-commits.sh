#!/bin/sh
branch=`git symbolic-ref HEAD`
if [ "$branch" = "refs/heads/master" ]; then
    gitflow_fail "- ERROR - direct commits to the branch master are not allowed"
    exit 1
else
	gitflow_ok " - ok, current branch is not master"
fi