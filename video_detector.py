import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO
import tempfile
import os
from pathlib import Path

# Configuración de la página
st.set_page_config(
    page_title="Detector de Objetos en Video",
    page_icon="🎥",
    layout="wide"
)

# Título y descripción
st.title("🎥 Detector de Objetos y Personas en Video")
st.markdown("""
Esta aplicación utiliza inteligencia artificial para detectar automáticamente:
- 👥 Personas
- 🚗 Vehículos
- 🐕 Animales
- 📦 Y muchos otros objetos (80+ categorías)
""")

@st.cache_resource
def load_model():
    """Carga el modelo YOLO"""
    try:
        model = YOLO('yolov8n.pt')  # Modelo nano (más rápido)
        return model
    except Exception as e:
        st.error(f"Error cargando el modelo: {e}")
        return None

def process_video(video_path, model, confidence_threshold):
    """Procesa el video y detecta objetos"""
    cap = cv2.VideoCapture(video_path)
    
    # Obtener propiedades del video
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Crear archivo de salida
    output_path = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4').name
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    # Barra de progreso
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Contador de objetos detectados
    detected_objects = {}
    frame_count = 0
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Realizar detección
        results = model(frame, conf=confidence_threshold, verbose=False)
        
        # Dibujar detecciones en el frame
        annotated_frame = results[0].plot()
        
        # Contar objetos detectados
        for box in results[0].boxes:
            class_id = int(box.cls[0])
            class_name = model.names[class_id]
            detected_objects[class_name] = detected_objects.get(class_name, 0) + 1
        
        # Escribir frame procesado
        out.write(annotated_frame)
        
        # Actualizar progreso
        frame_count += 1
        progress = frame_count / total_frames
        progress_bar.progress(progress)
        status_text.text(f"Procesando frame {frame_count}/{total_frames}")
    
    cap.release()
    out.release()
    progress_bar.empty()
    status_text.empty()
    
    return output_path, detected_objects

# Sidebar con configuración
st.sidebar.header("⚙️ Configuración")
confidence = st.sidebar.slider(
    "Umbral de confianza",
    min_value=0.1,
    max_value=1.0,
    value=0.5,
    step=0.05,
    help="Nivel mínimo de confianza para detectar un objeto"
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
### ℹ️ Información
Este detector usa **YOLOv8**, uno de los modelos más avanzados 
para detección de objetos en tiempo real.

**Objetos detectables:**
- Personas y animales
- Vehículos (coches, motos, bicicletas)
- Objetos cotidianos
- Y muchos más...
""")

# Cargar modelo
with st.spinner("🔄 Cargando modelo de IA..."):
    model = load_model()

if model is None:
    st.error("❌ No se pudo cargar el modelo. Por favor, verifica la instalación.")
    st.stop()

st.success("✅ Modelo cargado correctamente")

# Uploader de video
uploaded_file = st.file_uploader(
    "📤 Sube tu video",
    type=['mp4', 'avi', 'mov', 'mkv'],
    help="Formatos soportados: MP4, AVI, MOV, MKV"
)

if uploaded_file is not None:
    # Guardar video temporalmente
    tfile = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
    tfile.write(uploaded_file.read())
    video_path = tfile.name
    
    # Crear dos columnas
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📹 Video Original")
        st.video(video_path)
    
    # Botón para procesar
    if st.button("🚀 Detectar Objetos", type="primary", use_container_width=True):
        with st.spinner("🔍 Analizando video..."):
            try:
                output_path, detected_objects = process_video(
                    video_path, 
                    model, 
                    confidence
                )
                
                with col2:
                    st.subheader("🎯 Video Procesado")
                    st.video(output_path)
                
                # Mostrar estadísticas
                st.markdown("---")
                st.subheader("📊 Objetos Detectados")
                
                if detected_objects:
                    # Ordenar por cantidad
                    sorted_objects = sorted(
                        detected_objects.items(), 
                        key=lambda x: x[1], 
                        reverse=True
                    )
                    
                    # Mostrar en columnas
                    cols = st.columns(3)
                    for idx, (obj_name, count) in enumerate(sorted_objects):
                        col_idx = idx % 3
                        with cols[col_idx]:
                            st.metric(
                                label=obj_name.capitalize(),
                                value=count,
                                delta="detecciones"
                            )
                    
                    # Botón de descarga
                    st.markdown("---")
                    with open(output_path, 'rb') as f:
                        st.download_button(
                            label="⬇️ Descargar Video Procesado",
                            data=f,
                            file_name="video_detectado.mp4",
                            mime="video/mp4",
                            use_container_width=True
                        )
                else:
                    st.warning("⚠️ No se detectaron objetos. Intenta ajustar el umbral de confianza.")
                
                # Limpiar archivos temporales
                try:
                    os.unlink(output_path)
                except:
                    pass
                    
            except Exception as e:
                st.error(f"❌ Error procesando el video: {str(e)}")
    
    # Limpiar archivo temporal
    try:
        os.unlink(video_path)
    except:
        pass

else:
    st.info("👆 Sube un video para comenzar la detección")
    
    # Ejemplo visual
    st.markdown("---")
    st.subheader("🎬 ¿Cómo funciona?")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 1️⃣ Sube tu video")
        st.markdown("Selecciona cualquier video de tu dispositivo")
    
    with col2:
        st.markdown("### 2️⃣ Procesamiento IA")
        st.markdown("El modelo analiza cada frame detectando objetos")
    
    with col3:
        st.markdown("### 3️⃣ Resultados")
        st.markdown("Descarga el video con las detecciones marcadas")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>Desarrollado con ❤️ usando Streamlit y YOLOv8</p>
    </div>
    """,
    unsafe_allow_html=True
)
