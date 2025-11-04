from django import forms
from .models import StickyNote

class StickyNoteForm(forms.ModelForm):
    """ Form for creating and updating StickyNote objects.
    
    Fields: 
    - title: CharField for the sticky note title.
    - content: TextField for the sticky note content.
   

    Meta class:
    - Defines the StickyNote model to be used and the fields to include 
    in the form.

    :param forms.ModelForm: Django's ModelForm class.
    """

    class Meta:
        model = StickyNote
        fields = ["title", "content", "author"]