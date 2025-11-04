from django.db import models
from django.conf import settings

# Create your models here.
class StickyNote(models.Model):
    """ Model representing a sticky note.
    
    Fields:
    - title: CharField for the sticky note title with a maximum length of 255
    characters.
    - content: TextField for the sticky note content.
    - created_at: DateTimeField set to the current date and time when the
    sticky note is created.
    
    Relationships:
    - Author: ForeignKey representing the author of the sticky note.

    Methods:
    - __str__: Returns a string representation of the sticky note, showing
    the first 20 characters of the content.
    
    :param models.Model: Django's base model class.
    """

    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.title
    
