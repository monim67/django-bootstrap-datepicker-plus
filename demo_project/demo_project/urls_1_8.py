from django.conf.urls import include, url
# from django.contrib import admin

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('demo_app.urls_1_8', namespace="demo_app")),
]
