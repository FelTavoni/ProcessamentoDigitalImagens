# Trabalho 1 - Filtros Não-Lineares (Em desenvolvimento...)

O trabalho 1 da disciplina de *Processamento Digital de Imagens* consiste em implementar os filtros *média geométrica* e de *mediana* em imagens.

**Remover**

- Explicação do método implementado;
- Motivação do uso do método (porque usar? Em que situações ele é importante?);
- Explicação da parte mais importante do código.

**Remover**

## Filtro geométrico

O filtro de média geométrica consiste em implementar um filtro conforme a função abaixo.

<img src=".\images\MediaGeom.png" alt="Média Geométrica" width="40%" style="display: block; margin: auto;">

Com isso, dado o tamanho de um filtro, a média geométrica será correspondente ao valor da multiplicação dos vizinhos, conforme o tamanho do filtro,  extraindo por fim a n-ésima raíz do conjunto.

## Começando

### Pré-requisitos

--

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

## Autores

*Graduandos da Universidade Federal de São Carlos.*

- **Felipe Tavoni**

- **Gabriel Rodrigues Malaquias**

- **Lucas Cruz do Reis**

- **Renan Bobadilla Morelli**
