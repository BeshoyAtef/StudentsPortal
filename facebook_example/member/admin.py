from django.contrib import admin
from member.models import *
from django_facebook import *
try:
    from auth import User
except:
    pass

try:
    admin.site.register(member.UserProfile)
    admin.site.register(memeber.MyCustomProfile)
except:
    pass

try:
    admin.site.register(django_facebook.FacebookCustomUser)
except:
    pass
    
try:
    admin.site.register(auth.User)
except:
    pass