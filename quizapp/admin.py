from django.contrib import admin
from .models import Answer, Question, Quiz, Category
from django.contrib.admin import TabularInline, StackedInline, site
from super_inlines.admin import SuperInlineModelAdmin, SuperModelAdmin

# Register your models here.

class AnswerInline(SuperInlineModelAdmin, admin.TabularInline):
    model = Answer
    extra = 4

class QuestionInline(SuperInlineModelAdmin, admin.StackedInline):
    model = Question
    extra = 1
    inlines = (AnswerInline,)

class QuizAdmin(SuperModelAdmin):
    model = Quiz
    inlines = (QuestionInline,)


admin.site.register(Category)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
admin.site.register(Answer)



