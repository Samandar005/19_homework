from django.shortcuts import render, redirect, get_object_or_404
from .models import Test, Question, Answer
from .forms import TestForm, QuestionFormSet, AnswerFormSet


def test_list(request):
    tests = Test.objects.all()
    ctx = {'tests': tests}
    return render(request, 'questions/test-list.html', ctx)


def create_test(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        question_formset = QuestionFormSet(request.POST)

        if form.is_valid() and question_formset.is_valid():
            test = form.save()
            questions = question_formset.save(commit=False)

            # First, handle question deletions
            for obj in question_formset.deleted_objects:
                obj.delete()

            # Then save new/updated questions and their answers
            for question_form in question_formset.forms:
                if question_form.is_valid() and not question_form.cleaned_data.get('DELETE', False):
                    question = question_form.save(commit=False)
                    question.test = test
                    question.save()

                    # Create answer formset for this question
                    answer_formset = AnswerFormSet(
                        request.POST,
                        instance=question,
                        prefix=f'answers_{question_form.prefix}'
                    )

                    if answer_formset.is_valid():
                        answers = answer_formset.save(commit=False)

                        # Handle answer deletions
                        for obj in answer_formset.deleted_objects:
                            obj.delete()

                        # Save new/updated answers
                        for answer in answers:
                            answer.question = question
                            answer.save()

            return redirect('questions:list')
    else:
        form = TestForm()
        question_formset = QuestionFormSet(queryset=Question.objects.none())

    return render(request, 'questions/test-formset.html', {
        'form': form,
        'question_formset': question_formset
    })


def update_test(request, pk):
    test = get_object_or_404(Test, pk=pk)

    if request.method == 'POST':
        form = TestForm(request.POST, instance=test)
        question_formset = QuestionFormSet(request.POST, instance=test)

        if form.is_valid() and question_formset.is_valid():
            test = form.save()

            # Handle question deletions
            for obj in question_formset.deleted_objects:
                obj.delete()

            # Save new/updated questions and their answers
            for question_form in question_formset.forms:
                if question_form.is_valid() and not question_form.cleaned_data.get('DELETE', False):
                    question = question_form.save(commit=False)
                    question.test = test
                    question.save()

                    # Create answer formset for this question
                    answer_formset = AnswerFormSet(
                        request.POST,
                        instance=question,
                        prefix=f'answers_{question_form.prefix}'
                    )

                    if answer_formset.is_valid():
                        answers = answer_formset.save(commit=False)

                        # Handle answer deletions
                        for obj in answer_formset.deleted_objects:
                            obj.delete()

                        # Save new/updated answers
                        for answer in answers:
                            answer.question = question
                            answer.save()

            return redirect('questions:list')
    else:
        form = TestForm(instance=test)
        question_formset = QuestionFormSet(instance=test)

    return render(request, 'questions/test-formset.html', {
        'form': form,
        'question_formset': question_formset
    })

def delete(request, pk):
    test = get_object_or_404(Test, pk=pk)
    test.delete()
    return redirect('questions:list')