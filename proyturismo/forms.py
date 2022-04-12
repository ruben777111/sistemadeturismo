from django.forms import ModelForm, TextInput, Textarea

from proyturismo.models import Transporte


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