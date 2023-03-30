from django.contrib import admin
from .models import Jogo, Loja

class JogosAdmins(admin.ModelAdmin):
    list_display = ('nome', 'preco')
    
admin.site.register(Jogo, JogosAdmins)
    
class LojaAdmins(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'telefone')
    
admin.site.register(Loja, LojaAdmins)



    
    
