# http://kevindias.com/writing/django-class-based-views-multiple-inline-formsets/
from django.views import generic
from .models import Question, Survey, Species
from django.core.urlresolvers import reverse_lazy
from .forms import QuestionForm, ChoiceFormSet
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404


class QuestionIndexView(generic.ListView):
    """ Question list. """
    template_name = 'survey/questions.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        """ Return the last five published questions. """
        return Question.objects.order_by('-question_text')


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
    success_url = reverse_lazy('survey:index')
    template_name = 'survey/survey_form.html'

    # Have to specify the 'fields' attribute
    # else it will raise error Using ModelFormMixin without fields is prohibited
    fields = '__all__'


class QuestionCreateView(generic.CreateView):
    """ Create new question. """
    model = Question
    # fields = '__all__'  # ['question_text']
    template_name = 'survey/question_form.html'
    form_class = QuestionForm
    # have to specify the 'success_url' else there will be error
    success_url = reverse_lazy('survey:question_list')

    def get(self, request, *args, **kwargs):
        """ Handle GET. display inline formset for choices as well.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        choice_form = ChoiceFormSet()
        return self.render_to_response(self.get_context_data(form=form, choice_form=choice_form))

    def post(self, request, *args, **kwargs):
        """ Handle POST
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        choice_form = ChoiceFormSet(request.POST)
        if form.is_valid() and choice_form.is_valid():
            return self.form_valid(form, choice_form)
        else:
            return self.form_invalid(form, choice_form)

    def form_valid(self, form, choice_form):
        """ If all form are valid, save it
        :param form:
        :param choice_form:
        :return:
        """
        self.object = form.save()
        choice_form.instance = self.object
        choice_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, choice_form):
        """ If a form is invalid
        :param form:
        :param choice_form:
        :return:
        """
        return self.render_to_response(self.get_context_data(form=form, choice_form=choice_form))


class QuestionUpdateView(generic.UpdateView):
    """ Update question
    """
    model = Question
    template_name = 'survey/question_form.html'
    form_class = QuestionForm
    success_url = 'survey:question_list'

    def get(self, request, *args, **kwargs):
        """ GET request
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.object = get_object_or_404(Question, pk=self.kwargs['pk'])
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        choice_form = ChoiceFormSet()
        return self.render_to_response(self.get_context_data(object=self.object, form=form, choice_form=choice_form))

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        choice_form = ChoiceFormSet(request.POST)
        if form.is_valid() and choice_form.is_valid():
            return self.form_valid(form, choice_form)
        else:
            return self.form_invalid(form, choice_form)

    def form_valid(self, form, choice_form):
        """ If all form are valid, save it
        :param form:
        :param choice_form:
        :return:
        """
        self.object = form.save()
        choice_form.instance = self.object
        choice_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, choice_form):
        """ If a form is invalid
        :param form:
        :param choice_form:
        :return:
        """
        return self.render_to_response(self.get_context_data(form=form, choice_form=choice_form))


class SpeciesIndexView(generic.ListView):
    """ Species list. """
    model = Species
    context_object_name = 'species_list'
    template_name = 'survey/species.html'

    def get_queryset(self):
        return Species.objects.order_by('-name')


class SpeciesCreateView(generic.CreateView):
    """ Add species to list. """
    model = Species
    template_name = 'survey/species_form.html'
    success_url = reverse_lazy('survey:species_index')
    fields = '__all__'


class SpeciesDetailView(generic.DetailView):
    """ Detail of species. """
    model = Species
    template_name = 'survey/species_detail.html'


