from rest_framework import generics

from django.contrib.auth.models import User
from blog.models import Post
from blog.api.serializers import PostSerializer, UserSerializer, PostDetailSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class PostList(generics.ListCreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Post.objects.all()
  serializer_class = PostDetailSerializer

class UserDetail(generics.RetrieveAPIView):
    lookup_field = "email"
    queryset = User.objects.all()
    serializer_class = UserSerializer
