@echo off
setlocal

:: Obtém o nome do computador
set "computerName=%COMPUTERNAME%"

:: Define o caminho do arquivo com o nome do computador
set "filePath=C:\temp\%computerName%.txt"

:: Gera o relatório
msinfo32 /report "%filePath%"
echo Informações do sistema salvas em %filePath%
pause