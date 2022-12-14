all: lint check

lint:
	LIBCST_PARSER_TYPE=native poetry run gray --log-level error src -f add-trailing-comma,autoflake,fixit,isort,pyupgrade,trim,unify,black

check:
	poetry run mypy src --show-error-codes