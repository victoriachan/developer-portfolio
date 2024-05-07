from django.db import models
from wagtail.images.models import AbstractImage, AbstractRendition, Image


# We're not doing anything different with our custom image yet. But as it would be a
# lot of trouble to introduce a custom image later, it is better to just start with one.
class CustomImage(AbstractImage):
    admin_form_fields = Image.admin_form_fields


class CustomRendition(AbstractRendition):
    image = models.ForeignKey(
        CustomImage, related_name="renditions", on_delete=models.CASCADE
    )

    class Meta:
        unique_together = (("image", "filter_spec", "focal_point_key"),)
