ifeq ($(OS), Windows_NT)

define log
	@echo ">>> $(1)"
endef

else

define log
	@tput bold 2>/dev/null || exit 0
	@tput setaf 3  2>/dev/null || exit 0
	@echo ">>> $(1)"
	@tput sgr0  2>/dev/null || exit 0
endef

endif


# Секции python команд


.PHONY: install
install:
	$(call log, installing packages)
	poetry install --no-dev

.PHONY: format
format:
	$(call log, reorganizing imports & formatting code)
	poetry run black .
	poetry run isort .
	poetry run ruff . --fix --exit-zero
	poetry run pre-commit run --all
	poetry run mypy .

# Секция запуска

.PHONY: run
run:
	$(call log, Starting)
	poetry run python run.py
