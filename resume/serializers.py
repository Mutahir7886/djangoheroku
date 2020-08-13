from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Bio_data, Education, Experience,Project
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.response import Response
from rest_framework import  status

class Biodata_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Bio_data
        fields = ('id', 'name', 'contact', 'email', 'Address',)


# class Edu_Serializer(serializers.ModelSerializer):
#     id=serializers.IntegerField()
#     class Meta:
#         model = Education
#         fields = ("id",'Institute_name','Marks_GPA', 'Degree', 'Bio_edu')
#         read_only_fields = ('Bio_edu',)
#
#
#     def create(self, validated_data):
#
#         person_data=validated_data.pop('Bio_edu')
#         bio= Bio_data.objects.get(id=person_data.id)
#         instance=Education.objects.create(**validated_data, Bio_edu=bio)
#         return instance
#
#
#
#     def update(self, instance, validated_data):
#
#         person_data = validated_data.pop('Bio_edu')
#         instance.Institute_name = validated_data.get('Institute_name', instance.Institute_name)
#         instance.Marks_GPA = validated_data.get('Marks_GPA', instance.Marks_GPA)
#         instance.Degree = validated_data.get('Degree', instance.Degree)
#         instance.save()
#         return instance
#
#
#         # educat_id = validated_data.get("id")
#         # for item in instance:
#         #     if item.id == educat_id:
#         #      item.Institute_name = validated_data.get('Institute_name', item.Institute_name)
#         #      item.Marks_GPA = validated_data.get('Marks_GPA', item.Marks_GPA)
#         #      item.Degree = validated_data.get('Degree', item.Degree)
#         #      item.save()
#         #     else:
#         #         continue
#         #     return item

class Edu_LIST_Serializer(serializers.ListSerializer):


    def create(self, validated_data):
        single_item=validated_data[0]
        person_data=single_item.get('Bio_edu')
        #print(person_data)
        bio = Bio_data.objects.get(name=person_data)
        list=[]
        #print(validated_data)
        for item in validated_data:
            #print(item)
            item.pop('Bio_edu')
            #print(item)
            list.append(Education.objects.create(**item,Bio_edu=bio))
            #print(1)
        return list


    def update(self, instance, validated_data):

        print(validated_data)
        print(instance)
        education_obj = list(instance)
        print(education_obj)


        for item in validated_data:
            education = education_obj.pop(0)
            print(education)
            print(item)
            education.Institute_name = item.get('Institute_name', education.Institute_name)
            education.Marks_GPA = item.get('Marks_GPA', education.Marks_GPA)
            education.Degree = item.get('Degree', education.Degree)
            print(education.Institute_name)
            education.save()
        return instance



class Edu_Serializer(serializers.Serializer):

    id = serializers.IntegerField()
    Bio_edu = serializers.CharField()
    #Bio_edu = Biodata_Serializer(many=True)
    Institute_name = serializers.CharField(max_length=200)
    Marks_GPA = serializers.CharField(max_length=200)
    Degree = serializers.CharField(max_length=200)

    class Meta:
         list_serializer_class=Edu_LIST_Serializer






class Exp_Serializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Experience
        fields = ("id",'company_name', 'job_title', 'duration','description','Bio_exp')


    def create(self, validated_data):
        person_data=validated_data.pop('Bio_exp')
        bio= Bio_data.objects.get(id=person_data.id)
        instance=Experience.objects.create(**validated_data, Bio_exp=bio)
        return instance

    def update(self, instance, validated_data):
        person_data = validated_data.pop('Bio_exp')
        instance = Experience.objects.filter(Bio_exp=person_data.id)
        exp_id = validated_data.get("id")

        for item in instance:
            if item.id == exp_id:
                item.company_name = validated_data.get('company_name', item.company_name)
                item.job_title = validated_data.get('job_title', item.job_title)
                item.duration = validated_data.get('duration', item.duration)
                item.description = validated_data.get('description', item.description)
                item.save()
            else:
                continue
            return item


class Prj_Serializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Project
        fields = ("id",'name', 'prjct_description', 'Bio_prjct')

    def create(self, validated_data):
        person_data=validated_data.pop('Bio_prjct')
        bio= Bio_data.objects.get(id=person_data.id)
        instance=Project.objects.create(**validated_data, Bio_prjct=bio)
        return instance
    def update(self, instance, validated_data):
        person_data = validated_data.pop('Bio_prjct')
        instance = Project.objects.filter(Bio_prjct=person_data.id)
        prj_id = validated_data.get("id")

        for item in instance:
            if item.id == prj_id:
                item.name = validated_data.get('name', item.name)
                item.prjct_description = validated_data.get('prjct_description', item.prjct_description)
                item.save()
            else:
                continue
            return item




class Resume_Serializer(serializers.ModelSerializer):
    education = Edu_Serializer(many=True)
    experience = Exp_Serializer(many=True)
    project = Prj_Serializer(many=True)

    class Meta:
        model = Bio_data
        fields = ('id',  'name','contact','email','Address','education','experience','project')
        validators=[ UniqueTogetherValidator (queryset=Bio_data.objects.all(),fields=['name','email'],
                                              message="Name and email already exist")]

    def create(self, validated_data):
        #try:
         education = validated_data.pop('education')
         experience = validated_data.pop('experience')
         project=validated_data.pop('project')
         bio = Bio_data.objects.create(**validated_data)
         for item in education:
            Education.objects.create(**item, Bio_edu=bio)
         for item in experience:
            Experience.objects.create(**item, Bio_exp=bio)
         for item in project:
            Project.objects.create(**item, Bio_prjct=bio)
         return bio

        ##   ValidationError

    def update(self, instance, validated_data):
        education_data = validated_data.pop('education')
        experience_data = validated_data.pop('experience')
        project_data = validated_data.pop('project')

        education_obj = (instance.education).all()
        education_obj = list(education_obj)

        experience_obj = (instance.experience).all() 
        experience_obj = list(experience_obj)

        project_obj = (instance.project).all()
        project_obj = list(project_obj)

        instance.name = validated_data.get('name', instance.name)
        instance.contact = validated_data.get('contact', instance.contact)
        instance.email = validated_data.get('email', instance.email)
        instance.Address = validated_data.get('Address', instance.Address)
        instance.save()

        for item in education_data:
            education = education_obj.pop(0)
            education.Institute_name = item.get('Institute_name', education.Institute_name)
            education.Marks_GPA = item.get('Marks_GPA', education.Marks_GPA)
            education.Degree = item.get('Degree', education.Degree)
            education.save()

        for item in experience_data:
            experience = experience_obj.pop(0)
            experience.job_title = item.get('job_title', experience.job_title)
            experience.company_name = item.get('company_name', experience.company_name)
            experience.duration = item.get('duration', experience.duration)
            experience.description = item.get('description', experience.description)
            experience.save()
        for item in project_data:
            project = project_obj.pop(0)
            project.name = item.get('name', project.name)
            project.prjct_description = item.get('prjct_description', project.prjct_description)
            project.save()

        return instance

    def validate(self, attrs):

       raise ValidationError('RESUME WITH SAME NAME AND EMAIL ALREADY ENTERED')



class Education_Serializer(serializers.Serializer):
    education=Edu_Serializer(many=True)
    id=serializers.IntegerField()
    class Meta:
        model = Bio_data
        fields = ("id",'education')

    def create(self, validated_data):

        person_id=validated_data.get("id")
        edu=validated_data.pop('education')
        bio=Bio_data.objects.get(id=person_id)
        for item in edu:
            Education.objects.create(**item,Bio_edu=bio)
        return  bio

    def update(self, instance, validated_data):
        print(validated_data)
        education_data = validated_data.pop('education')
        print(education_data)
        education_obj = (instance.education).all()
        print(education_obj)
        education_obj = list(education_obj)
        print(education_obj)

        for item in education_data:
            education = education_obj.pop(0)
            education.Institute_name = item.get('Institute_name', education.Institute_name)
            education.Marks_GPA = item.get('Marks_GPA', education.Marks_GPA)
            education.Degree = item.get('Degree', education.Degree)
            education.save()
        return instance

