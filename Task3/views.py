from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Comment, Post, Blog
from .forms import PostForm, BlogForm, CommentForm


def home(request):
    posts = Post.objects.filter().order_by('-created_at')
    paginator = Paginator(posts, 5)
    page_num = request.GET.get('page')
    posts = paginator.get_page(page_num)
    return render(request, 'index.html', {'posts': posts})


# 게시글 생성
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.blog = Blog.objects.get(author=request.user)
            post.save()
            form.save_m2m()  # Save many-to-many relationships
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_create.html', {'form': form})


# 게시글 리스트 조회
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


# 게시글 하나만 조회
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


# 게시글 업데이트
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()  # 폼으로부터 게시글 업데이트
            return redirect('post_detail', pk=post.pk)  # 업데이트된 게시글의 상세 페이지로 리디렉션
    else:
        form = PostForm(instance=post)
    return render(request, 'post_update.html', {'form': form, 'post': post})


# 게시글 삭제
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()  # 게시글 삭제
        messages.success(request, '게시글이 삭제되었습니다.')
        return redirect('post_list')  # 게시글 목록 페이지로 리디렉션
    else:
        messages.error(request, '잘못된 요청입니다.')
        return redirect('post_detail', pk=post.pk)  # 게시글 상세 페이지로 리디렉션
    

# 블로그 생성
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.writer = request.user
            blog.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = BlogForm()
    return render(request, 'blog_create.html', {'form': form})


# 블로그 리스트 조회
def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs})


# 블로그 세부 정보 조회
def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog_detail.html', {'blog': blog})


# 블로그 업데이트
def blog_update(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog_update.html', {'form': form, 'blog': blog})


# 블로그 삭제
def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        blog.delete()
        messages.success(request, '블로그가 삭제되었습니다.')
        return redirect('blog_list')
    else:
        messages.error(request, '잘못된 요청입니다.')
        return redirect('blog_detail', pk=blog.pk)
    
# 댓글 생성
def comment_create(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.writer = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'comment_create.html', {'form': form})


# 댓글 업데이트
def comment_update(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'comment_update.html', {'form': form, 'comment': comment})


# 댓글 삭제
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    if request.method == 'POST':
        comment.delete()
        messages.success(request, '댓글이 삭제되었습니다.')
        return redirect('post_detail', pk=post_pk)
    else:
        messages.error(request, '잘못된 요청입니다.')
        return redirect('post_detail', pk=post_pk)