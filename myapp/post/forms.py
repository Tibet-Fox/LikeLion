from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content_text',
            'content_img',
            'content_file',
            'writer',
        ]

#'date_created','date_updated'필드는 'auto_now_add=True'와 auto_now=True'로 설정되어 있으므로
#장고가 자동으로 관리하므로 위의 양식에서 제외함.
#hits는 조회수이고 사용자가 직접 수정하지 않으므로 제외, writer필드는 로그인된 사용자로 자동 설정될 수 있으며 추후에 뷰에서 처리..?
#이미지 필드랑 파일필드는 템플릿에서