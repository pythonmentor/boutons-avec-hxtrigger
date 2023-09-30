from django.urls import path
from .views import home_view, htmx_select_button, htmx_unselect_button

app_name = "pages"

urlpatterns = [
    path("", home_view, name="home"),
    path(
        "htmx/button/select/<int:position>/",
        htmx_select_button,
        name="button-select",
    ),
    path(
        "htmx/button/unselect/<int:position>/",
        htmx_unselect_button,
        name="button-unselect",
    ),
]
