from django.urls import path
from .views.requirements_views import RequirementsListAPiView, RequirementsCreateApiView
from .views.order_views import OrderCreateView, OrderListAPiView
from .views.quotation_views import QuotationCreateView
from .views.addons_views import AddonsListView, AddonsCreateUpdateDeleteApiView
from .views.instruction_views import InstructionListApiView

urlpatterns = [
    # requirements urls
    path('requirements/', RequirementsListAPiView.as_view()),
    path('requirements/add/', RequirementsCreateApiView.as_view()),
    path('requirements/update/<int:pk>/', RequirementsCreateApiView.as_view()),
    path('requirements/delete/<int:pk>/', RequirementsCreateApiView.as_view()),
    # addons urls
    path('addons/', AddonsListView.as_view()),
    path('addons/add/', AddonsCreateUpdateDeleteApiView.as_view()),
    path('addons/<int:pk>/', AddonsCreateUpdateDeleteApiView.as_view()),
    # order urls
    path('order/', OrderListAPiView.as_view()),
    path('order/create/', OrderCreateView.as_view()),
    # quotation data
    path('quotation/create/', QuotationCreateView.as_view()),
    # instructions
    path('instructions/', InstructionListApiView.as_view()),
]
