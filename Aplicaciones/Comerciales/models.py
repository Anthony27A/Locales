from django.db import models

# Create your models here.


class Proyecto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    presupuesto = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Contratista(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} - {self.especialidad}"

class Local(models.Model):
    id = models.AutoField(primary_key=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    numero_local = models.CharField(max_length=20)
    estado = models.CharField(max_length=50, choices=[("Disponible", "Disponible"), ("Ocupado", "Ocupado")])
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    contratista = models.ForeignKey(Contratista, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Local {self.numero_local} - {self.proyecto.nombre}"
