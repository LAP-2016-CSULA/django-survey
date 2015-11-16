#  http://stackoverflow.com/questions/949268/django-accessing-the-model-instance-from-within-modeladmin

from django.contrib import admin
from .models import Question, Choice, Species, SurveyQuestion, Survey
from django import forms
# Register your models here.

    
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    model = Question
    inlines = [ChoiceInline]


# class SurveyQuestionForm(forms.ModelForm):
#     class Meta:
#         model = SurveyQuestion
#         fields = '__all__'
#
#     def __init__(self, *args, **kwargs):
#         super(SurveyQuestionForm, self).__init__(*args, **kwargs)
#         self.fields['key_choice'].queryset = Choice.objects.filter(question__exact=self.instance.previous_question)
#
#
# class SurveyQuestionAdmin(admin.ModelAdmin):
#     form = SurveyQuestionForm
#     # def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
#     #     if db_field.name == 'key_choice':
#     #         previous = self.get_obj(request, Question)
#     #         kwargs['queryset'] = Choice.objects.filter(question=previous)
#     #     return super(SurveyQuestionAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
#
#     def get_obj(self, request, model):
#         object_id = request.META['PATH_INFO'].strip('/').split('/')[-1]
#         # ?? object_id = resolve(request.path).args[0]
#         try:
#             object_id = int(object_id)
#         except ValueError:
#             return None
#         return model.objects.get(pk=object_id)


# class QuestionInline(forms.ModelChoiceField):
#     model = Survey.questions.through
#
#
# class SurveyAdmin(admin.ModelAdmin):
#     model = Survey
#     inlines = [QuestionInline,]


class SurveyQuestionInline(admin.TabularInline):
    model = SurveyQuestion
    extra = 3

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        field = super(SurveyQuestionInline, self).formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.name == 'key_choice' and self is not None:
            if request._obj_ is not None:
                field.queryset = field.queryset.filter(question=self.get_obj(request, Question))
            else:
                field.queryset = field.queryset.none()
        return field

    def get_obj(self, request, model):
        object_id = request.META['PATH_INFO'].strip('/').split('/')[-1]
        # ?? object_id = resolve(request.path).args[0]
        try:
            object_id = int(object_id)
        except ValueError:
            return None
        return model.objects.get(pk=object_id)


class SurveyAdmin(admin.ModelAdmin):
    model = Survey
    inlines = [SurveyQuestionInline,]

    def get_form(self, request, obj=None, **kwargs):
        request._obj_ = obj
        return super(SurveyAdmin, self).get_form(request, obj, **kwargs)


admin.site.register(Question, QuestionAdmin)
#admin.site.register(Survey)
admin.site.register(Species)
# admin.site.register(SurveyQuestion, SurveyQuestionAdmin)
admin.site.register(Survey, SurveyAdmin)

