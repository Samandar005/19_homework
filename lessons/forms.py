from django import forms
from .models import Lesson


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('name', 'description',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded p-2'}),
            'description': forms.Textarea(attrs={'class': 'w-full border border-gray-300 rounded p-2', 'rows': 4}),
        }

        def clean_name(self):
            name = self.cleaned_data.get('name')
            if len(name) <= 3:
                raise forms.ValidationError("Lesson nomi 3ta harfdan kam bolmasin")
            return name

        def clean_desc(self):
            description = self.cleaned_data.get('description')
            if len(description) <= 10:
                raise forms.ValidationError("Lesson desc 10 ta harfdan kam bolmasin")
            return description
