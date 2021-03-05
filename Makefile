ENV?=staging
PY_MODULE=workshop
MODULE?=workshop
UNAME=klarna


default: help

help:
	@echo 'Usage: make [target] ...'
	@echo
	@echo 'Targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
	| awk 'BEGIN {FS = ":.*?## "}; {printf "%-16s %s\n", $$1, $$2}'

#----------- TEST --------------------------------------------------------------
test: ## Lint and unit test python code
	@$(PRE_ACTIVATE) $(MAKE) -j4 --no-print-directory \
	  test-unit \

test-unit:
	@mkdir -p var
	pytest test  \

black: ## Format all the python code
	black -l 80 $(PY_MODULE)
