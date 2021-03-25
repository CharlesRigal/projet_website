from django.contrib import admin
from .models import Projet, Skill, Cv, Index_wording, Category

# Register your models here.

admin.site.register(Projet)
admin.site.register(Skill)
admin.site.register(Cv)
admin.site.register(Index_wording)
admin.site.register(Category)
