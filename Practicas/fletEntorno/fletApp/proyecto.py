import flet as ft
from flet import *
from random import randint
import funciones

# Variables
container = Container(
        gradient=LinearGradient(['#f1fcf8', '#cff8ea']),
        border_radius=20,
        border=border.all(2, '#178a71'),
        blur=ft.Blur(10, 0, ft.BlurTileMode.MIRROR),
        padding=20,
        margin=80
)

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
    
   
    # Matriz Gauss Seidel
    def slider_changed(e):
        print(f"Slider changed to {e.control}")
        page.update()
        
    def ajusteMatriz(e): 
         
        columnatemporal = matrix_size(int(slider_size.value)) #Se obtiene la matriz A con el nuevo tamaño
        columna_Matriz_A.controls = columnatemporal #Se muestra la matriz A con el nuevo tamaño
        
        columnatemporal = array_size(int(slider_size.value), 80, False) #Se obtiene la matriz A con el nuevo tamaño
        columna_vector_X.controls = columnatemporal #Se muestra la matriz A con el nuevo tamaño
        
        columnatemporal = array_size(int(slider_size.value), 80, False) #Se obtiene la matriz A con el nuevo tamaño
        columna_vector_resultado.controls = columnatemporal #Se muestra la matriz A con el nuevo tamaño
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
        alignment="CENTER"
    )
    
    page.add(
        fila_contenedores
    )


# Modo Desktop:
ft.app(target=main)

# Modo Web:
