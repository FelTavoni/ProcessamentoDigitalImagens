import sys
import numpy as np
import matplotlib.pyplot as plt

def filtro_geometrico(path):
    """
    Desc.: Implemeta o filtro de média geométrica.
    I: Uma imagem path
    O: A imagem X resultante da aplicação do filtro.
    """
    print("Qual a dimensão do filtro? (1 valor apenas)")
    tamanho_filtro = int(input())
    tamanho_filtro_ext = tamanho_filtro//2

    img = plt.imread(path)
    grade = img.shape                                             
    linhas = grade[0]                                             
    colunas = grade[1]                                            
    dimensoes = grade[2] if (len(grade) == 3) else 1              

    # Extendendo a borda da imagem utilizando a técnica "wraparound".
    img_ext = np.pad(img, (tamanho_filtro_ext, tamanho_filtro_ext), mode='wrap')

    # Essa variável armazenará a imagem resultante.
    img_filtrada = np.zeros((linhas, colunas, dimensoes))

    # O coeficiente da raíz da média geométrica
    raiz = 1 / (tamanho_filtro * tamanho_filtro)
    
    # Para imagens coloridas, temos de calcular a suavização para os 3 níveis RGB, senão a trasparência...
    if len(grade) >= 3:
        for i in range(dimensoes):
            for lin in range(linhas):
                for col in range(colunas):
                    mult = np.product(img_ext[lin:lin + tamanho_filtro,
                                      col:col + tamanho_filtro, i],
                                      dtype=np.longdouble)
                    img_filtrada[lin, col, i] = mult**raiz
    # Já em caso de imagens monocromáticas, uma única dimensão deve ser processada.
    else:
        # Processo idêntico ao anterior, no entanto, adaptado a apenas uma dimensão.
        for i in range(dimensoes):
            for lin in range(linhas):
                for col in range(colunas):
                    mult = np.product(img_ext[lin:lin+tamanho_filtro, col:col+tamanho_filtro], dtype=np.longdouble)
                    img_filtrada[lin, col] = mult**raiz

    plt.imshow(img_filtrada, vmin=0, vmax=255)
    plt.title('Filtrada')
    plt.savefig("Result.png")

    return img_filtrada


if __name__ == "__main__":
    img = filtro_geometrico(sys.argv[1])
