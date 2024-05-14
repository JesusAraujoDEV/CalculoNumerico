import flet as ft
from flet import *
from random import randint
import funciones

# Variables


class matrix(Container):
    def __init__(self, rowNumbers):
        for i in range(rowNumbers):
            for j in range(rowNumbers):
                self.matriz_textfields[rowNumbers] = TextField(value="", text_align='center', width=100)
            self.content = self.matriz_textfields
        self = TextField(value="", text_align='center', width=100)


def main(page: Page):
    page.title = 'Flet Counter'
    page.vertical_alignment = 'center'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_resizable = False
    page.window_width = 1300
    page.window_height = 700
    animation_style = animation.Animation(500,AnimationCurve.DECELERATE)
    
    """
        Matriz Gauss Seidel
    """
    
    side_bar_column = Column(
        spacing=0,
        controls=[
        Row(
            controls=[
            Container(
                data = 0,
                on_click=lambda e: switch_page(e,'page1'),
                expand=True,
                height=40,
                content=Text("Matriz Gauss-Seidel"),
            ),
            ]
        ),
        Row(
            controls=[
            Container(
                on_click=lambda e: switch_page(e,'page2'),
                data = 1,
                expand=True,
                height=40,
                content=Icon(
                icons.BADGE,
                color='blue'
                ),
            ),
            ]
        ),
        ]
        )

    indicator =Container(
      height=40,
      bgcolor='red',
      offset=transform.Offset(0,0),
      animate_offset=animation.Animation(500,AnimationCurve.DECELERATE)
    )

    def switch_page(e,point):
        print(point)
        for page in switch_control:
            switch_control[page].offset.x = 2
            switch_control[page].update()

        switch_control[point].offset.x = 0
        switch_control[point].update()
        
        indicator.offset.y = e.control.data
        indicator.update()
    
    
    
     # Matriz Gauss Seidel
        
    def ajusteMatriz(e):
        """
        Ajusta el tamaño de la matriz y los vectores en función del valor del slider.
        """
        # Crea una nueva columna de TextField para la matriz con el tamaño especificado por el slider
        columnatemporal = matrix_size(int(slider_size.value))
        columna_Matriz_A.controls = columnatemporal

        # Crea una nueva columna de TextField para el vector X con el tamaño especificado por el slider
        columnatemporal = array_size(int(slider_size.value), 80, False)
        columna_vector_X.controls = columnatemporal

        # Crea una nueva columna de TextField para el vector resultado con el tamaño especificado por el slider
        columnatemporal = array_size(int(slider_size.value), 80, False)
        columna_vector_resultado.controls = columnatemporal

        page.update()  # Actualiza la página para reflejar los cambios

        
    # Contenedor A (Inicializaciones)
        
    def limitar_caracteres(e): 
        """
        Limita la longitud del texto en un control a 3 caracteres.
        """
        if len(e.control.value) > 3:
            e.control.value = e.control.value[:3]  # Limita el texto a los primeros 3 caracteres
        page.update()  # Actualiza la página para reflejar los cambios

    def matrix_size(rowNumbers):
        """
        Crea una matriz de TextField con el tamaño especificado.

        Args:
        - rowNumbers: Número de filas y columnas de la matriz.

        Returns:
        - columnas: Lista de filas de TextField.
        """
        columnas = []
        for i in range(rowNumbers):
            filas = []
            for j in range(rowNumbers):
                # Crea un nuevo TextField para cada celda de la matriz
                filas.append(
                    TextField(
                        bgcolor="#cff8ea",
                        text_size=14,
                        border_radius=15,
                        value="",
                        cursor_color="black",
                        color="#176e5d",
                        text_align='left',
                        on_change=limitar_caracteres,  # Limita la longitud del texto
                        width=60,
                        height=50,
                        input_filter=ft.InputFilter(allow=True, regex_string=[0,1,2,3,4,5,6,7,8,9], replacement_string="")
                    )
                )
            # Agrega la fila a la lista de columnas
            columnas.append(
                Row(
                    controls=filas,
                    alignment="CENTER"
                )
            )
        return columnas  # Retorna la lista de filas de TextField

    # Se define el título para el primer contenedor
    titulo_matriz_A = ft.Text(
        "Matriz A",
        theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM,
        weight=ft.FontWeight.BOLD,
        size=16,
        color="#9BA8AB",
        text_align="CENTER"
    )

    # Se define el slider para ajustar el tamaño de la matriz
    slider_size = Slider(
        value=3,
        width=250,
        min=2,
        max=6,
        divisions=4,
        autofocus=True,
        label="{value}x{value}",
        inactive_color=colors.GREEN,
        overlay_color="#174a3f",
        thumb_color="#176e5d",
        on_change=ajusteMatriz  # Llama a la función ajusteMatriz cuando cambia el valor del slider
    )

    # Se crea una fila que contiene el título de la matriz y el slider para el tamaño de la matriz
    fila_titulos = Row(
        controls=[titulo_matriz_A, slider_size],
        alignment="CENTER"
    )

    # Se crea una columna para contener los TextField que forman la matriz A
    columna_temporal = matrix_size(3)  # Se crea una matriz inicial de tamaño 3x3

    columna_Matriz_A = Column(
        controls=columna_temporal,  
        alignment="CENTER",
        height=400
    )

    # Función para limpiar las matrices y los vectores
    def limpieza_matrices(e):
        """
        Limpia los valores de las matrices y los vectores en la interfaz de usuario.
        """
        # Itera sobre el tamaño especificado por el slider
        for i in range(int(slider_size.value)):
            # Limpia los valores del vector X y del vector resultado
            columna_vector_X.controls[i].value = ""
            columna_vector_resultado.controls[i].value = ""
            # Itera sobre el tamaño especificado por el slider para limpiar los valores de la matriz A
            for j in range(int(slider_size.value)):
                columna_Matriz_A.controls[i].controls[j].value = ""
        e.bgcolor="#20ac8b"  # Cambia el color del botón para indicar que se ha limpiado
        page.update()  # Actualiza la página para reflejar los cambios

    
    boton_limpiar = ft.ElevatedButton( 
        "Limpiar",
        bgcolor= "#20ac8b",
        color= "#f1fcf8",
        icon=icons.BACKSPACE,
        icon_color="#cff8ea",
        on_click=limpieza_matrices
    )
    
    def operacionMatriz(e):
        """
        Realiza la operación de Gauss-Seidel con los datos ingresados por el usuario.
        """
        try:
            lista_matriz = []  # Lista para almacenar los elementos de la matriz
            lista_vector = []  # Lista para almacenar los elementos del vector
            # Itera sobre el tamaño especificado por el slider para obtener los elementos del vector
            for i in range(int(slider_size.value)):
                lista_vector.append(float(columna_vector_X.controls[i].value))
                # Itera sobre el tamaño especificado por el slider para obtener los elementos de la matriz
                for j in range(int(slider_size.value)):
                    lista_matriz.append(float(columna_Matriz_A.controls[i].controls[j].value))
            resultadolista = []  # Lista para almacenar los resultados de Gauss-Seidel
            # Realiza la operación de Gauss-Seidel y almacena los resultados en resultadolista
            resultadolista = funciones.GaussSeidel(funciones.creacionMatriz(int(slider_size.value), lista_matriz), funciones.creacionVector(int(slider_size.value), lista_vector))
            # Itera sobre los resultados y formatea los valores a dos decimales antes de asignarlos a los controles de la columna de vector resultado
            for i in range(len(resultadolista)):
                stringtemporal = str(resultadolista[i])
                stringtemporal = "{:.2f}".format(float(stringtemporal))
                columna_vector_resultado.controls[i].value = stringtemporal
            page.update()  # Actualiza la página para mostrar los resultados
        except:
            # Si ocurre un error, muestra una alerta de error
            mensaje_error = ft.AlertDialog(title=ft.Text("Entrada de datos incorrecta!!."),
                                content=ft.Text("Ha ingresado incorrectamente los datos, están incompletos"),
                                bgcolor="#bed1ca"
                                )
            page.dialog = mensaje_error
            mensaje_error.open = True
            page.update()

    
    boton_operar = ft.ElevatedButton( 
        "Operar",
        bgcolor= "#20ac8b",
        color= "#f1fcf8",
        icon=icons.CLEAR,
        icon_color="#cff8ea",
        on_click=operacionMatriz
    )
    
    def llenar_matriz(e): 
         for i in range(int(slider_size.value)):
            columna_vector_X.controls[i].value = randint(1,99)
            columna_vector_resultado.controls[i].value = ""
            for j in range(int(slider_size.value)):
                columna_Matriz_A.controls[i].controls[j].value = randint(1,99)
         page.update()
    
    boton_randomm = ft.ElevatedButton( 
        "Random",
        bgcolor= "#20ac8b",
        color= "#f1fcf8",
        icon=icons.CACHED,
        icon_color="#cff8ea",
        on_click=llenar_matriz
    )
    
    fila_botones = Row(
        controls=[boton_limpiar, boton_operar, boton_randomm],
        alignment="CENTER"
    )
    
    # Contenedores
    
    columna_elementos_A = Column(
        controls=[
            fila_titulos,
            columna_Matriz_A,
            fila_botones
        ],
        alignment="CENTER"
    )
    
    # Vector X
    
    def array_size(rowNumbers, width, booleano):
        """
        Crea una lista de TextField con el tamaño y las propiedades especificadas.

        Args:
        - rowNumbers: Número de TextField que se crearán.
        - width: Ancho de cada TextField.
        - booleano: Booleano que indica si los TextField son de solo lectura o no.

        Returns:
        - columnas: Lista de TextField creados.
        """
        columnas = []
        for i in range(rowNumbers):
            # Crea un nuevo TextField con las propiedades especificadas y lo agrega a la lista columnas
            columnas.append(
                TextField(
                    bgcolor="#cff8ea",
                    text_size=14,
                    border_radius=15,
                    value="",
                    cursor_color="black",
                    color="#176e5d",
                    text_align='left',
                    on_change=limitar_caracteres,  # Llama a la función limitar_caracteres cuando cambia el texto
                    read_only=booleano,  # Establece si el TextField es de solo lectura o no
                    width=width,  # Establece el ancho del TextField
                    height=60,
                    input_filter=ft.InputFilter(allow=True, regex_string=[0,1,2,3,4,5,6,7,8,9], replacement_string="")
                    # Establece el filtro de entrada para permitir solo dígitos
                )
            )
        return columnas  # Retorna la lista de TextField creados

    
    titulo_vector_x = ft.Text("Matriz X   ", #Se define el titulo para el primer contenedor
                       theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM,
                       weight=ft.FontWeight.BOLD,
                       size=16,
                       color="#f1fcf8")
        
    fila_titulosX = Row(
        controls=[
            titulo_vector_x
        ],
        alignment=MainAxisAlignment.CENTER
    )
    
    columna_temporal_X = array_size(3, 80, False)
    
    columna_vector_X = Column(
        controls=columna_temporal_X,  
        alignment=MainAxisAlignment.CENTER,
        height=400
    )
    
    columna_elementos_X = Column(
        controls=[
            fila_titulosX,
            columna_vector_X
        ],
        alignment=MainAxisAlignment.CENTER
    )
    
    # Vector Resultado
    
    titulo_matriz_resultado = ft.Text("Vector Resultado", #Se define el titulo para el primer contenedor
                       theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM,
                       weight=ft.FontWeight.BOLD,
                       size=16,
                       color="#9BA8AB",
                       text_align="CENTER")
        
    fila_titulos_resultado = Row(
        controls=[
            titulo_matriz_resultado
        ],
        alignment=MainAxisAlignment.CENTER
    )
    
    columna_temporal_resultado = array_size(3, 150, True)
    
    columna_vector_resultado = Column(
        controls=columna_temporal_resultado,  
        alignment=MainAxisAlignment.CENTER,
        height=400
    )
    
    columna_elementos_resultado = Column(
        controls=[
            fila_titulos_resultado,
            columna_vector_resultado
        ],
        alignment=MainAxisAlignment.CENTER
    )
    
    # Contenedores
    
    container_A = Container(
        content=columna_elementos_A,
        height=550,
        width=450,
        gradient=LinearGradient(['#f1fcf8', '#cff8ea']),
        border_radius=20,
        border=border.all(2, '#178a71'),
        blur=ft.Blur(10, 0, ft.BlurTileMode.MIRROR),
        padding=2,
    )
    
    container_X = Container(
        content=columna_elementos_X,
        height=550,
        width=150,
        gradient=LinearGradient(['#178a71', '#20ac8b']),
        border_radius=20,
        border=border.all(2, '#176e5d'),
        blur=ft.Blur(10, 0, ft.BlurTileMode.MIRROR),
        padding=40,
    )
    
    container_resultado = Container(
        content=columna_elementos_resultado,
        height=550,
        width=225,
        gradient=LinearGradient(['#f1fcf8', '#cff8ea']),
        border_radius=20,
        border=border.all(2, '#178a71'),
        blur=ft.Blur(10, 0, ft.BlurTileMode.MIRROR),
        padding=50,
    )

    fila_contenedores = Row(
        controls=[container_A, container_X, container_resultado],
        alignment=MainAxisAlignment.CENTER,
        #top=20
    )
    
    # Paginas
    
    page1 = Container(
        offset=transform.Offset(0,0),
        animate_offset=animation_style,
        bgcolor='blue',
        content=[fila_contenedores],
        alignment="CENTER",
        padding=1,
        width=20
    )

    page2 = Container(
      alignment=alignment.center,
      offset=transform.Offset(0,0),
      animate_offset=animation_style,
      bgcolor='green',
      content=Text('PAGE 2',size=50)
    )

    switch_control = {
      'page1':page1,
      'page2':page2,
    }
    
    
    """
        Conversion de números
    """
    
    # Funciones
    
    def abrir_informacion_sistema(e): 
        """Abre la ventana de información del sistema."""
        # Asigna el diálogo de alerta a la página y lo abre
        page.dialog = dialogo_alerta_info
        dialogo_alerta_info.open = True
        # Actualiza la página para mostrar los cambios
        page.update()
            
    def limpiar_salida(e): 
        """Limpia el campo de salida."""
        # Limpia el campo de salida
        numero_salida.value = ""
        # Actualiza la página para mostrar los cambios
        page.update()

        
    def cambio_parametros(e): 
        """Maneja el evento de cambio de parámetros."""
        # Reinicia los campos de entrada y salida
        numero_entrada.value = ""
        numero_salida.value = ""
        
        # Verifica si se ha seleccionado alguna opción numérica
        if str(opciones_numericas.value) == str(None):
            numero_entrada.read_only = True
        else:
            # Habilita la entrada de texto
            numero_entrada.read_only = False
            
            # Establece el filtro de entrada basado en la opción numérica seleccionada
            if str(opciones_numericas.value) == "DEC":
                numero_entrada.input_filter = ft.InputFilter(allow=True, regex_string=[0,1,2,3,4,5,6,7,8,9], replacement_string="")
            elif str(opciones_numericas.value) == "BIN":
                numero_entrada.input_filter = ft.InputFilter(allow=True, regex_string=[0,1], replacement_string="")
            elif str(opciones_numericas.value) == "TER":
                numero_entrada.input_filter = ft.InputFilter(allow=True, regex_string=[0,1,2], replacement_string="")
            elif str(opciones_numericas.value) == "CUA":
                numero_entrada.input_filter = ft.InputFilter(allow=True, regex_string=[0,1,2,3], replacement_string="")
            elif str(opciones_numericas.value) == "OCT":
                numero_entrada.input_filter = ft.InputFilter(allow=True, regex_string=[0,1,2,3,4,5,6,7], replacement_string="")
            elif str(opciones_numericas.value) == "HEX":
                numero_entrada.input_filter = ft.InputFilter(allow=True, regex_string=[0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F','a','b','c','d','e','f'], replacement_string="")
        
        # Actualiza la página para reflejar los cambios
        page.update()

        
    def conversion_numerica(e): 
        """
        Realiza la conversión de números entre diferentes bases numéricas.
        """
        baseEntrada = 0
        baseSalida = 0
        
        # Verifica si se ha ingresado un número en la entrada
        if numero_entrada.value == "": 
            # Muestra una alerta si no se ha ingresado ningún número
            requerimientosalerta = ft.AlertDialog(title=ft.Text("Falta el valor de entrada"),
                                content=ft.Text("No se ha ingresado ningún número o valor de entrada.")
                                )
            page.dialog = requerimientosalerta
            requerimientosalerta.open = True
            
        elif str(opciones_numericas.value) == str(None) or str(opciones_numericas_salida.value) == str(None): 
            # Verifica si se han seleccionado bases numéricas de entrada y salida
            # Muestra una alerta si alguna base numérica no está definida
            requerimientosalerta = ft.AlertDialog(title=ft.Text("Faltan bases numéricas por definir."),
                                content=ft.Text("Revisa las bases de entrada y salida.")
                                )
            page.dialog = requerimientosalerta
            requerimientosalerta.open = True

        else:
            # Determina la base numérica de entrada y el valor de entrada
            if str(opciones_numericas.value) == "DEC":
                baseEntrada = 10
                valorEntrada = numero_entrada.value
            elif str(opciones_numericas.value) == "BIN":
                baseEntrada = 2
                valorEntrada = numero_entrada.value
            elif str(opciones_numericas.value) == "TER":
                baseEntrada = 3
                valorEntrada = numero_entrada.value
            elif str(opciones_numericas.value) == "CUA":
                baseEntrada = 4
                valorEntrada = numero_entrada.value
            elif str(opciones_numericas.value) == "OCT":
                baseEntrada = 8
                valorEntrada = numero_entrada.value
            elif str(opciones_numericas.value) == "HEX":
                baseEntrada = 16
                valorEntrada = numero_entrada.value

            # Determina la base numérica de salida
            if str(opciones_numericas_salida.value) == "DEC":
                baseSalida = 10
            elif str(opciones_numericas_salida.value) == "BIN":
                baseSalida = 2
            elif str(opciones_numericas_salida.value) == "TER":
                baseSalida = 3
            elif str(opciones_numericas_salida.value) == "CUA":
                baseSalida = 4
            elif str(opciones_numericas_salida.value) == "OCT":
                baseSalida = 8
            elif str(opciones_numericas_salida.value) == "HEX":
                baseSalida = 16

            # Realiza la conversión basada en las bases de entrada y salida
            if baseEntrada == 10:
                if baseSalida == 10: 
                    numero_salida.value = str(valorEntrada)
                elif baseSalida == 16: 
                    cadena = hex(int(valorEntrada))
                    cadena = cadena[2:]
                    cadena = cadena.upper()
                    numero_salida.value = cadena
                else: 
                    numero_salida.value = funciones.fromDEC(valorEntrada, baseSalida)
            else: 
                valorEntrada = funciones.toDEC(valorEntrada, baseEntrada)
                if baseSalida == 10: 
                    numero_salida.value = str(valorEntrada)
                elif baseSalida == 16: 
                    cadena = hex(int(valorEntrada))
                    cadena = cadena[2:]
                    cadena = cadena.upper()
                    numero_salida.value = cadena
                else: 
                    numero_salida.value = funciones.fromDEC(valorEntrada, baseSalida)
        page.update()

        
    def limpieza_entradas(e): 
        """
        Limpia los campos de entrada y salida.
        """
        # Limpia los campos de entrada y salida
        numero_entrada.value = ""
        numero_salida.value = ""
        # Actualiza la página para reflejar los cambios
        page.update()

    
    # Titulos
    # Título principal de la interfaz de conversión de números
    titulo_conversion = ft.Text("Conversión de números", 
                        theme_style=ft.TextThemeStyle.HEADLINE_LARGE,
                        weight=ft.FontWeight.BOLD,
                        size=30,
                        color="#9BA8AB"
                    )

    # Diálogo de alerta/información sobre las bases de los sistemas numéricos
    dialogo_alerta_info = ft.AlertDialog(title=ft.Text("Bases de Sistemas Numéricos"), 
                                content=ft.Text("DEC = Decimal (Base 10)\nBIN = Binario (Base 2)\nTER = Terciario (Base 3)\nCUA = Cuaternario(Base 4)\nOCT = Octal (Base 8)\nHEX = Hexadecimal (Base 16)")
                                )

    # Botón de información para mostrar el diálogo de alerta
    informacion_sistema = ft.IconButton(
        icon= ft.icons.INFO_ROUNDED,
        icon_color= "#4A5C6A",
        on_click= abrir_informacion_sistema
    )

    # Campos de entrada y dropdowns
    # Campo de entrada para números de entrada
    numero_entrada = ft.TextField( 
        width=280,
        height=40,
        hint_text= 'Números de Entrada',
        border ='underline',
        border_color="#174a3f",
        color ='black',
        read_only= False,
        input_filter=ft.InputFilter(allow=True,regex_string=[0,1,2,3,4,5,6,7,8,9],replacement_string=""),
        on_change=limpiar_salida
    )

    # Campo de entrada para números de salida (solo lectura)
    numero_salida = ft.TextField( 
        width=280,
        height=40,
        hint_text= 'Números de Salida',
        border ='underline',
        color ='black',
        read_only= True
    )

    # Dropdown para seleccionar la base numérica de entrada
    opciones_numericas = ft.Dropdown(width=100,
                                    border_color= "#4A5C6A",
                                    options=[
                                        ft.dropdown.Option("DEC"),
                                        ft.dropdown.Option("BIN"),
                                        ft.dropdown.Option("TER"),
                                        ft.dropdown.Option("CUA"),
                                        ft.dropdown.Option("OCT"),
                                        ft.dropdown.Option("HEX"),
                                        ],
                                    label="Base",
                                    on_change=cambio_parametros,
                                    value="DEC"
                            )

    # Dropdown para seleccionar la base numérica de salida
    opciones_numericas_salida = ft.Dropdown(width=100, 
                        border_color= "#4A5C6A",
                        options=[
                                ft.dropdown.Option("DEC"),
                                ft.dropdown.Option("BIN"),
                                ft.dropdown.Option("TER"),
                                ft.dropdown.Option("CUA"),
                                ft.dropdown.Option("OCT"),
                                ft.dropdown.Option("HEX"),
                                ],
                            label="Base",
                            on_change= limpiar_salida,
                            value="DEC"
                        )

    # Botón para realizar la conversión de números
    boton_operar_sistemas = ft.ElevatedButton( 
        "Operar",
        bgcolor= "#20ac8b",
        color= "#f1fcf8",
        icon=icons.CLEAR,
        icon_color="#cff8ea",
        on_click= conversion_numerica
    )

    # Botón para limpiar los campos de entrada y salida
    boton_limpiar_sistemas = ft.ElevatedButton( 
        "Limpiar",
        bgcolor= "#20ac8b",
        color= "#f1fcf8",
        icon=icons.BACKSPACE,
        icon_color="#cff8ea",
        on_click= limpieza_entradas
    )

    # Definición de filas y columnas
    # Fila que contiene el título y el botón de información
    fila1 = ft.Row(controls=[titulo_conversion,informacion_sistema],
                alignment="CENTER",
                spacing=5)

    # Fila que contiene el campo de entrada y el dropdown de la base numérica de entrada
    fila2 = ft.Row(controls=[numero_entrada,opciones_numericas],
                alignment="CENTER")

    # Fila que contiene el campo de salida y el dropdown de la base numérica de salida
    fila3 = ft.Row(controls=[numero_salida,opciones_numericas_salida],
                alignment="CENTER")

    # Fila que contiene los botones de operar y limpiar
    fila4 = ft.Row(controls=[boton_operar_sistemas,boton_limpiar_sistemas],
                alignment="CENTER",
                spacing= 40)

    # Columna que contiene todas las filas
    columna_datos_numericos = ft.Column(controls=[fila1,fila2,fila3,fila4],
                alignment="CENTER",
                spacing=80
                )

    # Contenedor que contiene la columna de datos numéricos
    container_conversor = ft.Container(
        columna_datos_numericos,
        height=550,
        width=600,
        gradient=LinearGradient(['#f1fcf8', '#cff8ea']),
        border=border.all(2, '#178a71'),
        bgcolor= "#cff8ea",
        border_radius= 15,
        margin = margin.only(
            top=8,
            left=330
        ),
        #alignment="CENTER"
        )

    
    """
        Cambio de Pestañas
    """
    
    def changetab(e):
        """
        Cambia entre las pestañas de la barra de navegación.
        """
        # Obtiene el índice de la pestaña seleccionada
        my_index = e.control.selected_index
        # Muestra el contenido de la pestaña correspondiente según el índice
        tab_1.visible = True if my_index == 0 else False
        tab_2.visible = True if my_index == 1 else False
        # Actualiza la página para reflejar los cambios
        page.update()

    # Barra de navegación con dos destinos: "Gauss Seidel" y "Conversión de Números"
    page.navigation_bar = NavigationBar(
        bgcolor="#a0efd6",
        on_change=changetab,  # Llama a la función changetab cuando cambia la pestaña
        selected_index = 0,  # Inicialmente selecciona la primera pestaña
        destinations = [
            NavigationDestination(icon="home", label="Gauss Seidel"),  # Pestaña 1: Gauss Seidel
            NavigationDestination(icon="explore", label="Conversión de Numeros"),  # Pestaña 2: Conversión de Números
        ]
    )

    # Asigna el contenido de las pestañas a variables
    tab_1 = fila_contenedores  # Contenido de la pestaña 1
    tab_2 = container_conversor  # Contenido de la pestaña 2

    # Agrega un contenedor que contiene el contenido de las pestañas a la página
    page.add(
        Container(
            content=Column([
                tab_1,  # Agrega el contenido de la pestaña 1
                tab_2   # Agrega el contenido de la pestaña 2
            ])
        ),
    )



# Modo Desktop:
ft.app(target=main)

# Modo Web:
