@echo off

rem Cria a pasta principal de Backup de Drivers no C:
if not exist "C:\Driver_Backup" mkdir "C:\Driver_Backup"

rem Copia os drivers para a pasta de Backup de Drivers
xcopy "%windir%\System32\drivers" "C:\Driver_Backup\drivers" /e /i

rem Cria uma pasta compactada no formato ZIP
"%ProgramFiles%\7-Zip\7z.exe" a -tzip "C:\Driver_Backup\drivers.zip" "C:\Driver_Backup\drivers"

rem Exclui a pasta não compactada
rd /s /q "C:\Driver_Backup\drivers"

echo Backup de drivers concluído com sucesso!
pause
