from django.shortcuts import render, redirect, get_object_or_404
from .models import Test
from .forms import *
from lessons.models import Lesson

def test_list(request):
    tests = Test.objects.all()
    ctx = {'tests': tests}
    return render(request, 'questions/test-list.html', ctx)


def create_test(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            test = form.save()
            questions_data = request.POST.getlist('questions')
            for question_data in questions_data:
                question_text = question_data.get('text')
                question = Question.objects.create(test=test, text=question_text)
                answers_data = question_data.get('answers', [])
                for answer_data in answers_data:
                    Answer.objects.create(
                        question=question,
                        text=answer_data.get('text'),
                        is_correct=answer_data.get('is_correct', False)
                    )
            return redirect('questions:list')

    form = TestForm()
    return render(request, 'questions/test-formset.html', {'form': form})

def delete(request, pk):
    test = get_object_or_404(Test, pk=pk)
    test.delete()
    return redirect('questions:list')