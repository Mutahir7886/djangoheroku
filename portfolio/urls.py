"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from resume import views

app_name='resume'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage', views.IndexView1.as_view(), name='logger'),
    path('resume/<int:pk>/view', views.DetailView1.as_view(), name='example'),
    path('resume/', views.IndexView.as_view(), name='Main_page'),
    path('resume/<int:pk>', views.DetailView.as_view(), name='resume_detail'),
    path('resume/bio_data', views.Resume_List.as_view()),
    path('resume/<int:id>/bio_data/', views.Resumelist_edit.as_view()),
    path('resume/education', views.Edu_List.as_view()),
    path('resume/<int:id>/education', views.Edu_ListInd.as_view()),
    #path('resume/<int:id>/education', views.Edu_List_Ind.as_view()),
    path('resume/<int:id>/education/edit', views.Edu_ListInd_EDIT.as_view()),
    #path('resume/<int:id>/education/update', views.Edu_List_Ind_EDIT.as_view()),
    path('resume/<int:id>/experience/update', views.Exp_ListInd_EDIT.as_view()),
    path('resume/<int:id>/project/update', views.Prj_ListInd_EDIT.as_view()),
    path('resume/<int:id>/experience', views.Exp_ListInd.as_view()),
    path('resume/<int:id>/project', views.Prj_ListInd.as_view()),
    path('resume/experience', views.Exp_List.as_view()),
    path('resume/projects', views.Prj_List.as_view()),
    path('resume/<int:id>/education/update/patch', views.Edu_ListPATCHEDIT.as_view()),


]
