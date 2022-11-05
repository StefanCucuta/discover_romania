from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm
from django.views.generic import CreateView, UpdateView, DeleteView


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

# Adding CRUD
    # Create a Post


class CreatePostView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """ If user is logged can create a new post """

    model = Post
    template_name = "add_post.html"
    fields = ['title', 'content', 'featured_image', 'excerpt']
    success_url = reverse_lazy('home')
    success_message = ("New post has been created - Waiting for approval")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Updating or Editing Post


class UpdatePostView(UserPassesTestMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """ If user is logged can update a post """

    model = Post
    template_name = "add_post.html"
    fields = ['title', 'content', 'featured_image', 'excerpt']
    success_url = reverse_lazy('home')
    success_message = ("Your Post has been updated")


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    # Delete a Post


class DeletePostView(UserPassesTestMixin, LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """ If user is logged can delete a his post """

    model = Post
    success_url = reverse_lazy('home')
    success_message = ("Your Post has been deleted")

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
