import datetime

from social.models import Swiped, Friend
from user.models import User


def rcmd_users(user):
    dating_sex = user.profile.dating_sex
    location = user.profile.location
    min_dating_age = user.profile.min_dating_age
    max_dating_age = user.profile.max_dating_age

    curr_year = datetime.date.today().year
    min_year = curr_year - max_dating_age
    max_year = curr_year - min_dating_age
    users = User.objects.filter(sex=dating_sex, location=location,
                                birth_year__gte=min_year,
                                birth_year__lte=max_year)

    return users


def like_someone(user, sid):
    Swiped.like(user.id, sid)
    if Swiped.is_liked(sid, user.id):  # 检查对方是否喜欢过自己
        Friend.make_friend(user.id, sid)
        return True
    else:
        return False


def superlike_someone(user, sid):
    Swiped.superlike(user.id, sid)
    if Swiped.is_liked(sid, user.id):  # 检查对方是否喜欢过自己
        Friend.make_friend(user.id, sid)
        return True
    else:
        return False


def rewind(user):
    '''反悔'''
    # 检查取出最后一次滑动记录
    swiped = Swiped.objects.filter(uid=user.id).latest().delete()
    # 删除好友关系
    if swiped.flag in ['superlike', 'like']:
        Friend.break_off(user.id, swiped.sid)
    # 删除滑动记录
    swiped.delete()


def users_liked_me(user):
    swipes = Swiped.liked_me(user.id)
    swiper_uid_list = [s.uid for s in swipes]
    return User.objects.filter(id__in=swiper_uid_list)
