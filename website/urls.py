from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    # path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
    path('detail/<int:pk>',views.detail,name='detail'),
    path('delete_detail/<int:pk>',views.delete_detail,name='delete_detail'),
    path('add_detail/',views.add_detail,name='add_detail'),
    path('update_detail/<int:pk>',views.update_detail,name='update_detail'),

    
]