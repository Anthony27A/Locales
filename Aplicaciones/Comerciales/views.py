from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from datetime import datetime
from .models import Proyecto, Cliente, Contratista, Local
from django.template.loader import render_to_string
from django.db import transaction


# Create your views here.
#Funcion para presentar en pantalla (renderizar) el codigo html del template inicio.html
def inicio(request):
    return render(request,'inicio.html')

# Proyecto
# Presentando en pantalla el formulario de nuevo Proyecto
def nuevoProyecto(request):
    return render(request, 'nuevoProyecto.html')

# Presentando en pantalla el listado de Proyectos
def listadoProyecto(request):
    proyectosBdd = Proyecto.objects.all()
    return render(request, 'listadoProyecto.html', {'proyectos': proyectosBdd})


# GUARDAR PROYECTO
# GUARDAR PROYECTO
def guardarProyecto(request):
    nombre = request.POST['txt_nombre']
    descripcion = request.POST['txt_descripcion']
    fecha_inicio = request.POST['txt_fecha_inicio']
    fecha_fin = request.POST.get('txt_fecha_fin', None)
    presupuesto = request.POST['txt_presupuesto']

    nuevoProyecto = Proyecto.objects.create(
        nombre=nombre,
        descripcion=descripcion,
        fecha_inicio=fecha_inicio,
        fecha_fin=fecha_fin if fecha_fin else None,
        presupuesto=presupuesto
    )

    messages.success(request, "Proyecto Insertado Exitosamente")
    return redirect('/listadoProyecto')



# ELIMINAR PROYECTO
def eliminarProyecto(request, id):
    proyectoEliminar = get_object_or_404(Proyecto, id=id)
    proyectoEliminar.delete()
    messages.success(request, "Proyecto Eliminado")
    return redirect('/listadoProyecto')

# EDITAR PROYECTO
def editarProyecto(request, id):
    proyectoEditar = get_object_or_404(Proyecto, id=id)
    return render(request, "editarProyecto.html", {'proyecto': proyectoEditar})


# PROCESAR EDICIÓN PROYECTO
def procesarEdicionProyecto(request):
    proyecto = Proyecto.objects.get(id=request.POST['id'])
    nombre = request.POST['txt_nombre']
    descripcion = request.POST['txt_descripcion']
    fecha_inicio = request.POST['txt_fecha_inicio']
    fecha_fin = request.POST.get('txt_fecha_fin', None)
    presupuesto = request.POST['txt_presupuesto']
    
    proyecto.nombre = nombre
    proyecto.descripcion = descripcion
    proyecto.fecha_inicio = fecha_inicio
    proyecto.fecha_fin = fecha_fin if fecha_fin else None
    proyecto.presupuesto = presupuesto
    proyecto.save()
    
    messages.success(request, "Proyecto Editado Exitosamente")
    return redirect('/listadoProyecto')


# CLIENTE
# Presentando en pantalla el formulario de nuevo Cliente
def nuevoCliente(request):
    return render(request, 'nuevoCliente.html')

# Presentando en pantalla el listado de Clientes
def listadoCliente(request):
    clientesBdd = Cliente.objects.all()
    return render(request, 'listadoCliente.html', {'clientes': clientesBdd})


# GUARDAR CLIENTE
def guardarCliente(request):
    nombre = request.POST['txt_nombre']
    correo = request.POST['txt_correo']
    telefono = request.POST['txt_telefono']
    
    nuevoCliente = Cliente.objects.create(
        nombre=nombre,
        correo=correo,
        telefono=telefono
    )
    
    messages.success(request, "Cliente registrado exitosamente")
    return redirect('/listadoCliente')


# ELIMINAR CLIENTE
def eliminarCliente(request, id):
    clienteEliminar = Cliente.objects.get(id=id)
    clienteEliminar.delete()
    messages.success(request, "Cliente eliminado exitosamente")
    return redirect('/listadoCliente')

# EDITAR CLIENTE
def editarCliente(request, id):
    clienteEditar = Cliente.objects.get(id=id)
    return render(request, "editarCliente.html", {'cliente': clienteEditar})


# PROCESAR EDICIÓN CLIENTE
def procesarEdicionCliente(request):
    cliente = Cliente.objects.get(id=request.POST['id'])
    nombre = request.POST['txt_nombre']
    correo = request.POST['txt_correo']
    telefono = request.POST['txt_telefono']
    
    cliente.nombre = nombre
    cliente.correo = correo
    cliente.telefono = telefono
    cliente.save()
    
    messages.success(request, "Cliente editado exitosamente")
    return redirect('/listadoCliente')



# CONTRATISTA
# Presentando en pantalla el formulario de nuevo Contratista
def nuevoContratista(request):
    return render(request, 'nuevoContratista.html')

# Presentando en pantalla el listado de Contratistas
def listadoContratista(request):
    contratistasBdd = Contratista.objects.all()
    return render(request, 'listadoContratista.html', {'contratistas': contratistasBdd})



# GUARDAR CONTRATISTA
def guardarContratista(request):
    nombre = request.POST['txt_nombre']
    especialidad = request.POST['txt_especialidad']
    telefono = request.POST['txt_telefono']
    correo = request.POST['txt_correo']
    
    nuevoContratista = Contratista.objects.create(
        nombre=nombre,
        especialidad=especialidad,
        telefono=telefono,
        correo=correo
    )
    
    messages.success(request, "Contratista insertado exitosamente")
    return redirect('/listadoContratista')


# ELIMINAR CONTRATISTA
def eliminarContratista(request, id):
    contratistaEliminar = Contratista.objects.get(id=id)
    contratistaEliminar.delete()
    messages.success(request, "Contratista eliminado exitosamente")
    return redirect('/listadoContratista')

# EDITAR CONTRATISTA
def editarContratista(request, id):
    contratistaEditar = Contratista.objects.get(id=id)
    return render(request, "editarContratista.html", {'contratista': contratistaEditar})


# PROCESAR EDICIÓN CONTRATISTA
def procesarEdicionContratista(request):
    contratista = Contratista.objects.get(id=request.POST['id'])
    nombre = request.POST['txt_nombre']
    especialidad = request.POST['txt_especialidad']
    telefono = request.POST['txt_telefono']
    correo = request.POST['txt_correo']
    
    contratista.nombre = nombre
    contratista.especialidad = especialidad
    contratista.telefono = telefono
    contratista.correo = correo
    contratista.save()
    
    messages.success(request, "Contratista editado exitosamente")
    return redirect('/listadoContratista')


# Presentando en pantalla el formulario de nuevo Local
def nuevoLocal(request):
    proyectos = Proyecto.objects.all()  # Obtiene todos los proyectos de construcción
    clientes = Cliente.objects.all()  # Obtiene todos los clientes
    contratistas = Contratista.objects.all()  # Obtiene todos los contratistas
    return render(request, 'nuevoLocal.html', {'proyectos': proyectos, 'clientes': clientes, 'contratistas': contratistas})

# Presentando en pantalla el listado de Locales
def listadoLocal(request):
    locales = Local.objects.select_related('proyecto', 'cliente', 'contratista').all()  # Optimización con select_related
    return render(request, 'listadoLocal.html', {'locales': locales})


def guardarLocal(request):
    if request.method == 'POST':
        try:
            # Obtener los datos del formulario
            numero_local = request.POST['txt_numero_local']
            proyecto = Proyecto.objects.get(id=request.POST['select_proyecto'])
            estado = request.POST['select_estado']
            cliente_id = request.POST.get('select_cliente', None)
            contratista_id = request.POST.get('select_contratista', None)

            # Verificar si el local ya existe con el mismo número en el proyecto
            if Local.objects.filter(proyecto=proyecto, numero_local=numero_local).exists():
                messages.error(request, "Ya existe un local con ese número en el proyecto seleccionado.")
                return redirect('/nuevoLocal/')

            # Verificar si cliente y contratista son válidos
            cliente = Cliente.objects.get(id=cliente_id) if cliente_id else None
            contratista = Contratista.objects.get(id=contratista_id) if contratista_id else None

            # Crear el nuevo local
            Local.objects.create(
                numero_local=numero_local,
                proyecto=proyecto,
                estado=estado,
                cliente=cliente,
                contratista=contratista
            )

            messages.success(request, "Local guardado correctamente.")
            return redirect('/listadoLocal/')

        except Proyecto.DoesNotExist:
            messages.error(request, "El proyecto seleccionado no existe.")
            return redirect('/nuevoLocal/')
        except Cliente.DoesNotExist:
            messages.error(request, "El cliente seleccionado no existe.")
            return redirect('/nuevoLocal/')
        except Contratista.DoesNotExist:
            messages.error(request, "El contratista seleccionado no existe.")
            return redirect('/nuevoLocal/')
    
    # Si no es un POST, renderiza el formulario de nuevo local
    proyectos = Proyecto.objects.all()
    clientes = Cliente.objects.all()
    contratistas = Contratista.objects.all()
    return render(request, 'nuevo_local.html', {
        'proyectos': proyectos,
        'clientes': clientes,
        'contratistas': contratistas
    })



def eliminarLocal(request, id):
    try:
        with transaction.atomic():
            localEliminar = Local.objects.get(id=id)

            # Obtén los IDs relacionados antes de eliminar el local
            proyecto_id = localEliminar.proyecto.id
            cliente_id = localEliminar.cliente.id if localEliminar.cliente else None
            contratista_id = localEliminar.contratista.id if localEliminar.contratista else None

            # Elimina el local
            localEliminar.delete()

            # Elimina registros relacionados si no hay otros locales asociados
            if not Local.objects.filter(proyecto_id=proyecto_id).exists():
                Proyecto.objects.filter(id=proyecto_id).delete()

            if cliente_id and not Local.objects.filter(cliente_id=cliente_id).exists():
                Cliente.objects.filter(id=cliente_id).delete()

            if contratista_id and not Local.objects.filter(contratista_id=contratista_id).exists():
                Contratista.objects.filter(id=contratista_id).delete()

            messages.success(request, "Local y elementos relacionados eliminados.")
    except Local.DoesNotExist:
        messages.error(request, "El local no existe.")
    except Exception as e:
        messages.error(request, f"Error al eliminar: {e}")
    
    return redirect('/listadoLocal/')



def editarLocal(request, id):
    local = get_object_or_404(Local, id=id)
    proyectos = Proyecto.objects.all()
    clientes = Cliente.objects.all()
    contratistas = Contratista.objects.all()

    return render(request, "editarLocal.html", {
        'local': local,
        'proyectos': proyectos,
        'clientes': clientes,
        'contratistas': contratistas
    })



def procesarEdicionLocal(request):
    if request.method == 'POST':
        try:
            local = Local.objects.get(id=request.POST['id'])
            
            # Actualiza los campos del local
            local.numero_local = request.POST['txt_numero_local']
            local.proyecto = Proyecto.objects.get(id=request.POST['select_proyecto'])
            local.estado = request.POST['select_estado']
            local.cliente = Cliente.objects.get(id=request.POST['select_cliente']) if request.POST.get('select_cliente') else None
            local.contratista = Contratista.objects.get(id=request.POST['select_contratista']) if request.POST.get('select_contratista') else None
            
            # Guarda los cambios
            local.save()

            messages.success(request, "Local actualizado correctamente.")
        except Local.DoesNotExist:
            messages.error(request, "El local no existe.")
        except Proyecto.DoesNotExist:
            messages.error(request, "El proyecto seleccionado no existe.")
        except Cliente.DoesNotExist:
            messages.error(request, "El cliente seleccionado no existe.")
        except Contratista.DoesNotExist:
            messages.error(request, "El contratista seleccionado no existe.")
        except Exception as e:
            messages.error(request, f"Error al actualizar: {e}")

    return redirect('/listadoLocal/')
