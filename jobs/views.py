from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import action
from django.http import HttpResponseRedirect

import re
from datetime import datetime, timedelta
import random

from utils import get_or_none
from .models import Job, UserJob
from skills.models import Skill
from .serializers import JobSerializer, UserJobSerializer


def generate_skills(request):
    job = Job.objects.get(id=1) 

    i = 0
    for job in Job.objects.all():
        desc = job.description
        for skill in Skill.objects.all():
            if (skill.name.lower() in desc) or (skill.name in desc):
                job.required_skills.add(skill.id)
        job.save()

        print("#" * (i%5))
        i += 1

    # job.required_skills.add('SQL')
    # job.save()

    # i = 0
    # for job in Job.objects.all():
    #     for skill in Skill.objects.all():

    #         if i == 5:
    #             break
    #         i += 1
    #     print(job)

    return HttpResponseRedirect('')

def generate_date():
    start = datetime(2020, 1, 1)
    end = start + timedelta(days=365)
    return (start + (end - start) * random.random()).strftime("%Y-%m-%d")

def import_db(request):
    f = open('sadf.csv', 'r', encoding="mac_roman")
    j = 0
    for line in f:
        line =  line.split('|')
        date = generate_date()

        tempDesc = line[2].replace("'", "").replace('"', '')
        if len(tempDesc) < 1000:
            continue

        tmp = Job.objects.create(title="", company="", description="", date_posted=date, 
                                application_src="http://www.placeholder.com")
        for i in range(4):
            print(line[i].replace("'", ""))
        tmp.title = line[0].replace("'", "")
        tmp.company = line[1].replace("'", "")
        tmp.description = tempDesc
        tmp.application_src = line[3].replace("'", "").replace("\n", '')
        # tmp.date_posted = generate_date()
        tmp.save()
        if j == 1000:
            break
        j += 1

    f.close()
    return HttpResponseRedirect('')

class JobViewSet(viewsets.ModelViewSet):
    """API endpoints pertaining to jobs.
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class UserJobViewSet(viewsets.ModelViewSet):
    """API endpoints pertaining to user-jobs.
    """
    queryset = UserJob.objects.all()
    serializer_class = UserJobSerializer