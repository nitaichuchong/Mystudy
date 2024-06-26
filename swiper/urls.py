"""
URL configuration for swiper project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from user import api as user_api
from social import api as social_api
from vip import api as vip_api

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/user/vcode$', user_api.get_verify_code),
    re_path(r'^api/user/login$', user_api.login),
    re_path(r'^api/user/profile/show$', user_api.show_profile),
    re_path(r'^api/user/profile/modify$', user_api.modify_profile),
    re_path(r'^api/user/avatar/upload$', user_api.upload_avatar),

    re_path(r'^api/social/rcmd_users$', social_api.get_rcmd_users),
    re_path(r'^api/social/like$', social_api.like),
    re_path(r'^api/social/superlike$', social_api.superlike),
    re_path(r'^api/social/dislike$', social_api.dislike),
    re_path(r'^api/social/rewind$', social_api.rewind),
    re_path(r'^api/social/liked_me$', social_api.show_liked_me),
    re_path(r'^api/social/friends$', social_api.get_friends),

    re_path(r'^api/vip/permissions$', vip_api.show_vip_permissions),
]
