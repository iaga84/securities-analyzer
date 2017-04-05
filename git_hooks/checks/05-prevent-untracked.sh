#!/bin/sh
untracked=`git ls-files --others --exclude-standard`
if [ "$untracked" != "" ]; then
    gitflow_fail "- ERROR - found untracked files"
    exit 1
else
	gitflow_ok " - ok, no untracked files"
fi
