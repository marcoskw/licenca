@echo off

call venv\Scripts\activate

REM Executa as migrações do banco de dados
python manage.py migrate

REM Inicializa o servidor Django
python manage.py runserver

REM Mantém a janela do prompt aberta após o comando ser executado
pause