from django.views import generic
from django.db import IntegrityError

from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth import authenticate
from .models import Bio_data,Education,Experience,Project
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import  status
from .serializers import Resume_Serializer,Edu_Serializer,Exp_Serializer,Prj_Serializer,Education_Serializer


class IndexView(generic.ListView):
    template_name = 'resume/Main_Page.html'
    context_object_name = 'all_resumes'

    def get_queryset(self):
        return Bio_data.objects.all()


class IndexView1(generic.ListView):
    template_name = 'resume/logger.html'
    context_object_name = 'all_resumes'

    def get_queryset(self):
        return Bio_data.objects.all()


class DetailView(generic.DetailView):
    model = Bio_data
    template_name = 'resume/resume_detail.html'


class DetailView1(generic.DetailView):
    model = Bio_data
    template_name = 'resume/example.html'


class Resume_List(APIView):
    def get(self,request):
        ORGI=Bio_data.objects.all()
        serializer=Resume_Serializer(ORGI,context={'request':request},many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = Resume_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Resumelist_edit(APIView):

    def get_object(self, id):
        try:
            product = Bio_data.objects.get(id=id)
        except Bio_data.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def get(self, request, id):

        instance=Bio_data.objects.get(id=id)
        serailizer = Resume_Serializer(instance)
        return Response(serailizer.data)

    def put(self, request, id):

        data = request.data
        instance = Bio_data.objects.get(id=id)
        serializer = Resume_Serializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class Edu_List(APIView):

    def get(self,request):
        ORGI=Education.objects.all()
        serializer=Edu_Serializer(ORGI,context={'request':request},many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = Edu_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Edu_ListInd(APIView):
    def get(self,request,id):

        Education_obj=Education.objects.filter(Bio_edu=id)
        serializer = Edu_Serializer(Education_obj,many=True)
        return Response(serializer.data)

    def post(self,request,id):

        serializer = Edu_Serializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Edu_ListInd_EDIT(APIView):

    def get(self,request,id):

        Education_obj=Education.objects.filter(Bio_edu=id)
        serializer = Edu_Serializer(instance=Education_obj,many=True)
        return Response(serializer.data)

    def put(self, request, id):

        data = request.data
        Education_obj =Education.objects.filter(Bio_edu=id)
        serializer = Edu_Serializer(Education_obj, data=data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def post(self,request,id):

        serializer = Edu_Serializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        data = request.data
        Education_obj =Education.objects.filter(Bio_edu=id)
        serializer = Edu_Serializer(Education_obj, data=data, many=True,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class Edu_ListPATCHEDIT(APIView):


    def patch(self, request, id):
        data = request.data
        Education_obj =Education.objects.filter(Bio_edu=id)
        serializer = Edu_Serializer(Education_obj, data=data, many=True,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)









class Exp_List(APIView):
    def get(self,request):
        ORGI=Experience.objects.all()
        serializer=Exp_Serializer(ORGI,context={'request':request},many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = Exp_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Exp_ListInd(APIView):


    def get(self,request,id):

        Experience_obj=Experience.objects.filter(Bio_exp=id)
        dictionary_Experience=[]
        for item in Experience_obj:
         serializer = Exp_Serializer(item)
         dictionary_Experience.append(serializer.data)
        return Response(dictionary_Experience)

    def post(self,request,id):

        serializer = Exp_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class Exp_ListInd_EDIT(APIView):

    def get(self,request,id):

        Experience_obj=Experience.objects.filter(Bio_exp=id)
        dictionary_Experience=[]
        for item in Experience_obj:
         serializer = Exp_Serializer(item)
         dictionary_Experience.append(serializer.data)
        return Response(dictionary_Experience)

    def put(self, request, id):
        data = request.data
        Experience_obj =Experience.objects.filter(Bio_exp=id)
        serializer = Exp_Serializer(instance=Experience_obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class Edu_List_Ind(APIView):

    def get(self, request, id):
        Education_obj = Bio_data.objects.get(id=id)
        serializer = Education_Serializer(instance=Education_obj)
        return Response(serializer.data)

    def post(self, request, id):
        serializer = Education_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Edu_List_Ind_EDIT(APIView):

    def get(self, request, id):
        Education_obj = Bio_data.objects.get(id=id)
        serializer = Education_Serializer(instance=Education_obj)
        return Response(serializer.data)

    def put(self, request, id):
        data = request.data
        Education_obj = Bio_data.objects.get(id=id)
        serializer = Education_Serializer(instance=Education_obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)




class Prj_List(APIView):
    def get(self,request):
        ORGI=Project.objects.all()
        serializer=Prj_Serializer(ORGI,context={'request':request},many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = Prj_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Prj_ListInd(APIView):


    def get(self,request,id):

        Project_obj=Project.objects.filter(Bio_prjct=id)
        dictionary_Project=[]
        for item in Project_obj:
         serializer = Prj_Serializer(item)
         dictionary_Project.append(serializer.data)
        return Response(dictionary_Project)

    def post(self,request,id):

        serializer = Prj_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Prj_ListInd_EDIT(APIView):

    def get(self,request,id):

        Project_obj=Project.objects.filter(Bio_prjct=id)
        dictionary_Project=[]
        for item in Project_obj:
         serializer = Prj_Serializer(item)
         dictionary_Project.append(serializer.data)
        return Response(dictionary_Project)

    def put(self, request, id):
        data = request.data
        Project_obj =Project.objects.filter(Bio_prjct=id)
        serializer = Prj_Serializer(instance=Project_obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

