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
	  test-pylint \

test-unit: ## Run unit-tests and pylint 
	@mkdir -p var
	pytest test  \

test-pylint:
	pylint -f parseable --rcfile=setup.cfg -j 4 --ignore-patterns=".*test_.*.py" workshop

.PHONY: help test test-unit test-pylint
