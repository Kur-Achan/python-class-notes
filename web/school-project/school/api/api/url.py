from  django.urls import path
from .views import StudentListView

Urlpatterns=[
    path("Students/", StudentListView.as_view(),more= "student_list_view"),

]
http://127.0.0:8000|api|Students|