import requests

response = requests.get('https://httpbin.org/')
for line in response.iter_lines():
    print(line)

    INSTALLED_APPS  =  ( 
    ... , 
    "django_stripe" , 
)
from django.urls import include, path

urlpatterns = [
    # Assuming we're at the root, this will make the webhook
    # available at /stripe/webhook/
    path("stripe/", include("django_stripe.urls", namespace="stripe"))
]
STRIPE_WEBHOOK_SECRET = "whsec_0DoBceBjS0jjm7aQj459FXiFSluJEBxt"