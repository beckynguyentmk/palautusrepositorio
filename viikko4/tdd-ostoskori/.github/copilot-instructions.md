## Project shape

- This is a small Python TDD exercise for an implementation of `Ostoskori` (shopping cart).
- Application code is in `src/`.
- Tests are in `src/tests/`.
- The project uses Python 3.14 (see `.python-version`) and pytest as the test runner. Dependencies are declared in `pyproject.toml`; pytest is the only development dependency.

## Required rules

- Execute tests with `uv run pytest`.
- Do not change the code in `src/ostos.py` or `src/tuote.py`.
- Do not edit tests unless the user explicitly asks.
- Always implement absolutely minimal code that makes the tests pass.

## Run the project

Use `uv` to select the configured Python environment and run pytest:

- Full suite: `uv run pytest`
- One test file: `uv run pytest src/tests/ostoskori_test.py`
- One test method: `uv run pytest src/tests/ostoskori_test.py::TestOstoskori::test_ostoskorin_hinta_ja_tavaroiden_maara_alussa`

There is no separate build step or configured lint command.

## Architecture

- `Tuote` represents a product: name, unit price, and its own state.
- `Ostos` is a cart line. It combines a `Tuote` with a quantity and computes the line subtotal.
- `Ostoskori` is the cart aggregate. Its public operations expose item count, total price, add/remove, clear, and the list of cart lines.
- The implementation currently keeps the Finnish domain API (`tavaroita_korissa`, `lisaa_tuote`, `poista_tuote`, `tyhjenna`, `ostokset`) and public methods are stubbed until implemented.
- Modules import peers by bare module name, for example `from tuote import Tuote`; preserve this convention because `src` is the application/test execution source directory.
- `src/index.py` is only a placeholder and does not provide an executable entry point.

## Test conventions

- Tests use `unittest.TestCase` and are run by pytest; new tests should fit the existing class-based style.
- `setUp` creates the cart under test, usually stored as `self.kori`.
- Assertions use `assertEqual` and other `unittest` assertions.
- Test and method names are descriptive Finnish sentences, commonly reflecting behavior and setup, for example `_alussa` for initial state.
