from django.views.generic import View
from django.shortcuts import render
from home.models import University
from home.mixins import SidebarUnies

class HomeView(SidebarUnies, View):

    def get(self, request, *args, **kwargs):

        context = {
            'universities': self.get_unies()
        }
        return render(request, 'index.html', context)
