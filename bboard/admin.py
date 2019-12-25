from django.contrib import admin
from .models import Bb, Rubric

class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'rubric', 'content', 'price', 'published')
    list_display_links = ('title', 'rubric', 'content')
    search_fields = ('title', 'rubric', 'content')

admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)
