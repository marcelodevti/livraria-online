from django.urls import path
from . import views

urlpatterns = [
    path('historico-compras/', views.historico_compras, name='historico_compras'),
    path('historico-compras-pdf/', views.exportar_historico_pdf, name='exportar_historico_pdf'),
]
