from django.shortcuts import render
from .models import University
from django.views.generic import ListView
# Create your views here.
class UniverListView(ListView):
    model = University
    context_object_name = 'universities'
    template_name = 'list_univers.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category', '')
        if category:
            queryset = queryset.filter(category=category)
        return queryset

    def get_context_data(self, **kwargs):   
        context = super().get_context_data(**kwargs)
        context["top_vnz"] = University.objects.order_by('top')[:10]
        return context