from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=""),

    path('Home', views.home,name="Home"),

    path('register', views.register, name="register"),

    path('my-login', views.my_login, name="my-login"),

    path('logout', views.logout, name="logout"),

    path('dashboard', views.dashboard, name="dashboard"),

    path('create-record', views.create_record, name="create-record"),

    path('santa', views.santa, name="santa"),

    path('update-record', views.update_record, name="update-record"),

    path('record/<int:pk>', views.singular_record, name="record"),

    path('delete-record/<int:pk>', views.delete_record, name="delete_reocrd"),
]