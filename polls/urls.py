from django.urls import path

from . import views


## add the app_name so that it can be used in the templates
app_name = 'polls'

urlpatterns = [
    path('',views.index,name="index"),
    path('<int:pk>/',views.detail, name = "detail"),
    path('<int:pk>/results/',views.results,name = "results"),
    path("<int:pk>/vote/",views.vote, name = "vote"),
]