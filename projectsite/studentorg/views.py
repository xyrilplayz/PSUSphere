from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization, OrgMember, Student, College, Program
from studentorg.forms import OrganizationForm,  OrgMemberForm, StudentForm, CollegeForm, ProgramForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Q
import calendar
import re
@method_decorator(login_required, name='dispatch')
class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"

@method_decorator(login_required, name='dispatch')
class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = "org_list.html"
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super(OrganizationList, self).get_queryset(*args, **kwargs)
        if self.request.GET.get('q'):
            query = self.request.GET.get('q')
            qs = qs.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )
        return qs

@method_decorator(login_required, name='dispatch')
class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_add.html'
    success_url = reverse_lazy('organization-list')
    
@method_decorator(login_required, name='dispatch')
class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_edit.html'
    success_url = reverse_lazy('organization-list')

@method_decorator(login_required, name='dispatch')
class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')

@method_decorator(login_required, name='dispatch')
class OrgMemberListView(ListView):
    model = OrgMember
    context_object_name = 'org_member'
    template_name = "org_member_list.html"
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        query = self.request.GET.get('q')

        if query:
            filters = (
                Q(organization__name__icontains=query) | 
                Q(student__firstname__icontains=query) | 
                Q(student__lastname__icontains=query) | 
                Q(student__middlename__icontains=query)
            )

            if query.isdigit() and len(query) == 4:  
                filters |= Q(date_joined__year=int(query))

            elif query.capitalize() in calendar.month_name[1:]:  
                month_number = list(calendar.month_name).index(query.capitalize())
                filters |= Q(date_joined__month=month_number)

            else:  
                match = re.match(r'(\w+) (\d{4})', query)  
                if match:
                    month_str, year_str = match.groups()
                    if month_str.capitalize() in calendar.month_name[1:]:
                        month_number = list(calendar.month_name).index(month_str.capitalize())
                        filters |= Q(date_joined__month=month_number, date_joined__year=int(year_str))

            qs = qs.filter(filters)
        return qs
@method_decorator(login_required, name='dispatch')
class OrgMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'org_member_add.html'
    success_url = reverse_lazy('org-member-list')

@method_decorator(login_required, name='dispatch')
class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'org_member_edit.html'
    success_url = reverse_lazy('org-member-list')

@method_decorator(login_required, name='dispatch')
class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = 'org_member_del.html'
    success_url = reverse_lazy('org-member-list')

@method_decorator(login_required, name='dispatch')
class StudentListView(ListView):
    model = Student
    context_object_name = 'student'
    template_name = "student_list.html"
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super(StudentListView, self).get_queryset(*args, **kwargs)
        if self.request.GET.get('q'):
            query = self.request.GET.get('q')
            qs = qs.filter(
                Q(student_id__icontains=query) | 
                Q(firstname__icontains=query) | 
                Q(lastname__icontains=query) | 
                Q(middlename__icontains=query) |
                Q(program__prog_name__icontains=query)
            )
        return qs

@method_decorator(login_required, name='dispatch')
class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_add.html'
    success_url = reverse_lazy('student-list')

@method_decorator(login_required, name='dispatch')
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_edit.html'
    success_url = reverse_lazy('student-list')

@method_decorator(login_required, name='dispatch')
class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_del.html'
    success_url = reverse_lazy('student-list')

@method_decorator(login_required, name='dispatch')
class CollegeListView(ListView):
    model = College
    context_object_name = 'college'
    template_name = "college_list.html"
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super(CollegeListView, self).get_queryset(*args, **kwargs)
        if self.request.GET.get('q'):
            query = self.request.GET.get('q')
            qs = qs.filter(
                Q(college_name__icontains=query)
            )
        return qs
@method_decorator(login_required, name='dispatch')
class CollegeCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_add.html'
    success_url = reverse_lazy('college-list')

@method_decorator(login_required, name='dispatch')
class CollegeUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_edit.html'
    success_url = reverse_lazy('college-list')

@method_decorator(login_required, name='dispatch')
class CollegeDeleteView(DeleteView):
    model = College
    template_name = 'college_del.html'
    success_url = reverse_lazy('college-list')

@method_decorator(login_required, name='dispatch')
class ProgramListView(ListView):
    model = Program
    context_object_name = 'program'
    template_name = "program_list.html"
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super(ProgramListView, self).get_queryset(*args, **kwargs)
        if self.request.GET.get('q'):
            query = self.request.GET.get('q')
            qs = qs.filter(
                Q(prog_name__icontains=query) |
                Q(college__college_name__icontains=query)
            )
        return qs
@method_decorator(login_required, name='dispatch')
class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_add.html'
    success_url = reverse_lazy('program-list')

@method_decorator(login_required, name='dispatch')
class ProgramUpdateView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_edit.html'
    success_url = reverse_lazy('program-list')

@method_decorator(login_required, name='dispatch')
class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'program_del.html'
    success_url = reverse_lazy('program-list')