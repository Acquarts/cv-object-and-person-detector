#!/bin/bash

echo "🚀 Iniciando Detector de Objetos en Video"
echo "=========================================="
echo ""

# Verificar si existe el entorno virtual
if [ ! -d "venv" ]; then
    echo "📦 Creando entorno virtual..."
    python3 -m venv venv
fi

# Activar entorno virtual
echo "🔧 Activando entorno virtual..."
source venv/bin/activate

# Instalar dependencias
echo "📥 Instalando dependencias..."
pip install -q --upgrade pip
pip install -q -r requirements.txt

echo ""
echo "✅ Todo listo!"
echo ""
echo "🌐 Iniciando aplicación Streamlit..."
echo "📱 La aplicación se abrirá en tu navegador"
echo ""
echo "Para detener la aplicación, presiona Ctrl+C"
echo ""

# Iniciar Streamlit
streamlit run video_detector.py
