# OK = 0
#
# VCODE_ERROR = 1000
# LOGIN_REQUIRE = 1001
# USER_NOT_EXIST = 1002
# PROFILE_ERROR = 1003

class LogicError(Exception):
    code = 0

    def __str__(self):
        return self.__class__.__name__

def generate_logic_errro(name, code):
    base_cls = (LogicError,)
    return type(name, base_cls, {'code': code})


OK = generate_logic_errro('OK', 0)
VcodeError = generate_logic_errro('VcodeError', 1000)
VcodeExist = generate_logic_errro('VcodeError', 1001)
LoginRequire = generate_logic_errro('LoginRequire', 1002)
UserNotExist = generate_logic_errro('UserNotExist', 1003)
ProfileError = generate_logic_errro('ProfileError', 1004)