from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.reg_view,name='reg-page'),
    path('login/',views.login_view,name='login-page'),
    path('home/',views.home,name='home-page'),
    path('logout/',views.logout,name='logout'),
    path('additem/',views.add_item,name='add-item'),
    path('update/<int:item_id>',views.update_item,name='update-item'),
    path('delete/<str:item_id>',views.delete_item,name='delete-item'),
    path('update/',views.update_data,name='update-data'),
    path('search/',views.search_item,name="search-item")
    ]