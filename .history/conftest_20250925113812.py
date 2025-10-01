import pytest
from utils.driver_factory import create_driver


@pytest.fixture
def driver():

     # 👉 Pass True for emulator, False for real device
    driver = create_driver(use_emulator=True)   # Emulator
    # driver = create_driver(use_emulator=False)  # Real device
    # driver = create_driver()
    yield driver
    driver.quit()
