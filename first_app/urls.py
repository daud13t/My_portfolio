from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('about/',views.about.as_view(),name='about1'),
    path('project1/',views.project1.as_view(),name='project1'),
    path('project2/',views.project2.as_view(),name = 'project2'),
    path('sign_up/',views.sign_in_for_project1.as_view(),name = "signin"),
    path("contact/", views.contact_view, name="contact"),

]
