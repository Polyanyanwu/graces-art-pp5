"""Utility to validate user belongs to Group """

from .templatetags import user_belong_group


def check_in_group(request_user, group_name=None):
    """ Check if a user is authenticated and belongs to stated group
    IF no group is provided, just check that user is logged in
    Params:
        group_name is a tuple of groups to check
        request_user is the user object
    Return:
      Message OK if authenticated or the error message
      """
    if request_user.is_authenticated:
        if group_name is None:
            return "OK"
        for grp in group_name:
            if user_belong_group.belong_group(request_user, grp):
                return "OK"
        return "Sorry you do not have access to this page"
    else:
        return "Login is required to access this page"
