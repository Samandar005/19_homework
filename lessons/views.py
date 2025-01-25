from django.shortcuts import render, redirect, get_object_or_404
from .forms import LessonForm
from .models import Lesson


def home(request):
    return render(request, 'index.html')

def lesson_list(request):
    lessons = Lesson.objects.all()
    ctx = {'lessons': lessons}
    return render(request, 'lessons/lesson-list.html', ctx)

def create_lesson(request):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lessons:list')
    form = LessonForm()
    ctx = {'form': form}
    return render(request, 'lessons/lesson-create.html', ctx)

def update_lesson(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    if request.method == 'POST':
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            form.save()
            return redirect(lesson.get_detail_url())
    form = LessonForm(instance=lesson)
    ctx = {'form': form,
           'lesson': lesson
           }
    return render(request, 'lessons/lesson-create.html', ctx)

def detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    ctx = {'lesson': lesson}
    return render(request, 'lessons/lesson-detail.html', ctx)

def delete(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    lesson.delete()
    return redirect('lessons:list')
