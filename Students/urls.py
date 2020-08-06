from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from Students import views

app_name='Students'

urlpatterns=[
    path('upload/',views.upload,name='upload'),
    path('students/',views.student_list,name='student_list'),
    path('students/upload',views.upload_student,name='upload_student'),
    path('students/<int:pk>/',views.delete_student,name='delete_student'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)