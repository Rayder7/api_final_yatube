from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField('Название', max_length=200)
    slug = models.SlugField('Слаг', unique=True)
    description = models.TextField('Описание')

    class Meta:
        ordering = ('title',)
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name='posts', verbose_name='Сообщество',
        blank=True, null=True)
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True, default=None)

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    def __str__(self):
        return '"{}" to post "{}" by author "{}"'.format(self.text,
                                                         self.post,
                                                         self.author)


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True,
        blank=True, related_name='following')
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, 
        blank=True, related_name='followers')

    def __str__(self):
        return '{} follows {}'.format(self.user, self.following)
