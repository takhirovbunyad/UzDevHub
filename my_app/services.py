from django.db import connection
from django.utils import timezone
from django.utils.text import slugify
from .models import Dash, News, Kurs, Projects, Category, CustomUser


# ------------------- DASHBOARD -------------------
def get_all_dash(page_size=8, offset=0):
    query = """
        SELECT * FROM my_app_dash
        ORDER BY id DESC
        LIMIT %s OFFSET %s
    """
    return list(Dash.objects.raw(query, [page_size, offset]))


def get_initial_dash(limit=6):
    query = """
        SELECT * FROM my_app_dash
        ORDER BY id DESC
        LIMIT %s
    """
    return list(Dash.objects.raw(query, [limit]))


# ------------------- NEWS -------------------
def get_all_news():
    query = """
        SELECT * FROM my_app_news
        ORDER BY created DESC
    """
    return list(News.objects.raw(query))


# ------------------- LEARN -------------------
def get_all_courses():
    query = """
        SELECT * FROM my_app_kurs
    """
    return list(Kurs.objects.raw(query))


# ------------------- PROJECTS -------------------
def get_published_projects(limit=6, offset=0):
    query = """
        SELECT * FROM my_app_projects
        WHERE status='published'
        ORDER BY publish DESC
        LIMIT %s OFFSET %s
    """
    return list(Projects.objects.raw(query, [limit, offset]))


def get_all_published_projects():
    query = """
        SELECT * FROM my_app_projects
        WHERE status='published'
        ORDER BY publish DESC
    """
    return list(Projects.objects.raw(query))


def get_project_detail(slug, year, month, day):
    query = """
        SELECT * FROM my_app_projects
        WHERE slug=%s AND status='published'
        AND EXTRACT(YEAR FROM publish)=%s
        AND EXTRACT(MONTH FROM publish)=%s
        AND EXTRACT(DAY FROM publish)=%s
    """
    projects = list(Projects.objects.raw(query, [slug, year, month, day]))
    return projects[0] if projects else None


def get_all_categories():
    query = """
        SELECT * FROM my_app_category
    """
    return list(Category.objects.raw(query))


# ------------------- USERS -------------------
def get_user_by_id(user_id):
    query = """
        SELECT * FROM my_app_customuser WHERE id=%s
    """
    users = list(CustomUser.objects.raw(query, [user_id]))
    return users[0] if users else None


def get_user_by_name(first, last):
    query = """
        SELECT * FROM my_app_customuser
        WHERE first_name=%s AND last_name=%s
    """
    users = list(CustomUser.objects.raw(query, [first, last]))
    return users[0] if users else None
