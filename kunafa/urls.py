from django.urls import path
from . import views

urlpatterns = [
	path('',views.home, name="home"),
	path('menu', views.MenuView.as_view(), name='menu'),
	path('contact-us',views.contact, name="contact"),
	path('about-us',views.about, name="about"),
	path('answer',views.what, name="what"),

]

