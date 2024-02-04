import os
import django
from dotenv import load_dotenv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cliqued.settings')
django.setup()

from django.contrib.auth import get_user_model

def create_superuser(username, email, password):
    # 获取当前激活的用户模型
    User = get_user_model()
    print("Creating superuser")
    
    # 检查用户是否已经存在
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f"Superuser {username} created successfully!")
        print('Username: %s' % username, 'Password: %s' % password)
    else:
        print(f"Superuser {username} already exists!")

load_dotenv()
create_superuser('alan', 'email@email.com', os.getenv('DJANGO_ADMIN_PASSWORD'))
