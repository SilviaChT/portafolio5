from django.urls import path
from .views import PersonaView,PersonasView,AcademicoView,AcademicosView,ConocimientoView,ConocimientosView,HabilidadView,HabilidadesView,HobbieView,HobbiesView,LaboralView,LaboralesView, RegistroView, LoginView

urlpatterns = [
    path('persona', PersonasView.as_view(), name="Personas"),
    path('persona/<int:personaId>',PersonaView.as_view()),

    path('academico', AcademicosView.as_view(), name="Academicos"),
    path('academico/<int:academicoId>',AcademicoView.as_view()),

    path('conocimiento', ConocimientosView.as_view(), name="Conocimientos"),
    path('conocimiento/<int:conocimientoId>',ConocimientoView.as_view()),

    path('habilidad', HabilidadesView.as_view(), name="Habilidades"),
    path('habilidad/<int:habilidadId>',HabilidadView.as_view()),

    path('hobbie', HobbiesView.as_view(), name="Hobbies"),
    path('hobbie/<int:hobbieId>',HobbieView.as_view()),

    path('laboral', LaboralesView.as_view(), name="Laborales"),
    path('laboral/<int:laboralId>',LaboralView.as_view()),

    path('registro', RegistroView.as_view()),
    path('login', LoginView.as_view()),

    
]