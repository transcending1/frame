import os
if not os.environ.get("DJANGO_SETTINGS_MODULE"):
    import django
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
    django.setup()