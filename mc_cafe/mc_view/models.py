from distutils.command.upload import upload
from django.db import models
from django.urls import reverse_lazy

# Create your models here.

# PROFILE #
    

# COFFEE #
class MC_Coffee(models.Model):
  card_header = models.CharField(max_length=20, verbose_name='Наименование карты')
  card_image = models.ImageField(upload_to='mc_images/%Y/%m/%d', verbose_name='Изображение карты')
  card_body = models.TextField(verbose_name='Текст карты')
  card_footer = models.CharField(max_length=20, verbose_name='Футер Карты')
  category_coffee = models.ForeignKey('Category_Coffee', on_delete=models.PROTECT, null=True)

  def get_absolute_url(self):
      return reverse_lazy("view_coffee", kwargs={"coffee_id": self.pk})

  def __str__(self) -> str:
      return self.card_header


class Category_Coffee(models.Model):
  title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категорий кофе')

  def get_absolute_url(self):
      return reverse_lazy("category_coffee", kwargs={"category_coffee_id": self.pk})
  

  def __str__(self) -> str:
      return self.title

# DILIKATES #
class MC_Dilikates(models.Model):
  card_header = models.CharField(max_length=20, verbose_name='Наименование карты')
  card_image = models.ImageField(upload_to='mc_images/%Y/%m/%d', verbose_name='Изображение карты')
  card_body = models.TextField(verbose_name='Текст карты')
  card_footer = models.CharField(max_length=20, verbose_name='Футер Карты')
  category_dilikates = models.ForeignKey('Category_Dilikates', on_delete=models.PROTECT, null=True)

  def get_absolute_url(self):
      return reverse_lazy("view_dilikates", kwargs={"dilikates_id": self.pk})

  def __str__(self) -> str:
      return self.card_header

class Category_Dilikates(models.Model):
  title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категорий диликатесов')

  def get_absolute_url(self):
      return reverse_lazy("category_dilikates", kwargs={"category_dilikates_id": self.pk})

  def __str__(self) -> str:
      return self.title
# DILIKATES #



  

