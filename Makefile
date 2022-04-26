#!/bin/bash
help:
	@echo "make"
	@echo "    pypi"
	@echo "        make and upload python package."
pypi:
	rm -f dist/*.tar.gz
	python setup.py sdist bdist_wheel
	# twine upload dist/*.tar.gz
clean:
	rm -rf build
	rm -rf dist
	rm -rf feishu_python_sdk.egg-info