class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def highlight(self, element, name="element"):
        """Highlight element - works for web & logs/screenshots in native app"""
        try:
            # Works if running tests in webview/browser
            self.driver.execute_script(
                "arguments[0].style.border='3px solid red'", element
            )
            print(f"🔦 Highlighted (web): {name}")
        except Exception:
            # Native app fallback → just log + optional screenshot
            print(f"🔦 Highlighted (native): {name} -> {element}")
            try:
                self.driver.save_screenshot(f"screenshots/highlight_{name}.png")
            except Exception:
                pass
