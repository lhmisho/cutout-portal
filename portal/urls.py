from django.urls import path
from .views.requirements_views import RequirementsListAPiView
urlpatterns = [
    path('requirements/', RequirementsListAPiView.as_view())
]