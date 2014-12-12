from django.contrib import admin
from member.models import *
from django_facebook import *
try:
    from auth import User
except:
    pass

admin.site.register(UserProfile)
admin.site.register(MyCustomProfile)
admin.site.register(FacebookCustomUser)
try:
    admin.site.register(User)
except:
    pass