from django.db import models

class BookQuote(models.Model):
    title_books = models.CharField(max_length=100, verbose_name='Название книги')
    quote_author = models.TextField(verbose_name='Цитата автора')
    cover_image = models.ImageField(upload_to='books_covers/', verbose_name='Обложка книги')
    documentation_books = models.FileField(upload_to='books_docs/', verbose_name='Документация к книге', null=True, blank=True)
    url_books = models.URLField(max_length=200, verbose_name='Ссылка на книгу', null=True, blank=True)
    email_author = models.EmailField(max_length=254, verbose_name='Email автора', null=True, blank=True)
    author_books = models.TextField(verbose_name='Автор книги')
    yootube_link = models.URLField(max_length=200, verbose_name='Ссылка на YouTube', null=True, blank=True)
    created_date_books = models.PositiveBigIntegerField(blank=True, verbose_name='Год издания')
    created_at_message = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_books

    class Meta:
        verbose_name = 'Цитата из книги'
        verbose_name_plural = 'Цитаты из книг'