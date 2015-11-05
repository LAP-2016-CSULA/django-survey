from django.conf.urls import url
from .views import QuestionIndexView

urlpatterns = [
    url(r'^questions/$', QuestionIndexView.as_view()),
               ]