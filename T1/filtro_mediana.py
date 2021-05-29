import sys
import numpy as np
import matplotlib.pyplot as plt

def filtro_mediana(img_path, filter_size):
    """
    Desc.: Implemeta o filtro de média com base na mediana.
    I: O caminho de uma imagem(img_path), o tamanho do filtro(filter_size)
    O: A imagem X resultante da aplicação do filtro.
    """
    filter_size_ext = filter_size // 2

    img = plt.imread(img_path)
    num_rows, num_cols = img.shape[:2]
    dim = img.shape[2] if (len(img.shape) == 3) else 1

    # Extendendo a borda da imagem utilizando a técnica "wraparound".
    img_ext = np.pad(img, (filter_size_ext, filter_size_ext), mode='wrap')

    # Essa variável armazenará a imagem resultante. Não deve ser float64 (padrão), mas sim uint8...
    img_filtered = np.zeros((num_rows, num_cols, dim), dtype=np.uint8)

    # O coeficiente da raíz da média geométrica
    exp_root = 1 / (filter_size ** 2)

    # Para imagens coloridas, temos de calcular a suavização para os 3 níveis RGB, senão a trasparência...
    if len(img.shape) >= 3:
        for i in range(dim):
            for row in range(num_rows):
                for col in range(num_cols):
                    img_filtered[row, col, i] = int(np.median(img_ext[row:row + filter_size,
                                                                col:col + filter_size, i]))

        # Exibindo imagem resultante.
        plt.imshow(img_filtered, vmin=0, vmax=255)

    # Já em caso de imagens monocromáticas, uma única dimensão deve ser processada.
    else:
        # Processo idêntico ao anterior, no entanto, adaptado para apenas uma dimensão.
        for i in range(dim):
            for row in range(num_rows):
                for col in range(num_cols):
                    img_filtered[row, col, i] = int(np.median(img_ext[row:row + filter_size,
                                                                col:col + filter_size]))

        # Imagens monocromaticas devem ser mapeadas para a escala cinza, durante a chamada imshow.
        plt.imshow(img_filtered, cmap='gray', vmin=0, vmax=255)
    
    plt.title('Filtrada')
    plt.axis('off')
    plt.savefig("Result2.tiff")

    return img_filtered


if __name__ == "__main__":
    filter_size = 6
    img = filtro_mediana(sys.argv[1], filter_size)
