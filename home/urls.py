from urls import path
from . import views
urlpatterns = [
    path ('produtos /', views.ver_produtos, name="produtos")
]