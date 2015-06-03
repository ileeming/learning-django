from django.contrib import admin
from polls.models import Choice, Question

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['questionText']}),
		('Date Information', {'fields': ['pubDate'], 'classes' : ['collapse']}),
	]
	inlines = [ChoiceInline]
	list_display = ('questionText', 'pubDate', 'wasPublishedRecently')
	list_filter = ['pubDate']
	search_fields = ['questionText']


admin.site.register(Question, QuestionAdmin)
