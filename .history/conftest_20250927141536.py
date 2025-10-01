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

import pytest
from utils.driver_factory import create_driver


@pytest.fixture
def driver():
    # 👉 Pass True for emulator, False for real device
    driver = create_driver(use_emulator=True)  # Emulator
    # driver = create_driver(use_emulator=False)  # Real device
    yield driver
    driver.quit()


import pytest


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")  # only if driver fixture exists
        if driver:
            screenshot_path = f"reports/screenshots/{item.name}.png"
            driver.save_screenshot(screenshot_path)
            if "pytest_html" in item.config.pluginmanager.list_plugin_distinfo():
                extra = getattr(rep, "extra", [])
                extra.append(pytest_html.extras.png(screenshot_path))
                rep.extra = extra
