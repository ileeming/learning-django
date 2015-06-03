import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
	questionText = models.CharField(max_length=200)
	pubDate = models.DateTimeField('date published')
	def __unicode__(self):
		return unicode(self.questionText)
	def wasPublishedRecently(self):
		return self.pubDate >= timezone.now() - datetime.timedelta(days=1)
	wasPublishedRecently.admin_order_field = 'pub_date'
	wasPublishedRecently.boolean = True
	wasPublishedRecently.short_description = 'Published recently?'

class Choice(models.Model):
	question = models.ForeignKey(Question)
	choiceText = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __unicode__(self):
		return unicode(self.choiceText)
