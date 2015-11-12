# http://kevindias.com/writing/django-class-based-views-multiple-inline-formsets/

from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from .models import Question, Choice


class QuestionForm(ModelForm):
    """ Form for question. """
    class Meta:
        model = Question
        fields = '__all__'

ChoiceFormSet = inlineformset_factory(Question, Choice, fields=['choice_text',])
