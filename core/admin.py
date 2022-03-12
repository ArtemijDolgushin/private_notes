from django.contrib import admin

from core.models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('text', 'user', 'created')
    list_display_links = ('text', 'user', 'created')
    search_fields = ('text', 'user', 'created')


admin.site.register(Note, NoteAdmin)
