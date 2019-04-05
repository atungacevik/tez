from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404
from .models import University
from home.mixins import SidebarUnies


class UniversityPageView(SidebarUnies, View):

    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        obj = get_object_or_404(University, pk=pk)
        context = {
            'university': obj,
            'universities': self.get_unies()
        }
        return render(request, 'uniPage.html', context)
