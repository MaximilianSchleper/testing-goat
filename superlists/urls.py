from lists import views as list_views
from django.urls import include, path

urlpatterns = [
    path('', list_views.home_page, name="home"),
    path('lists/', include("lists.urls")),
]
