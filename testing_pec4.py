import pandas as pd
from covid_approval_checker.src.functions import *

def main():
    ac = ApprovalChecker('covid_approval_checker/src/covid_approval_polls.csv',
                     'covid_approval_checker/src/covid_concern_polls.csv',
                     'covid_approval_checker/src/pollster_ratings.xlsx')

    ac.preparar_datasets()
    
    print('\nEjercicio 1\n')
    
    print('1.1 # ocurrencias término Huffington Post')
    ac.contar_termino_palabra('Huffington Post')
    
    print('1.1 # ocurrencias url https://d2..jqd6u5mv/econTabReport.pdf')
    ac.contar_termino_url(
    'https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/73jqd6u5mv/econTabReport.pdf')
    
    print("""1.2 La implementación de Pandas, la librería en que se apalanca
    este módulo, para leer un archivo de 1Gb es eficiente.\n""")
    
    print("""1.3 Para cargar 100 archivos de 1Gb se usaría la técnica de 
    paralelización. Se crearían n procesos que cargarían paulatinamente
    los datasets y finalmente se los unificaría.\n""")
    
    print('\nEjercicio 2\n')
    print('Filtrado de datos según las condiciones de la PEC\n\n')
    ac.filtrar_datasets()
    
    print('\nEjercicio 3\n')
    print('Graficando aprobación/desaprobación {Trump, Coronavirus}')
    ac.graficar_aprobacion_covid_trump()
    
    print('\nEjercicio 4\n')
    ac.participacion_gente()

if __name__ == '__main__':
    main()