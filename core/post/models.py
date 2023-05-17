from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


#Blog
class Blog(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# Category
class Category(models.Model):
    category = models.CharField(max_length=15)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.category


# Post
class Post(models.Model):  # pk값 지정 안 하면 Django가 알아서 판단하고 생성
    title = models.CharField(max_length=200)  # 작성한 글의 제목, 길이가 정해진 문자열
    content_text = models.TextField()
    # 작성한 글의 제목, CharField함수를 사용해 길이가 정해지지 않은 문자열을 저장하도록 함.
    content_img = models.ImageField()  # 이미지 업로드
    content_file = models.FileField()  # 파일 업로드
    date_created = models.DateTimeField(
        auto_now_add=True
    )  # 작성한 글의 생성 날짜, DateTimeField 함수를 통해 날짜와 시간을 저장하도록 함, auto_now_add옵션을 통해 데이터 생성시 현재 시간을 저장하도록 지정.
    date_updated = models.DateTimeField(
        auto_now=True
    )  # 작성한 글의 수정일,auto_now옵션을 통해 데이터 갱신시 현재 시간을 저장하도록 함.
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    hits = models.PositiveIntegerField(verbose_name="조회수", default=0)  # 게시글 조회수

    def __str__(self):  # 꼭 정의해야 나중에 후회안함 ㅋ
        return self.title


class Comment(models.Model):
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment


# Like Blog
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} likes {self.post}"


# Tag
class Tag(models.Model):
    tag = models.CharField(max_length=15)

    def __str__(self):
        return self.tag

# Add Neighbor
class Neighbor(models.Model):
    user = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    neighbor = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} follows {self.neighbor.username}"
