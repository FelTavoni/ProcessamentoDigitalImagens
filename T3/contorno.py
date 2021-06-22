import sys
import numpy as np
import matplotlib.pyplot as plt

def threshold_otsu(img):
    '''
    Calcula e aplica o limiar de Otsu utilizando o histograma da imagem
    '''
    
    bins = range(0, 257)
    hist, _ = np.histogram(img, bins)
    
    num_pixels = img.shape[0]*img.shape[1] 
    sum_img = np.sum(img)
    m_G = sum_img/num_pixels
    max_sigma_I = -1
    
    sum_back = 0
    num_back = 0
    for threshold in range(0, 256):
        num_back = num_back + hist[threshold]  # Número de pixels com valor menor que threshold
        sum_back = sum_back + threshold*hist[threshold]  # Soma dos valores de pixel background

        num_fore = num_pixels - num_back
        sum_fore = sum_img - sum_back
        
        if num_back == 0 or num_fore == 0:
            continue
        
        P_back = num_back/num_pixels
        P_fore = num_fore/num_pixels
        m_back = sum_back/num_back   
        m_fore = sum_fore/num_fore    
        
        sigma_I = P_back*(m_back-m_G)**2 + P_fore*(m_fore-m_G)**2
        
        if sigma_I > max_sigma_I:
            max_sigma_I = sigma_I
            best_threshold = threshold

    img_bin = np.zeros((img.shape[0], img.shape[1]))

    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            if img[row, col] > best_threshold:
                img_bin[row, col] = 1
    
    return img_bin

def image_contour(img):
    '''
    Obtém o contorno paramétrico de um objeto contido no array img.
    '''
    
    # Mapeamento utilizado para encontrar o vizinho inicial a ser
    # buscado na próxima iteração dado o vizinho do ponto atual
    # Por exemplo, se o ponto atual for (12, 15) e o próximo ponto
    # de borda for (12, 16), isso significa que o vizinho de índice
    # 2 será o próximo ponto de borda. Nesse novo ponto, precisamos
    # buscar a partir do vizinho de índice 1, pois o vizinho de
    # índice 0 foi o último ponto a ser verificado antes de encontrarmos
    # o ponto atual
    neighbor_map = [7, 7, 1, 1, 3, 3, 5, 5]
    
    # Adiciona 0 ao redor da imagem para evitar pontos do objeto tocando a borda
    img_pad = np.pad(img, 1, mode='constant')
    
    num_rows, num_cols = img_pad.shape
    k = 0
    row = 0
    col = 0
    # Busca do primeiro ponto do objeto
    while img_pad[row, col]==0:
        k += 1
        row = k//num_cols
        col = k - row*num_cols
        
    curr_point = (row, col)    # Ponto atual
    contour = [curr_point]     # Pontos do contorno
    starting_index = 2         # Índice do vizinho inicial a ser verificado
    while True:
        next_point, last_index = get_next_point(img_pad, curr_point, starting_index)

        # Novo índice do vizinho inicial baseado no último índice buscado
        starting_index = neighbor_map[last_index]
        
        # Critério de parada. Se o ponto adicionado na iteração anterior (contour[-1])
        # for o mesmo que o primeiro ponto (contour[0]) e o ponto atual for o mesmo
        # que o segundo ponto adicionado, o algoritmo termina. Só podemos fazer essa
        # verificação se o contorno possuir ao menos 2 pontos. Ou seja, nosso algoritmo
        # não está tratando o caso de um objeto com apenas 1 pixel
        if len(contour)>1:
            if next_point==contour[1] and contour[-1]==contour[0]:
                break
                
        contour.append(next_point)
        curr_point = next_point
        
    # Subtrai 1 de cada ponto pois o contorno foi encontrado para a imagem preenchida com 0 na borda
    for point_index, point in enumerate(contour):
        contour[point_index] = (point[0]-1, point[1]-1)
        
    return contour

def get_next_point(img, curr_point, starting_index):
    '''Encontra o próximo ponto de borda dado um ponto
       corrente curr_point e o índice do primeiro vizinho
       a ser verificado (starting_index)'''
     
    # Lista dos pontos vizinhos dado o índice do vizinho
    nei_list = [(-1,0), (-1,1), (0,1), (1,1), 
                (1,0), (1,-1),(0,-1), (-1,-1)]
    
    curr_index = starting_index
    nei_value = 0
    while nei_value==0:
        nei_shift = nei_list[curr_index]
        nei_row = curr_point[0] + nei_shift[0]
        nei_col = curr_point[1] + nei_shift[1]
        nei_value = img[nei_row, nei_col]
        if nei_value==1:
            return (nei_row, nei_col), curr_index
        else:
            curr_index = (curr_index+1)%8

def curvature(cont):
    '''
    Calculo da curvatura ao longo do contorno de objetos.
    '''
    # Suavizando o contorno segundo uma funcao gaussiana
    x = gaussian_suavization_1d(cont[:, 0], 6)
    y = gaussian_suavization_1d(cont[:, 1], 6)

    # Calculo da primeira derivada no eixo x e y.
    dx = np.gradient(x)
    dy = np.gradient(y)

    # Calculo da segunda derivada no eixo x e y.
    ddx = np.gradient(dx)
    ddy = np.gradient(dy)

    # Por fim, o calculo da curvatura
    curvature = ((dx * ddy) - (ddx * dy)) / ((dx**2 + dy**2)**1.5)

    t = range(0, len(curvature))

    plt.figure(figsize=[10,6])
    plt.subplot(1, 2, 1)
    plt.plot(t, curvature)
    plt.title('Normal')
    plt.subplot(1, 2, 2)
    plt.plot(t, curvature)
    plt.title('Suavizado')

    plt.show()

def gaussian_suavization_1d(signal, filter_size):
    sigma = filter_size/6.
    x = np.linspace(-3*sigma, 3*sigma, filter_size)
    y = np.exp(-x**2/(2*sigma**2))
    
    # Filtros de suavização precisam ter soma igual a 1
    y = y/np.sum(y)

    smoothed_signal = np.convolve(signal, y, 'same')

    return smoothed_signal

if __name__ == "__main__":
    # Lendo a imagem e a mostrando.
    img_path = sys.argv[1]
    img = plt.imread(img_path)
    plt.imshow(img, 'gray')
    plt.show()
    print(np.unique(img))

    # Calculando a limiarização de Otsu para apenas 2 únicos valores.
    new_img = threshold_otsu(img)
    plt.imshow(new_img, 'gray')
    plt.show()
    print(np.unique(new_img))

    # Cálculando o contorno paramétrico da imagem.
    new_img = (new_img > 0).astype(np.uint8)
    cont = image_contour(new_img)
    # Transforma o contorno em um array numpy
    cont = np.array(cont)
    plt.figure()
    plt.subplot(111, aspect='equal')
    # Plota os pontos de contorno, precisamos inverter os valores em y porque, na imagem, a origem está no ponto superior esquerdo
    plt.plot(cont[:,1], img.shape[0]-cont[:,0])
    plt.show()

    # Dado o contorno, cálcular a curvatura ao longo do contorno.
    curvature(cont)