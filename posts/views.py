from django.shortcuts import render, get_object_or_404, redirect
from .models import StickyNote
from .forms import StickyNoteForm

# Create your views here.
def sticky_note_display(request):
    """ View to display all the sticky notes.
    
    :param request: HTTP request object.
    :return: Rendered template displaying all of the sticky notes.
    """
    sticky_notes = StickyNote.objects.all()

    # Creating a context dictionary to pass data
    context = {
        "notes": sticky_notes,
        "page_title": "Sticky Notes Board"
    }

    return render(request, "posts/post_display.html", context)

def sticky_note_create(request):
    """ View to create a new sticky note.
    
    :param request: HTTP request object.
    :return: Rendered template for creating a new sticky note.
    """
    if request.method == "POST":
        form = StickyNoteForm(request.POST)
        if form.is_valid():
            sticky_note = form.save(commit=False)
            sticky_note.save()
            return redirect("sticky_note_display")
    else:
        form = StickyNoteForm()
    return render(request, "posts/post_form.html", {"form": form})

def sticky_note_update(request, pk):
    """ View to update an existing sticky note.
    
    :param request: HTTP request object.
    :param pk: Primary key of the sticky note to be updated.
    :return: Rendered template for updating the specified sticky note.
    """
    sticky_note = get_object_or_404(StickyNote, pk=pk)
    if request.method == "POST":
        form = StickyNoteForm(request.POST, instance=sticky_note)
        if form.is_valid():
            sticky_note = form.save(commit=False)
            sticky_note.save()
            return redirect("sticky_note_display")
    else:
        form = StickyNoteForm(instance=sticky_note)
    return render(request, "posts/post_form.html", {"form": form})

def sticky_note_delete(request, pk):
    """ View to delete a sticky note.
    
    :param request: HTTP request object.
    :param pk: Primary key of the sticky note to be deleted.
    :return: Redirects to the sticky note display view after deletion.
    """
    sticky_note = get_object_or_404(StickyNote, pk=pk)
    sticky_note.delete()
    return redirect("sticky_note_display")