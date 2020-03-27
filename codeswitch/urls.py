from django.urls import include, path
from django.contrib import admin
from rest_framework import routers

import users.views
import skills.views
import interests.views
import courses.views
import jobs.views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', users.views.UserViewSet)
router.register(r'skills', skills.views.SkillViewSet)
router.register(r'interests', interests.views.InterestViewSet)
router.register(r'courses', courses.views.CourseViewSet)
router.register(r'jobs', jobs.views.JobViewSet)
router.register(r'user_jobs', jobs.views.UserJobViewSet)
# router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    # path('generate_skills', jobs.views.generate_skills),
    # path('import_db', jobs.views.import_db),
    path('jobs_list', jobs.views.JobQueryList.as_view()),
    path('user_jobs_list/<int:user_id>', jobs.views.UserJobList.as_view()),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]