from django.urls import path
from . import views
urlpatterns = [
    path('get_members',views.GetMemberInfo.as_view()),
    path('get_count',views.Get_Count.as_view()),
    path('search_member',views.search_employee),
    path('add_member',views.add_member),
    path('update_member',views.UpdateMemberInfo.as_view())
]