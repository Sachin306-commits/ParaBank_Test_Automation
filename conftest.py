from selenium import webdriver
import allure
import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="Browser: chrome or firefox or edge")
    parser.addoption("--incognito", action="store_true", help="Run browser in incognito/private mode")


@pytest.fixture
def browserInstance(request):
    browser_name = request.config.getoption("--browser_name").lower()
    incognito = request.config.getoption("--incognito")

    if browser_name == "chrome":
        options = ChromeOptions()
        if incognito:
            options.add_argument("--incognito")
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=ChromeService(), options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        if incognito:
            options.set_preference("browser.privatebrowsing.autostart", True)
        driver = webdriver.Firefox(service=FirefoxService(), options=options)

    elif browser_name == "edge":
        options = EdgeOptions()
        if incognito:
            options.add_argument("--inprivate")
        driver = webdriver.Edge(service=EdgeService(), options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Run all other hooks to get the report
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("browserInstance")  # get browser fixture
        if driver:
            screenshot = driver.get_screenshot_as_png()
            allure.attach(
                screenshot,
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )


def _capture_screenshot(driver, file_name):
    driver.get_screenshot_as_file(file_name)