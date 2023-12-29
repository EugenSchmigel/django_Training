from django.urls import path
from django.views.decorators.cache import cache_page

from main.apps import MainConfig
from main.views import index, contact, StudentDetailView, StudentCreateView, StudentListView, StudentUpdateView, \
    StudentDeleteView, toggle_activity

app_name = MainConfig.name

urlpatterns = [
    path('', StudentListView.as_view(), name='index'),
    # path('', cache_page(60) (StudentListView.as_view()), name='index'),
    path('contact/', contact, name='contact'),
    path('view/<int:pk>/', StudentDetailView.as_view(), name='view_student'),
    path('create/', StudentCreateView.as_view(), name='create_student'),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='update_student'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='delete_student'),
    path('activity/<int:pk>/', toggle_activity, name='toggle_activity'),

]
