from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
# from rest_framework.response import Response

class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    # response = Response(serializer_class.data)


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer