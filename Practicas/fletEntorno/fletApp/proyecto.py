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
        columnatemporal = matrix_size(int(slider_size.value)) 
        columna_Matriz_A.controls = columnatemporal 
        
        columnatemporal = array_size(int(slider_size.value), 80, False) 
        columna_vector_X.controls = columnatemporal 
        
        columnatemporal = array_size(int(slider_size.value), 80, False) 
        columna_vector_resultado.controls = columnatemporal 
        page.update()
        
    # Contenedor A (Inicializaciones)
        
    def limitar_caracteres(e): 
        if len(e.control.value) > 3:
              e.control.value = e.control.value[:3]
        page.update()

    def matrix_size(rowNumbers):
        filas = []
        columnas = []
        for i in range(rowNumbers):
            filas = []
            for j in range(rowNumbers):
                filas.append(
                    TextField(
                        bgcolor="#cff8ea",
                        text_size=14,
                        border_radius=15,
                        value="",
                        cursor_color="black",
                        color="#176e5d",
                        text_align='left',
                        on_change=limitar_caracteres,
                        width=60,
                        height=50,
                        input_filter=ft.InputFilter(allow=True,regex_string=[0,1,2,3,4,5,6,7,8,9],replacement_string="")
                        #padding=5
                    )
                )
            columnas.append(
                Row(
                    controls=filas,
                    alignment="CENTER"
                )
            )
        return columnas
    
    titulo_matriz_A = ft.Text("Matriz A", #Se define el titulo para el primer contenedor
                       theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM,
                       weight=ft.FontWeight.BOLD,
                       size=16,
                       color="#9BA8AB",
                       text_align="CENTER")
        
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
        on_change=ajusteMatriz
    )
    
    fila_titulos = Row(
        controls=[
            titulo_matriz_A,
            slider_size
        ],
        alignment="CENTER"
    )
    
    columna_temporal = matrix_size(3)
    
    columna_Matriz_A = Column(
        controls=columna_temporal,  
        alignment="CENTER",
        height=400
    )
    
    # Botones A
    
    def limpieza_matrices(e):
        for i in range(int(slider_size.value)):
            columna_vector_X.controls[i].value = ""
            columna_vector_resultado.controls[i].value = ""
            for j in range(int(slider_size.value)):
                columna_Matriz_A.controls[i].controls[j].value = ""
        e.bgcolor="#20ac8b"
        page.update()
    
    boton_limpiar = ft.ElevatedButton( 
        "Limpiar",
        bgcolor= "#20ac8b",
        color= "#f1fcf8",
        icon=icons.BACKSPACE,
        icon_color="#cff8ea",
        on_click=limpieza_matrices
    )
    
    def operacionMatriz(e):
        try:
            lista_matriz = []
            lista_vector = []
            for i in range(int(slider_size.value)):
                    lista_vector.append(float(columna_vector_X.controls[i].value))
                    for j in range(int(slider_size.value)):
                        lista_matriz.append(float(columna_Matriz_A.controls[i].controls[j].value))
            resultadolista = []
            resultadolista = funciones.GaussSeidel(funciones.creacionMatriz(int(slider_size.value),lista_matriz),funciones.creacionVector(int(slider_size.value),lista_vector))
            for i in range(len(resultadolista)):
                    stringtemporal = str(resultadolista[i])
                    stringtemporal = str(round(float(stringtemporal),1))
                    columna_vector_resultado.controls[i].value = stringtemporal
            page.update()
        except:
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
            columna_vector_X.controls[i].value = randint(1,10)
            columna_vector_resultado.controls[i].value = ""
            for j in range(int(slider_size.value)):
                columna_Matriz_A.controls[i].controls[j].value = randint(1,10)
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
        columnas = []
        for i in range(rowNumbers):
            columnas.append(
                    TextField(
                        bgcolor="#cff8ea",
                        text_size=14,
                        border_radius=15,
                        value="",
                        cursor_color="black",
                        color="#176e5d",
                        text_align='left',
                        on_change=limitar_caracteres,
                        read_only=booleano,
                        width=width,
                        height=50,
                        input_filter=ft.InputFilter(allow=True,regex_string=[0,1,2,3,4,5,6,7,8,9],replacement_string="")
                        #padding=5
                    )
                )
        return columnas
    
    titulo_matriz_X = ft.Text("Matriz X   ", #Se define el titulo para el primer contenedor
                       theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM,
                       weight=ft.FontWeight.BOLD,
                       size=16,
                       color="#9BA8AB")
        
    fila_titulosX = Row(
        controls=[
            titulo_matriz_X
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
    
    columna_temporal_resultado = array_size(3, 125, True)
    
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
        gradient=LinearGradient(['#f1fcf8', '#cff8ea']),
        border_radius=20,
        border=border.all(2, '#178a71'),
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
        page.dialog = dialogo_alerta_info
        dialogo_alerta_info.open = True
        page.update()
        
    def limpiar_salida(e): 
        numero_salida.value = ""
        page.update()
        
    def cambio_parametros(e): 
        numero_entrada.value = ""
        numero_salida.value = ""
        if str(opciones_numericas.value) == str(None):
            numero_entrada.read_only = True
        else:
            numero_entrada.read_only = False
            if str(opciones_numericas.value) == "DEC":
                numero_entrada.input_filter=ft.InputFilter(allow=True,regex_string=[0,1,2,3,4,5,6,7,8,9],replacement_string="")
            elif str(opciones_numericas.value) == "BIN":
                numero_entrada.input_filter=ft.InputFilter(allow=True,regex_string=[0,1],replacement_string="")
            elif str(opciones_numericas.value) == "TER":
                numero_entrada.input_filter=ft.InputFilter(allow=True,regex_string=[0,1,2],replacement_string="")
            elif str(opciones_numericas.value) == "CUA":
                numero_entrada.input_filter=ft.InputFilter(allow=True,regex_string=[0,1,2,3],replacement_string="")
            elif str(opciones_numericas.value) == "OCT":
                numero_entrada.input_filter=ft.InputFilter(allow=True,regex_string=[0,1,2,3,4,5,6,7],replacement_string="")
            elif str(opciones_numericas.value) == "HEX":
                numero_entrada.input_filter=ft.InputFilter(allow=True,regex_string=[0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F','a','b','c','d','e','f'],replacement_string="")
        page.update()
        
    def conversion_numerica(e): 
        baseEntrada = 0
        baseSalida = 0
        if numero_entrada.value == "": 
            requerimientosalerta = ft.AlertDialog(title=ft.Text("Falta el valor de entrada"),
                                content=ft.Text("No se ha ingresado ningún número o valor de entrada.")
                                )
            page.dialog = requerimientosalerta
            requerimientosalerta.open = True
        
        elif str(opciones_numericas.value) == str(None) or str(opciones_numericas_salida.value) == str(None): #Validación para cuando los Dropdown no tienen alguna base seleccionada
            requerimientosalerta = ft.AlertDialog(title=ft.Text("Faltan bases numéricas por definir."),
                                content=ft.Text("Revisa las bases de entrada y salida.")
                                )
            page.dialog = requerimientosalerta
            requerimientosalerta.open = True

        else:

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

            if baseEntrada == 10:
                if baseSalida == 10: 
                        numero_salida.value = str(valorEntrada)
                elif baseSalida == 16: 
                        cadena = hex(int(valorEntrada))
                        cadena = cadena[2:]
                        cadena = cadena.upper()
                        numero_salida.value = cadena
                else: 
                    numero_salida.value = funciones.fromDEC(valorEntrada,baseSalida)
            else: 
                valorEntrada = funciones.toDEC(valorEntrada,baseEntrada)
                if baseSalida == 10: 
                        numero_salida.value = str(valorEntrada)
                elif baseSalida == 16: 
                        cadena = hex(int(valorEntrada))
                        cadena = cadena[2:]
                        cadena = cadena.upper()
                        numero_salida.value = cadena
                else: 
                    numero_salida.value = funciones.fromDEC(valorEntrada,baseSalida)
        page.update()
        
    def limpieza_entradas(e): 
        numero_entrada.value = ""
        numero_salida.value = ""
        page.update()
    
    # Titulos
    
    titulo_conversion = ft.Text("Conversión de numeros", 
                        theme_style=ft.TextThemeStyle.HEADLINE_LARGE,
                        weight=ft.FontWeight.BOLD,
                        size=30,
                        color="#9BA8AB"
                    )
        
    dialogo_alerta_info = ft.AlertDialog(title=ft.Text("Bases de Sistemas Numéricos"), #Dialogo de alerta/información que se ejecuta al presionar botón de Información
                                content=ft.Text("DEC = Decimal (Base 10)\nBIN = Binario (Base 2)\nTER = Terciario (Base 3)\nCUA = Cuaternario(Base 4)\nOCT = Octal (Base 8)\nHEX = Hexadecimal (Base 16)")
                                )

    informacion_sistema = ft.IconButton(
        icon= ft.icons.INFO_ROUNDED,
        icon_color= "#4A5C6A",
        on_click= abrir_informacion_sistema
    )

    # Text fields y dropdowns

    numero_entrada = ft.TextField( 
        width=280,
        height=40,
        hint_text= 'Numeros de Entrada',
        border ='underline',
        border_color="#174a3f",
        color ='black',
        read_only= False,
        input_filter=ft.InputFilter(allow=True,regex_string=[0,1,2,3,4,5,6,7,8,9],replacement_string=""),
        on_change=limpiar_salida
    )

    numero_salida = ft.TextField( 
        width=280,
        height=40,
        hint_text= 'Numeros de Salida',
        border ='underline',
        color ='black',
        read_only= True
    )
    
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
                                    #focused_bgcolor="#176e5d",
                                    on_change=cambio_parametros,
                                    value="DEC"
                            )

    

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

    boton_operar_sistemas = ft.ElevatedButton( 
        "Operar",
        bgcolor= "#20ac8b",
        color= "#f1fcf8",
        icon=icons.CLEAR,
        icon_color="#cff8ea",
        on_click= conversion_numerica
    )

    boton_limpiar_sistemas = ft.ElevatedButton( 
        "Limpiar",
        bgcolor= "#20ac8b",
        color= "#f1fcf8",
        icon=icons.BACKSPACE,
        icon_color="#cff8ea",
        on_click= limpieza_entradas
    )
    

    
    fila1 = ft.Row(controls=[titulo_conversion,informacion_sistema],
                alignment="CENTER",
                spacing=5)
    
    fila2 = ft.Row(controls=[numero_entrada,opciones_numericas],
                alignment="CENTER")
    fila3 = ft.Row(controls=[numero_salida,opciones_numericas_salida],
                alignment="CENTER")
    fila4 = ft.Row(controls=[boton_operar_sistemas,boton_limpiar_sistemas],
                alignment="CENTER",
                spacing= 40)
    columna_datos_numericos = ft.Column(controls=[fila1,fila2,fila3,fila4],
                alignment="CENTER",
                spacing=80
                )
    
    container_conversor = ft.Container(
        columna_datos_numericos,
        height=550,
        width=600,
        gradient=LinearGradient(['#f1fcf8', '#cff8ea']),
        border=border.all(2, '#178a71'),
        bgcolor= "#cff8ea",
        border_radius= 15,
        margin = margin.only(
            top=15,
            left=270
        ),
        #alignment="CENTER"
        )

    
    """
        Cambio de Pestañas
    """
    
    def changetab(e):
	# GET INDEX TAB
        my_index = e.control.selected_index
        tab_1.visible = True if my_index == 0 else False
        tab_2.visible = True if my_index == 1 else False
        page.update()


    page.navigation_bar = NavigationBar(
    bgcolor="#a0efd6",
    on_change=changetab,
    selected_index = 0,
    destinations = [
        NavigationDestination(icon="home", label="Gauss Seidel"),
        NavigationDestination(icon="explore", label="Conversión de Numeros"),
    ]
    )

    tab_1 = fila_contenedores
    tab_2 = container_conversor

    page.add(
        Container(

        content=Column([
                    tab_1,
                    tab_2
                ])
        

        ),
    )
        #fila_contenedores)


# Modo Desktop:
ft.app(target=main)

# Modo Web:
