from django.db import models
from wagtail.documents.models import AbstractDocument, Document
from wagtail.images.models import AbstractImage, AbstractRendition, Image
from wagtail.models import Page


class CustomImage(AbstractImage):
    pass


class CustomRendition(AbstractRendition):
    image = models.ForeignKey(
        CustomImage, related_name="renditions", on_delete=models.CASCADE
    )

    class Meta:
        unique_together = (("image", "filter_spec", "focal_point_key"),)


class CustomDocument(AbstractDocument):
    pass


class BasePage(Page):

    class Meta:
        abstract = True
