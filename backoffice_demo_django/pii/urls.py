from django.urls import path

from backoffice_demo_django.pii.views import (
    pii_detail_view,
)

app_name = "pii"
urlpatterns = [
    path("", view=pii_detail_view, name=""),
]