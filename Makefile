SHELL := /bin/bash
PROJECT = nf-caravans

-include .env

.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' ${MAKEFILE_LIST} | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: githooks
githooks: ## local git action to enable existing hooks under .githooks
	git config core.hooksPath .githooks

.PHONY: test
test: ## Run tests locally
	DEPLOY_ENV=test python src/manage.py collectstatic --noinput
	DEPLOY_ENV=test pytest src

.PHONY: ci-test
ci-test: ## Test run aimed at being executed in Github
	python src/manage.py collectstatic --noinput
	set -o pipefail ; pytest --junitxml=pytest.xml --cov-report=term-missing:skip-covered --cov=src src | tee pytest-coverage.txt

.PHONY: lint
lint: ## Check code wellformedness (local)
	flake8 src
	black --check src
	isort --profile black src/

.PHONY: cleanup
cleanup: ## Sanitise code (local)
	black src
	isort src

.PHONY: docker-test
docker-test: ## Runs [py]tests using the `test` container
	docker compose run test src/manage.py collectstatic --noinput
	docker compose run test pytest src

.PHONY: docker-lint
docker-lint: ## Check code wellformedness from within the container
	docker compose run web flake8 src
	docker compose run web black --check src

.PHONY: docker-cleanup
docker-cleanup: ## Sanitise code from within the web container
	docker compose run web black src
	docker compose run web isort -rc src


