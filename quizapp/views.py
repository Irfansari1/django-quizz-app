from django.shortcuts import render
from rest_framework import generics
from quizapp.models import Category, Quiz, Question
from quizapp.serializers import CategorySerializer, QuizSerializer, QuestionSerializer
from .pagination import CursorPagi, PageNumPagi
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

class QuizList (generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class QuizRead (generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return Quiz.objects.filter(category__name=category)

class QuestionRead(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    # pagination_class = PageNumPagi
    pagination_class = CursorPagi
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['difficulty']
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        quiz = self.kwargs['quiz'].capitalize()
        return Question.objects.filter(quiz__title=quiz)