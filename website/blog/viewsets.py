"""Viewsets for the Blog app"""
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import CursorPagination
from .models import Post
from .serializers import PostSerializer
from rest_framework.filters import OrderingFilter

class PostViewSet(ModelViewSet):
    """A set of views for Post model"""

    queryset = Post.objects.all()
    filter_backends = [OrderingFilter]
    ordering = "-pub_date"
    ordering_fields = ["pub_date"]
    required_scopes = ["post"]
    serializer_class = PostSerializer
    pagination_class = CursorPagination

    def get_object(self):
        """Override DRF's generic method

        http://www.cdrf.co/3.7/rest_framework.viewsets/ModelViewSet.html#get_object
        """
        month = self.kwargs.get("month")
        year = self.kwargs.get("year")
        slug = self.kwargs.get("slug")

        queryset = self.filter_queryset(self.get_queryset())

        post = get_object_or_404(
            queryset,
            pub_date__year=year,
            pub_date__month=month,
            slug=slug,
        )
        self.check_object_permissions(self.request, post)
        return post