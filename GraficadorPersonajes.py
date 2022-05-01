#-------------------------------------------------------------------------------
# Name:        Graficador de Personajes
# Purpose:     Presentar una interfaz intuitiva capaz de graficar
#               personajes de manera propia para el proyecto de IAN
#               utilizando el módulo Clases de Graficador de
#               Personajes
#
# Author:      &#128521;
#
# Created:     10/09/19
# Copyright:   (k) Ka-Tet Co. 1999
# Licence:     <uranus>
#-------------------------------------------------------------------------------

""" Módulo: Graficador de Personajes

Presenta una interfaz intuitiva capaz de graficar personajes
de manera propia para el proyecto de IAN utilizando el módulo
Clases de Graficador de Personajes. Utiliza maquinas de
soporte vectorial para entrenar un módelo capáz de realizar
rostros asociados a una Tarjeta de Personalidad 5G.

Recopila:
    Clase Marco

Referencia:
    Una tarjeta de Personalidad 5G es una estructura sencilla
     que almacena 5 valores numéricos que caracterizan la
     personalidad de un personaje en base a los 5 aspectos de
     la personalidad según el modelo de las Cinco Grandes.
"""

try: # Importa tkinter, con la excepcion por version de python
    import Tkinter as tk
except ImportError:
    import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ClasesGraficador import *

class Marco(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.maq_sop = MaquinaSoportVec.load()
        self.init_handler()
        self.init_rostro()
        self.init_components()
        self.init_configure()
        self.draw_character()

    def init_components(self):
        tk.Label(self,
                 text="Personaje generado actual",
                 bg="#202020",
                 fg="white",
                 font="Times").grid(row=0,
                                    column=0,
                                    columnspan=3,
                                    sticky="NEWS")

        tk.Label(self,
                 text="Personalidad generada actual",
                 bg="#202020",
                 fg="white",
                 font="Times").grid(row=0,column=3,sticky="NEWS")

        tk.Label(self,
                 text="Controles del modelo",
                 bg="#202020",
                 fg="white",
                 font="Times").grid(row=2,
                                    column=0,
                                    columnspan=3,
                                    sticky="NEWS")

        _tt = {'F':'Femenino',
               'M':'Masculino',
               None:'Inexistente'}[self.personaje.generoB]
        tk.Label(self,
                 text=f"Sexo del personaje: {_tt}",
                 bg="#202020",
                 fg="white",
                 font="Times").grid(row=3,column=3,sticky="NEWS")

        bt = tk.Button(self,
                       text="Preparar maquina de soporte",
                       command=lambda:[self.init_maquina(),
                                       self.init_character(True),
                                       self.init_components()])
        bt.grid(row=3,column=0,sticky="NEWS")
        bt = tk.Button(self,
                       text="Entrenar y almacenar maquina",
                       command=lambda:[self.maq_sop.fit(),
                                       self.maq_sop.save(),
                                       self.maq_sop.load()])
        bt.grid(row=4,column=0,sticky="NEWS")

        bt = tk.Button(self,
                       text="Actualizar gráficas",
                       command=lambda:[self.draw_character()])
        bt.grid(row=3,column=1,sticky="NEWS")
        bt = tk.Button(self,
                       text="Cargar maquina almacenada",
                       command=self.maq_sop.load,
                       state='disabled'
                             if self.maq_sop.isDataLoad()
                             else 'normal')
        bt.grid(row=4,column=1,sticky="NEWS")

        bt = tk.Button(self,
                       text="Reiniciar personaje y graficar",
                       command=lambda:[self.init_character(),
                                       self.init_rostro(),
                                       self.init_components(),
                                       self.draw_character()])
        bt.grid(row=3,column=2,sticky="NEWS")
        bt = tk.Button(self,
                       text="Reiniciar personalidad y graficar",
                       command=lambda:[self.init_char_card(),
                                       self.init_rostro(),
                                       self.draw_character()])
        bt.grid(row=4,column=2,sticky="NEWS")

        # inicialización del gráfico del personaje
        self.__figure_charac = plt.Figure(figsize = (5,4), dpi = 100)
        self.__ax_charac = self.__figure_charac.add_subplot(111)
        self.__figure_charac.tight_layout()
        self.grafico_charac = FigureCanvasTkAgg(self.__figure_charac,self)
        self.grafico_charac.get_tk_widget().grid(row=1, column=0, columnspan=3)

        # inicialización del gráfico de la tarjeta de personalidad
        self.__figure_char_card = plt.Figure(figsize = (5,4), dpi = 100)
        self.__ax_char_card = self.__figure_char_card.add_subplot(111)
        self.__ax_char_card.axes.get_xaxis().set_visible(False)
        self.__ax_char_card.axes.get_yaxis().set_visible(False)
        self.__figure_char_card.subplots_adjust(bottom=0,top=1,left=0,right=1)
        self.grafico_char_card = FigureCanvasTkAgg(self.__figure_char_card,
                                                   self)
        self.grafico_char_card.get_tk_widget().grid(row=1, column=3,rowspan=2)

        tk.Label(self,
                 text="Hecho con prisas y sin pausa entre sueños y sudor " +
                      "durante las largas vacaciones de 2022 para el " +
                      "proyecto IAN: (k) Ka-Tet Co. 1999/Software libre",
                 bg="#202020",
                 fg="#303030",
                 font="Consolas 9 italic").grid(row=5,
                                                column=0,
                                                columnspan=4,
                                                sticky="NEWS")

        #graf_n()

    def init_configure(self):
        # se asigna un evento Escape de parámetro perdido a través de una funcion
        #  lambda con un parametro inservible
        #  lambda llamara a la funcion salir de la interfaz
        self.bind('<Escape>', lambda dummy:self.out_GUI())

        # configura la geometria, el rotulo, el fondo de color, el protocolo de
        #  cierre, el icono, la barra de menú, el control de tamaño y el
        #  poscisionamiento en pantalla de marco
        self.geometry("+%d+%d" % (25, 25))
        self.title('Graficador de Personajes - IAN (Proyecto IAN)')
        self.configure(background='#202020')
        self.protocol("WM_DELETE_WINDOW",lambda:self.out_GUI())
        try: self.iconbitmap('recourses\\images\\Icono.ico')
        except: pass
        self.resizable(0,0)
        self.eval('tk::PlaceWindow . center')

    def init_handler(self):
        self.init_maquina()
        self.maq_sop.fit()
        self.init_character()

    def init_maquina(self):
        data = pd.read_csv('recourses/data/CaraBocas.csv',
                           delimiter=';')
        self.maq_sop = MaquinaSoportVec(data.iloc[:,0:5].dropna(axis=0),
                                        np.ravel(data.iloc[:,5:6].dropna(axis=
                                                                          0)))

    def init_character(self, reset = False):
        # inicialización de atributos de personaje
        #  (en proximas versiones debería moverse a la clase
        #  personaje como método de clase)
        cuerpos = {None: [None],
                   'M': [i+1 for i in range(7)],
                   'F': [i+1 for i in range(9)]}
        pelo = {None: [None],
                'M': [None] + [i+1 for i in range(2)] * 2,
                'F': [None] + [i+1 for i in range(1)] * 3}

        if not reset:
            del(cuerpos[None])
            del(pelo[None])

        else:
            cuerpos = {None: [None]}
            pelo = {None: [None]}

        gen_B = rd.choice(list(cuerpos.keys()))
        self.personaje = PersonajeGraficable5G(genero_b = gen_B,
                                               num_cuerpo =
                                                rd.choice(cuerpos[gen_B]),
                                               num_pelo =
                                                rd.choice(pelo[gen_B]))

    def init_char_card(self):
        # crea una nueva personalidad
        self.personaje.personalidad = PersonajeGraficable5G.Tarjeta5G()

    def init_rostro(self):
        # predice el rostro
        self.personaje.rostro = self.maq_sop.predict(
                                 self.personaje.personalidad)

    def draw_character(self):
        # crea y dibuja el personaje
        self.__ax_charac.cla()
        self.personaje.draw()
        self.__ax_charac.imshow(self.personaje.img)
        self.__figure_charac.canvas.draw()

        # crea y dibuja la tarjeta de personalidad
        self.__ax_char_card.cla()
        self.__ax_char_card.imshow(self.personaje.personalidad_img)
        self.__figure_char_card.canvas.draw()

    def out_GUI(self):
        """ Método: Salir de la Interfaz

        Método para salir de la interfaz de forma segura.
        """
        import sys
        # destruye el marco
        self.destroy()
        # finaliza la ejecucion
        sys.exit()

marco = None

def main():
    """ Main: Ejecucion de Interfaz

    Ejecuta la interfaz.
    """
    # para sobreescribir la variable global se debe invocar
    global marco
    marco = Marco()

    if not marco.maq_sop.isDataLoad():
        marco.init_handler()

    # maneja la excepcion KeyboardInterrupt, destruyendo el marco
    try: marco.mainloop()
    except KeyboardInterrupt: marco.out_GUI()
    finally:
        # *Se despide y va a la llorería*
        print("Chau-bye!")

if __name__ == '__main__': main()