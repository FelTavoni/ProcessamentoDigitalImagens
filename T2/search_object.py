import sys
import cv2
import numpy as np
import scipy.signal
import matplotlib.pyplot as plt

def search_object(img_path, obj_path):
	"""
    Desc.: Procura determinado objeto em uma imagem, o qual pode varia em sua luminosidade.
    I: O caminho de uma imagem (img_path) e o caminho para a imagem de um objeto (obj_path).
    O: A imagem X plotada com um retângulo desenhado.
    """

    # Lendo as imagens e as convertendo em float.
	img = plt.imread(img_path)
	img = img.astype(float)
	obj = plt.imread(obj_path)
	obj = obj.astype(float)

	# print(img.shape)
	# print(obj.shape)

	# Cálculo da diferença quadrática utilizando correlação cruzada.
	diff = square_correlation(img, obj)
	plt.imshow(diff, 'gray')
	plt.show()

	# Localizando a posição mínima na imagem.
	pos = find_minimum(diff)

	# Desenhando o retângulo para localização da imagem e apresentando o resultado final.
	foundObj = draw_rectangle(img, pos, obj.shape)
	plt.imshow(foundObj, 'gray')
	plt.show()

def square_correlation(img, obj):
	"""
    Desc.: Calcula a diferença quadrada na imagem via correlação cruzada.
    I: Uma imagem (img) e o objeto a ser buscado (obj).
    O: Uma imagem com a diferença.
    """
	w = np.ones(obj.shape)
	imgOw = scipy.signal.correlate(img**2, w, mode='same')
	imgOobj = scipy.signal.correlate(img, obj, mode='same')

	img_diff = imgOw + np.sum(obj**2) - 2*imgOobj

	# Removendo as bordas...
	half_num_row_obj = obj.shape[0]//2
	half_num_col_obj = obj.shape[1]//2
	img_diff_center = img_diff[half_num_row_obj:-half_num_row_obj, 
	                    		half_num_col_obj:-half_num_col_obj]

	return img_diff

def draw_rectangle(img, center, size):
	"""
	Desc: Desenha um quadrado no objeto a ser buscado.
	"""
	half_num_rows_obj = size[0]//2
	half_num_cols_obj = size[1]//2

	img_rectangle = img.copy()
	pt1 = (center[1]-half_num_cols_obj, center[0]-half_num_rows_obj)
	pt2 = (center[1]+half_num_cols_obj, center[0]+half_num_rows_obj)
	cv2.rectangle(img_rectangle, pt1=pt1, pt2=pt2, color=255, thickness=3)

	return img_rectangle

def find_minimum(img):
    """
	Encontra o valor mínimo na matriz e sua posição.
    """
    num_rows, num_cols = img.shape
    menor_valor = img[0,0]
    indice_menor_valor = (0, 0)
    for row in range(num_rows):
    	for col in range(num_cols):
    		valor = img[row,col]
    		if valor<=menor_valor:
    			menor_valor = valor
    			indice_menor_valor = (row, col)
    			print(menor_valor, indice_menor_valor)

    return indice_menor_valor

if __name__ == "__main__":
	img_path = sys.argv[1]
	obj_path = sys.argv[2]
	search_object(img_path, obj_path)