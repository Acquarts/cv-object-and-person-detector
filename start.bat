@echo off
echo.
echo 🚀 Iniciando Detector de Objetos en Video
echo ==========================================
echo.

REM Verificar si existe el entorno virtual
if not exist "venv\" (
    echo 📦 Creando entorno virtual...
    python -m venv venv
)

REM Activar entorno virtual
echo 🔧 Activando entorno virtual...
call venv\Scripts\activate.bat

REM Instalar dependencias
echo 📥 Instalando dependencias...
python -m pip install --upgrade pip --quiet
pip install -r requirements.txt --quiet

echo.
echo ✅ Todo listo!
echo.
echo 🌐 Iniciando aplicación Streamlit...
echo 📱 La aplicación se abrirá en tu navegador
echo.
echo Para detener la aplicación, presiona Ctrl+C
echo.

REM Iniciar Streamlit
streamlit run video_detector.py

pause
