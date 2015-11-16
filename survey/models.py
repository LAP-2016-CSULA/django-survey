from django.db import models


# Create your models here.
class Question(models.Model):
    """ Question model. """
    question_text = models.CharField(max_length=200)
    #pub_date = models.DateTimeField('date published', auto_now_add=True, blank=True)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    """ Choice model. """
    # ForeignKey is many-to-one or the other way around
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text


class Species(models.Model):
    """ Species model. For now, store plants info. """
    scientific_name = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    # survey = models.ForeignKey(Survey, null=True, blank=True)

    def __str__(self):
        return self.name


class Survey(models.Model):
    """ Survey with tree structure. """
    title = models.CharField(max_length=100, default='')
    species = models.ForeignKey(Species, null=True, blank=True)

    def __str__(self):
        return self.title


class SurveyQuestion(models.Model):
    """ Question in survey. It is something like a tree.
    Each choice can lead to another question.
    """
    survey = models.ForeignKey(Survey, null=True, blank=True)
    question = models.ForeignKey(Question, related_name='question')
    previous_question = models.ForeignKey(Question, related_name='next_question', null=True, blank=True)
    key_choice = models.ForeignKey(Choice, null=True, blank=True, related_name='survey_question')

    def __str__(self):
        return Question.objects.get(pk=self.question.pk).question_text


# class Survey(models.Model):
#     """ Survey model. """
#     title = models.CharField(max_length=200, default='')
#     # Since a survey contains many different questions, and a question
#     # can be belong to many different survey, ManyToManyField is
#     # needed in this case
#     questions = models.ManyToManyField(Question, related_name='surveys')
#
#     def __str__(self):
#         """
#         In order for django admin to display the title instead of
#         'Survey object', this function must be overload to return
#         the title. for python 2x, overload '__unicode__',
#         python 3x -> '__str__'
#         """
#         return self.title



