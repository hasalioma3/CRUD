from django.urls import path
from .views import  emp, show,edit,update,destroy
app_name ='employee'

urlpatterns = [
    path('', show, name='show'),
    path('emp', emp, name='emp'),
    path('edit/<int:id>', edit, name='edit'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', destroy, name='delete'),
]
