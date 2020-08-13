from django.db import models

class Bio_data(models.Model):

    name= models.CharField(max_length=20)
    contact=models.CharField(max_length=20)
    email = models.CharField(max_length=25)
    Address=models.CharField(max_length=50)

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(
    #             fields=['name','email'],
    #             name='name_email'
    #         ),
    #     ]

    def __str__(self):
        return self.name

    @property
    def education(self):
        return self.education_set.all()

    @property
    def experience(self):
        return self.experience_set.all()

    @property
    def project(self):
        return self.project_set.all()


class Education(models.Model):

    Institute_name=models.CharField(max_length=50)
    Marks_GPA=models.FloatField()
    Degree=models.CharField(max_length=50)
    Bio_edu=models.ForeignKey(Bio_data,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Institute_name) + '-' + self.Degree


class Experience(models.Model):

    company_name=models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    Bio_exp = models.ForeignKey(Bio_data, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.company_name) + '-' + self.job_title


class Project(models.Model):

    name = models.CharField(max_length=50)
    prjct_description = models.CharField(max_length=100)
    Bio_prjct = models.ForeignKey(Bio_data, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


