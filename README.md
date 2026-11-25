# CIS4150 Test Harness

```powershell
python -m pip install -r requirements.txt
python test_harness.py
```

Requires Chrome. Import your test functions from your own packages, then call:

```python
report = run_tests(driver, url, [test_title, test_heading], "Example tests")
```

Each function accepts `(driver, url)` and uses normal Python assertions.
The runner navigates to the URL before each test and continues after failures.
After all tests finish, it prints a report containing the test set title,
each test's name and PASS/FAIL result, failure details, and totals.
It also returns this information as a dictionary with `title`, `tests`,
`passed`, and `failed` keys.

Edit `main()` in `test_harness.py` to choose the URL and functions.
`main()` creates the driver and closes it after the run. Tests are called
directly, without classes or pytest.
