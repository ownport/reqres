PYTHON ?= /usr/bin/env python
PROJECT_NAME_BIN ?= reqres
PROJECT_NAME_SRC ?= reqres

clean:
	@ echo "[INFO] Cleaning directory:" $(shell pwd)/.local-ci
	@ rm -rf $(shell pwd)/.local-ci
	@ echo "[INFO] Cleaning directory:" $(shell pwd)/reqres.egg-info
	@ rm -rf $(shell pwd)/reqres.egg-info
	@ echo "[INFO] Cleaning files: *.pyc"
	@ find . -name "*.pyc" -delete
	@ echo "[INFO] Cleaning files: .coverage"
	@ rm -rf $(shell pwd)/.coverage


test-all: clean
	@ py.test

test-all-with-coverage: clean
		@ py.test --cov=reqres --cov-report term-missing --cov-config=.coveragerc

run-local-ci: clean
	local-ci -r $(shell pwd) -s .local-ci.yml
