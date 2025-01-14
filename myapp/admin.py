from django.contrib import admin
from myapp.models import *


class video_tabular(admin.TabularInline):
    model=Video

class Lesson_tabular(admin.TabularInline):
    model=Lesson

class course_admin(admin.ModelAdmin):
    inlines=(video_tabular,Lesson_tabular)



admin.site.register(Custom_user)
admin.site.register(viewerProfileModel)
admin.site.register(CreatorProfileModel)

admin.site.register(author_profile)
admin.site.register(CourseModel,course_admin)
admin.site.register(Category_model)
admin.site.register(Video)
admin.site.register(Lesson)
admin.site.register(CourseeeModel)
admin.site.register(author)
admin.site.register(only1)
