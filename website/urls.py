# -*- coding: utf-8 -*-
from django.conf.urls import include,url
from website.views import HomeView


urlpatterns = [
    url(r'^$', HomeView.as_view()),
]
