from my_app.models import CustomUser

# ----------------------------
# RAW SQL USER QUERIES
# ----------------------------

def get_user_by_username(username):
    query = """
        SELECT * FROM my_app_customuser
        WHERE username = %s
    """
    users = CustomUser.objects.raw(query, [username])
    return next(iter(users), None)


def get_user_by_name(first_name, last_name):
    query = """
        SELECT * FROM my_app_customuser
        WHERE first_name = %s AND last_name = %s
    """
    users = CustomUser.objects.raw(query, [first_name, last_name])
    return next(iter(users), None)


def search_users(first=None, last=None, exclude_username=None):
    query = "SELECT * FROM my_app_customuser WHERE 1=1"
    params = []

    if first:
        query += " AND first_name = %s"
        params.append(first)
    if last:
        query += " AND last_name = %s"
        params.append(last)
    if exclude_username:
        query += " AND username != %s"
        params.append(exclude_username)

    return list(CustomUser.objects.raw(query, params))
