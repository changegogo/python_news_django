from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 0

class QuestionAdmin(admin.ModelAdmin):
	# 分页
	list_per_page = 100
	# 按照时间筛选
	list_filter = ['pub_date']
	# 根据问题字段搜索
	search_fields = ['question_text']
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	fieldsets = [
		(None, {'fields': ['question_text']}),
		('日期信息', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]
	
admin.site.register(Question, QuestionAdmin)
