from wagtail.models import Page


class BasePage(Page):

    class Meta:
        abstract = True
