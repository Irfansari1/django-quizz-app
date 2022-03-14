from rest_framework.pagination import CursorPagination, PageNumberPagination


class PageNumPagi(PageNumberPagination):
    page_size = 1


class CursorPagi(CursorPagination):
    page_size = 2
    ordering = 'difficulty'