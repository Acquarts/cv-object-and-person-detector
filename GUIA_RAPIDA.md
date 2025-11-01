# 🚀 Guía Rápida de Uso

## Inicio Rápido (3 Pasos)

### 1️⃣ Ejecutar la aplicación

**En Windows:**
```
Doble clic en start.bat
```

**En macOS/Linux:**
```bash
./start.sh
```

O manualmente:
```bash
pip install -r requirements.txt
streamlit run video_detector.py
```

### 2️⃣ Subir tu video

1. Abre tu navegador en `http://localhost:8501`
2. Haz clic en "📤 Sube tu video"
3. Selecciona tu archivo de video

### 3️⃣ Detectar y descargar

1. Ajusta el umbral de confianza si lo deseas (sidebar)
2. Haz clic en "🚀 Detectar Objetos"
3. Descarga el video procesado

---

## 🎯 Ejemplos de Uso

### Interfaz Web (Streamlit)

La forma más fácil de usar la aplicación:

```bash
streamlit run video_detector.py
```

### Procesamiento por Lotes (CLI)

Para procesar videos sin interfaz gráfica:

```bash
# Ejemplo básico
python batch_processor.py --input mi_video.mp4 --output resultado.mp4

# Con configuración personalizada
python batch_processor.py \
  --input video_entrada.mp4 \
  --output video_salida.mp4 \
  --confidence 0.6 \
  --model yolov8m.pt
```

**Opciones disponibles:**

| Opción | Descripción | Default |
|--------|-------------|---------|
| `--input` / `-i` | Video de entrada (requerido) | - |
| `--output` / `-o` | Video de salida (requerido) | - |
| `--confidence` / `-c` | Umbral de confianza (0.0-1.0) | 0.5 |
| `--model` / `-m` | Modelo YOLO a usar | yolov8n.pt |

**Modelos disponibles:**
- `yolov8n.pt` - Nano (más rápido) ⚡
- `yolov8s.pt` - Small
- `yolov8m.pt` - Medium (balance)
- `yolov8l.pt` - Large
- `yolov8x.pt` - Extra Large (más preciso) 🎯

---

## ⚙️ Ajustar Configuraciones

### Umbral de Confianza

El umbral determina qué tan "seguro" debe estar el modelo:

- **0.3-0.4**: Más detecciones, pero puede incluir falsos positivos
- **0.5**: Balance recomendado (default)
- **0.7-0.9**: Menos detecciones, pero más precisas

### Elegir el Modelo

| Modelo | Velocidad | Precisión | Uso Recomendado |
|--------|-----------|-----------|-----------------|
| yolov8n | ⚡⚡⚡⚡⚡ | ⭐⭐⭐ | Videos largos, pruebas rápidas |
| yolov8s | ⚡⚡⚡⚡ | ⭐⭐⭐⭐ | Uso general |
| yolov8m | ⚡⚡⚡ | ⭐⭐⭐⭐ | Balance velocidad/precisión |
| yolov8l | ⚡⚡ | ⭐⭐⭐⭐⭐ | Alta precisión |
| yolov8x | ⚡ | ⭐⭐⭐⭐⭐ | Máxima precisión |

---

## 📝 Casos de Uso Prácticos

### 1. Análisis de Tráfico
```bash
python batch_processor.py \
  --input trafico_ciudad.mp4 \
  --output analisis_trafico.mp4 \
  --confidence 0.6
```
Detecta: coches, motos, autobuses, camiones, peatones

### 2. Seguridad y Vigilancia
```bash
python batch_processor.py \
  --input camara_seguridad.mp4 \
  --output deteccion_personas.mp4 \
  --confidence 0.7 \
  --model yolov8m.pt
```
Detecta: personas, vehículos, objetos sospechosos

### 3. Análisis de Vida Salvaje
```bash
python batch_processor.py \
  --input safari.mp4 \
  --output animales_detectados.mp4 \
  --confidence 0.5
```
Detecta: elefantes, jirafas, cebras, pájaros, etc.

### 4. Control de Inventario
```bash
python batch_processor.py \
  --input almacen.mp4 \
  --output conteo_objetos.mp4 \
  --confidence 0.6
```
Detecta: cajas, pallets, productos específicos

---

## 🐛 Solución de Problemas Comunes

### El video no se procesa
- ✅ Verifica que el formato sea compatible (MP4, AVI, MOV, MKV)
- ✅ Asegúrate de tener suficiente espacio en disco
- ✅ Intenta con un video más corto para probar

### Procesamiento muy lento
- ✅ Usa el modelo `yolov8n.pt` (más rápido)
- ✅ Reduce la resolución del video de entrada
- ✅ Cierra otras aplicaciones para liberar recursos

### Pocas detecciones
- ✅ Reduce el umbral de confianza (ej: 0.3-0.4)
- ✅ Usa un modelo más grande (ej: yolov8m.pt)
- ✅ Verifica que los objetos sean de las categorías soportadas

### Muchos falsos positivos
- ✅ Aumenta el umbral de confianza (ej: 0.7-0.8)
- ✅ Usa un modelo más preciso (yolov8l.pt o yolov8x.pt)

---

## 💡 Tips y Trucos

### 1. Procesamiento Rápido
Para procesar rápidamente múltiples videos:
```bash
for video in *.mp4; do
    python batch_processor.py --input "$video" --output "detected_$video"
done
```

### 2. Detección de Solo Personas
Edita `video_detector.py` para filtrar solo personas:
```python
if model.names[class_id] == 'person':
    # Solo procesa personas
```

### 3. Guardar Estadísticas en CSV
Modifica el script para exportar las estadísticas:
```python
import csv
with open('estadisticas.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(detected_objects.items())
```

### 4. Procesamiento en Tiempo Real
Usa la webcam en lugar de un archivo:
```python
cap = cv2.VideoCapture(0)  # 0 = webcam por defecto
```

---

## 📊 Rendimiento Esperado

### En una PC con CPU moderna:

| Resolución | FPS Procesamiento | Modelo |
|------------|-------------------|--------|
| 720p | ~15-20 FPS | yolov8n |
| 1080p | ~8-12 FPS | yolov8n |
| 720p | ~5-8 FPS | yolov8m |
| 1080p | ~3-5 FPS | yolov8m |

### Con GPU (NVIDIA con CUDA):

| Resolución | FPS Procesamiento | Modelo |
|------------|-------------------|--------|
| 720p | ~60-80 FPS | yolov8n |
| 1080p | ~30-40 FPS | yolov8n |
| 720p | ~25-35 FPS | yolov8m |
| 1080p | ~15-20 FPS | yolov8m |

---

## 📚 Recursos Adicionales

- [Documentación YOLOv8](https://docs.ultralytics.com/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [OpenCV Tutorials](https://docs.opencv.org/master/d9/df8/tutorial_root.html)

---

## 🆘 Soporte

Si encuentras algún problema:
1. Revisa la sección de Solución de Problemas
2. Verifica que todas las dependencias estén instaladas
3. Consulta el README.md para más detalles

**¡Disfruta detectando objetos! 🎬🔍**
