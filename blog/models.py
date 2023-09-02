from django.db import models


class Post(models.Model):
    '''данные о записи'''
    title = models.CharField("Заголовок", max_length=150)
    descriptions = models.TextField("Текс записи")
    author = models.CharField("Автор", max_length=100)
    date = models.DateTimeField("Дата публикации")
    img = models.ImageField('Изображение', upload_to='image/%Y')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return f'{self.title}, {self.author}'


class Comments(models.Model):
    '''Комментарии'''
    email = models.EmailField()
    name = models.CharField('Имя', max_length=50)
    text_comment = models.TextField('Текст комментария', max_length=2000)
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.name}, {self.post}'