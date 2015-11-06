from django.db import models

# Create your models here.
class Question(models.Model):
    """ Question model. """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
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
    
class Survey(models.Model):
    """ Survey model. """
    title = models.CharField(max_length=200, default='')
    # Since a survey contains many different questions, and a question
    # can be belong to many different survery, ManyToManyField is
    # needed in this case 
    questions = models.ManyToManyField(Question, related_name='surveys')
    
    def __str__(self):
        """
        In order for django admin to display the title instead of 
        'Survey object', this function must be overload to return
        the title. for python 2x, overload '__unicode__',
        python 3x -> '__str__'
        """
        return self.title