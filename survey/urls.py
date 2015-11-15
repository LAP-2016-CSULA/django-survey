from django.conf.urls import url
from .views import QuestionIndexView, SurveyIndexView, QuestionDetailView
from . import views
urlpatterns = [
    url(r'^questions/$', QuestionIndexView.as_view(), name='question_list'),
    url(r'^$', SurveyIndexView.as_view(), name='index'),
    url(r'^questions/(?P<pk>[0-9]+)/$', QuestionDetailView.as_view(), name='question_detail'),
    url(r'^(?P<pk>[0-9]+)/$', views.SurveyDetailView.as_view(), name='detail'),
    url(r'^create$', views.SurveyCreateView.as_view(), name='create'),
    url(r'^questions/create$', views.QuestionCreateView.as_view(), name='question_create'),
    url(r'^questions/update/(?P<pk>[0-9]+)/$', views.QuestionUpdateView.as_view(), name='question_update'),
    url(r'^species$', views.SpeciesIndexView.as_view(), name='species_index'),
    url(r'^species/create$', views.SpeciesCreateView.as_view(), name='species_create'),
    url(r'^species/(?P<pk>[0-9]+)/$', views.SpeciesDetailView.as_view(), name='species_detail')

               ]
