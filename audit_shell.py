import os,sys
from audit.backend import user_interactive

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MyAudit.settings")
    import django
    django.setup()  # 手动注册django所有的APP
    obj = user_interactive.UserShell()
    obj.start()