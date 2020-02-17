from django.db import models
from django.utils.text import slugify

class login(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.username)
        super().save()

        def __str__(self):
            return "{}. {}".format(self.id, self.username)
