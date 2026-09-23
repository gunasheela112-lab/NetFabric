PYTHON ?= python3

.PHONY: test api lab-up lab-down routes baseline

test:
	$(PYTHON) -m pytest -q

api:
	$(PYTHON) -m uvicorn api.main:app --reload

lab-up:
	./scripts/lab_up.sh

lab-down:
	./scripts/lab_down.sh

routes:
	./scripts/show_routes.sh

baseline:
	./scripts/run_baseline.sh
