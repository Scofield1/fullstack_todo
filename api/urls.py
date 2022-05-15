from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.ListTodo.as_view()),
    path('create', views.CreateTodo.as_view()),
    path('update/<str:pk>', views.UpdateTodo.as_view()),
    path('details/<str:pk>', views.DetailTodo.as_view()),
    path('delete/<str:pk>', views.DeleteTodo.as_view())
]

# urlpatterns = format_suffix_patterns(urlpatterns)