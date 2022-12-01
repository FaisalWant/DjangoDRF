from django.shortcuts import render

from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView,

	)
from .models import Post

from .serializers import (
	PostSerializer

	)

from django.views import View
from django.views.generic import (
	ListView
	)


# Create your views here.

class PostList(ListView):  #Generic List
	model= Post
	template_name="post/list.html"


class PostDetail(View):    

	def get(self, request, year, month, slug):
		post=get_object_or_404(
			Post,
			pub_date__year=year,
			pub_date__month=month,
			slug=slug
			)
		return render(
			request,"post/detail.html",{"post":post}

			)


### Django RestFrameWork

class PostAPIList(ListAPIView):
    """Return data for multiple Post objects"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostAPIDetail(RetrieveAPIView):
    """Return data for a single Post object"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_object(self):
        """Override DRF's generic method

        http://www.cdrf.co/3.7/rest_framework.generics/ListAPIView.html#get_object
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

