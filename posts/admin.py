from django.contrib import admin

# Register your models here.
from .models import Post, PersonalPost


class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'last_modified')


admin.site.register(Post, NoteAdmin)
admin.site.register(PersonalPost)
