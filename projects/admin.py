from django.contrib import admin
from .models import Project, Review, Tag
# Register your models here

admin.site.register(Project)
class ReviewAdmin(admin.ModelAdmin):
    list_display= ("project", "owner",  "value" )
    pass
admin.site.register(Review, ReviewAdmin)
admin.site.register(Tag)