from django.db import models

class ProjectMaster(models.Model):
    project_name = models.CharField(max_length = 100)
    project_title = models.CharField(max_length = 100)
    project_subtitle = models.CharField(max_length = 100)
    def __str__(self):
        return self.project_name

class ProjectImage(models.Model):
    project_master = models.ForeignKey(ProjectMaster, on_delete=models.CASCADE)
    image_name = models.CharField(max_length = 100)
    image_description = models.CharField(max_length = 500)

    def __str__(self):
        return self.image_path

class ProjectClient(models.Model):
    project_master = models.ForeignKey(ProjectMaster, on_delete=models.CASCADE)
    client_name = models.CharField(max_length = 100)
    client_url = models.CharField(max_length = 200)

    def __str__(self):
        return self.client_name