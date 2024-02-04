import os
import django
from dotenv import load_dotenv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cliqued.settings')
django.setup()

from django.contrib.auth.models import User
def create_superuser(username, email, password):
  # 创建管理员
  print("创建管理员")
  # 检查用户是否已经存在
  if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f"Superuser {username} created successfully!")
    print('Username: %s' % username, 'Password: %s' % password)
  else:
    print(f"Superuser {username} already exists!")

load_dotenv() 
create_superuser('alan', 'email@email.com', os.getenv('DJANGO_ADMIN_PASSWORD'))