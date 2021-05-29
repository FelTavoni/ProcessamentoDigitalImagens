# Trabalho 1 - Filtros Não-Lineares (Em desenvolvimento...)

O trabalho 1 da disciplina de *Processamento Digital de Imagens* consiste em implementar os filtros *média geométrica* e de *mediana* em imagens.

**- Remover -**

- Explicação do método implementado;
- Motivação do uso do método (porque usar? Em que situações ele é importante?);
- Explicação da parte mais importante do código.

**- Remover -**

Os **filtros não-lineares** se diferem de **filtros lineares** pois têm como característica principal o uso de alguma função não-linear ao processar as imagens, ou seja, qualquer filtro que não se apresente como uma relação ponderada dos pixels. Por isso, acabam sendo mais custosos computacionalmente.

Filtros não-lineares são comumente utilizados para alterar uma imagem sem diminuir sua resolução, intencionados a minimizar/realçar ruídos, além de suavizar/realçar bordas de objetos.

## Filtro geométrico

O filtro de média geométrica consiste em implementar um filtro conforme a função abaixo.

<img src=".\images\MediaGeom.png" alt="Média Geométrica" width="45%" style="display: block; margin: auto;">

A partir dele, dado o tamanho de um filtro, a média geométrica será correspondente ao valor da multiplicação dos vizinhos, conforme definido pelo filtro, extraindo por fim a n-ésima raíz do conjunto. 

O filtro de média geométrica obtém uma suavização próxima à aplicação do filtro de média aritmética, mas tende a perder menos detalhes da imagem no processo.

## Filtro mediana

O filtro da mediana, por sua vez, troca o valor do pixel pelo valor médio (mediana) de intensidade presente nos pixes da vizinhança, definido pelo filtro. Pode ser definida como:

<img src=".\images\Mediana.png" alt="Média Geométrica" width="45%" style="display: block; margin: auto;">

Os filtros de mediana são populares pois, para certos tipos de ruídos, eles providenciam uma capacidade excelente para a redução de ruídos, com menos "embaçamento" quando comparados a filtros lineares de tamanhos equivalentes. São bem efetivos na presença de ruídos de impulso bipolar e unipolar.

## Execução

### Como executar

A execução do filtro geométrico deve seguir a seguinte forma:

`python filtro_geometrico.py <caminho-da-imagem>`

Executado o código, será então retornada uma imagem que será armazenada no diretório em que o programa se encontra, com uma extensão *.png*.

Também é possível executar o código a partir da imagem de docker descrita no
Dockerfile no diretório da seguinte maneira:

```
docker run -d --name <nome_do_container> -p 8888:8888 -v $PWD:/home/jovyan/work pdiwk
```

Lembrando que para acessar a o servidor na web é necessário saber o token de
autenticação para tanto é necessário entrar no container com `docker exec -it
<nome_do_container> bash` e executar `jupyter lab list`.

### Executando os Testes

--

### Ferramentas Utilizadas

- [Python v3.9.5](https://www.python.org/)
    - [Numpy v1.20.0](https://numpy.org/)
    - [Matplotlib v3.4.2](https://matplotlib.org/)

### Referências

- Digital Image Processing, 4th Edition - Rafael C. Gonzales, Richard E. Woods.

## Autores

*Graduandos da Universidade Federal de São Carlos.*

- **Felipe Tavoni**

- **Gabriel Rodrigues Malaquias**

- **Lucas Cruz do Reis**

- **Renan Bobadilla Morelli**
