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
    driver = create_driver(use_emulator=True)  # Emulator
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
            screenshots_dir = "reports/screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            screenshot_path = os.path.join(screenshots_dir, f"{item.name}.png")
            driver.save_screenshot(screenshot_path)

            # Attach screenshot to pytest-html
            if "pytest_html" in item.config.pluginmanager.list_plugin_distinfo():
                extra = getattr(rep, "extra", [])
                extra.append(pytest_html.extras.png(screenshot_path))
                rep.extra = extra


# ✅ Customize pytest-html report (pytest-html>=4.0.0 way)
@pytest.hookimpl(optionalhook=True)
def pytest_html_report_title(report):
    report.title = "📊 My Project Test Report"


@pytest.hookimpl(optionalhook=True)
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend(
        [
            "Project: My Automation Project",
            "Company: My Company Pvt Ltd",
        ]
    )


@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_html(report, data):
    # Add company logo only once (not for every test)
    if report.when == "setup":
        data.append(
            "<div style='text-align:center; margin:10px;'>"
            "<img src='company_logo.png' alt='Company Logo' width='120'>"
            "</div>"
        )
