#!/usr/bin/env bash
M=`find src -type d -name migrations -exec git clean -n {} \;`
if [ -n "$M" ]; then
    gitflow_fail "- ERROR - found untracked migrations $M"
    exit 1
fi

gitflow_ok " - ok, no untracked migrations found"
