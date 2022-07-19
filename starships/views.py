from django.shortcuts import render, reverse
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Starship

class IndexView(TemplateView):
    template_name = 'starships/index.html'

class StarshipDetailView(DetailView):
    model = Starship
    template_name = 'starships/detail.html'

class CreateStarshipView(CreateView):
    template_name = 'starships/create.html'
    model = Starship
    fields = ['name', 'registry']
    
    def get_success_url(self):
        return reverse('starships:index')

class UpdateStarshipView(UpdateView):
    template_name = 'starships/update.html'
    model = Starship
    fields = ['name', 'registry']

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('starships:view-starship', kwargs={'pk': pk})

class DeleteStarshipView(DeleteView):
    template_name = 'starships/confirm_delete.html'
    model = Starship

    def get_success_url(self):
        return reverse('starships:index')

class StarshipLiewView(ListView):
    template_name = 'starships/list.html'
    model = Starship