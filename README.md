# Currículo do Professor 👨‍🏫

Sistema web completo para gerenciamento do currículo de um professor, incluindo áreas de pesquisa, projetos, publicações, orientações e formulário de contato.

## 🔧 Tecnologias utilizadas

- **Django** (backend, API REST)
- **Django REST Framework**
- **JWT Authentication**
- **SQLite** (banco de dados relacional)

## 📁 Funcionalidades

- Página de apresentação com biografia e foto
- CRUD completo para:
  - Áreas de Pesquisa
  - Projetos (classificados por tipo)
  - Publicações (artigos, livros etc.)
  - Orientações (alunos e trabalhos)
- Formulário de contato funcional
- Painel administrativo (via `/admin`) restrito ao professor
- API protegida com autenticação JWT

## 🚀 Como rodar o projeto localmente

1. Clone este repositório:

```bash
git clone https://github.com/Vanderwitch/curriculo-professor.git
cd curriculo-professor
