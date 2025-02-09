from django import forms
from django.forms import inlineformset_factory
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

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError("Test nomi kamida 3 ta belgidan iborat bo'lishi kerak")
        return name


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('text',)
        widgets = {
            'text': forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded p-2'})
        }

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if len(text) < 10:
            raise forms.ValidationError("Savol matni kamida 10 ta belgidan iborat bo'lishi kerak")
        return text


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('text', 'is_correct')
        widgets = {
            'text': forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded p-2'}),
            'is_correct': forms.CheckboxInput(attrs={'class': 'form-checkbox'})
        }

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if len(text) < 2:
            raise forms.ValidationError("Javob matni kamida 2 ta belgidan iborat bo'lishi kerak")
        return text


# Formset yaratish - bu muhim o'zgarish
QuestionFormSet = inlineformset_factory(
    Test,  # Parent model
    Question,  # Child model
    form=QuestionForm,
    fields=['text'],
    extra=1,  # Qo'shimcha bo'sh formalar soni
    can_delete=True,  # O'chirish imkoniyati
    min_num=1,  # Minimal formlar soni
    validate_min=True,  # Minimal sonni tekshirish
    max_num=10  # Maksimal formlar soni
)

AnswerFormSet = inlineformset_factory(
    Question,  # Parent model
    Answer,  # Child model
    form=AnswerForm,
    fields=['text', 'is_correct'],
    extra=2,  # Qo'shimcha bo'sh formalar soni
    can_delete=True,  # O'chirish imkoniyati
    min_num=2,  # Minimal formlar soni
    validate_min=True,  # Minimal sonni tekshirish
    max_num=4  # Maksimal formlar soni
)