import wagtail_factories

from portfolio.pages.models import HomePage


class HomePageFactory(wagtail_factories.PageFactory):
    title = "Home"

    class Meta:
        model = HomePage
