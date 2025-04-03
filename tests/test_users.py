
import pytest
from apps.users.models import User

@pytest.mark.django_db
def test_user_create():
    user = User.objects.create_user(username='juan', phone_number='787898989', dni='1111111111')
    assert user.username == 'juan'