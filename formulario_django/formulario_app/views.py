from django.shortcuts import render, get_object_or_404, redirect
from .forms import UsuarioForm
from .models import Usuario

def pagina_inicial(request):
    return render(request, 'formulario_app/index.html')


def criar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UsuarioForm()
    return render(request, 'formulario_app/criar_usuario.html', {'form': form})


def atualizar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'formulario_app/atualizar_usuario.html', {'form': form, 'usuario': usuario})


def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'formulario_app/lista_usuarios.html', {'usuarios': usuarios})

def consultar_usuarios(request):
    query = request.GET.get('q')
    if query:
        usuarios = Usuario.objects.filter(nome_completo__icontains=query)
    else:
        usuarios = Usuario.objects.all()
    return render(request, 'formulario_app/consultar_usuarios.html', {'usuarios': usuarios, 'query': query})


