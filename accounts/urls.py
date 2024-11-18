from django.urls import path,include

app_name = "accounts"

urlpatterns =[
    # Including default authentication urls
    path("", include("accounts.urls")),

] 