from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from mysite.api.views import RegisterViewApi, LoginViewApi, GetProfileApi, LogoutViewApi, GetTimelineApi, GetCommentsApi

urlpatterns = [
    url(r'^register/$', csrf_exempt(RegisterViewApi.as_view())),
    url(r'^login/$', csrf_exempt(LoginViewApi.as_view())),
    url(r'^logout/$', csrf_exempt(LogoutViewApi.as_view())),
    url(r'^me/$', GetProfileApi.as_view()),
    url(r'^timeline/$', GetTimelineApi.as_view()),
    url(r'^posts/(?P<post_id>\d+)/comments/$', GetCommentsApi.as_view()),
]