#!/usr/bin/env bash
ERROR=0
for file in $(gitflow_commit_files); do
    if grep -Erls "^<<<<<<< |^>>>>>>>" $file >/dev/null ; then
    	gitflow_fail "- ERROR - markers found in $file"
    	exit 1
    fi
done

gitflow_ok " - ok, no merge markers found"