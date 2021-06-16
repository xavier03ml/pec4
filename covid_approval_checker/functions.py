import pandas as pd
import matplotlib.pyplot as plt


class ApprovalChecker():
    """
    Esta clase implementa los métodos necesarios
    para resolver la tarea PEC4
    """

    def __init__(self, approval_polls_path, concern_polls_path,
                 pollster_ratings_path):
        """
        Inicialización del objeto.

        Args:
            approval_polls_path (str): ruta para cargar el dataset
            Approval Polls.

            concern_polls_path (str): ruta para cargar el dataset
            Concern Polls.

            pollster_ratings_path (str): ruta para cargar el dataset
            Pollster Ratings.
        """
        self.approval_polls_path = approval_polls_path
        self.concern_polls_path = concern_polls_path
        self.pollster_ratings_path = pollster_ratings_path
        self.ready = False

    def preparar_datasets(self):
        """
        Una vez definido las rutas de los datasets a usar
        se proceden a cargar los respectivos datasets.
        """
        try:
            self.df_approval_polls = pd.read_csv(self.approval_polls_path,
                                                 sep=',')
            self.df_concern_polls = pd.read_csv(self.concern_polls_path,
                                                sep=',')
            self.df_pollster_ratings = pd.read_excel(
                self.pollster_ratings_path)
            self.ready = True
        except Exception as e:
            print(f'Error al cargar datasets, {e}\n')
            self.ready = False

    def contar_termino_palabra(self, termino):
        """
        Cuenta las ocurrencias de un _termino_ dentro de
        la columna _Sponsor_ del datasets Approval polls.

        Este método no puede usarse si ready es False.

        Args:
            termino (str): El término a contar.

        Returns:
            int: número de ocurrencias del término.
        """
        try:
            if(self.ready):
                cnt = self.df_approval_polls[
                    self.df_approval_polls['sponsor'] ==
                    termino]['sponsor'].count()
                print(f'The pattern {termino} appears {cnt} times\n')
                return cnt
            else:
                print('Datasets no están listos, verifique su carga')
        except Exception as e:
            print(f'Error al contar término {termino}, {e}\n')

    def contar_termino_url(self, url):
        """
        Cuenta las ocurrencias de una _url_ dentro de
        la columna _url_ del datasets Approval polls.

        Este método no puede usarse si ready es False.

        Args:
            url (str): La URL a contar.

        Returns:
            int: número de ocurrencias de la url.
        """
        try:
            if(self.ready):
                cnt = self.df_approval_polls[
                    self.df_approval_polls['url'].str.match(url)][
                    'url'].count()
                print(f'The pattern {url} appears {cnt} times\n')
                return cnt
            else:
                print('Datasets no están listos, verifique su carga')
        except Exception as e:
            print(f'Error al contar url {url}, {e}\n')

    def is_ready(self):
        """
        Para poder hacer uso de las funciones de la tarea,
        es necesario que los datasets hayan sido cargados.
        Esta función checkea dicho estado

        Returns:
            bool: si los datasets han sido cargados.
        """
        return self.ready

    def graficar_aprobacion_covid_trump(self):
        """
        Calcula la cantidad de approved/dissaproved agrupados
        por partido y los grafica usando barras apiladas.
        
        El gráfico resultante se guarda como ejercicio4.png
        """
        if(self.ready):
            try:
                ds = self.f_approval_polls
                ds = ds[ds['text'].str.contains('Trump') |
                        ds['text'].str.contains('Coronavirus')]

                dsg = ds.groupby(['party'])[
                    ['party', 'approve', 'disapprove']].agg(
                    napprove=pd.NamedAgg(column='approve', aggfunc="sum"),
                    ndisapprove=pd.NamedAgg(column='disapprove', aggfunc="sum")
                ).reset_index()

                labels = list(dsg['party'].values)
                ls_approve = list(dsg['napprove'].values)
                ls_disapprove = list(dsg['ndisapprove'].values)

                fig, ax = plt.subplots()
                width = 0.35
                ax.bar(labels, ls_approve, width, label='Approve')
                ax.bar(labels, ls_disapprove, width, bottom=ls_approve,
                       label='Disapprove')

                ax.set_title('Number Approve vs Dissaprove by Party')
                ax.legend()

                plt.savefig('ejercicio3.png')
                print('Gráfico guardado correctamente')

            except Exception as e:
                print(f'Error al graficar, {e}\n')
        else:
            print('Datasets no están listos, verifique su carga')

    def ajustar_puntaje(self, nota):
        ptjs = {1: 'A', 0.5: 'B', 0: 'C', -0.5: 'D', -1: 'F'}
        return ptjs.get(nota)

    def participacion_gente(self):
        aux = self.df_pollster_ratings
        self.df_pollster_ratings['grade'] = aux.apply(
        lambda x: self.ajustar_puntaje(x['538 Grade']), axis = 1)
        
        total_ent = self.f_concern_polls['sample_size'].sum()
        print(f'Total Entrevistas: {total_ent}')

    def filtrar_datasets(self):
        """
        Filtra los datasets según las instrucciones de la PEC 4
        """
        if(self.ready):
            ent_unicos = self.df_pollster_ratings[
                self.df_pollster_ratings['Banned by 538'] == 'no']

            ent_unicos = list(ent_unicos['Pollster'].unique())

            ax = self.df_approval_polls
            self.f_approval_polls = ax[ax['pollster'].isin(ent_unicos) &
                                       ax['tracking'] == False]

            ax =  self.df_concern_polls
            self.f_concern_polls = ax[ax['pollster'].isin(ent_unicos) &
                                      ax['tracking'] == False]
        else:
            print('Datasets no están listos, verifique su carga')