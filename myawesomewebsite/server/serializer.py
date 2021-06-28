from rest_framework import serializers
from .models import ProjectMaster


class ProjectMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMaster
        fields = "__all__"