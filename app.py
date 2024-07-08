import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QComboBox,  QHBoxLayout
import openai
openai.api_key = 'sk-proj-oA7ftMdV2QImWHFvLaM6T3BlbkFJX6wuAaGewH4O8ZK1805z'

class RecomendacionesCanciones(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('SongiAdvice')

        # Crear los widgets
        self.titulo_label = QLabel('Seleccione las Areas', self)
        self.titulo_label.setStyleSheet(
            'font-size: 16px; font-family: Arial, sans-serif; font-weight: bold;'
            )
        
        self.etiqueta1 = QLabel('Curso:', self)
        self.etiqueta1.setStyleSheet(
            'font-size: 12px; font-family: Arial, sans-serif; font-weight: bold;'
            )
        
        self.etiqueta2 = QLabel('Unidad:', self)
        self.etiqueta2.setStyleSheet(
            'font-size: 12px; font-family: Arial, sans-serif; font-weight: bold;'
            )
        
        self.etiqueta3 = QLabel('Conocimientos:', self)
        self.etiqueta3.setStyleSheet(
            'font-size: 12px; font-family: Arial, sans-serif; font-weight: bold;'
            )
        
        self.etiqueta4 = QLabel('Vocabulario:', self)
        self.etiqueta4.setStyleSheet(
            'font-size: 12px; font-family: Arial, sans-serif; font-weight: bold;'
            )
        
        self.etiqueta5 = QLabel('Pronunciación:', self)
        self.etiqueta5.setStyleSheet(
            'font-size: 12px; font-family: Arial, sans-serif; font-weight: bold;'
            )
        

        self.desplegable1 = QComboBox(self)
        self.desplegable1.addItem('5º Basico')
        self.desplegable1.addItem('6º Basico')
        self.desplegable1.addItem('7º Basico')
        self.desplegable1.addItem('8º Basico')
        self.desplegable1.setStyleSheet(
            'background-color: white ; color: #566573;'
            'font-size: 12px; font-family: Arial, sans-serif; font-weight: bold;'
            'border: 2px solid #2874A6; border-radius: 5px;'
            'margin: 5px; padding: 3px;'
            )

        self.recomendar_btn = QPushButton('Obtener Recomendaciones', self)
        self.recomendar_btn.setStyleSheet(
            'background-color: #3498DB ; color: white;'
            'font-size: 12px; font-family: Arial, sans-serif; font-weight: bold;'
            'border: 2px solid #2874A6; border-radius: 10px;'
            'margin: 10px; padding: 5px;'
            )
        #self.recomendar_btn.setStyleSheet('font-size: 12px; font-family: Arial, sans-serif; font-weight: bold;')
        #self.recomendar_btn.setStyleSheet()
        #self.recomendar_btn.setStyleSheet()
        #self.recomendar_btn.setStyleSheet()

        self.resultado_label = QLabel('Recomendaciones:', self)
        self.resultado_label.setStyleSheet(
            'font-size: 12px; font-family: Arial, sans-serif; font-weight: bold;'
            )

        self.resultado_texto = QTextEdit(self)
        self.resultado_texto.setReadOnly(True)


        self.salir_btn = QPushButton('Salir', self)
        self.salir_btn.setFixedWidth(100)  # Ajusta el tamaño del botón
        self.salir_btn.setStyleSheet(
            'background-color: #C83737   ; color: white;'
            'font-size: 12px; font-family: Arial, sans-serif; font-weight: bold;'
            'border: 2px solid #A00000 ; border-radius: 10px;'
            'margin: 5px; padding: 5px;'
            )

        self.desplegable2 = QComboBox(self)
        self.desplegable2.setStyleSheet(
            'background-color: white ; color: #566573;'
            'font-size: 12px; font-family: Arial, sans-serif; font-weight: bold;'
            'border: 2px solid #2874A6; border-radius: 5px;'
            'margin: 5px; padding: 3px;'
            )
        self.desplegable1.currentIndexChanged.connect(self.actualizar_unidades)
        self.actualizar_unidades(0)

        self.desplegable3 = QComboBox(self)
        self.desplegable3.setStyleSheet(
            'background-color: white ; color: #566573;'
            'font-size: 12px; font-family: Arial, sans-serif; font-weight: bold;'
            'border: 2px solid #2874A6; border-radius: 5px;'
            'margin: 5px; padding: 3px;'
            )
        self.desplegable4 = QComboBox(self)
        self.desplegable4.setStyleSheet(
            'background-color: white ; color: #566573;'
            'font-size: 12px; font-family: Arial, sans-serif; font-weight: bold;'
            'border: 2px solid #2874A6; border-radius: 5px;'
            'margin: 5px; padding: 3px;'
            )
        self.desplegable5 = QComboBox(self)
        self.desplegable5.setStyleSheet(
            'background-color: white ; color: #566573;'
            'font-size: 12px; font-family: Arial, sans-serif; font-weight: bold;'
            'border: 2px solid #2874A6; border-radius: 5px;'
            'margin: 5px; padding: 3px;'
            )
        
        self.desplegable2.currentIndexChanged.connect(self.actualizar_detalles_unidad)
        self.actualizar_detalles_unidad(0)
        
        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(self.titulo_label)
        hbox1.addStretch(1)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.salir_btn)
        hbox2.addStretch(1)


        # Configurar el layout
        layout = QVBoxLayout()
        layout.addLayout(hbox1)
        layout.addWidget(self.etiqueta1)
        layout.addWidget(self.desplegable1)
        layout.addWidget(self.etiqueta2)
        layout.addWidget(self.desplegable2)
        layout.addWidget(self.etiqueta3)
        layout.addWidget(self.desplegable3)
        layout.addWidget(self.etiqueta4)
        layout.addWidget(self.desplegable4)
        layout.addWidget(self.etiqueta5)
        layout.addWidget(self.desplegable5)
        layout.addWidget(self.recomendar_btn)
        layout.addWidget(self.resultado_label)
        layout.addWidget(self.resultado_texto)
        layout.addLayout(hbox2)
        
        self.setLayout(layout)


    def actualizar_unidades(self, index):
        # Obtener el texto del grado seleccionado en el primer desplegable
        grado_seleccionado = self.desplegable1.currentText()

        # Limpiar el segundo desplegable antes de agregar nuevas unidades
        self.desplegable2.clear()

        # Añadir unidades según el grado seleccionado
        if grado_seleccionado == '5º Basico':
            self.desplegable2.addItem('Unidad 1: My world')
            self.desplegable2.addItem('Unidad 2: The place where I live')
            self.desplegable2.addItem('Unidad 3: What we eat?')
            self.desplegable2.addItem("Unidad 4: What's the weather like?")
        elif grado_seleccionado == '6º Basico':
            self.desplegable2.addItem('Unidad 1: Food and health')
            self.desplegable2.addItem('Unidad 2: Around town')
            self.desplegable2.addItem('Unidad 3: The natural world')
            self.desplegable2.addItem("Unidad 4: Let's travel")
        elif grado_seleccionado == '7º Basico':
            self.desplegable2.addItem('Unidad 1: Feelings and opinions')
            self.desplegable2.addItem('Unidad 2: Healthy habits')
            self.desplegable2.addItem('Unidad 3: Sports and free time activities')
            self.desplegable2.addItem('Unidad 4: Green issues')
        elif grado_seleccionado == '8º Basico':
            self.desplegable2.addItem('Unidad 1: Information and communication technologies')
            self.desplegable2.addItem('Unidad 2: Countries, cultures and customs')
            self.desplegable2.addItem('Unidad 3: Going places')
            self.desplegable2.addItem('Unidad 4: Future matters')

    def actualizar_detalles_unidad(self, index):
        # Obtener el texto de la unidad seleccionada en el segundo desplegable
        unidad_seleccionada = self.desplegable2.currentText()

        # Limpiar el tercer desplegable antes de agregar nuevas opciones
        self.desplegable3.clear()
        self.desplegable4.clear()
        self.desplegable5.clear()

        # Añadir opciones según la unidad seleccionada
        if unidad_seleccionada == 'Unidad 1: My world':
            self.desplegable3.addItem('Saludar y despedirse')
            self.desplegable3.addItem('Dar instrucciones')
            self.desplegable3.addItem('Agradecer')
            self.desplegable3.addItem('Identificar y describir')
            self.desplegable3.addItem('Describir acciones cotidianas')
            self.desplegable3.addItem('Expresar cantidad numérica')
            self.desplegable3.addItem('Agregar ideas')
            self.desplegable3.addItem('Abecedario')
            #
            self.desplegable4.addItem('Números del 1-10')
            self.desplegable4.addItem('Colores')
            self.desplegable4.addItem('Días de la semana')
            self.desplegable4.addItem('Adjetivos: up-down, happy-sad, open-shut, tallshort, young-old')
            self.desplegable4.addItem('Miembros de la familia')
            self.desplegable4.addItem('Objetos de la sala de clases')
            self.desplegable4.addItem('Lugares de la escuela')
            self.desplegable4.addItem('Asignaturas')
            self.desplegable4.addItem('Partes de la cara y cuerpo')

        elif unidad_seleccionada == 'Unidad 2: The place where I live':
            self.desplegable3.addItem('Describir acciones ')
            self.desplegable3.addItem('Identificar y describir objetos y lugares')
            self.desplegable3.addItem('Dar información a preguntas con what, who, where')
            self.desplegable3.addItem('Identificar y expresar cantidades there is/are; a/an')
            self.desplegable3.addItem('Describir posición de objetos')
            self.desplegable3.addItem('Describir posesiones')
            self.desplegable3.addItem('Agradecer, pedir permiso')
            #
            self.desplegable4.addItem('La casa')
            self.desplegable4.addItem('Los objetos de la casa')
            self.desplegable4.addItem('Números del 1-10')
            self.desplegable4.addItem('Expresiones: hurry up, I’m fine...')
            self.desplegable4.addItem('Antónimos: big-small, new-old, quiet-noisy...')

        elif unidad_seleccionada == 'Unidad 3: What we eat?':
            self.desplegable3.addItem('Disculparse y pedir favor')
            self.desplegable3.addItem('Describir acciones cotidianas')
            self.desplegable3.addItem('Describir objetos o comida')
            self.desplegable3.addItem('Solicitar y dar información')
            self.desplegable3.addItem('Números hasta el 12')
            self.desplegable3.addItem('Expresar posesión')
            self.desplegable3.addItem('Reemplazar nombres y sustantivos por pronombres plurales')
            #
            self.desplegable4.addItem('Comidas del día')
            self.desplegable4.addItem('Alimentos')
            self.desplegable4.addItem('Bebidas')
            self.desplegable4.addItem('Números hasta el 12')
            self.desplegable4.addItem('Antónimos: good-bad')

        elif unidad_seleccionada == "Unidad 4: What's the weather like?":
            self.desplegable3.addItem('Describir el clima')
            self.desplegable3.addItem('Describir acciones cotidianas')
            self.desplegable3.addItem('Describir ropa')
            self.desplegable3.addItem('Describir posesiones')
            self.desplegable3.addItem('Expresar cantidades numéricas hasta el 20')
            #
            self.desplegable4.addItem('El estado del tiempo')
            self.desplegable4.addItem('La ropa')
            self.desplegable4.addItem('Estaciones del año')
            self.desplegable4.addItem('Números hasta el 20')
            self.desplegable4.addItem('Antónimos: hot-cold, day-night, sunny-cloudy')

        elif unidad_seleccionada == 'Unidad 1: Food and health':
            self.desplegable3.addItem('Expresar habilidad e inhabilidad')
            self.desplegable3.addItem('Expresiones para preguntar acerca de la comida')
            self.desplegable3.addItem('Describir y preguntar por acciones')
            self.desplegable3.addItem('Contrastar ideas')
            
            self.desplegable4.addItem('Uso común')
            self.desplegable4.addItem('Preguntar acerca de la comida')
            self.desplegable4.addItem('Estado de salud')
            self.desplegable4.addItem('Antónimos: empty-full')
            self.desplegable4.addItem('Números hasta el 50')

            self.desplegable5.addItem('ch')
            self.desplegable5.addItem('sh')

        elif unidad_seleccionada == 'Unidad 2: Around town':
            self.desplegable3.addItem('Pedir y decir la hora')
            self.desplegable3.addItem('Preguntar y dar indicaciones para llegar a un lugar')
            self.desplegable3.addItem('Indicación de posición')

            self.desplegable4.addItem('Ocupaciones')
            self.desplegable4.addItem('Acciones asociadas a ocupaciones')
            self.desplegable4.addItem('Lugares o elementos de la ciudad')
            self.desplegable4.addItem('Antónimos: early-late')
            self.desplegable4.addItem('Decenas hasta el 50')
            self.desplegable4.addItem('Expresiones de uso común')

            self.desplegable5.addItem('ch')
            self.desplegable5.addItem('sh')

        elif unidad_seleccionada == 'Unidad 3: The natural world':
            self.desplegable3.addItem('Acciones de uso cotidiano en pasado')
            self.desplegable3.addItem('Preguntar acerca de los animales')
            
            self.desplegable4.addItem('Animales y sus hábitat')
            self.desplegable4.addItem('Descripción de personalidad')
            self.desplegable4.addItem('Sustantivos con plurales irregulares')
            self.desplegable4.addItem('Expresiones como a lot of, very, yesterday, last summer, last year')
            self.desplegable4.addItem('Antónimos: many-few, large-small, fast-slowly, hot-cold')
            self.desplegable4.addItem('Números hasta el 50')

            self.desplegable5.addItem('b/v')
            
        elif unidad_seleccionada == "Unidad 4: Let's travel":
            self.desplegable3.addItem('Expresar posesión de objetos y animales')
            self.desplegable3.addItem('Indagar sobre precio')
            self.desplegable3.addItem('Expresión de estados y lo que hay o no en pasado')
            self.desplegable3.addItem('Acciones comunes y familiares en pasado')
            self.desplegable3.addItem('Expresiones para preguntar')
            
            self.desplegable4.addItem('Estados de ánimo')
            self.desplegable4.addItem('Descripción de lugares')
            self.desplegable4.addItem('Medios de transporte')
            self.desplegable4.addItem('Lugares')
            self.desplegable4.addItem('Eventos')
            self.desplegable4.addItem('Números hasta el 50')
            
            self.desplegable5.addItem('b/v')

        elif unidad_seleccionada == "Unidad 1: Feelings and opinions":
            self.desplegable3.addItem('Expresiones de cantidades')
            self.desplegable3.addItem('Intensificadores')
            self.desplegable3.addItem('Verbos de estado de ánimo o sentimientos')
            self.desplegable3.addItem('Preguntas')
            self.desplegable3.addItem('Verbos: think, find, need, know, meet')
            self.desplegable3.addItem('Conectores: because, first, second, next, finally')
            
            self.desplegable4.addItem('Adjetivos relacionados con sentimientos o personalidad')
            self.desplegable4.addItem('Actividades')
            
            self.desplegable5.addItem('h')
        
        elif unidad_seleccionada == "Unidad 2: Healthy habits":
            self.desplegable3.addItem('Expresiones de cantidades')
            self.desplegable3.addItem('Preguntas')
            self.desplegable3.addItem('Conectores: or/too')
            self.desplegable3.addItem('Verbos modales para expresar obligación, ofrecimientos')
            self.desplegable3.addItem('Verbos: want, understand, eat, cook, walk, read')
            self.desplegable3.addItem('Expresiones acerca de la comida')
            self.desplegable3.addItem('Hacer referencia a rutinas')
            self.desplegable3.addItem('Expresar intensidad')
            self.desplegable3.addItem('Uso de punto, coma en enumeraciones y signo de interrogación')
            
            self.desplegable4.addItem('Frutas y verduras')
            self.desplegable4.addItem('Comida')
            self.desplegable4.addItem('Bebidas')
            self.desplegable4.addItem('Almuerzo, cena')
            self.desplegable4.addItem('Comida sana, comida rápida, comida chatarra')

            self.desplegable5.addItem('z/s')
            
        elif unidad_seleccionada == "Unidad 3: Sports and free time activities":
            self.desplegable3.addItem('Identificar y describir deportes y hobbies')
            self.desplegable3.addItem('Expresarse sobre actividades')
            self.desplegable3.addItem('Expresarse acerca del pasado')
            self.desplegable3.addItem('Expresarse acerca de actividades pasadas que fueron interrumpidas')
            self.desplegable3.addItem('Expresar cantidades')
            self.desplegable3.addItem('Señalar el tiempo, el modo y el grado en que ocurren las acciones')
            self.desplegable3.addItem('Expresar posesión en plurales y nombres terminados en s')
            self.desplegable3.addItem('Verbos: play, go, do, hit, kick, win, lose, beat, enjoy')
            self.desplegable3.addItem('Uso de punto y coma en enumeraciones y signo de interrogación')
            
            self.desplegable4.addItem('Deportes')
            self.desplegable4.addItem('Equipamiento deportivo')
            self.desplegable4.addItem('Personas relacionadas al deporte')
            self.desplegable4.addItem('Actividades de tiempo libre')

            self.desplegable5.addItem('g')

        elif unidad_seleccionada == "Unidad 4: Green issues":
            self.desplegable3.addItem('Expresiones: made of, cut down, throw away, take care of, for example, ask for')
            self.desplegable3.addItem('Expresar causa-efecto: If we pollute water, fish die')
            self.desplegable3.addItem('Imperativos')
            self.desplegable3.addItem('Expresarse acerca de actividades pasadas que fueron interrumpidas')
            self.desplegable3.addItem('Preguntas')
            self.desplegable3.addItem('Verbos modales')
            self.desplegable3.addItem('Conectores: first, second, next, finally, because')
            self.desplegable3.addItem('Uso de punto, coma en enumeraciones y signo de interrogación')
            
            self.desplegable4.addItem('Ambiente')
            self.desplegable4.addItem('Plastico')
            self.desplegable4.addItem('Vidrio')
            self.desplegable4.addItem('Metal')
            self.desplegable4.addItem('Segunda mano')
            self.desplegable4.addItem('Fabrica')
            self.desplegable4.addItem('Contaminar')
            self.desplegable4.addItem('Recursos naturales')
            self.desplegable4.addItem('Basura')
            

            self.desplegable5.addItem('g/j')

        elif unidad_seleccionada == "Unidad 1: Information and communication technologies":
            self.desplegable3.addItem('Expresión de cantidades: a lot of, all')
            self.desplegable3.addItem('Expresión de consejos: verbos modales: should/shouldnt')
            self.desplegable3.addItem('Gustos y preferencias: I like/love/enjoy/dont mind/hate/ dont like ')
            self.desplegable3.addItem('Expresar posesión: pronombres posesivos: his, hers, theirs, mine')
            
            self.desplegable4.addItem('Palabras: site, smartphones, social network, learning tool; technological too')
            self.desplegable4.addItem('Expresiones: to download; tired of; thats OK; to copy/paste; lets, it belongs to…; chat online; download/upload music/ photos; watch videos, visit websites')

            self.desplegable5.addItem('th')

        elif unidad_seleccionada == "Unidad 2: Countries, cultures and customs":
            self.desplegable3.addItem('Expresión de números, cantidades: first, second, third')
            self.desplegable3.addItem('Adjetivos: last, good, bad, tall, long, high, amazing, beautiful, popular, interesting, expensive, crowded')
            self.desplegable3.addItem('Comparaciones: comparative and superlative adjectives')
            self.desplegable3.addItem('Preposiciones: in/on/at')
            self.desplegable3.addItem('Verbos make/do: make friends/a mess/noise/a mistake/the bed/an effort; do the housework /homework/your best/a favor')
            self.desplegable3.addItem('Preguntas: When…? Where are you from…? I m from…')
            self.desplegable3.addItem('Conectores: and then, first, then, next')
            self.desplegable3.addItem('Sufijos: …er; …est')
            self.desplegable3.addItem('Puntuación: uso de dos puntos (colon)')
            
            self.desplegable4.addItem('Países y nacionalidades')
            self.desplegable4.addItem('Costumbres y cultura')

            self.desplegable5.addItem('w')

        elif unidad_seleccionada == "Unidad 3: Going places":
            self.desplegable3.addItem('Números y cantidades')
            self.desplegable3.addItem('Conectores: first, then, next, finally; until')
            self.desplegable3.addItem('Descripciones: the man in…; the woman with…; fantastic, amazing, interesting')
            self.desplegable3.addItem('Preposiciones: into, out of')
            self.desplegable3.addItem('Preguntas: How much is it? Its…; Which…? What is it like?')
            self.desplegable3.addItem('Expresar planes, intenciones y acuerdos futuros')
            self.desplegable3.addItem('Expresiones de tiempo: tomorrow, next week/Saturday/month/weekend; the day after tomorrow')
            self.desplegable3.addItem('Sufijo ion: accommodation, location, destination, vacation')
            self.desplegable3.addItem('Puntuación: uso de dos puntos (colon)')
            
            self.desplegable4.addItem('Expresiones: catch a bus/train; arrive at/in; go on holidays, eat out')
            self.desplegable4.addItem('Vocabulario relacionado con visitar lugares')

            self.desplegable5.addItem('r')

        elif unidad_seleccionada == "Unidad 4: Future matters":
            self.desplegable3.addItem('Números y cantidades')
            self.desplegable3.addItem('Preposiciones: to, from')
            self.desplegable3.addItem('Expresión de tiempo: tomorrow; next week/month/year')
            self.desplegable3.addItem('Predicciones futuras: We will use clean energy in the future')
            self.desplegable3.addItem('Expresar condiciones futuras: If we use clean energy, we wont have smog')
            self.desplegable3.addItem('Conectores: also')
            self.desplegable3.addItem('Prefijo dis-: disagree, disappoint, dislike, disappear')
            self.desplegable3.addItem('Preguntas: What will you do if…? How will you feel if…? What will you do when…? Shall I open the window?')
            self.desplegable3.addItem('Puntuación: uso de dos puntos (colon)')
            
            self.desplegable4.addItem('Expresiones: clean energy; energy efficient; solar/gas/wind energy; smart cars; fuel efficiency')
            self.desplegable4.addItem('Vocabulario relacionado con la vida futura')

            self.desplegable5.addItem('w')
            self.desplegable5.addItem('t')
            self.desplegable5.addItem('ld')

    # Conectar el botón a la función para obtener recomendaciones
        self.recomendar_btn.clicked.connect(self.obtener_recomendaciones)
        # Conectar la señal de selección cambiada
        self.salir_btn.clicked.connect(self.cerrar_aplicacion)
            

    def obtener_recomendaciones(self):

        curso = self.desplegable1.currentText()
        unidad = self.desplegable2.currentText()
        conocimientos = self.desplegable3.currentText()
        vocabulario = self.desplegable4.currentText()
        pronunciacion = self.desplegable5.currentText()

        print("Pronunciacion: "+pronunciacion)
        prompt = (f"Dame solo una lista precisa con máximo 5 recomendaciones de canciones en inglés para un curso de {curso} que está "
                  f"viendo la unidad de {unidad}. Los conocimientos clave son {conocimientos}, "
                  f"el vocabulario incluye {vocabulario} y se busca mejorar la pronunciación en la letra {pronunciacion} incluida en las palabras en ingles. "
                  "En el contexto de la educación chilena para estudiantes de entre 8 y 13 años de edad, ademas ten en consideracion que no deben incluir nombres y/o letras explicitas o que puedan resultar ofensivas "
                  "y aprovecha de darme un dato curioso sobre risk of rain 2")
        print(prompt)
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Eres un asistente educativo."},
                    {"role": "user", "content": prompt}
                ]
            )
            recomendaciones = response['choices'][0]['message']['content']
            self.resultado_texto.setText(recomendaciones)
            
        except openai.error.OpenAIError as e:
            self.resultado_texto.setPlainText(f"Error al obtener recomendaciones: {str(e)}")

    def cerrar_aplicacion(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RecomendacionesCanciones()
    ex.show()
    sys.exit(app.exec_())