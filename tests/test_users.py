
import pytest
from apps.users.models import User

@pytest.mark.django_db
def test_user_create():
    user = User.objects.create_user(username='juanglarproplayer123', phone_number='787898989', dni='1111111111')
    assert user.username == 'juanglarproplayer123'

@pytest.mark.django_db
def test_user_createe():
    user = User.objects.create_user(username='laurita12cute', phone_number='310493223', dni='1107857432')
    assert user.username == 'laurita12cute'