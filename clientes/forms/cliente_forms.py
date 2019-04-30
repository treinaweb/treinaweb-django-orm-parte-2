from django import forms
from ..models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'sobrenome', 'sexo', 'data_nascimento', 'email', 'profissao']