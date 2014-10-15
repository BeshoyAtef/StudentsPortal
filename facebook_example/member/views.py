# Create your views here.
from django.conf import settings
from django.contrib import messages
from django.http import Http404
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template.context import RequestContext
from django.utils.translation import ugettext as _
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django_facebook import exceptions as facebook_exceptions, \
    settings as facebook_settings
from django_facebook.connect import CONNECT_ACTIONS, connect_user
from django_facebook.decorators import facebook_required_lazy
from django_facebook.utils import next_redirect, get_registration_backend, \
    to_bool, error_next_redirect, get_instance_for
from open_facebook import exceptions as open_facebook_exceptions
from open_facebook.utils import send_warning
from django_facebook.models import * 
import logging

def example(request):
    context = RequestContext(request)
    return render_to_response('example.html', context)

def collectinfo(request):
    user_id = request.POST['user_id']
    user=FacebookCustomUser.objects.get(id=user_id)
    profile = UserProfile.objects .get_or_create(user=user)
    try:
        if request.POST.get('email2'):
            profile.email2=request.POST['email2']
            print  "email saved"
            profile.save()
    except ImportError as e:
        logger.info('Couldnt save email2, got error %s', e)
        pass

    try:
        if request.POST.get('mobilenumber'):
            profile.mobilenumber=request.POST['mobilenumber']
            print  "mobilenumber saved"
            profile.save()
    except ImportError as e:
        logger.info('Couldnt save mobilenumber, got error %s', e)
        pass
    profile.save()
    print profile.email2
    print profile.mobilenumber

    # if request.method == 'POST':
    #     try:
    #         user_id = request.POST['user_id']
    #         user=user.objects.get(id=user_id)
    #         profile=user.profile
    #         if request.POST['email2']:
    #             profile.email2=request.POST['email2']
    #             print  "email saved"
    #         if request.POST['mobilenumber']:
    #             profile.mobilenumber=request.POST['mobilenumber']
    #         profile.save()
    #         print 'done and saved'
    #         data={'mobile':'done'}
    #     except:
    #         data={'error_mobile':True}
    #         print 'feild'
    # context = RequestContext(request)
    return redirect('/')