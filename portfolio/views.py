from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.

def home_page(request, uname='sandeepnegi'):

    user_detail = User.objects.filter(username=uname).first()
    contact_info = ContactInformation.objects.filter(user = user_detail)
    context = {
        "uname": uname,
        "user_detail": user_detail,
        "contact_info": contact_info 
    }
    return render(request, 'portfolio/home.html', context)


def about(request, uname='sandeepnegi'):

    user_detail = User.objects.filter(username=uname).values("first_name", 'last_name').first()
    personal_info = PersonalInformation.objects.filter(user__username=uname).first()
    contact_info = ContactInformation.objects.filter(user__username=uname).filter(Q(contact_type='whatsapp') | Q(contact_type='envelope')).values()
    education_info = Education.objects.filter(user__username=uname).values().order_by('-end_year').first()
    skill_info = Skill.objects.filter(user__username=uname).values()
    project_info = Project.objects.filter(work_experience__user__username=uname)

    context = {
        "user_detail": user_detail,
        "uname": uname,
        "personal_info": personal_info,
        "contact_info": contact_info,
        "education_info": education_info,
        "skill_info": skill_info,
        "project_info": project_info,
        "product_count": len(project_info)
    }
    print(context)
    return render(request, 'portfolio/about.html', context)



def resume(request, uname='sandeepnegi'):

    user_detail = User.objects.filter(username=uname).values("first_name", 'last_name').first()
    education_info = Education.objects.filter(user__username=uname)
    work_exp_info = Project.objects.filter(work_experience__user__username=uname).values("work_experience__start_year", "work_experience__end_year", "work_experience__is_present", "work_experience__company", 'project_name', "languages", "url")
    context = {
        "uname": uname,
        "user_detail": user_detail,
        "education_info": education_info,
        "work_exp_info": work_exp_info
    }
    print(context)
    
    return render(request, 'portfolio/resume.html', context)


def projects(request, uname='sandeepnegi'):
    
    user_detail = User.objects.filter(username=uname).values("first_name", 'last_name').first()
    project_info = Project.objects.filter(work_experience__user__username=uname)
    context = {
        "uname": uname,
        "user_detail": user_detail,
        "project_info": project_info
    }
    print(context)

    return render(request, 'portfolio/projects.html', context)


def contact(request, uname='sandeepnegi'):

    user_detail = User.objects.filter(username=uname).values("first_name", 'last_name').first()
    personal_info = PersonalInformation.objects.filter(user__username=uname).values('address','city', 'district', 'state', 'country').first()
    contact_info = ContactInformation.objects.filter(user__username=uname).values()
    context = {
        "uname": uname,
        "user_detail": user_detail,
        "contact_info": contact_info ,
        "personal_info": personal_info
    }
    print(context)
    
    return render(request, 'portfolio/contact.html', context)
