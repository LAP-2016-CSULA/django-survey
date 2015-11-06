from django.shortcuts import render
from django.views import generic
from .models import Question, Choice, Survey

# Create your views here.
class QuestionIndexView(generic.ListView):
    template_name = 'survey/questions.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        """ Return the last five published questions. """
        return Question.objects.order_by('-pub_date')[:5]
    
class SurveyIndexView(generic.ListView):
    template_name = 'survey/surveys.html'
    context_object_name = 'latest_survey_list'
    
    def get_queryset(self):
        """ Return the last five published surveys. """
        return Survey.objects.order_by('-title')
    
class QuestionDetailView(generic.DetailView):
    model = Question
    template_name = 'survey/question_detail.html'
    
class SurveyDetailView(generic.DetailView):
    model = Survey
    template_name = 'survey/survey_detail.html'