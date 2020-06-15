from django.urls import path

from . import views

app_name = 'cal'

urlpatterns = [
    path('',views.loginfunc,name="top"),
    # path('signup/',signupfunc,name='signup'),
    path('login/',views.loginfunc),
    path('cal_list/', views.TOPListView.as_view(), name='cal_list'),
    path('item_list/', views.CalorieListView.as_view(), name='item_list'),
    path('day_create/', views.DayCreateView.as_view(), name='day_create'),
    path('calorie_create/', views.CalorieCreateView.as_view(), name='calorie_create'),
    path('create_done/',views.create_done, name='create_done'),
    # path('new_cal/',views.TOPView, name='new_cal'),
    path('update/<int:pk>',views.TOPUpdateView.as_view(),name='TOP_update'),
    path('update_done/', views.update_done, name='update_done'),
    path('delete/<int:pk>/',views.TOPDeleteView.as_view(),name='TOP_delete'),
    path('delete_done',views.delete_done,name='delete_done')
    ]