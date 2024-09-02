from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('poems/', include('poems.urls')),  # 包含应用程序的子路由表
]