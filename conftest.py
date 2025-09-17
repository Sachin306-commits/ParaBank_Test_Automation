import pytest
from selenium import webdriver
import os
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from Utils.selenium_helpers import capture_screenshot


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Browser name: chrome or firefox"
    )

@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("--browser_name")

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.implicitly_wait(5)

    # Attach driver to the node so it's accessible in the report hook
    request.node.driver = driver

    yield driver

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when in ("call", "setup"):
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            driver = getattr(item, "driver", None)
            if driver:
                reports_dir = os.path.join(os.path.dirname(__file__), 'reports')
                os.makedirs(reports_dir, exist_ok=True)
                file_name = os.path.join(reports_dir, report.nodeid.replace("::", "_") + ".png")
                print("Saving screenshot to:", file_name)
                _capture_screenshot(driver, file_name)

                html = f'<div><img src="{file_name}" style="width:304px; height:228px;" ' \
                       f'onclick="window.open(this.src)" align="right"/></div>'
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(driver, file_name):
    driver.get_screenshot_as_file(file_name)


