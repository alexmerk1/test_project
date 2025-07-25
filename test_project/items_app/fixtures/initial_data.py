from django.contrib.auth.models import User
from items_app.models import Item

def create_test_data():
    user = User.objects.create_user(
        username='testuser',
        password='testpass'
    )
    
    for i in range(5):
        Item.objects.create(
            title=f'Item {i}',
            description=f'Описание {i}',
            user=user
        )
