from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('fullposts/<int:id>/', views.fullposts, name='fullposts'),
    path('blogs/', views.blogs_posts, name='blogs'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit_post/<int:id>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:id>/', views.delete_post, name='delete_post'),
    path('add_post/', views.add_post, name='add_post'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('changepassword/', views.change_password, name='changepassword'),
]
