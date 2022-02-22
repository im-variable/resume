from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class PersonalInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_personal_info')
    nickname = models.CharField(max_length=255)
    nickname_active = models.BooleanField(default=True)
    profession = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    about = models.TextField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


HIGH_SCHOOL = 'high school'
INTERMEDIATE = 'intermediate'
BACHELOR = 'bachelor' 
DIPLOMA = 'diploma'
MASTER = 'master'
CERTIFICATE = 'certification'


EDUCATION_TYPE = [
    (HIGH_SCHOOL,'High School'),
    (INTERMEDIATE,'Intermediate'),
    (BACHELOR,'Bachelor'),
    (DIPLOMA,'Diploma'),
    (MASTER,'Master'),
    (CERTIFICATE,'Certification'),
]

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_education')
    education_type = models.CharField(choices=EDUCATION_TYPE ,default=HIGH_SCHOOL, max_length=20)
    education_detail = models.TextField()
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    university = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username}_{self.education_type}'
    

class WorkExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_work_exp')
    company = models.CharField(max_length=255)
    start_year = models.DateField()
    end_year = models.DateField(blank=True, null=True)
    is_present = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username}_{self.company}'


class Project(models.Model):
    work_experience = models.ForeignKey(WorkExperience, on_delete=models.CASCADE, related_name='work_exp_project')
    project_name = models.CharField(max_length=255)
    languages = models.CharField(max_length=255)
    project_logo = models.CharField(max_length=255, default='https://pic.onlinewebfonts.com/svg/img_98811.png', null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.work_experience}_{self.project_name}'

FACEBOOK = 'facebook'
TWITTER = 'twitter' 
WHATSAPP = 'whatsapp' 
INSTAGRAM = 'instagram' 
LINKEDIN = 'linkedin' 
GITHUB = 'github'
EMAIL = 'envelope' 


CONTACT_TYPE = [
    (FACEBOOK, 'Facebook'),
    (TWITTER, 'Twitter'),
    (WHATSAPP, 'Whatsapp'),
    (INSTAGRAM, 'Instagram'),
    (LINKEDIN, 'Linkedin'),
    (GITHUB, 'Github'),
    (EMAIL, 'Email'),

]


class ContactInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_contact_info')
    contact_type = models.CharField(choices=CONTACT_TYPE,default=WHATSAPP, max_length=20)
    contact_detail = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.user.username}_{self.contact_type}'

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_skill')
    skill_name =  models.CharField(max_length=20)
    skill_rate = models.IntegerField(default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
    
    def __str__(self):
        return f'{self.user.username}_{self.skill_name}'