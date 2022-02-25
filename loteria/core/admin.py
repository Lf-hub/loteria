from django.contrib import admin
from .models import Jogo, NumeroRepetido, NumeroSorteado
from .process import Base

class JogoAdmin(admin.ModelAdmin):
    list_display = ['id_jogo', 'data', 'ganhador']

class NumeroSorteadoAdmin(admin.ModelAdmin):
    list_display = ['id_jogo', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6',
                    'n7', 'n8', 'n9', 'n10', 'n11', 'n12', 'n13',
                    'n14', 'n15', 'n16', 'n17', 'n18', 'n19', 'n20'
                    ]
    print(NumeroSorteado.objects.all())

class NumeroRepetidoAdmin(admin.ModelAdmin):
    list_display = ['id_jogo', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6',
                    'n7', 'n8', 'n9', 'n10'
                   ]
    
admin.site.register(Jogo,JogoAdmin)
admin.site.register(NumeroSorteado,NumeroRepetidoAdmin)
admin.site.register(NumeroRepetido,NumeroRepetidoAdmin)