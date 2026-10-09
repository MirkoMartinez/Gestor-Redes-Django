from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count, Q
from django.contrib.auth.decorators import login_required
from .models import Cliente, Publicacion
from .forms import PublicacionForm

@login_required
def lista_clientes(request):
    mis_clientes = Cliente.objects.annotate(
        borradores=Count('publicacion', filter=Q(publicacion__estado='Borrador')),
        programados=Count('publicacion', filter=Q(publicacion__estado='Programado'))
    )
    return render(request, 'gestor/lista_clientes.html', {'clientes': mis_clientes})

@login_required
def detalle_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    publicaciones = Publicacion.objects.filter(cliente=cliente).order_by('-fecha_publicacion')

    if request.method == 'POST':
        form = PublicacionForm(request.POST, request.FILES)
        if form.is_valid():
            nueva_pub = form.save(commit=False)
            nueva_pub.cliente = cliente
            nueva_pub.save()
            return redirect('detalle_cliente', cliente_id=cliente.id)
    else:
        form = PublicacionForm()

    return render(request, 'gestor/detalle_cliente.html', {
        'cliente': cliente,
        'publicaciones': publicaciones,
        'form': form
    })

@login_required
def editar_publicacion(request, post_id):
    post = get_object_or_404(Publicacion, id=post_id)
    if request.method == 'POST':
        form = PublicacionForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('detalle_cliente', cliente_id=post.cliente.id)
    else:
        form = PublicacionForm(instance=post)
    return render(request, 'gestor/editar_publicacion.html', {'form': form, 'post': post})

@login_required
def eliminar_publicacion(request, post_id):
    post = get_object_or_404(Publicacion, id=post_id)
    cliente_id = post.cliente.id
    if request.method == 'POST':
        post.delete()
    return redirect('detalle_cliente', cliente_id=cliente_id)