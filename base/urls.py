from django.urls import path , include 
from . import views


urlpatterns = [
                path("", views.home , name = "Home"),
                path("certification/" , views.certification , name = "Certifications"),
                path("projects/" , views.projects , name= "Projects"),
                path("about/",views.about , name = "About"),
                path('contact/',views.contact , name="Contact"),
]