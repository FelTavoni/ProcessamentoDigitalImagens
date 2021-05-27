import sys
import numpy as np
import matplotlib.pyplot as plt

def renormalize(img):
    """
    Função de normalização de Imagens
    """
    img_norm = img - np.min(img)
    img_norm = img_norm/np.max(img_norm)
    img_norm = 255*img_norm
    img_norm = img_norm.astype(np.uint8)
    
    # O mesmo que acima em um único comando
    # img_norm = (255*(img-np.min(img))/(np.max(img)-np.min(img))).astype(np.uint8)
    
    return img_norm

def filtro_geometrico(img_path, filter_size):
    """
    Desc.: Implemeta o filtro de média geométrica.
    I: O caminho de uma imagem(img_path), o tamanho do filtro(filter_size)
    O: A imagem X resultante da aplicação do filtro.
    """
    filter_size_ext = filter_size // 2

    img = plt.imread(img_path)
    num_rows, num_cols = img.shape[:2]
    dim = img.shape[2] if (len(img.shape) == 3) else 1

    # Extendendo a borda da imagem utilizando a técnica "wraparound".
    img_ext = np.pad(img, (filter_size_ext, filter_size_ext), mode='wrap')
    # Essa variável armazenará a imagem resultante.
    img_filtered = np.zeros((num_rows, num_cols, dim))
    # O coeficiente da raíz da média geométrica
    exp_root = 1 / (filter_size ** 2)

    # Para imagens coloridas, temos de calcular a suavização para os 3 níveis RGB, senão a trasparência...
    if len(img.shape) >= 3:
        for i in range(dim):
            for row in range(num_rows):
                for col in range(num_cols):
                    mult = np.product(img_ext[row:row + filter_size,
                                      col:col + filter_size, i],
                                      dtype=np.longdouble)
                    img_filtered[row, col, i] = mult**exp_root
    # Já em caso de imagens monocromáticas, uma única dimensão deve ser processada.
    else:
        # Processo idêntico ao anterior, no entanto, adaptado a apenas uma dimensão.
        for i in range(dim):
            for row in range(num_rows):
                for col in range(num_cols):
                    mult = np.product(img_ext[row:row + filter_size,
                                      col:col + filter_size],
                                      dtype=np.longdouble)
                    img_filtered[row, col] = mult**exp_root

    plt.imshow(renormalize(img_filtered), vmin=0, vmax=255)
    plt.title('Filtrada')
    plt.savefig("Result.png")

    return img_filtered


if __name__ == "__main__":
    filter_size = 5
    img = filtro_geometrico(sys.argv[1], filter_size)
