from django.urls import path

from . import views

urlpatterns = [
    path('',views.student_list, name='student_list'),
    path('create/',views.create_student,name='create'),
    path('delete/<int:id>',views.delete_student, name='delete'),
    path('update/<int:id>',views.update_student,name='update'),
    path('register/',views.register, name='register'),
    path('login/',views.user_login, name='login'),
    path('logout/',views.logout_user, name='logout')

]