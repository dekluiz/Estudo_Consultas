# -*- coding: utf-8 -*-
"""
Script de download de arquivo FTP.

"""

import wget

lista_estados = ['AC.zip',
'AL.zip',
'AM.zip',
'AP.zip',
'BA.zip',
'CE.zip',
'DF.zip',
'ES.zip',
'GO.zip',
'MA.zip',
'MG.zip',
'MS.zip',
'MT.zip',
'PA.zip',
'PB.zip',
'PE.zip',
'PI.zip',
'PR.zip',
'RJ.zip',
'RN.zip',
'RO.zip',
'RR.zip',
'RS.zip',
'SC.zip',
'SE.zip',
'SP.zip',
'TO.zip',
'SP.zip',
'TO.zip']

for estado in lista_estados:
    url = 'http://ftp.dadosabertos.ans.gov.br/FTP/PDA/TISS/AMBULATORIAL/2019/%s' %(estado)
    print('Baixando ' + estado)
    file = wget.download(url)
    print(estado + ' 100%')
    

