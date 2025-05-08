.ONESHELL:
SHELL=/bin/bash

VENV_DIR=.intro_venv
PYTHON=$(VENV_DIR)/bin/python
PIP=$(VENV_DIR)/bin/pip

install:
	@if ! command -v uv &> /dev/null; then \
		echo ">>> uv not found. Please install it via 'curl -LsSf https://astral.sh/uv/install.sh | sh'" ; \
		exit 1 ; \
	fi
	@echo ">>> Creating virtual environment in $(VENV_DIR)..."
	uv venv $(VENV_DIR)
	@echo ">>> Installing dependencies..."
	source $(VENV_DIR)/bin/activate && \
		uv pip install -e . && \
		uv pip install -U commitizen pre-commit && \
		pre-commit install

remove-env:
	@echo -n "Do you want to remove the environment at $(VENV_DIR) for a clean install? [y/N] " && read ans && if [ $${ans:-'N'} = 'y' ]; then rm -rf $(VENV_DIR); fi

test:
	source $(VENV_DIR)/bin/activate && \
		python -m pytest tests/

clean:
	$(VENV_DIR)/bin/black -l 120 exercises/
	$(VENV_DIR)/bin/black -l 120 tests/
	$(VENV_DIR)/bin/isort --profile black -l 120 --filter-files exercises/
	$(VENV_DIR)/bin/isort --profile black -l 120 --filter-files tests/

update:
	uv pip install -e .
