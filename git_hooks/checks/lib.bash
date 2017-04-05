#!/usr/bin/env bash

## Colors
RED=`printf '\033[1;31m'`
GREEN=`printf '\033[1;32m'`
WHITE=`printf '\033[1;37m'`
GREY=`printf '\033[1;36m'`
NC='\033[0m' # No Color

## Icons
CHECK=`printf ${GREEN}'✔'${NC}`
CROSS=`printf ${RED}'✘'${NC}`

REPO_DIR=$(git rev-parse --show-toplevel 2> /dev/null)
DOT_GIT_DIR=$(git rev-parse --git-dir)
if [ "$DOT_GIT_DIR" = ".git" ]; then
	DOT_GIT_DIR="$REPO_DIR"/"$DOT_GIT_DIR"
fi
HOOKS_CHECK_DIR="$DOT_GIT_DIR"/hooks/checks

AVH_MAJOR=""
AVH_MINOR=""
AVH_PATCH_LEVEL=""
AVH_PRE_RELEASE=""
AVH_VERSION=""

gitflow_contains() {
	local return

	case $1 in
		*$2*)
			return=0
			;;
		*)
			return=1
			;;
	esac
	return $return
}

gitflow_fail() {
	echo -e "\t"${CROSS} ${GREY}$1${NC}
}

gitflow_ok() {
	echo -e "\t"${CHECK} ${GREY}$1${NC}
}

h1() {
	echo -e "\n${NC}$1 ...\n"
}

gitflow_error() {
	echo -e "\n${RED}$1 ...\n"
}

gitflow_success() {
	echo -e "\n${CHECK} ${GREEN}$1 ...${NC}\n"
}

gitflow_commit_files() {

	if [ $# -eq 0 ] ; then
	    echo $(git diff-index --name-only --diff-filter=ACM --cached HEAD --)
	    exit 0
	fi

	extensions=''
	for extension in "$@"
	do
		extensions="${extensions}(${extension})|"
	done
	regex="\.(${extensions%?})$"
	echo $(git diff-index --name-only --diff-filter=ACM --cached HEAD -- | grep -E "$regex")
}
