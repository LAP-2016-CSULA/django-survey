from django.contrib import admin
from .models import Question, Choice, Survey
from django import forms
# Register your models here.

    
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None,
                  {'fields': ['question_text']}),
                 ('Date information', {'fields': ['pub_date'],
                'classes': ['collapse']}),]
    inlines = [ChoiceInline]

class QuestionInline(forms.ModelChoiceField):
    model = Survey.questions.through
    
class SurveyAdmin(admin.ModelAdmin):
    model = Survey
    inlines = [QuestionInline,]

    
    
admin.site.register(Question, QuestionAdmin)
admin.site.register(Survey)