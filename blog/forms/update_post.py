from django import forms
from blog.models import PostModel

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['title','image' ,'categories','is_active','content' ]
       
       