from django.urls import path
from . import views
urlpatterns = [
    path('get_members',views.GetMemberInfo.as_view()),
    path('get_count',views.Get_Count.as_view()),
    path('search_member',views.search_employee),
    path('add_member',views.add_member),
    path('update_member',views.UpdateMemberInfo.as_view()),
    path('get_recent_data',views.MostRecentDataView.as_view()),
    path('get_dependent_data',views.GetMemberAndDependentsView.as_view()),
    path('get_daily_count',views.GetMemberCountView.as_view()),
    path('get_claims',views.GetTotalClaimsDataView.as_view()),
    path('get_claim_no_data',views.GetClaimsDataUsingClaimNoView.as_view()),
    path('get_claims_using_ssn',views.GetClaimsDataView),
]
