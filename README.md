# Reconhecimento de empresas de avião usando deeplearning

Esse projeto busca resolver o problema proposto pela cyberlabs (ler o outro readme para mais detalhes)

## Getting Started

Usando classificação supervisionada vamos aplicar redes neurais profundas para automaticamente distinguir a identidade visual de duas empresas de tranporte aereo (TAP e KLM)

### Prerequisitos
Para o codigo, foram usados dois virtual environments, um com python 2.7 e scrapy (pois algumas dependencias do scrapy não são compativeis com o python 3.x) e outro com python 3.7, tensorflow = 2.0 e pillow (biblioteca necessariam para o carregamento de fotos)

### Construindo o dataset

Parte do desenho foi montar nosso proprio dataset, que no momento se encontra no link: https://drive.google.com/open?id=1Yo6W6OZf7pq0VgqLDAYn8GQlaiSOpyp0

ele foi construido usando scrapy, então para criar o mesmo dataset, vá até a pasta scraper e rode:

```
#para baixar as fotos da KLM
scrapy crawl airplanes
#para baixar as fotos da TAP
scrapy crawl airplanestap
```
### dificuldades na construção do dataset

Como queriamos raspar o sistema de persquisa do site airliners, foi necessario configurar o scraper para ignorar o robot.txt do site

### treinamento da rede neural
O codigo foi treinado usando TensorFlow 2.0 como backend numa placa GTX 1060

### instalando


O arquivo possui 4 notebooks:

move files: responsavel por deixar os arquivos da forma como foram preparados pelo scrper no modelo como a keras API prefere

pipeline: responsavel pelo trabalho de load e e treino da rede neural

Predict_image: um pequeno preditor onde você pode usar o modelo em uma unica foto (divirta-se :) )

Predict: o que será usado pelo usuario para testar os seus proprios casos

### testes e mais teste

Uma arquitetura que já se provou neste trabalho foi a vgg, fiz testes com vgg de apenas um bloco ou mais, porem houve pouco ganho em accuracia, assim, preferi ficar com a vgg16 que já havia se provado em outros datasets

Estranhamente os testes com vgg16 costumavam inicialmente apresentar algo como 97% de acerto e depois diminuir, o que suponho que está relacionado com overfittings

Essa arquitetura já usa varias tecnicas interessantes como dropout e transfer learning, não continuei o treino pois a arquitetura já era melhor separando as companhias que eu a priori(e é assim que começa a era das maquinas) pois essas empresas possuem modelos de aviões com uma identidade visual diferente da usual, que não estou acostumado a ver, mas que a maquina se acostumou rapidamente, o que segue uma impressão minha de que algoritmos de classificação de imagens tendem a ir superando seres humanos na medida que os casos se tornam cada vez mais incomuns



## Como usar esse repositorio

### treinando o modelo a partir das fotos que usei

1. Faça o download do arquivo das fotos como extraidas pelo scraper no link a seguir: https://drive.google.com/open?id=1Yo6W6OZf7pq0VgqLDAYn8GQlaiSOpyp0
2. Rode notebook "move files.ipnb", ele automaticamente organizara do jeito que é necessario
3. Rode o notebook "pipeline.ipynb" ele irá automaticamente treinar o modelo usando a arquitetura vgg16
4. Os modelos serão salvos na pasta "model" e você pode colocar o modelo que achar melhor na pasta best model, pois ele automaticamente~usa um dos modelos nesta pasta para fazer as predições (idealmente só deve haver um modelo nela)

### fazendo predições

1. Abra o arquivo "predict.ipynb"
2. Mude a variavel "dataset_path" para a string correspondente ao path do repositorio com as fotos que deseja classificar
3. Rode o arquivo e ele irá automaticamente criar duas pastas no directorio especificado (klm e tap), e irá separar os arquivos nos directorios que ele prever o mais adequado
4. Divirta-se


## Agradecimentos

### links uteis na produção do codigo

1. https://machinelearningmastery.com/how-to-develop-a-convolutional-neural-network-to-classify-photos-of-dogs-and-cats/
2. https://www.pyimagesearch.com/2019/11/04/traffic-sign-classification-with-keras-and-deep-learning/
3. https://www.tensorflow.org/tutorials/keras/classification
4. https://keras.io/