import sys
import numpy as np
import matplotlib.pyplot as plt

# Implemeta o filtro de média geométrica.
# Input: Uma imagem x
# Output: A imagem X resultante da aplicação do filtro.
def filtro_geometrico(path):

    # De ínicio, recebemos a dimensão do filtro a partir da entrada do usuário. Isso ira determinar o quanto de vizinhança deve ser
    #   levado em consideração.
    print("Qual a dimensão do filtro? (1 valor apenas)")
    tamanho_filtro = int(input())
    tamanho_filtro_ext = tamanho_filtro//2

    img = plt.imread(path)
    grade = img.shape                                             # Obtém a grade da imagem, suas dimensões.
    linhas = grade[0]                                             # Número de linhas.
    colunas = grade[1]                                            # Número de colunas.
    dimensoes = grade[2] if (len(grade) == 3) else 1              # Em caso de imagem colorida, imagem possui mais que 1 dimensão..

    # Como o filtro geométrico tem um fator multiplicativo com seus vizinho, elementos da borda podem tever valores muito inferiores
    #   quando comparados a elementos mais próximos ao centro da imagem se preenchidos com 0. Assim, utilizamos a técnica wraparound
    #   para tratar o problema de borda. Lembre-se de que o tamanho do filtro depende da entrada.
    img_ext = np.pad(img, (tamanho_filtro_ext, tamanho_filtro_ext), mode='wrap')

    # Essa variável armazenará a imagem resultante.
    img_filtrada = np.zeros((linhas, colunas, dimensoes))

    # A variável abaixo mantém o expoente da raíz a ser extraída. Isso evitará que seja multiplicado inúmeras vezes dentro do loop.
    raiz = 1 / (tamanho_filtro * tamanho_filtro)

    # Para imagens coloridas, temos de calcular a suavização para os 3 níveis RGB, senão a trasparência...
    if len(grade) >= 3:
        # Em caso de imagens coloridas, temos de calcular o fltro para cada uma se suas composições RGB. Caso seja cinza, teremos apenas
        #   uma dimensão, portanto o for a seguir executará apenas uma vez!
        for i in range(dimensoes):
            # Com a biblioteca numpy, fica fácil implementar o filtro geométrico. Como apresentado no READMe, o filtro geométrico obtém
            #   os valores vizinhos e os multiplica, extraindo a raíz dependendo da dimensão da matriz, calculada anteriormente.
            for lin in range(linhas):
                for col in range(colunas):
                    # Calculando a multiplicação da região...(usar tipo long double devido valores altos)
                    mult = np.product(img_ext[lin:lin+tamanho_filtro, col:col+tamanho_filtro, i], dtype=np.longdouble)
                    # ...e então tira a raíz (pela técnica de exponenciação)...
                    img_filtrada[lin, col, i] = mult**raiz
    # Já em caso de imagens monocromáticas, uma única dimensão deve ser processada.
    else:
        # Processo idêntico ao anterior, no entanto, adaptado a apenas uma dimensão.
        for i in range(dimensoes):
            for lin in range(linhas):
                for col in range(colunas):
                    mult = np.product(img_ext[lin:lin+tamanho_filtro, col:col+tamanho_filtro], dtype=np.longdouble)
                    img_filtrada[lin, col] = mult**raiz

    # Aqui, já teremos em mão a imagem filtrada. Então as plotamos para mostrar o retultado.
    plt.imshow(img_filtrada, vmin=0, vmax=255)
    plt.title('Filtrada')
    plt.savefig("Result.png")

    # Retorna a imagem para ser escrita.
    return img_filtrada


if __name__ == "__main__":
    img = filtro_geometrico(sys.argv[1])