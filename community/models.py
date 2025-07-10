from django.db import models
from user.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    area_si = models.CharField(max_length=20)   # 시/도
    area_sgg = models.CharField(max_length=20)
    
    BOARD_CHOICES = [
        ('shared_items', '구비템 공유 게시판'),
        ('resident_tips', '입주민 실전팁 게시판'),
    ]
    
    POST_TYPE_CHOICES = [
        ('question', '질문해요'),
        ('share', '공유해요'),
    ]
    
    board = models.CharField(max_length=20, choices=BOARD_CHOICES, default='shared_items')
    title = models.CharField(max_length=200)
    content = models.TextField()
    post_type = models.CharField(max_length=10, choices=POST_TYPE_CHOICES, default='question')
    # image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    # likes = models.ManyToManyField(User, related_name='like_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def like_count(self):
        return self.likes.count()

    def comment_count(self):
        return self.comments.count()
    
    def __str__(self):
        return self.title
    
    
class Image(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    image=models.ImageField(upload_to = 'images/', null=True, blank = True)
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')  # 중복 좋아요 방지

    def __str__(self):
        return f'{self.user.username} likes {self.post.title}'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.title}'