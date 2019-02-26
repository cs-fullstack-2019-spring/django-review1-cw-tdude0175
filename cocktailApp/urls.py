from django.urls import path
from . import views

urlpatterns = \
    [
        path('', views.index , name ='index'),
        path('details/<int:cocktailID>/', views.details, name ='details'),
        path('home/<str:lastpage>/', views.home, name ='home'),
        path('page2/<str:lastpage>/', views.page2, name ='page2'),
        path('page3/<str:lastpage>/', views.page3 , name ='page3'),
        path('page4/<str:lastpage>/', views.page4 , name ='page4'),
        path('page5/<str:lastpage>/', views.page5 , name ='page5'),
    ]