import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class SimplePasswordValidator:
    def validate(self, password, user=None):
        if len(password) < 6:
            raise ValidationError(_("Parol kamida 6 ta belgidan iborat bo‘lishi kerak."))

        if not re.search(r"[0-9!@#$%^&*(),.?\":{}|<>]", password):
            raise ValidationError(_("Parolda kamida 1 ta raqam yoki belgi bo‘lishi kerak."))

    def get_help_text(self):
        return _("Parol kamida 6 ta belgi va 1 ta raqam yoki belgi o‘z ichiga olishi kerak.")
