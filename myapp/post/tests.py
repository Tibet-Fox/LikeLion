from django.test import TestCase  # Django의 기본 테스트 클래스  
from django.contrib.auth.models import User  # Django의 기본 User 모델
from .forms import PostForm, BlogForm, CommentForm, TagForm, CategoryForm


class TestForms(TestCase):

    # 각 테스트 메소드는 "test_"로 시작해야 합니다.

    def test_post_form_valid(self):
        form = PostForm(data={
            'title': 'Test title',
            'content_text': 'Test content text',
            'content_img': 'Test image',
            'content_file': 'Test file',
            'writer': 'Test writer',
        })
        self.assertTrue(form.is_valid())  # 폼이 유효해야 합니다.

    def test_blog_form_valid(self):
        form = BlogForm(data={
            'title': 'Test title',
            'description': 'Test description',
        })
        self.assertTrue(form.is_valid())

    def test_comment_form_valid(self):
        form = CommentForm(data={
            'comment': 'Test comment',
        })
        self.assertTrue(form.is_valid())

    def test_tag_form_valid(self):
        form = TagForm(data={
            'tag': 'Test tag',
        })
        self.assertTrue(form.is_valid())

    def test_category_form_valid(self):
        form = CategoryForm(data={
            'blog': 'Test blog',
            'category': 'Test category',
        })
        self.assertTrue(form.is_valid())
        self.assertIn('writer', form.errors)  # 'writer'가 form.errors에 있는지 확인합니다.
