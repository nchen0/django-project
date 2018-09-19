from django.db import models
from uuid import uuid4

# Create your models here.


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """A string representation of the model."""
        return self.text[:50]
