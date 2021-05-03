import os


def is_allowed(user_id):
    ids = os.environ.get("ALLOWED_USER_IDS").split(",")
    ids = list(map(lambda item: int(item), ids))
    if user_id in ids:
        return True
    return False


def is_admin(user_id):
    ids = os.environ.get("ADMIN_USER_IDS").split(",")
    ids = list(map(lambda item: int(item), ids))
    if user_id in ids:
        return True
    return False
