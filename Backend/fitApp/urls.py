"""
URL configuration for fitApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from ejercicio.api.router import router as ejercicio_router
from rutina.api.router import router as rutina_router
from rutina.api.router import rutinas_router
from ejercicio.api.router import diaEjercicio_router
from dieta.api.router import router_dieta, router_momento_dia, router_dia_dieta
from alimento.api.router import router_alimento, router_momento_dia_alimento

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('user.api.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include(ejercicio_router.urls)),
    path('api/', include(rutina_router.urls)),
    path('api/', include(rutinas_router.urls)),
    path('api/', include(diaEjercicio_router.urls)),
    path('api/', include(router_dieta.urls)),
    path('api/', include(router_momento_dia.urls)),
    path('api/', include(router_dia_dieta.urls)),
    path('api/', include(router_alimento.urls)),
    path('api/', include(router_momento_dia_alimento.urls)),
]
