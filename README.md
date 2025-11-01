# 🎥 Detector de Objetos y Personas en Video

Una aplicación web interactiva construida con Streamlit que utiliza YOLOv8 para detectar automáticamente objetos y personas en videos.

## ✨ Características

- 🎯 Detección automática de **80+ categorías de objetos**
- 👥 Reconocimiento de personas
- 🚗 Detección de vehículos (coches, motos, bicicletas)
- 🐕 Identificación de animales
- 📊 Estadísticas en tiempo real de objetos detectados
- ⬇️ Descarga del video procesado con anotaciones
- ⚙️ Umbral de confianza ajustable

## 🚀 Demo en Vivo

Puedes probar la aplicación en línea sin instalar nada:

**[🔗 Abrir App en Streamlit Cloud](https://cv-object-and-person-detector.streamlit.app)**

## 📦 Instalación Local

### Prerrequisitos

- Python 3.8 - 3.10 (recomendado 3.10)
- pip

### Pasos de instalación

1. **Clona el repositorio**

```bash
git clone https://github.com/Acquarts/cv-object-and-person-detector.git
cd cv-object-and-person-detector
```

2. **Crea un entorno virtual (recomendado)**

```bash
python -m venv venv

# En Windows:
venv\Scripts\activate

# En macOS/Linux:
source venv/bin/activate
```

3. **Instala las dependencias**

```bash
pip install -r requirements.txt
```

**Nota para Windows:** Si encuentras errores de DLL con PyTorch, ejecuta el script de reparación incluido:
```bash
fix_dependencies.bat
```

Nota: La primera vez que ejecutes la aplicación, se descargará automáticamente el modelo YOLOv8 (~6MB).

## 🎮 Uso

1. **Ejecuta la aplicación:**

```bash
streamlit run video_detector.py
```

2. **Abre tu navegador:**
   - La aplicación se abrirá automáticamente en `http://localhost:8501`

3. **Sube un video:**
   - Haz clic en "Sube tu video"
   - Selecciona un archivo (MP4, AVI, MOV, MKV)

4. **Ajusta la configuración (opcional):**
   - Usa el slider en la barra lateral para ajustar el umbral de confianza
   - Valores más altos = menos detecciones pero más precisas
   - Valores más bajos = más detecciones pero pueden incluir falsos positivos

5. **Detecta objetos:**
   - Haz clic en "🚀 Detectar Objetos"
   - Espera mientras se procesa el video
   - Visualiza los resultados y estadísticas

6. **Descarga el resultado:**
   - Haz clic en "⬇️ Descargar Video Procesado"

## 📋 Objetos Detectables

El modelo YOLOv8 puede detectar las siguientes categorías:

### Personas y Animales
- Personas
- Perros, gatos, pájaros, caballos, ovejas, vacas, elefantes, osos, cebras, jirafas

### Vehículos
- Coches, motocicletas, aviones, autobuses, trenes, camiones, barcos, bicicletas

### Objetos de Exterior
- Semáforos, hidrantes, señales de stop, parquímetros, bancos

### Objetos de Interior
- Sofás, sillas, mesas, camas, inodoros, televisores, laptops, ratones, teclados
- Teléfonos móviles, microondas, hornos, tostadoras, refrigeradores
- Libros, relojes, jarrones, tijeras, peluches

### Comida y Bebida
- Botellas, copas de vino, tazas, tenedores, cuchillos, cucharas, bols
- Plátanos, manzanas, sándwiches, naranjas, brócoli, zanahorias, pizzas, donas

### Y muchos más... (80+ categorías en total)

## 🛠️ Tecnologías Utilizadas

- **Streamlit**: Framework para la interfaz web
- **YOLOv8**: Modelo de detección de objetos de última generación
- **OpenCV**: Procesamiento de video
- **Ultralytics**: Implementación de YOLO
- **NumPy**: Operaciones numéricas

## ⚙️ Configuración Avanzada

### Cambiar el modelo YOLO

Por defecto se usa `yolov8n.pt` (nano) que es rápido pero menos preciso. Puedes cambiar a modelos más grandes en la línea 26 del código:

```python
# Opciones disponibles:
model = YOLO('yolov8n.pt')  # Nano (más rápido) ⚡
model = YOLO('yolov8s.pt')  # Small
model = YOLO('yolov8m.pt')  # Medium
model = YOLO('yolov8l.pt')  # Large
model = YOLO('yolov8x.pt')  # Extra Large (más preciso) 🎯
```

### Ajustar el rendimiento

- Para videos largos, considera reducir la resolución
- Ajusta el FPS de procesamiento si necesitas más velocidad
- Usa el modelo nano (yolov8n) para procesamiento más rápido

## 🐛 Solución de Problemas

### Error de DLL en Windows (WinError 1114)
Este es un problema común con PyTorch en Windows. Solución:
```bash
# Ejecuta el script de reparación incluido
fix_dependencies.bat
```

O manualmente:
```bash
pip install torch==2.0.1 torchvision==0.15.2 --index-url https://download.pytorch.org/whl/cpu
pip install "numpy<2" opencv-python==4.10.0.84
```

### Error al cargar el modelo
```bash
pip install --upgrade ultralytics
```

### Problemas con OpenCV
```bash
pip install opencv-python-headless==4.10.0.84
```

### Video no se reproduce
- Asegúrate de que el video esté en un formato compatible (MP4, AVI, MOV, MKV)
- Prueba con un codec diferente

### El procesamiento es muy lento
- Usa el modelo `yolov8n.pt` (nano)
- Reduce la resolución del video de entrada
- Procesa solo una parte del video

## 🌐 Deploy en Streamlit Cloud

Para desplegar tu propia versión:

1. Haz fork de este repositorio
2. Ve a [share.streamlit.io](https://share.streamlit.io)
3. Conecta tu cuenta de GitHub
4. Selecciona el repositorio y la rama
5. El archivo principal es `video_detector.py`
6. ¡Deploy automático!

Los archivos necesarios ya están configurados:
- `requirements.txt`: Dependencias de Python
- `packages.txt`: Dependencias del sistema (Linux)
- `.streamlit/config.toml`: Configuración de la app

## 📝 Notas

- El primer procesamiento puede tardar más debido a la descarga del modelo
- El tiempo de procesamiento depende de:
  - Duración del video
  - Resolución del video
  - Modelo YOLO utilizado
  - Capacidad de tu hardware
- Videos de alta resolución y larga duración requieren más tiempo y recursos

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si encuentras algún bug o tienes sugerencias de mejora, no dudes en reportarlo.

## 📄 Licencia

Este proyecto utiliza:
- YOLOv8: Licencia AGPL-3.0
- Streamlit: Licencia Apache 2.0

## 🙏 Agradecimientos

- [Ultralytics](https://github.com/ultralytics/ultralytics) por YOLOv8
- [Streamlit](https://streamlit.io/) por el framework
- La comunidad de Open Source

---

**¡Disfruta detectando objetos en tus videos! 🎬🔍**
