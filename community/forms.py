

from django import forms

from community.models import Comment, Post


class PostForm(forms.ModelForm):

    
    class Meta:
        model=Post
        fields=['board', 'title', 'content', 'post_type']
        
        widgets = {
            'board': forms.RadioSelect,
            'post_type': forms.RadioSelect,
        }
        
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ('post', 'user',)
        # fields=['content','created_at','updated_at']