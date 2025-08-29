import graphviz
import os

RUTA_DOT = r"C:\Users\aliso\OneDrive\Documentos\USAC\Cuarto semestre\Programación\IPC2\Proyecto1\Graficasdot"
RUTA_PNG = r"C:\Users\aliso\OneDrive\Documentos\USAC\Cuarto semestre\Programación\IPC2\Proyecto1\Graficas"

def generar_grafica(matriz, titulo, lista_filas, lista_columnas, nombre_base):
    try:
        ruta_dot = os.path.join(RUTA_DOT, f"{nombre_base}.dot")
        ruta_png = os.path.join(RUTA_PNG, nombre_base)

        contenido_dot = f'''digraph G {{
    rankdir = "TB";
    node [shape = none, fontname = "Arial"];
    
    titulo [label = "{titulo}", fontsize = "18"];
    
    matriz [label = <<table border="1" cellborder="1" cellspacing="0" cellpadding="6">
'''

        contenido_dot += '        <tr><td bgcolor="#f0f0f0"></td>'
        for j in range(lista_columnas.tamanio()):
            sensor = lista_columnas.obtener_en(j)
            contenido_dot += f'<td bgcolor="#e8e8e8"><b>{sensor.id}</b></td>'
        contenido_dot += '</tr>\n'

        for i in range(lista_filas.tamanio()):
            estacion = lista_filas.obtener_en(i)
            contenido_dot += f'        <tr><td bgcolor="#e8e8e8"><b>{estacion.id}</b></td>'
            for j in range(lista_columnas.tamanio()):
                reg = matriz.extraer(i, j)
                bg = "#d0f0d0" if reg.valor > 0 else "#ffffff"
                contenido_dot += f'<td bgcolor="{bg}">{reg.valor}</td>'
            contenido_dot += '</tr>\n'
        contenido_dot += '    </table>>, shape = plain];\n\n'
        contenido_dot += '    titulo -> matriz [style = invis];\n'
        contenido_dot += '}'

        with open(ruta_dot, 'w', encoding='utf-8') as f:
            f.write(contenido_dot)

        dot = graphviz.Source(contenido_dot)
        dot.render(ruta_png, format='png', cleanup=True)

        # === 4. Mensaje final ===
        print("\n" + "="*60)
        print(f"Archivo .dot generado: {ruta_dot}")
        print(f"Gráfica generada: {ruta_png}.png")
        print("="*60)

    except Exception as e:
        print(f"\nError al generar gráfica: {e}")