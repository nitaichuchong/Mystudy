from lib.http import render_json
from lib.sms import send_verify_code
from lib.sms import check_vcode
from common import errors

from user.models import User

def get_verify_code(request):
    phonenum = request.GET.get('phonenum')
    send_verify_code(phonenum)
    return render_json(None)


def login(request):
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')
    if not check_vcode(phonenum, vcode):
        user, created = User.objects.get_or_create(phonenum=phonenum)
        request.session['uid'] = user.id
        return render_json(user.to_dict())
    else:
        return render_json(None, errors.VCODE_ERROR)



def show_profile(request):
    return render_json()


def modify_profile(request):
    return render_json()


def upload_avatar(request):
    return render_json()