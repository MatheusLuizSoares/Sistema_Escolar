# Sistema_Escolar
# Sistema Academia Dev Python

Sistema de gerenciamento acadêmico simples com Django, PostgreSQL e Docker.

## Funcionalidades

- Cadastro de alunos
- Cadastro de cursos
- Matrículas entre alunos e cursos
- Interface admin
- API REST
- Dockerizado

## Tecnologias

- Python 3.11
- Django
- Django REST Framework
- PostgreSQL
- Docker e Docker Compose
- Bootstrap

## Como rodar o projeto

### Requisitos
- Docker
- Docker Compose

### Passos

```bash
Git Clone: https://github.com/MatheusLuizSoares/Sistema_Escolar.git
cd Sistema_Escolar

docker-compose up --build
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
