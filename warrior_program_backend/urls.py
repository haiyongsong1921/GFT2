"""warrior_program_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_nested import routers

from user_and_role.views import CurrentUserView
from target.views import TargetView
from factor.views import SharedL1FactorView, PrivateL1FactorView, L2FactorView

router = routers.DefaultRouter()
router.register('users', CurrentUserView)
router.register('targets', TargetView)
router.register('shared_l1factors', SharedL1FactorView)
router.register('private_l1factors', PrivateL1FactorView)

shared_l1_router = routers.NestedSimpleRouter(router, 'shared_l1factors', lookup='l1')
shared_l1_router.register('l2factors', L2FactorView)
private_l1_router = routers.NestedSimpleRouter(router, 'private_l1factors', lookup='l1')
private_l1_router.register('l2factors', L2FactorView)

schema_view = get_swagger_view(title='Warrior Program API', urlconf='warrior_program_backend.urls')

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', obtain_jwt_token),
    url(r'^api/', include(router.urls)),
    url(r'^api/', include(shared_l1_router.urls)),
    url(r'^api/', include(private_l1_router.urls)),
]
