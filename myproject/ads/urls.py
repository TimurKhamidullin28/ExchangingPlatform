from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    AdCreateView,
    AdsListView,
    AdUpdateView,
    AdDeleteView,
    AdViewSet,
    ExchangeCreateView,
    ExchangesListView,
    ExchangeUpdateView,
    ExchangeViewSet,
)

app_name = "ads"

routers = DefaultRouter()
routers.register("ads", AdViewSet)
routers.register("exchanges", ExchangeViewSet)

urlpatterns = [
    path("list/", AdsListView.as_view(), name="ads_list"),
    path("create/", AdCreateView.as_view(), name="ad_create"),
    path("<int:pk>/update/", AdUpdateView.as_view(), name="ad_update"),
    path("<int:pk>/delete/", AdDeleteView.as_view(), name="ad_delete"),
    path("api/", include(routers.urls)),
    path("exchange/create/", ExchangeCreateView.as_view(), name="exchange_create"),
    path("exchanges/list/", ExchangesListView.as_view(), name="exchanges_list"),
    path("exchange/<int:pk>/update/", ExchangeUpdateView.as_view(), name="exchange_update"),
]
