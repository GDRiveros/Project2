from django.contrib import admin

# Register your models here.

from AppAvanci.models import Estudiante, Profesor, Entregable, Curso

admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Entregable)
admin.site.register(Curso)

