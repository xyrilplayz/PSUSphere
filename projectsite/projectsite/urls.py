"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from studentorg.views import (HomePageView, 
OrganizationList, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView, 
OrgMemberListView, OrgMemberCreateView, OrgMemberUpdateView, OrgMemberDeleteView,
StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView,
CollegeListView, CollegeCreateView, CollegeUpdateView, CollegeDeleteView,
ProgramListView, ProgramCreateView, ProgramUpdateView, ProgramDeleteView, 
PieCountByProgram, OrgMembersCountByOrg, TopCollegesByStudentCount, CommonLastName, OrgCountByColleges)
from studentorg import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.HomePageView.as_view(), name= 'home'),
    path('organization_list', views.OrganizationList.as_view(), name= 'organization-list'),
    path('organization_list/add', OrganizationCreateView.as_view(), name = 'organization-add'),
    path('organization_list/<pk>', OrganizationUpdateView.as_view(), name = 'organization-update'),
    path('organization_list/<pk>/delete', OrganizationDeleteView.as_view(), name = 'organization-delete'),

    path('org_member_list', OrgMemberListView.as_view(), name='org-member-list'),
    path('org_member_list/add', OrgMemberCreateView.as_view(), name='org-member-add'),
    path('org_member_list/<pk>', OrgMemberUpdateView.as_view(), name='org-member-update'),
    path('org_member_list/<pk>/delete', OrgMemberDeleteView.as_view(), name='org-member-delete'),

    path('student_list', StudentListView.as_view(), name='student-list'),
    path('student_list/add', StudentCreateView.as_view(), name='student-add'),
    path('student_list/<pk>', StudentUpdateView.as_view(), name='student-update'),
    path('student_list/<pk>/delete', StudentDeleteView.as_view(), name='student-delete'),

    path('college_list', CollegeListView.as_view(), name='college-list'),
    path('college_list/add', CollegeCreateView.as_view(), name='college-add'),
    path('college_list/<pk>', CollegeUpdateView.as_view(), name='college-update'),
    path('college_list/<pk>/delete', CollegeDeleteView.as_view(), name='college-delete'),

    path('program_list', ProgramListView.as_view(), name='program-list'),
    path('program_list/add', ProgramCreateView.as_view(), name='program-add'),
    path('program_list/<pk>', ProgramUpdateView.as_view(), name='program-update'),
    path('program_list/<pk>/delete', ProgramDeleteView.as_view(), name='program-delete'),

    re_path(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

    path('pieCountByProgramChart/', views.PieCountByProgram, name='chart'),
    path('orgMembersCountByOrg/', views.OrgMembersCountByOrg, name='chart'),
    path('topCollegesByStudentCount/', views.TopCollegesByStudentCount, name='chart'),
    path('commonLastNames/', views.CommonLastName, name='chart'),
    path('orgCountByCollege/', views.OrgCountByColleges, name='chart'),
]