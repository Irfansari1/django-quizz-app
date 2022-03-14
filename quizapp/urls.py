from django.urls import include, path
from quizapp.views import QuizList, QuizRead, QuestionRead

urlpatterns = [
    path('', QuizList.as_view(), name="quiz_list"),
    path("<category>/", QuizRead.as_view(), name="quiz_read"),
    path("<category>/<quiz>", QuestionRead.as_view(), name="question_read")
]