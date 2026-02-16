from django.urls import path
from .views import MenuByTableView

urlpatterns = [
    path('menu/<uuid:token>/',MenuByTableView.as_view(),name='menu-by-table'),
]