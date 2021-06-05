from django.urls import path
from .views.requirements_views import RequirementsListAPiView, RequirementsCreateApiView

from .views.addons_views import AddonsListView, AddonsCreateUpdateDeleteApiView


urlpatterns = [
    path('requirements/', RequirementsListAPiView.as_view()),
    path('requirements/add/', RequirementsCreateApiView.as_view()),
    path('requirements/update/<int:pk>/', RequirementsCreateApiView.as_view()),
    path('requirements/delete/<int:pk>/', RequirementsCreateApiView.as_view()),
    path('addons/', AddonsListView.as_view()),
    path('addons/add/', AddonsCreateUpdateDeleteApiView.as_view()),
    path('addons/<int:pk>/', AddonsCreateUpdateDeleteApiView.as_view()),
]
