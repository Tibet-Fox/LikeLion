from django.test import TestCase  # Django의 기본 테스트 클래스
from django.core.files.uploadedfile import SimpleUploadedFile  # 테스트를 위한 간단한 파일 업로드 클래스
from django.contrib.auth.models import User  # Django의 기본 User 모델
from .forms import PostForm  # 테스트할 PostForm

class PostFormTest(TestCase):  # PostForm을 테스트할 TestCase 클래스를 정의합니다.
    def setUp(self):  # 각 테스트 케이스 실행 전에 호출되는 메서드
        self.user = User.objects.create_user(username='testuser', password='testpassword')  # 테스트용 User 생성
        self.image = SimpleUploadedFile(name='test_image.jpg', content=b'\x00\x01\x02\x03', content_type='image/jpeg')  # 테스트용 이미지 파일 생성
        self.file = SimpleUploadedFile(name='test_file.txt', content=b'abc', content_type='text/plain')  # 테스트용 텍스트 파일 생성

    def test_valid_form(self):  # 유효한 데이터를 가진 폼의 테스트 케이스
        form = PostForm(data={  # PostForm 인스턴스를 생성하고 데이터를 넣습니다.
            'title': 'Test title', 
            'content_text': 'Test content', 
            'writer': self.user.id, 
        }, files={  # 파일 데이터도 함께 넣습니다.
            'content_img': self.image, 
            'content_file': self.file, 
        })
        self.assertTrue(form.is_valid())  # form.is_valid()가 True를 반환하는지 확인합니다.

    def test_form_with_missing_title(self):  # 'title' 필드가 없는 경우를 테스트하는 케이스
        form = PostForm(data={ 
            'content_text': 'Test content', 
            'writer': self.user.id,
        }, files={
            'content_img': self.image,
            'content_file': self.file,
        })
        self.assertFalse(form.is_valid())  # form.is_valid()가 False를 반환하는지 확인합니다.
        self.assertIn('title', form.errors)  # 'title'이 form.errors에 있는지 확인합니다.

    def test_form_with_missing_content_text(self):  # 'content_text' 필드가 없는 경우를 테스트하는 케이스
        form = PostForm(data={
            'title': 'Test title',
            'writer': self.user.id,
        }, files={
            'content_img': self.image,
            'content_file': self.file,
        })
        self.assertFalse(form.is_valid())  
        self.assertIn('content_text', form.errors)  # 'content_text'가 form.errors에 있는지 확인합니다.

    def test_form_with_missing_writer(self):  # 'writer' 필드가 없는 경우를 테스트하는 케이스
        form = PostForm(data={
            'title': 'Test title',
            'content_text': 'Test content',
        }, files={
            'content_img': self.image,
            'content_file': self.file,
        })
        self.assertFalse(form.is_valid())  
        self.assertIn('writer', form.errors)  # 'writer'가 form.errors에 있는지 확인합니다.
