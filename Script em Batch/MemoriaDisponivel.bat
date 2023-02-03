@echo off
:loop
for /F "tokens=2 delims==" %%a in ('wmic OS get FreePhysicalMemory /Value ^| find "="') do set _mem=%%a
set /a _mem=%_mem%/1024
echo Memoria RAM Disponivel: %_mem% MB
ping localhost -n 2 >nul
goto loop