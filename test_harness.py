from selenium import webdriver
from examples.site_checks import test_heading, test_title


def run_tests(driver, url, functions, test_set_title):
    results = []
    for function in functions:
        try:
            driver.get(url)
            function(driver, url)
            results.append({"name": function.__name__, "result": "PASS", "error": ""})
        except Exception as error:
            results.append({
                "name": function.__name__,
                "result": "FAIL",
                "error": f"{type(error).__name__}: {error}",
            })

    passed = sum(test["result"] == "PASS" for test in results)
    failed = len(results) - passed
    print(f"\nTest report: {test_set_title}")
    for test in results:
        print(f"{test['result']}: {test['name']}")
        if test["error"]:
            print(f"  {test['error']}")
    print(f"Summary: {passed} passed, {failed} failed")

    return {"title": test_set_title, "tests": results, "passed": passed, "failed": failed}


def main():
    driver = webdriver.Chrome()
    url = "https://example.com"
    try:
        report = run_tests(
            driver, url, [test_title, test_heading], "Example tests"
        )
        return 1 if report["failed"] else 0
    finally:
        driver.quit()


if __name__ == "__main__":
    raise SystemExit(main())
