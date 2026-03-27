from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import NoteForm
from .models import Note

NOTES_PER_PAGE = 10

FUN_COLORS = [
    "#FFD166",
    "#CDEAC0",
    "#A0C4FF",
    "#FFADAD",
    "#D8B4FE",
    "#FDE68A",
]


def _back_to_notes(request):
    next_url = request.POST.get("next", "")
    if next_url.startswith("/"):
        return redirect(next_url)
    return redirect("note_list")


@login_required
def note_list(request):
    query = request.GET.get("q")
    notes = Note.objects.filter(owner=request.user)

    if query:
        notes = notes.filter(Q(title__icontains=query) | Q(content__icontains=query))

    notes = notes.order_by("-pinned", "-created_at")

    paginator = Paginator(notes, NOTES_PER_PAGE)
    page_number = request.GET.get("page")
    notes_page = paginator.get_page(page_number)

    return render(
        request,
        "note_list.html",
        {
            "notes": notes_page,
            "query": query or "",
        },
    )


@login_required
def note_create(request):
    form = NoteForm(request.POST or None)

    if form.is_valid():
        note = form.save(commit=False)
        note.owner = request.user
        note.save()
        return redirect("note_list")

    return render(request, "note_form.html", {"form": form})


@login_required
def note_edit(request, id: int):
    note = get_object_or_404(Note, id=id, owner=request.user)
    form = NoteForm(request.POST or None, instance=note)

    if form.is_valid():
        form.save()
        return redirect("note_list")

    return render(request, "note_form.html", {"form": form})


@login_required
def note_delete(request, id: int):
    note = get_object_or_404(Note, id=id, owner=request.user)

    if request.method == "POST":
        note.delete()
        return redirect("note_list")

    return render(request, "note_confirm_delete.html", {"note": note})


@login_required
def note_toggle_pin(request, id: int):
    note = get_object_or_404(Note, id=id, owner=request.user)
    if request.method == "POST":
        note.pinned = not note.pinned
        note.save(update_fields=["pinned", "updated_at"])
    return _back_to_notes(request)


@login_required
def note_set_color(request, id: int):
    note = get_object_or_404(Note, id=id, owner=request.user)
    if request.method == "POST":
        new_color = request.POST.get("color")
        if new_color in FUN_COLORS:
            note.color = new_color
            note.save(update_fields=["color", "updated_at"])
    return _back_to_notes(request)


def register_view(request):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("note_list")

    return render(request, "register.html", {"form": form})

# Create your views here.
