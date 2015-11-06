from django.conf.urls import url
from .views import QuestionIndexView, SurveyIndexView, QuestionDetailView
from . import views
urlpatterns = [
    url(r'^questions/$', QuestionIndexView.as_view()),
    url(r'^$', SurveyIndexView.as_view()),
    url(r'^questions/(?P<pk>[0-9]+)/$', QuestionDetailView.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.SurveyDetailView.as_view()),
    url(r'^create$', views.SurveyCreateView.as_view()),
    url(r'^questions/create$', views.QuestionCreateView.as_view()),
               ]