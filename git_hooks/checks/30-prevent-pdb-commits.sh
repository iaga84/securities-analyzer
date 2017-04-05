#!/usr/bin/env bash
ERROR=0
for file in $(gitflow_commit_files py); do
    if grep -Erls "pdb\." $file >/dev/null ; then
    	gitflow_fail "- ERROR - found pdb call in <$file>"
    	exit 1
    fi
done
gitflow_ok " - ok, no pdb statements found"

for file in $(gitflow_commit_files py); do
    if grep -Erls "print\(+111" $file >/dev/null ; then
    	gitflow_fail "- ERROR - found print statement in <$file>"
    	exit 1
    fi
done

gitflow_ok " - ok, no print statements found"
