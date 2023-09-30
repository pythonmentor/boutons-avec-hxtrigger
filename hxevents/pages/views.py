from django.template.response import TemplateResponse

MAX_SELECTIONS = 2


def home_view(request):
    return TemplateResponse(request, "pages/home.html")


def htmx_select_button(request, position):
    return TemplateResponse(
        request,
        "pages/fragments/selected-button.html",
        {
            "button_text": request.GET.get("button-text"),
            "position": position + 1,
        },
        headers={"HX-Trigger-After-Swap": "watch-button-selected"},
    )


def htmx_unselect_button(request, position):
    template = (
        "pages/fragments/selected-button.html"
        if position < MAX_SELECTIONS
        else "pages/fragments/unselected-button.html"
    )
    position = position + 1 if position < MAX_SELECTIONS else 0
    return TemplateResponse(
        request,
        template,
        {
            "button_text": request.GET.get("button-text"),
            "position": position,
        },
    )
