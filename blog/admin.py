from django.contrib import admin

# Register your models here.
from django.contrib import admin
from  blog.models import Post  , Subscription ,CustomerReportRecord , Student

from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class PostAdmin(SummernoteModelAdmin): #instead of  model.Admin
   # exclude = ('slug',)
   list_display = ('id' , 'title' , 'excerpt' , 'date_created')
   list_display_links = ('id' , 'title' )
   search_fields = ('title' , )
   list_per_page = 10
   summernote_fields = ('content', )


admin.site.register(Post , PostAdmin)
admin.site.register(CustomerReportRecord)
admin.site.register(Subscription)
# admin.site.register(Author)
# admin.site.register(Category)

admin.site.register(Student )