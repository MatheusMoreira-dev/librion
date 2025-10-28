1 - Instalar todas as bibliotecas com o comando:
pip install -r requirements.txt

2 - Criar arquivo .env com a chave(para criptografia de dados no banco):
SECRET_KEY = ""

3 - Inicializar o Banco de Dados com o ALEMBIC
alembic revision --autogenerate -m "mensagem"
alembic upgrade head

4 - Abrir servidor local com reload ativo
fastapi dev main.py
