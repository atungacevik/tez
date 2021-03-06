from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import University, Department, DepName, Year
from home.mixins import SidebarUnies


class UniversityPageView(SidebarUnies, View):

    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        obj = get_object_or_404(University, pk=pk)

        q1 = Year.objects.order_by('-min_point').filter(department__university__name__icontains=obj.name, year='2018')
        q2 = Year.objects.order_by('-min_point').filter(department__university__name__icontains=obj.name, year='2017')
        q3 = Year.objects.order_by('-min_point').filter(department__university__name__icontains=obj.name, year='2016')
        q4 = Year.objects.order_by('-min_point').filter(department__university__name__icontains=obj.name, year='2015')

        context={}
        context['department'] = obj
        context['universities'] = self.get_unies()
        if q1 is not None:
            context['uniresults2018'] = q1

        if q2 is not None:
            context['uniresults2017'] = q2

        if q3 is not None:
            context['uniresults2016'] = q3

        if q4 is not None:
            context['uniresults2015'] = q4

        return render(request, 'uniPage.html', context)


class DepartmentPageView(SidebarUnies, View):

    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        obj = get_object_or_404(DepName, pk=pk)
        q1 = Year.objects.order_by('-min_point').filter(department__dep_name__icontains=obj.department_name, year='2018')
        q2 = Year.objects.order_by('-min_point').filter(department__dep_name__icontains=obj.department_name, year='2017')
        q3 = Year.objects.order_by('-min_point').filter(department__dep_name__icontains=obj.department_name, year='2016')
        q4 = Year.objects.order_by('-min_point').filter(department__dep_name__icontains=obj.department_name, year='2015')

        context={}

        context['department'] = obj

        context['universities'] = self.get_unies()

        if q1 is not None:
            context['departments2018'] = q1

        if q2 is not None:
            context['departments2017'] = q2

        if q3 is not None:
            context['departments2016'] = q3

        if q4 is not None:
            context['departments2015'] = q4

        print(Year.objects.filter(department__dep_name__icontains='Yazılım Mühendisliği'))
        # context = {
        #     'department': obj,
        #     'universities': self.get_unies(),
        #
        #
        #     }
        return render(request, 'depPage.html', context)