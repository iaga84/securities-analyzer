develop:
	pip install -U pip setuptools
	CFLAGS='-std=c99' pip install -e .[dev] --no-cache-dir
	@${MAKE} setup-git

setup-git:
	@git config branch.autosetuprebase always
	@git config branch.autosetupmerge always
	@git config push.default simple
	@chmod +x git_hooks/*
	@cd .git/hooks && ln -fs ../../git_hooks/* .