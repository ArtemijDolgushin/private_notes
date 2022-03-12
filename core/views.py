from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from core.forms import NoteForm, UserForm
from core.models import Note


def index(request):
    if request.user.is_authenticated:
        notes_count = Note.objects.filter(user=request.user).count()
        context = {
            'notes_count': notes_count,
        }
    else:
        context = {
            'project_title': 'Приватные заметки.',
        }
    return render(request, 'index.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        username = request.POST['email']
        if User.objects.filter(username=username).count():
            form.add_error('email', 'User with this email already exists')
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')
    else:
        form = UserForm()
    context = {
        'form': form,
    }
    return render(request, 'registration/signup.html', context)


@login_required
def notes_list(request):
    notes = Note.objects.filter(user=request.user)
    context = {
        'notes': notes,
    }
    return render(request, 'note_list.html', context)


@login_required
def add(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user_id = request.user.id
            form.save()
            return redirect('list')
    else:
        form = NoteForm()
        context = {
            'form': form,
            'title': 'Добавить заметку',
        }
        return render(request, 'note_form.html', context)


@login_required
def edit(request, note_id):
    user = request.user
    note = get_object_or_404(Note, pk=note_id)
    if user.id != note.user_id:
        raise PermissionDenied
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form = form.save(commit=False)
            form.user_id = request.user.id
            form.save()
            return redirect('list')

    else:
        form = NoteForm(instance=note)

    context = {
        'form': form, 'title': 'Редактировать заметку',
    }
    return render(request, 'note_form.html', context)


@login_required
def delete(request, note_id):
    user = request.user
    note = get_object_or_404(Note, pk=note_id)
    if user.id == note.user_id:
        note.delete()
        return redirect('list')
    else:
        raise PermissionDenied
