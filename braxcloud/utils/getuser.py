from braxcloud.accounts.models import AcessoUsuario

def getUser(request):
    usuario_username = request.user.username
    cliente = AcessoUsuario.objects.filter(usuario__username=usuario_username).values('cliente_id')
    return (cliente[0]['cliente_id'])