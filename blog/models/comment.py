from django.contrib.auth.models import User
from django.db import models
from .post import PostModel
from .dateAbstract import DateAbstract

class CommentModel(DateAbstract):
    post = models.ForeignKey(PostModel, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField(max_length=500)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        db_table = 'comment'
        ordering = ['-publish_date']