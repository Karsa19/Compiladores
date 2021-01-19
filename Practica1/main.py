from automata.af import AF

def main():
    print('Hola mundo')

    af = AF()
    af.cargar_desde('/Users/koren/Dropbox/Compiladores/Practica1/af.txt')
    print("Estados:")
    
    for estado in af.conj_estados:
        print(af.conj_estados[estado])


if __name__ == '__main__':
    main()
