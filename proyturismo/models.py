from django.db import models

# Create your models here.

class Destinoturistico(models.Model):
    iddestino=models.AutoField(primary_key=True)
    nomdestino=models.CharField(max_length=30, verbose_name="Destino Turistico",null=True)
    preciodestino=models.IntegerField(verbose_name="Precio destino",null=True)
    multimedia=models.ImageField(upload_to='imagenes/',verbose_name="Imagen", null=True)
    direcllegada=models.CharField(max_length=50, verbose_name="Direccion llegada",null=True)
    descripciondes=models.CharField(max_length=50, verbose_name="Descripcion",null=True)
    horario_viaje=models.CharField(max_length=10, verbose_name="Horario",null=True)
    
    def __str__(self):
        fila="Titulo:" + self.nomdestino + "-" + "Destino:" + self.descripciondes
        return fila
    def delete(self,using=None, keep_parents=False):
        self.multimedia.storage.delete(self.multimedia.name)
        super().delete()
    class Meta:
        db_table = 'destinoTuristico'
        
class Cliente(models.Model):
    idcliente = models.IntegerField(primary_key=True)
    nombrecliente = models.CharField(max_length=20, null=True)
    apellidoscliente = models.CharField(max_length=40, null=True)
    edadcliente = models.IntegerField(null=True)
    direccioncliente = models.CharField(max_length=30, null=True)
    celularcliente = models.IntegerField(null=True)
    
    class Meta:
        db_table = 'Cliente'
        ordering = ['idcliente']

class Transporte(models.Model):
    idtransporte = models.AutoField(primary_key=True)
    tipotransporte = models.CharField(max_length=20)
    preciotransporte = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    descripciontransporte = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'Transportes'
        ordering = ['idtransporte']
class Boleto(models.Model):
    idboleto = models.AutoField(primary_key=True)
    idcliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    iddestino = models.ForeignKey(Destinoturistico, on_delete=models.CASCADE)
    idtransporte = models.ForeignKey(Transporte, on_delete=models.CASCADE)
    fechaviaje = models.DateTimeField(auto_now_add=False)
    fechaemision = models.DateTimeField(auto_now=False)
    tipopago = models.CharField(max_length=20)
    cantidad = models.IntegerField()
    preciototal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    
    class Meta:
        db_table = 'Boleto'
        ordering = ['idboleto']