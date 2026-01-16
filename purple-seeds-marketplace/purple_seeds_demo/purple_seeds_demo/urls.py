from django.contrib import admin
from django.urls import path
from marketplace import views as marketplace_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', marketplace_views.root_redirect, name='root_redirect'),
    path('login/', marketplace_views.login_view, name='login'),
    path('logout/', marketplace_views.logout_view, name='logout'),
    path('portal/', marketplace_views.portal, name='portal'),
    path('marketplace/', marketplace_views.marketplace, name='marketplace'),
    path('solutions/<slug:slug>/', marketplace_views.solution_detail, name='solution_detail'),
    path('customize/<slug:slug>/', marketplace_views.customize, name='customize'),
    path('deploy/', marketplace_views.deploy, name='deploy'),
    path('support/', marketplace_views.support, name='support'),
]
