from django.db import models


class Material(models.Model):
    title = models.CharField(max_length=150, verbose_name='Name')
    body = models.TextField(verbose_name='Content')

    views_count = models.IntegerField(default=0, verbose_name='Views')
    is_published = models.BooleanField(default=True, verbose_name='Published')
    slug = models.CharField(max_length=150, verbose_name='slug', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materialy'



