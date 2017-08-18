from django.contrib import admin
from models import *

class NewsAdmin(admin.ModelAdmin):
    list_display=('title','author','publish_date','likes',)
 
admin.site.register(News,NewsAdmin)

class UserlikesAdmin(admin.ModelAdmin):


    list_display=('user','news','like_time','status',)
 
admin.site.register(Userlikes,UserlikesAdmin)

class UserprofileAdmin(admin.ModelAdmin):


    list_display=('user','picture','intro',)
 
admin.site.register(UserProfile,UserprofileAdmin)
'''

# Register your models here.
class NewsAdmin(object):
    list_display=('title','author','publish_date',)
 
xadmin.site.register(News,NewsAdmin)

class LikesAdmin(object):
    list_display=('news','likes_user',)
 
xadmin.site.register(Likes,LikesAdmin)'''