from  rest_framework import serializers
from blog.models import Post

class PostSerialier(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = "__all__"
    read_only = ["modified_at", "created_at"]
    