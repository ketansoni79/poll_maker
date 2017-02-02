from django import forms
from .models import Question

class CustomNameTextInput(forms.TextInput):
    def render(self, name, value, attrs=None):
        if 'name' in attrs:
            name = attrs['name']
            del attrs['name']
        return super(TextInput, self).render(name, value, attrs)

class QuestionForm(forms.ModelForm):
	choice = forms.CharField(required=False, widget=forms.TextInput(attrs={'name':'choice []','label':'Question Choice'}))
	class Meta:
		model = Question
		exclude = ('pub_date',)

