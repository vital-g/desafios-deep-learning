# Reconhecimento de empresas de avi�o usando deeplearning

Este projeto busca resolver o problema proposto pela cyberlabs (ler o outro readme para mais detalhes: https://github.com/vital-g/desafios-deep-learning/blob/master/README_cyberlabs.md)

## Getting Started

Usando classifica��o supervisionada vamos aplicar redes neurais profundas para automaticamente distinguir a identidade visual de duas empresas de tranporte aereo (TAP e KLM)

### Prerequisitos
Para o codigo, foram usados dois virtual environments, um com python 2.7 e scrapy (pois algumas dependencias do scrapy n�o s�o compativeis com o python 3.x) e outro com python 3.7, tensorflow = 2.0 e pillow (biblioteca necessaria para o carregamento de fotos)

### Construindo o dataset

Parte do desenho foi montar nosso proprio dataset, que no momento se encontra no link: https://drive.google.com/open?id=1Yo6W6OZf7pq0VgqLDAYn8GQlaiSOpyp0

ele foi construido usando scrapy, ent�o para criar o mesmo dataset, v� at� a pasta scraper e rode:

```
#para baixar as fotos da KLM
scrapy crawl airlinersklm
#para baixar as fotos da TAP
scrapy crawl airlinerstap
```
### Dificuldades na constru��o do dataset

Como queriamos raspar o sistema de persquisa do site airliners, foi necessario configurar o scraper para ignorar o robot.txt do site

### Treinamento da rede neural
O codigo foi treinado usando TensorFlow 2.0 como backend numa placa GTX 1060

### Instalando


O arquivo possui 4 notebooks:

move files: responsavel por deixar os arquivos da forma como foram preparados pelo scrper no modelo como a keras API prefere

pipeline: responsavel pelo trabalho de load e e treino da rede neural

Predict_image: um pequeno preditor onde voc� pode usar o modelo em uma unica foto (divirta-se :) )

Predict: o que ser� usado pelo usuario para testar os seus proprios casos

### Testes e mais teste

Uma arquitetura que j� se provou neste trabalho foi a vgg, fiz testes com vgg de apenas um bloco ou mais, porem houve pouco ganho em acuracia, assim, preferi ficar com a vgg16 que j� havia se provado em outros datasets

Os testes com vgg16 costumavam inicialmente apresentar algo como 97% de acerto no teste, mas 89% no treino depois diminuir, o que suponho que est� relacionado com overfittings

Esta arquitetura j� usa varias tecnicas interessantes como dropout e transfer learning. Realizei varios treinos com diferentes quantidades de epocas (epoch) e alterando a quantidade de data utilizado no dataset, mas n�o apresentaram grandes altera��es na acuracia no teste.Minha hipotese para os erros foi, de maneira intuitiva, podemos separar as fotos em 3 categorias: fotos de avi�es iconicos das empresas, fotos de avi�es com identidade visual antiga, ou de subsidiarias e fotos tiradas muito de perto ou de posi��es que n�o permitiam distinguir a empresa (fotos da turbina, ou da camara de pilotos, por exemplo). As fotos de perto s�o uma grande fonte de erros e os caso de subsidiarias exoticas se tornam mais faceis para a maquina do que para os seres humanos j� que ela treina com uma quantidade maior de casos do que humanos.

Algumas tecnicas de pre-processamento, como tirar uma media de cada foto ou dividir o valor dos pixels por uma variancia, n�o foram utilizadas pois aumentaram o tempo necessario para o o calculo, sem adicionar resultados a taxa de acuracia, alem de que, como a identidade visual est� intimamente ligada as cores especificas para criar um reconhecimento imediato. Tambem tentei o uso do algoritmo CLAHE, metodo que aplica algo semelhante a um ajuste de luminosidade em uma foto, mas ele tambem n�o apresentou melhora na acuracia (imagino que foi pois, pela origem das fotos, eas foram todas tiradas por aficcionados por avi�es sempre tomando cuidado com a luminosidade). No mais, como a identidade visual est� intimamente atrelada a cores especificas nos avi�es e dada a falta de ganho na acuracia, decidi n�o usar um pre-processamento

Aumenta��o de dados n�o foi utilizada, principalmente, pois a qunatidade total de dados j� era enorme, causando sobrecargas no hardware, mesmo usando cuDNN.

## Como usar esse repositorio

### Treinando o modelo a partir das fotos que usei

1. Fa�a o download do arquivo das fotos como extraidas pelo scraper no link a seguir: https://drive.google.com/open?id=1Yo6W6OZf7pq0VgqLDAYn8GQlaiSOpyp0
2. Rode notebook "move files.ipnb", ele automaticamente organizara do jeito que � necessario
3. Rode o notebook "pipeline.ipynb" ele ir� automaticamente treinar o modelo usando a arquitetura vgg16
4. Os modelos ser�o salvos na pasta "model" e voc� pode colocar o modelo que achar melhor na pasta best model, pois ele automaticamente~usa um dos modelos nesta pasta para fazer as predi��es (idealmente s� deve haver um modelo nela)

### Fazendo predi��es

1. Abra o arquivo "predict.ipynb"
2. Mude a variavel "dataset_path" para a string correspondente ao path do repositorio com as fotos que deseja classificar
Obs: voc� pode configurar "dataset_path = 'pred'", o que far� o c�digo rodar num mini dataset que separei para esse tipo de teste
3. Rode o arquivo e ele ir� automaticamente criar duas pastas no directorio especificado (klm e tap), e ir� separar os arquivos nos directorios que ele prever o mais adequado

4. Divirta-se


## Agradecimentos

### Links uteis na produ��o do codigo

1. https://machinelearningmastery.com/how-to-develop-a-convolutional-neural-network-to-classify-photos-of-dogs-and-cats/
2. https://www.pyimagesearch.com/2019/11/04/traffic-sign-classification-with-keras-and-deep-learning/
3. https://www.tensorflow.org/tutorials/keras/classification
4. https://keras.io/