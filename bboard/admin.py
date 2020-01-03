from django.contrib import admin
from .models import Bb, Rubric, City, Country, State, SubRubricOne

class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'rubric','city', 'kind', 'price', 'published')
    list_display_links = ('title', 'rubric', 'kind')
    search_fields = ('title', 'rubric', 'kind')

admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)
admin.site.register(SubRubricOne)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(State)