# repo_tag

## Acesse o link abaixo e experimente a aplicação hospedada no heroku

- [repo-tag](https://repo-tag.herokuapp.com/)

## Preparação do ambiente

Para preparar o ambiente, você pode seguir os passos abaixo utilizando o docker e o docker-compose. Para isso, baixo-os e instale de acordo com os links abaixo.
  - [Download docker](https://docs.docker.com/engine/installation/)
  - [Download docker-compose](https://docs.docker.com/compose/install/)
  
  
  - Após clonar o projeto, entre na pasta raíz:

  `cd repo_tag`

  - Construa as imagens do docker:

  `sudo docker-compose build`

  - Prepare o banco de dados realizando as migrações pelos comandos:

  `sudo docker-compose run web python manage.py makemigrations`

  `sudo docker-compose run web python manage.py migrate`
  
## Rodando Aplicação

  - Após a preparação do ambiente, suba o container docker pelo comando

  `sudo docker-compose up`
  
  - Acesse o seu localhost:8000
