from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys


class ExampleFunctionalTest(FunctionalTest):

    def test_visit_home_page(self):
        # Jane goes to the homepage
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024,768)
