#  Sistema Escolar — Academia Dev Python

Sistema de gerenciamento acadêmico desenvolvido com **Django**, **Django REST Framework**, **PostgreSQL** e totalmente **Dockerizado**.  
Permite administrar **alunos, cursos e matrículas**, oferecendo interface web e API REST completa.

---

##  Funcionalidades

###  Alunos
- Cadastro de alunos  
- Listagem  
- Edição  
- Exclusão  
- API REST completa

###  Cursos
- Cadastro e edição de cursos  
- Status ativo/inativo  
- API REST completa

###  Matrículas
- Relação entre alunos e cursos  
- Registro automático da data  
- Status da matrícula (ativa, cancelada, concluída)  
- API REST completa

###  Recursos adicionais
- Interface administrativa Django  
- Templates HTML com Bootstrap  
- Organização modular (alunos, cursos, matrículas)

---

##  Tecnologias Utilizadas

- **Python 3.11**
- **Django**
- **Django REST Framework**
- **PostgreSQL**
- **Docker & Docker Compose**
- **Bootstrap 5**
- **HTML + Templates Jinja2**


---

##  Como Rodar o Projeto

### **Requisitos obrigatórios**
- Docker  
- Docker Compose  

---

##  Passo a passo

Clone o repositório:

```bash
git clone https://github.com/MatheusLuizSoares/Sistema_Escolar.git
cd Sistema_Escolar
docker-compose up --build -d
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser


