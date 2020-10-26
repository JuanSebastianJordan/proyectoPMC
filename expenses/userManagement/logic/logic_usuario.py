from userManagement.models import XpensesUser

def get_user(searchusername):
    queryset = XpensesUser.object(username=searchusername)
    return (queryset)

def create_usuario(form):
    usuario = form.save()
    usuario.save()
    return usuario