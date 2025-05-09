from django.urls import path
from .views import todoList,todoDetail,todoView,todoLoginView,todoHomeView,todoEdit,todoDelete,todoCreate,logoutfunc
urlpatterns = [
    path('',todoLoginView.as_view(),name="login"),
    path('register/',todoView.as_view(),name="register"),
    path('login/',todoLoginView.as_view(),name="login"),
    path('logout/',logoutfunc,name="logout"),
    path('home/',todoHomeView.as_view(),name="home"),
    path('create/',todoCreate.as_view(),name="create"),
    path('edit/<int:pk>/',todoEdit.as_view(),name="edit_todo"),
    path('delete/<int:pk>/',todoDelete.as_view(),name="delete_todo"),
    path('listview/',todoList.as_view(),name="todoList"),
    path('detailview/<int:pk>/',todoDetail.as_view(),name="todoDetail"),
]
