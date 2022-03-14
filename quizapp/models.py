from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    CAT_CHOICES = [
        ('AWS','AWS'),
        ('Frontend','Frontend'),
        ('Backend','Backend'),
    ]
    name = models.CharField(max_length=15, choices=CAT_CHOICES, default='Frontend')
    
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name




class Quiz(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="quizzes")
    title = models.CharField(max_length = 30)
    createDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Quizzes"

    def __str__(self):
        return f'{self.category}-{self.title}'



class Question(models.Model):

    DIFF_CHOICES = [
        ('Easy','Easy'),
        ('Medium','Medium'),
        ('Hard','Hard'),
    ]

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    title = models.TextField(max_length = 100)
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)
    difficulty = models.CharField(max_length=6, choices=DIFF_CHOICES, default='Easy')
    
    

    def __str__(self):
        return f'{self.quiz}-{self.title}'



class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    answer_text = models.CharField(max_length=50)
    is_correct = models.BooleanField(default=False)
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f'{self.question}-{self.answer_text}'















