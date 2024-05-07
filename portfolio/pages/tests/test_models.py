from wagtail.test.utils import WagtailPageTestCase

from portfolio.pages.factories import HomePageFactory


class TestHomePageFactory(WagtailPageTestCase):
    def test_create(self):
        HomePageFactory()
