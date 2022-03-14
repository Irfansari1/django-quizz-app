from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Quizz API",
      default_version='v1',
      description="Quizz API",
      terms_of_service="#",
      contact=openapi.Contact(email="irfan@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [

    # setup
    path("admin/", admin.site.urls),
    path(
        "swagger(<format>\.json|\.yaml)",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc",
         cache_timeout=0), name="schema-redoc"),
    path("__debug__/", include("debug_toolbar.urls")),

    # apps urls
    path("users/", include("users.urls")),
    path("quizapp/", include("quizapp.urls")),
]