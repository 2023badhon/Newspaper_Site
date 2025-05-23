from django.conf import settings
from django.shortcuts import render
from posts.models import Post
from django.views.generic import TemplateView

class PostListTemplate(TemplateView):
  template_name="post-list.html"
  def get_context_data(self, **kwargs):
    context=super().get_context_data(**kwargs)
    post_data=Post.objects.all()
    context["data"]=post_data
    return context

def portfolio_view(request): 
  context = {
    "profile_pic": settings.MEDIA_URL + "profile-pic.jpeg",
    }
  return render(request, "portfolio.html",context)