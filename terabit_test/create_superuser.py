import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'terabit_test.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin123')

if not User.objects.filter(username=username).exists():
    print(f"Создание суперпользователя: {username}")
    User.objects.create_superuser(username=username, email=email, password=password)
else:
    print(f"Суперпользователь {username} уже существует.")
