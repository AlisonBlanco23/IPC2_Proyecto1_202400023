import graphviz

def generar_grafica(matriz, titulo, lista_filas, lista_columnas, nombre_base):
    try:
        dot = graphviz.Digraph()
        dot.attr('graph', rankdir='TB')
        dot.node('titulo', titulo, shape='none', fontsize='18', fontname='Arial')

        tabla = ['<<table border="1" cellborder="1" cellspacing="0" cellpadding="6">']

        tabla.append('<tr><td bgcolor="#f0f0f0"></td>')
        for j in range(matriz.columnas):
            sensor = lista_columnas.obtener_en(j)
            tabla.append(f'<td bgcolor="#e8e8e8"><b>{sensor.id}</b></td>')
        tabla.append('</tr>')

        for i in range(matriz.filas):
            estacion = lista_filas.obtener_en(i)
            tabla.append(f'<tr><td bgcolor="#e8e8e8"><b>{estacion.id}</b></td>')
            for j in range(matriz.columnas):
                reg = matriz.extraer(i, j)
                bg = "#d0f0d0" if reg.valor > 0 else "#ffffff"
                tabla.append(f'<td bgcolor="{bg}">{reg.valor}</td>')
            tabla.append('</tr>')
        tabla.append('</table>>')

        dot.node('matriz', ''.join(tabla), shape='plain')
        dot.edge('titulo', 'matriz', style='invis')

        dot.render(nombre_base, format='png', cleanup=True)
        print(f"Gráfica generada: {nombre_base}.png")

    except Exception as e:
        print(f"Error al generar gráfica: {e}")