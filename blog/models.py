from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200, default="기본 제목이다.")
	text = models.TextField(default='기본 내용입니다.')
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		null=True, blank=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
