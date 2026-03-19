install:
	pip install -r requirements.txt
	python -m playwright install

run:
	uvicorn app.main:app --reload

test-api:
	python -m pytest -q tests/api --cov=app --cov-report=term-missing --html=reports/api_report.html --self-contained-html

test-ui:
	python -m pytest -q tests/ui --html=reports/ui_report.html --self-contained-html --screenshot=only-on-failure --video=retain-on-failure

test-e2e:
	python -m pytest -q tests/e2e --html=reports/e2e_report.html --self-contained-html

test-all:
	python -m pytest -q tests/api tests/e2e --cov=app --cov-report=term-missing --html=reports/all_api_e2e_report.html --self-contained-html
	python -m pytest -q tests/ui --html=reports/ui_report.html --self-contained-html --screenshot=only-on-failure --video=retain-on-failure