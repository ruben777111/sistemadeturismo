from django.db import models

# Create your models here.

class Destinoturistico(models.Model):
    iddestino=models.AutoField(primary_key=True)
    nomdestino=models.CharField(max_length=30, verbose_name="Destino Turistico",null=True)
    preciodestino=models.IntegerField(verbose_name="Precio destino",null=True)
    multimedia=models.ImageField(upload_to='imagenes/',verbose_name="Imagen", null=True)
    direcllegada=models.CharField(max_length=50, verbose_name="Direccion llegada",null=True)
    descripciondes=models.CharField(max_length=50, verbose_name="Descripcion",null=True)
    horario_viaje=models.DateTimeField(auto_now_add=False,verbose_name="Horario",null=True)
    
    def __str__(self):
        fila="Titulo:" + self.nomdestino + "-" + "Destino:" + self.descripciondes
        return fila
    def delete(self,using=None, keep_parents=False):
        self.multimedia.storage.delete(self.multimedia.name)
        super().delete()
    class Meta:
        db_table = 'destinoTuristico'
        
        
class cliente(models.Model):
    ci = models.IntegerField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    ap_pa = models.CharField(max_length=20)
    ap_ma = models.CharField(max_length=20)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=30)
    celular = models.IntegerField()
    
    class Meta:
        db_table = 'cliente'
        
