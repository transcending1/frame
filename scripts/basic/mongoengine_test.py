from apps.users.models import User

user = User.objects.all().first()
print(user)