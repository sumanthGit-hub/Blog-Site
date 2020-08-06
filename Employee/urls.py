from django.urls import path,include
from Employee import views

app_name='Employee'

urlpatterns=[
    path('list/',views.list,name='list'),
    path('form/',views.form,name='form'),
    path('<int:id>/',views.form,name='update_form'),
    path('delete/<int:id>/',views.delete,name='delete')
]