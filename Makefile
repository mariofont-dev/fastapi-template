DC=docker compose

.PHONY: build
build:
	$(DC) build

.PHONY: test
test:
	$(DC) run --rm tests

