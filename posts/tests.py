from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import StickyNote
# Create your tests here.
User = get_user_model()

class StickyNoteModelTest(TestCase):
    def setUp(self):
        author = User.objects.create_user(username="Test Author", password="password123")
        StickyNote.objects.create(title="Test StickyNote", 
                                  content="This is a test" \
        " sticky note.", 
        author=author)

    def test_sticky_note_has_title(self):
        sticky_note = StickyNote.objects.get(id=1)
        self.assertEqual(sticky_note.title, "Test StickyNote")

    def test_sticky_note_has_content(self):
        sticky_note = StickyNote.objects.get(id=1)
        self.assertEqual(sticky_note.content, "This is a test sticky note.")

class StickyNoteViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="Test Author", password="password123")
        self.note = StickyNote.objects.create(
            title="Another Test Sticky Note",
            content="Some content here",
            author=self.user
        )
        
    
    def test_sticky_note_display_view(self):
        response = self.client.get(reverse("sticky_note_display"))
        self.assertEqual(response.status_code, 200)
        print(response.content.decode())
        self.assertContains(response, "Another Test Sticky Note")


    def test_sticky_note_create_view(self):
        """A new sticky note can be created."""
        response = self.client.post(reverse("sticky_note_create"), {
            "title": "New Note",
            "content": "A new sticky note",
            "author": self.user.id,
        })
        self.assertEqual(response.status_code, 302)  
        self.assertTrue(StickyNote.objects.filter(title="New Note").exists())

    def test_sticky_note_update_view(self):
        """An existing note can be updated."""
        response = self.client.post(reverse("sticky_note_update", args=[self.note.id]), {
            "title": "Updated Sticky Note",
            "content": "Updated content",
            "author": self.user.id,
        })
        self.note.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.note.title, "Updated Sticky Note")

    def test_delete_view(self):
        """A note can be deleted."""
        response = self.client.get(reverse("sticky_note_delete", args=[self.note.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(StickyNote.objects.filter(id=self.note.id).exists())


