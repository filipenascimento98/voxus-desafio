# Desafio Técnico Voxus

Nesse projeto temos a implementação de uma API como solução para o problema apresentado no desafio técnico para o processo seletivo de desenvolvedor Python.

# Tecnologias 
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- Testes Unitários

# Instalação
Para ter acesso a API basta clonar este repositório.
```bash
git clone https://github.com/filipenascimento98/voxus-desafio.git
```

# Como utilizar
Esse projeto tem como dependência o [Docker](https://www.docker.com/) e o [Docker Compose](https://docs.docker.com/compose/). Com as dependências resolvidas, navegue até o diretório do projeto que contém o arquivo __docker_compose.yml__ e execute o seguinte comando que irá buildar e colocar no ar a aplicação: 

```bash
docker-compose up -d
```

Assim, a aplicação será executada em um container Docker.

# Rotas disponíveis
Nessa API temos rotas que retornam piadas do Chuck Norris com base em alguns parâmetros de busca. A documentação das rotas pode ser acessada através do seguinte endpoint:

```bash
{url_base}/docs/
```

# Testes automatizados

Para executar os testes automatizados navegue até o diretório onde se encontra o arquivo __manage.py__ e execute o seguinte comando:

```bash
python manage.py test -b
```