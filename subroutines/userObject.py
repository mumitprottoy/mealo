from django.contrib.auth.models import User

def getUser(username:str):
    if User.objects.filter(username=username).exists():
        return User.objects.get(username=username)
    elif User.objects.filter(email=username).exists():
        return User.objects.get(email=username)
    else: return None