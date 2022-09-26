# App URLs
from django.urls import path

from departments_app.departments.views import show_departments, show_not_found

urlpatterns = (
    path('', show_departments, name='show department'),
    path('not-found-slivi-za-smet/', show_not_found, name='not found'),
    path('<department_id>/', show_departments, name='show department details with string'),
    path('int/<int:department_id>/', show_departments, name='show department details'),
)
