#!/usr/bin/env bash
if git diff-index --quiet HEAD --; then
    # no changes between index and working copy; just run tests
    OUT=`isort -c -rc src/ tests/`
    RET=$?
else
    # Test the version that's about to be committed,
    # stashing all unindexed changes
    git stash -q --keep-index
    FILES=$(gitflow_commit_files py)
    if [ -n "$FILES" ]; then
        OUT=`isort -c $FILES`
        RET=$?
    else
        gitflow_ok " - ok, isort skipped (no .py file in commit)"
        RET=-1
    fi
    git stash pop -q
fi

if [ $RET -eq 0 ];then
    gitflow_ok " - ok, isort didn't find any issue"
elif [ $RET -gt 0 ];then
    gitflow_fail "- ERROR - isort found some issues:"
    echo "$OUT"
    exit $RET

fi
