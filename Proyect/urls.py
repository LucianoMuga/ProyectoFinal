from django.urls import path
from Proyect.views import *

urlpatterns = [
    path("", ListEmpleado.as_view(), name="list-empleado"),
    path("crear/", CreateEmpleado.as_view(), name="crear-empleado"),
    path('<int:pk>/borrar', DeleteEmpleado.as_view(), name="borrar-empleado"),
    path('<int:pk>/actualizar', ActualizarEmpleado.as_view(), name="actualizar-empleado"),
    path("<int:pk>/detail", DetailEmpleado.as_view(), name="detail-empleado"),
    path("login/", LoginEmpleado.as_view(), name="login-empleado"),
    path("logou/", LogoutEmpleado.as_view(), name="logout-empleado"),
    path('signup/', SignUpEmpleado.as_view(), name="signup-empleado"),
    path('user-profile/<int:pk>', ProfileUpdate.as_view(), name="profile-update"),
    path("about", about, name="about-empleado"),
]
