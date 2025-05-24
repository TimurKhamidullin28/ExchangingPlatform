from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.shortcuts import reverse
from django.urls import reverse_lazy
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Ad, ExchangeProposal
from .forms import AdForm
from .serializers import AdSerializer, ExchangeSerializer


class AdsListView(ListView):
    """Отображение списка всех объявлений"""

    template_name = "ads/ads-list.html"
    queryset = Ad.objects.select_related("user").all()


class AdCreateView(CreateView):
    """Создание объявления"""

    model = Ad
    fields = "user", "title", "description", "image_url", "category", "condition"
    success_url = reverse_lazy("ads:ads_list")


class AdUpdateView(UpdateView):
    """Редактирование объявления"""

    model = Ad
    template_name_suffix = "_update_form"
    form_class = AdForm

    def get_success_url(self):
        return reverse("ads:ads_list")

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            return HttpResponse("You are not allowed to update this Ad", status=401)
        return super(AdUpdateView, self).dispatch(request, *args, **kwargs)


class AdDeleteView(DeleteView):
    """Удаление объявления"""

    model = Ad
    success_url = reverse_lazy("ads:ads_list")


class AdViewSet(ModelViewSet):
    """Реализация поиска и фильтрации объявлений"""

    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["title", "description"]
    filterset_fields = [
        "category",
        "condition",
    ]


class ExchangeCreateView(CreateView):
    """Создание предложения обмена"""

    model = ExchangeProposal
    fields = "ad_sender", "ad_receiver", "comment"
    success_url = reverse_lazy("ads:exchanges_list")


class ExchangeUpdateView(UpdateView):
    """Обновление предложения"""

    model = ExchangeProposal
    template_name_suffix = "_update_form"
    fields = ("status",)

    def get_success_url(self):
        return reverse("ads:exchanges_list")


class ExchangesListView(ListView):
    """Просмотр списка всех предложений"""

    template_name = "ads/exchange-list.html"
    queryset = ExchangeProposal.objects.select_related("ad_sender", "ad_receiver").all()


class ExchangeViewSet(ModelViewSet):
    """Реализация фильтрации предложений"""

    queryset = ExchangeProposal.objects.all()
    serializer_class = ExchangeSerializer
    filterset_fields = [
        "ad_sender",
        "ad_receiver",
        "status",
    ]
