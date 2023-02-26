from django.urls import path

from .views import review, thank_you

urlpatterns = [
    path("",review,name="home"),
    path("thank-you/", thank_you, name='thank-you')
]
