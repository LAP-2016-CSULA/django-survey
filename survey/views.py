from django.shortcuts import render
from django.views import generic
from .models import Question, Choice, Survey

# Create your views here.
class QuestionIndexView(generic.ListView):
    template_name = 'survey/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        """ Return the last five published questions. """
        return Question.objects.order_by('-pub_date')[:5]