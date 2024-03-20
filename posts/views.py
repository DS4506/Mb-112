from django.views.generic import(
    ListView,
    DetailView,
    CreateView
)
from .models import Post


class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_list"] = Post.object.order_by(
            "created_on").reverse()
        return context
    (variable) template_name: Literal['post/details.html']
        
    

class PostDetailView(DetailView):
    template_name = "posts/detail.httml"
    model = Post

class PostCreateView(CreateView):
    template_name = "post/new.html"
    model = Post
    fields = ["title", "subtitle", "body"]
