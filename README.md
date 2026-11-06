# QA Automation Framework

End-to-end UI and API test automation framework built with **Playwright (Python)** and **pytest**.
UI tests target the public practice shop [saucedemo.com](https://www.saucedemo.com); API tests target the
public [JSONPlaceholder](https://jsonplaceholder.typicode.com) service.

## Highlights
- **Page Object Model**: locators and actions live in `pages/`, tests read like user stories
- **Tagged test suites**: `smoke` (fast, critical flows), `regression`, `api`
- **Data-driven tests**: login failures use `pytest.mark.parametrize`
- **CI/CD**: GitHub Actions runs smoke tests first, then the full suite, nightly and on every push; HTML reports are uploaded as artifacts

## Project layout
```
pages/          page objects (login, inventory, cart, checkout)
tests/ui/       browser tests
tests/api/      REST API tests
conftest.py     shared fixtures (login, logged-in inventory page)
pytest.ini      markers, base URL, HTML report settings
```

## Setup
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
```

## Run
```bash
pytest                    # everything
pytest -m smoke           # critical flows only
pytest -m api             # API tests only
pytest --headed           # watch the browser
pytest -n auto            # (optional) parallel, after: pip install pytest-xdist
```
An HTML report is written to `reports/report.html`.

## Test plan (summary)
| Area | Coverage |
|------|----------|
| Login | valid login, wrong password, empty fields, locked-out user |
| Inventory | sorting by name and price, cart badge updates |
| Checkout | full purchase, required-field validation |
| API | GET one/list/filter, POST, 404 handling |

## Roadmap
- [ ] Add accessibility checks
- [ ] Add visual regression screenshots
- [ ] Add a failing-test screenshot/trace on CI
