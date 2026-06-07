from django.urls import path
from .views import SearchView, UsageSummaryView

urlpatterns = [
    path(
        "query/",
        SearchView.as_view()
    ),

    path(
        "admin/usage-summary/",
        UsageSummaryView.as_view()
    ),
]