from automata.af import AF


def main():
    print("")
    af = AF()
    af.cargar_desde('/Users/koren/Documents/GitHub/Compiladores/Practica1/af.txt')
    cadena = "ababababaaabb"
    acepta_estatus = af.acepta(cadena)
    if acepta_estatus: print('Cadena aceptada {cadena}'.format(cadena=cadena))
    else: print('Cadena inválida {cadena}'.format(cadena=cadena))

    print("")
    cad = af.generar_cadena(7)
    print("Cadenas válidas")
    print(af.obtener_finales())
    print(af.cadenas_generadas)

    print("")
    af.guardar_en("")


if __name__ == '__main__':
    main()
