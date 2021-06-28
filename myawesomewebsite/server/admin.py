from django.contrib import admin

from .models import ProjectMaster, ProjectImage, ProjectClient

class ProjectMasterAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'project_title', 'project_subtitle']

class ProjectImagesAdmin(admin.ModelAdmin):
    list_display = ['project_master', 'image_name', 'image_description']

class ProjectClientsAdmin(admin.ModelAdmin):
    list_display = ['project_master', 'client_name', 'client_url']

admin.site.register(ProjectMaster, ProjectMasterAdmin)
admin.site.register(ProjectImage, ProjectImagesAdmin)
admin.site.register(ProjectClient, ProjectClientsAdmin)