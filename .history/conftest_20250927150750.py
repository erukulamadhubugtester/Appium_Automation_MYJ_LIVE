# ======================================================== 1 code  ========================================================

# import pytest
# from utils.driver_factory import create_driver


# @pytest.fixture
# def driver():


#     driver = create_driver()
#     yield driver
#     driver.quit()


# ======================================================== 1 code  ========================================================

# ======================================================== 2 code  ========================================================

import os
import pytest
import pytest_html
from utils.driver_factory import create_driver


# ✅ Driver Fixture
@pytest.fixture
def driver():
    # 👉 Pass True for emulator, False for real device
    driver = create_driver(use_emulator=True)  # Emulator
    # driver = create_driver(use_emulator=False)  # Real device
    yield driver
    driver.quit()


# ✅ Hook for HTML reporting + screenshots
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            # Make sure screenshot folder exists
            screenshots_dir = "reports/screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            # Save screenshot
            screenshot_path = os.path.join(screenshots_dir, f"{item.name}.png")
            driver.save_screenshot(screenshot_path)

            # Attach to pytest-html
            if "pytest_html" in item.config.pluginmanager.list_plugin_distinfo():
                extra = getattr(rep, "extra", [])
                extra.append(pytest_html.extras.png(screenshot_path))
                rep.extra = extra


# import pytest


def pytest_configure(config):
    # Change project title in pytest-html report
    config._metadata["Project"] = "My Automation Project"
    config._metadata["Company"] = "My Company Pvt Ltd"

    # Add custom title
    config._html = getattr(config, "_html", None)
    if config._html:
        config._html.title = "📊 My Project Test Report"
