from django.urls import path

from api.views.whatsapp import whatsapp_health, whatsapp_webhook

urlpatterns = [
    path('whatsapp/webhook', whatsapp_webhook, name='whatsapp_webhook'),
    path('whatsapp/health', whatsapp_health, name='whatsapp_health'),
]

