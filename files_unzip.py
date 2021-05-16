# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 20:27:56 2021

@author: derec
"""
import zipfile

estados = ['AC.zip',
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

for est in estados:
    with zipfile.ZipFile(est, 'r') as Proceds_Amb:
        Proceds_Amb.extractall(est)
    print(est)