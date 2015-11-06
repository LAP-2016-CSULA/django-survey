from django.shortcuts import render
from django.views import generic
from .models import Question, Choice, Survey
from django.core.urlresolvers import reverse_lazy


class QuestionIndexView(generic.ListView):
    """ Question list. """
    template_name = 'survey/questions.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        """ Return the last five published questions. """
        return Question.objects.order_by('-pub_date')[:5]
    
class SurveyIndexView(generic.ListView):
    """ Survey list. """
    template_name = 'survey/surveys.html'
    context_object_name = 'latest_survey_list'
    
    def get_queryset(self):
        """ Return the last five published surveys. """
        return Survey.objects.order_by('-title')
    
class QuestionDetailView(generic.DetailView):
    """ Detail content of Question. """
    model = Question
    template_name = 'survey/question_detail.html'
    
class SurveyDetailView(generic.DetailView):
    """ Detail content of Survey. """
    model = Survey
    template_name = 'survey/survey_detail.html'
    
class SurveyCreateView(generic.CreateView):
    """ Create new survey. """
    model = Survey
    #success_url = reverse_lazy()
    template_name = 'survey/survey_form.html'
    
    # Have to specify the 'fields' attribute
    # else it will raise error Using ModelFormMixin without fields is prohibited
    fields = '__all__'
    
class QuestionCreateView(generic.CreateView):
    """ Create new question. """
    model = Question
    fields = '__all__'#['question_text']
    template_name = 'survey/question_form.html'
    # have to specify the 'success_url' else there will be error
    success_url = ''
    