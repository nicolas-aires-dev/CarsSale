from django.db import models


#Cria uma nova tabela com os dados abaixo listados
class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
class Car(models.Model):
    #Cria uma nova tabela com os dados abaixo listados
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    #Brand: Primeiro parametro, vai buscar a foreignkey da classe "Brand"
    #on_delete=models.PROTECT: Protege a linha de ser deletada.
    #related_name ='car_brand': Chama a relacao das models de "car_brand"
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=200, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    #blank=True: Permite que o campo esteja em branco
    #null=True: Permite que o campo seja nulo
    #max_length=200: Limita até 200 caracteres
    #models.ImageField: Campo que recebera uma imagem que estara na raiz de "cars"

    #Retornara o nome do objeto sendo o "modelo" do carro
    #def __str__(self): é o nome que indica o nome do objeto 
    def __str__(self):
        return self.model
    


class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'