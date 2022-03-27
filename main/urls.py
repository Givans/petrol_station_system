from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('', views.home, name='home'),
    path('admin_page', views.admin_page, name='admin_page'),
    path('staff', views.staff, name='staff'),
    path('update', views.update, name='update'),
    path('register_staff', views.register_staff, name='register_staff'),
    path('new_category', views.new_category, name='new_category'),
    path('new_sell/<str:username>', views.new_sell, name='new_sell'),
    path('new_update', views.new_update, name='new_update'),
    path('logout', views.logout, name='logout'),
    path('delete_staff/<str:username>', views.delete_staff, name='delete_staff'),
    path('delete_category/<str:category>', views.delete_category, name='delete_category'),
    path('post_about', views.post_about, name='post_about'),
    # path('send_message', views.customer_contact name='send_message'),
]
