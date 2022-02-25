from django.contrib import admin
from .models import Jogo, NumeroRepetido, NumeroSorteado
import pandas as pd

class JogoAdmin(admin.ModelAdmin):
    list_display = ['id_jogo', 'data', 'ganhador']

class NumeroSorteadoAdmin(admin.ModelAdmin):
    list_display = ['id_jogo', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6',
                    'n7', 'n8', 'n9', 'n10', 'n11', 'n12', 'n13',
                    'n14', 'n15', 'n16', 'n17', 'n18', 'n19', 'n20'
                    ]
    
class NumeroRepetidoAdmin(admin.ModelAdmin):
    list_display = ['id_jogo', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6',
                    'n7', 'n8', 'n9', 'n10'
                   ]
    
    loto = pd.io.html.read_html('file:///home/luis/Projetos/loteria/Resultado%20da%20Lotomania.html')[0]
    loto.dropna(thresh=15, inplace=True)
    ltframe = loto[range(18)] 
    print(ltframe)
    # ltframe.columns = [
    #                 'Concurso', 'Data Sorteio', 'Bola1', 'Bola2', 'Bola3', 'Bola4', 'Bola5', 'Bola6', 'Bola7',
    #                 'Bola8', 'Bola9', 'Bola10', 'Bola11', 'Bola12', 'Bola13', 'Bola14','Bola15', 'Bola16', 'Bola17'
    #                 'Bola18', 'Bola19', 'Bola20'
    #                 ]
    # ltframe.drop(0, inplace=True)
    # print(ltframe)
    # bolas = ['Bola%s' % i for i in range(1,21)] 
    # ltframe[bolas] = ltframe[bolas].apply(pd.to_numeric) 
    # ltframe['Soma'] = ltframe[bolas].sum(axis=1)











admin.site.register(Jogo,JogoAdmin)
admin.site.register(NumeroSorteado,NumeroRepetidoAdmin)
admin.site.register(NumeroRepetido,NumeroRepetidoAdmin)