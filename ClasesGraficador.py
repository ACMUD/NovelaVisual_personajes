#-------------------------------------------------------------------------------
# Name:        Clases de Graficador de Personajes
# Purpose:     Presentar las clases orientadas a graficar personajes
#               de manera propia para el proyecto de IAN
#
# Author:      &#128521;
#
# Created:     10/09/19
# Copyright:   (k) Ka-Tet Co. 1999
# Licence:     <uranus>
#-------------------------------------------------------------------------------

""" Módulo: Clases de Graficador de Personajes

Presenta las clases orientadas a graficar personajes de
manera propia para el proyecto de IAN.

Recopila:
    Clase PersonajeGraficable5G
    Clase Anidada Tarjeta5G
    Clase MaquinaSoportVec
"""

import pandas as pd
import numpy as np
import random as rd
import math
from PIL import Image

class PersonajeGraficable5G:
    class Tarjeta5G:
        def __init__(self,extroversion:int=None,
                          estabilidad_emocional:int=None,
                          amabilidad:int=None,
                          conciencia:int=None,
                          intelecto_imaginacion:int=None,
                          auto_init:bool=True):
            if (not type(extroversion) == int or
                not type(estabilidad_emocional) == int or
                not type(amabilidad) == int or
                not type(conciencia) == int or
                not type(intelecto_imaginacion) == int):
                auto_init = True
            else:
                auto_init = False
            if auto_init:
                self.__init__(self.calcExtroversion(),
                              self.calcEstabilidadEmocional(),
                              self.calcAmabilidad(),
                              self.calcConciencia(),
                              self.calcIntelectoImaginacion())

            else:
                self.extroversion = extroversion
                self.estabilidad_emocional = estabilidad_emocional
                self.amabilidad = amabilidad
                self.conciencia = conciencia
                self.intelecto_imaginacion = intelecto_imaginacion

            self.__img = None

        @staticmethod
        def calcExtroversion(seed = None):
            if not seed: seed = rd.randint(10,50)/10
            return math.trunc((0.1435*(seed**6)) -
                              (1.8247*(seed**5)) +
                              (7.3386*(seed**4)) -
                              (9.0045*(seed**3)) +
                              (3.7692*(seed**2)) +
                              (1.2185*seed) -
                              (0.0354))

        @staticmethod
        def calcEstabilidadEmocional(seed = None):
            if not seed: seed = rd.randint(10,50)/10
            return math.trunc((0.2163*(seed**6)) -
                              (2.7549*(seed**5)) +
                              (11.572*(seed**4)) -
                              (17.3*(seed**3)) +
                              (10.891*(seed**2)) -
                              (1.2324*seed) -
                              (0.0239))

        @staticmethod
        def calcAmabilidad(seed = None):
            if not seed: seed = rd.randint(10,50)/10
            return math.trunc((0.3832*(seed**6)) -
                              (6.8086*(seed**5)) +
                              (45.159*(seed**4)) -
                              (137.91*(seed**3)) +
                              (197.41*(seed**2)) -
                              (107.13*seed) -
                              (0.0028))

        @staticmethod
        def calcConciencia(seed = None):
            if not seed: seed = rd.randint(10,50)/10
            return math.trunc((0.6434*(seed**6)) -
                              (10.271*(seed**5)) +
                              (61.407*(seed**4)) -
                              (170.29*(seed**3)) +
                              (224.94*(seed**2)) -
                              (114.56*seed) -
                              (0.0023))

        @staticmethod
        def calcIntelectoImaginacion(seed = None):
            if not seed: seed = rd.randint(10,50)/10
            return math.trunc((1.391386165*(seed**6)) -
                              (26.43986331*(seed**5)) +
                              (197.1863751*(seed**4)) -
                              (730.1871814*(seed**3)) +
                              (1401.003617*(seed**2)) -
                              (1282.44321*seed) +
                              (400.3471777))

        @staticmethod
        def getFactores() -> list:
            return ['Extroversion',
                    'Estabilidad Emocional',
                    'Amabilidad',
                    'Conciencia',
                    'Intelecto e Imaginacion']

        @staticmethod
        def getMax() -> list:
            return [PersonajeGraficable5G.Tarjeta5G.calcExtroversion(5),
                    PersonajeGraficable5G.Tarjeta5G.calcEstabilidadEmocional(5),
                    PersonajeGraficable5G.Tarjeta5G.calcAmabilidad(5),
                    PersonajeGraficable5G.Tarjeta5G.calcConciencia(5),
                    PersonajeGraficable5G.Tarjeta5G.calcIntelectoImaginacion(5)]

        @staticmethod
        def getMin() -> list:
            return [PersonajeGraficable5G.Tarjeta5G.calcExtroversion(1),
                    PersonajeGraficable5G.Tarjeta5G.calcEstabilidadEmocional(1),
                    PersonajeGraficable5G.Tarjeta5G.calcAmabilidad(1),
                    PersonajeGraficable5G.Tarjeta5G.calcConciencia(1),
                    PersonajeGraficable5G.Tarjeta5G.calcIntelectoImaginacion(1)]

        @staticmethod
        def nFactores():
            return len(PersonajeGraficable5G.Tarjeta5G.getMax())

        @property
        def personalidad(self):
            return [self.extroversion,
                    self.estabilidad_emocional,
                    self.amabilidad,
                    self.conciencia,
                    self.intelecto_imaginacion]

        @property
        def img(self):
            if self.__img is None:
                self.draw()
            return self.__img

        def draw(self):
            recourse = 'recourses\\images\\char_card.png'
            import matplotlib.pyplot as plt

            abs_min = abs(np.array(self.getMin()))

            values_pers = ((np.array(self.personalidad) + abs_min) /
                           (np.array(self.getMax()) + abs_min))
            values_max = np.ones(self.nFactores())
            x = np.array([i for i in range(len(values_max))]) + 0.3
            width = 0.4
            colors = plt.cm.BuPu(np.linspace(0.3, 0.8, len(values_max)))

            for i in range(len(values_max)):
                plt.bar(x[i] + 0.1,values_max[i],width,color=colors[i])
                plt.bar(x[i],values_pers[i],width,color=colors[i][3:0:-1])

            plt.table(cellText=[self.getMin(),self.getMax(),self.personalidad],
                      rowLabels=['Mínimo','Máximo','Personaje'],
                      colLabels=[f'{i[:11]}...' for i in self.getFactores()],
                      #colLabels=[i.replace(' ','\n') for i in self.getFactores()],
                      colColours=colors,
                      loc='bottom').auto_set_font_size(False)

            plt.subplots_adjust(bottom=0.15)
            plt.title("Tarjeta de Personalidad\n" +
                       "(contrastada con los máximos factores)")
            plt.xticks([])

            plt.savefig(recourse)
            plt.clf()
            self.__img = plt.imread(recourse)

    def __init__(self,extroversion:int = None,
                      estabilidad_emocional:int = None,
                      amabilidad:int = None,
                      conciencia:int = None,
                      intelecto_imaginacion:int = None,
                      auto_init:bool = True,
                      genero_b:str = None,
                      num_cuerpo:int = None,
                      num_boca:int = None,
                      num_ojos:int = None,
                      num_pelo:int = None):
        self._tarjetaPersonalidad = self.Tarjeta5G(extroversion,
                                                   estabilidad_emocional,
                                                   amabilidad,
                                                   conciencia,
                                                   intelecto_imaginacion,
                                                   auto_init)

        self.generoB = genero_b
        self.num_cuerpo = num_cuerpo
        self.num_boca = num_boca
        self.num_ojos = num_ojos
        self.num_pelo = num_pelo
        self.__img = None

    @property
    def personalidad(self):
        return self._tarjetaPersonalidad.personalidad

    @personalidad.setter
    def personalidad(self, value):
        self._tarjetaPersonalidad = value

    @property
    def personalidad_img(self):
        if not self.generoB:
            return Image.fromarray(np.array([[0,0,0,0]]))
        return self._tarjetaPersonalidad.img

    @property
    def img(self):
        if self.__img is None:
            self.draw()
        return self.__img

    @property
    def rostro(self):
        try: return f'{self.num_ojos}' + '{:02d}'.format(self.num_boca)
        except TypeError: return None

    @rostro.setter
    def rostro(self, value: str):
        if value is None: return
        elif type(value) == np.ndarray:
            value = int(value[0])
        self.num_ojos = int(value)//100
        self.num_boca = int(str(value)[-2:])

    def draw(self):
        _cuerpo, _boca, _ojos, _pelo = self.build()

        if _cuerpo is not None:
            if _boca is not None:
                quoin_boca = (78,
                              int(_cuerpo.shape[1]/2 - _boca.shape[1]/2) - 10)
            if _ojos is not None:
                quoin_ojos = (50,
                              int(_cuerpo.shape[1]/2 - _ojos.shape[1]/2) - 10)
            if _pelo is not None:
                quoin_pelo = (-55,
                              int(_cuerpo.shape[1]/2 - _pelo.shape[1]/2) - 10)

            self.__img = np.zeros_like(_cuerpo)

            for y in range(_cuerpo.shape[0]):
                for x in range(_cuerpo.shape[1]):
                    self.__img[y,x,:] += _cuerpo[y,x,:]

                    if (_pelo is not None and
                        (quoin_pelo[0] <= y and
                         quoin_pelo[0] + _pelo.shape[0] >= y) and
                        (quoin_pelo[1] <= x and
                         quoin_pelo[1] + _pelo.shape[1] >= x) and
                       _pelo[y - quoin_pelo[0] - 1,x - quoin_pelo[1] - 1,3] >=
                       self.__img[y,x,3] / 10):
                       self.__img[y,x,:] = _pelo[y - quoin_pelo[0] - 1,
                                                 x - quoin_pelo[1] - 1,
                                                 :]

                    if (_ojos is not None and
                        (quoin_ojos[0] <= y and
                         quoin_ojos[0] + _ojos.shape[0] >= y) and
                        (quoin_ojos[1] <= x and
                         quoin_ojos[1] + _ojos.shape[1] >= x) and
                       _ojos[y - quoin_ojos[0] - 1,x - quoin_ojos[1] - 1,3] >=
                       self.__img[y,x,3] / 10):
                       self.__img[y,x,:] = _ojos[y - quoin_ojos[0] - 1,
                                                 x - quoin_ojos[1] - 1,
                                                 :]

                    if (_boca is not None and
                        (quoin_boca[0] <= y and
                         quoin_boca[0] + _boca.shape[0] >= y) and
                        (quoin_boca[1] <= x and
                         quoin_boca[1] + _boca.shape[1] >= x) and
                       _boca[y - quoin_boca[0] - 1,x - quoin_boca[1] - 1,3] >=
                       self.__img[y,x,3] / 10):
                       self.__img[y,x,:] = _boca[y - quoin_boca[0] - 1,
                                                 x - quoin_boca[1] - 1,
                                                 :]
        else:
            self.__img = np.random.random((720,556,4)) * 255
            self.__img[:,:,rd.randint(0,3)] = np.random.randint(0,
                                                                256,
                                                                (720,
                                                                 556))
            self.__img = self.__img.astype(np.uint8)

        Image.fromarray(self.__img).save('recourses\\images\\char.png')

    def build(self):
        from os.path import exists
        if self.generoB in ['M','F']:
            path = 'recourses\\images\\'

            _cuerpo = f'{path}Cuerpos\\{self.generoB}{self.num_cuerpo}.png'
            if self.num_cuerpo and exists(_cuerpo):
                _cuerpo = Image.open(_cuerpo)
                _cuerpo = _cuerpo.resize((int(_cuerpo.size[0]*
                                              (720/_cuerpo.size[1])),
                                          720),
                                         Image.ANTIALIAS)
                _cuerpo = np.asarray(_cuerpo)
            else: _cuerpo = None

            _boca = f'{path}Bocas\\{self.generoB}{self.num_boca}.png'
            if self.num_boca and exists(_boca):
                _boca = Image.open(_boca)
                _boca = _boca.resize((int(_boca.size[0]*
                                          (141/_boca.size[1])),
                                      141),
                                     Image.ANTIALIAS)
                _boca = np.asarray(_boca)
            else: _boca = None

            _ojos = f'{path}Ojos\\{self.generoB}{self.num_ojos}.png'
            if self.num_ojos and exists(_ojos):
                _ojos = Image.open(_ojos)
                _ojos = _ojos.resize((int(_ojos.size[0]*
                                          (141/_ojos.size[1])),
                                      141),
                                     Image.ANTIALIAS)
                _ojos = np.asarray(_ojos)
            else: _ojos = None

            _pelo = f'{path}Pelo\\{self.generoB}{self.num_pelo}.png'
            if self.num_pelo and exists(_pelo):
                _pelo = Image.open(_pelo)
                _pelo = _pelo.resize((int(_pelo.size[0]*
                                          (314/_pelo.size[1])),
                                      314),
                                     Image.ANTIALIAS)
                _pelo = np.asarray(_pelo)
            else: _pelo = None

        else:
            _cuerpo = None
            _boca = None
            _ojos = None
            _pelo = None

        return _cuerpo, _boca, _ojos, _pelo

class MaquinaSoportVec:
    PERSISTENCE = 'recourses/model/sopor_vect.txt'

    def __init__(self,
                 x,
                 y,
                 kernel:str='poly',
                 degree:int=3,
                 test_size:float=0.2,
                 seed:int=2):
        self.x = x
        self.y = y
        from sklearn.svm import SVC
        self.sopor_vect = SVC(kernel=kernel,degree=degree)
        self.train_test_split(test_size,seed)

    @staticmethod
    def load():
        """ Método de clase: Cargar Maquina de Soporte
                              Vectorial

        Devuelve el objeto almacenado en el archivo plano.

        Retorno:
            un Maquina de Soporte Vectorial
        """
        import pickle
        try:
            stt = open(MaquinaSoportVec.PERSISTENCE,"rb")
            obj = pickle.load(stt)
            stt.close()
            return obj
        except (FileNotFoundError, pickle.UnpicklingError):
            x = np.zeros((2,5))
            y = np.array([0,0])
            return MaquinaSoportVec(x,y,test_size=0.5)

    @property
    def data(self):
        return self.x,self.y

    @data.setter
    def data(self,value):
        self.__init__(value[0],value[1])

    def train_test_split(self,test_size:float=0.2,seed:int=2):
        from sklearn.model_selection import train_test_split
        _Xtr,_Xts,_Ytr,_Yts = train_test_split(self.x,
                                               self.y,
                                               test_size=test_size,
                                               random_state=seed)
        self.x_train,self.y_train = _Xtr,_Ytr
        self.x_test,self.y_test = _Xts,_Yts

    def fit(self):
        try:
            self.sopor_vect.fit(self.x_train, self.y_train)
        except ValueError:
            print('Los datos reales no han sido cargados')
            return
        self.score = self.sopor_vect.score(self.x_test,self.y_test)
        prediccion = self.predict(self.x_test)
        from sklearn.metrics import confusion_matrix
        self.confusion_matrix = confusion_matrix(self.y_test,
                                                 prediccion)

        from sklearn.metrics import classification_report
        self.reporte = classification_report(self.y_test,
                                             prediccion)

    def save(self):
        import pickle
        stt = open(self.PERSISTENCE,"wb")
        pickle.dump(self,stt)
        stt.close()

    def predict(self, personalidad: (list,np.array)):
        if type(personalidad) == list:
            personalidad = np.array(personalidad).reshape(1, -1)
        try:
            return self.sopor_vect.predict(personalidad)
        except AttributeError:
            print('Los datos reales no han sido cargados')
            return

    def isDataLoad(self) -> bool:
        return self.x.shape[0] > 2

    def getScore(self):
        return self.score

    def getConfusionMatrix(self):
        return self.confusion_matrix

    def getClasificationReport(self):
        return self.reporte

    def getReporte(self):
        return (self.getScore(),
                self.getConfusionMatrix(),
                self.getClasificationReport())

def main():
    #data=pd.read_csv('recourses/data/CaraBocas.csv', delimiter=';')
    #x=data.iloc[:,0:5].dropna(axis=0)
    #y=np.ravel(data.iloc[:,5:6].dropna(axis=0))
    #maq = MaquinaSoportVec(x,y)
    maq = MaquinaSoportVec.load()
    #print(maq.isDataLoad())
    #maq.data = x, y
    maq.fit()
    maq.save()
    #print(maq.getReporte())
    import matplotlib.pyplot as plt
    #p = PersonajeGraficable5G(genero_b = 'M', num_cuerpo = 1, num_boca=2,num_ojos=5,num_pelo=1)
    #p = PersonajeGraficable5G(genero_b = 'M', num_cuerpo = 1, num_boca=2,num_ojos=5)
    cuerpos = {'M': [i+1 for i in range(7)],
               'F': [i+1 for i in range(9)]}
    pelo = {'M': [None] + [i+1 for i in range(2)],
            'F': [None] + [i+1 for i in range(1)]}
    genB = rd.choice(list(cuerpos.keys()))
    p = PersonajeGraficable5G(genero_b = genB,num_cuerpo = rd.choice(cuerpos[genB]),num_pelo = rd.choice(pelo[genB]))
    #p = PersonajeGraficable5G()
    #p.rostro = maq.predict(p.personalidad)
    plt.imshow(p.img)
    plt.show()
    plt.imshow(p.personalidad_img)
    plt.show()
    #p.personalidad = PersonajeGraficable5G.Tarjeta5G()
    #plt.imshow(p.personalidad_img)
    #plt.show()

if __name__ == '__main__': main()