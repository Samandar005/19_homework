from django import forms
from .models import Test, Question, Answer
from lessons.models import Lesson


class TestForm(forms.ModelForm):
    lesson = forms.ModelChoiceField(
        queryset=Lesson.objects.all(),
        widget=forms.Select(attrs={'class': 'w-full border border-gray-300 rounded p-2'})
    )
    class Meta:
        model = Test
        fields = ('name', 'lesson')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded p-2'}),
        }

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('text',)
        widgets = {
            'text': forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded p-2'})
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('text', 'is_correct')
        widgets = {
            'text': forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded p-2'}),
            'is_correct': forms.CheckboxInput(attrs={'class': 'form-checkbox'})
        }

QuestionFormSet = forms.modelformset_factory(
    Question,
    form=QuestionForm,
    extra=2
)

AnswerFormSet = forms.modelformset_factory(
    Answer,
    form=AnswerForm,
    extra=2
)