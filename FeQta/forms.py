from django import forms
from .models import Question,Topic,Answer

class QuestionCreateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'topic',
            'question',
            'desc',
        ]

    def clean_question(self):
        ques = self.cleaned_data.get("question")
        if ques == 'Hello':
            raise forms.ValidationError('Not a valid question')
        return ques

class AnswerCreateForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = [
            'question',
            'answer',
        ]
