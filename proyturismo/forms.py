from turtle import textinput
from django.forms import ModelForm, NumberInput, TextInput, Textarea

from proyturismo.models import Cliente, Transporte


class TransporteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():  # información repetida
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['idtransporte'].widget.attrs['autofocus'] = True  # Autofocus

    class Meta:
        model = Transporte
        fields = '__all__'  # Enviamos todas las columnas
        # exclude = (campos que no querramos mostrar)

        labels = {
            'idtransporte': 'ID transporte',
            'tipotransporte' : 'Tipo Transporte',
            'preciotransporte': 'Precio Transporte',
            'descripciontransporte': 'Descripcion Transporte'
        }

        widgets = {
            'tipotransporte' : TextInput(
                attrs={
                    'label' : 'Tipo Transporte',
                    'placeholder': 'Tipo Bus',

                }
            ),

            'idtransporte' : TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder': '1',

                }
            ),
            'descripciontransporte' : Textarea(
                attrs={
                    'class' : 'form-control',
                    'placeholder': 'Ingrese una descripción',
                    'rows': 3,

                }
            ),
            'preciotransporte' : TextInput(
                attrs={
                    'class' : 'form-control',
                }
            ),
        }
        
class ClienteForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
            
    
    class Meta:
        model = Cliente
        fields = '__all__'
        
        labels = {
            'idcliente': 'Carnet',
            'nombrecliente': 'Nombre',
            'apellidoscliente': 'Apellidos',
            'edadcliente': 'Edad',
            'direccioncliente': 'Direccion',
            'celularcliente': 'Celular'
        }
        
        widgets = {
            'idcliente': TextInput(
                attrs= {
                    'placeholder': '1',
                }
            ),
            'nombrecliente': TextInput(
                attrs={
                    'placeholder': 'Eduardo'
                }
            ),
            'apellidoscliente' : TextInput(
                attrs={
                    'placeholder': 'Vargas Loza'
                }
            ),
            'edadcliente': NumberInput(
                attrs={
                    'placeholder': '18'
                }
            ),
            'direccioncliente': TextInput(
                attrs={
                    'placeholder': 'Av. Achachicala # 20'
                }
            ),
            'celularcliente': TextInput(
                attrs={
                    'placeholder': '69945077'
                }
            ),
            
        }