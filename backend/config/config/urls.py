from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from courses.views import CourseAPIList, CourseAPIUpdate, CourseAPIDestroy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/course/', CourseAPIList.as_view()),
    path('api/v1/course/<int:pk>/', CourseAPIUpdate.as_view()),
    path('api/v1/coursedelete/<int:pk>/', CourseAPIDestroy.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #Если раскоментишь следующую строчку то появится куча ошибок, но в видосе она была
    #Предполагаю что там в импортах ошибка
    #path('api/v1/token/verify/' TokenVerifyView.as_view(), names='token_verify')

]
