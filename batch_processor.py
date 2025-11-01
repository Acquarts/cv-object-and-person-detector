#!/usr/bin/env python3
"""
Script para procesamiento por lotes de videos
Uso: python batch_processor.py --input video.mp4 --output resultado.mp4
"""

import argparse
import cv2
from ultralytics import YOLO
import sys
from pathlib import Path

def process_video_batch(input_path, output_path, confidence=0.5, model_name='yolov8n.pt'):
    """
    Procesa un video y guarda el resultado con detecciones
    
    Args:
        input_path: Ruta del video de entrada
        output_path: Ruta donde guardar el video procesado
        confidence: Umbral de confianza para detecciones (0.0 - 1.0)
        model_name: Nombre del modelo YOLO a usar
    """
    print(f"🔄 Cargando modelo {model_name}...")
    model = YOLO(model_name)
    
    print(f"📹 Abriendo video: {input_path}")
    cap = cv2.VideoCapture(input_path)
    
    if not cap.isOpened():
        print(f"❌ Error: No se pudo abrir el video {input_path}")
        sys.exit(1)
    
    # Propiedades del video
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    print(f"📊 Resolución: {width}x{height} | FPS: {fps} | Frames: {total_frames}")
    
    # Crear writer para video de salida
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    if not out.isOpened():
        print(f"❌ Error: No se pudo crear el archivo de salida {output_path}")
        sys.exit(1)
    
    # Estadísticas
    detected_objects = {}
    frame_count = 0
    
    print(f"🚀 Procesando video...")
    print(f"⚙️  Umbral de confianza: {confidence}")
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Detección
        results = model(frame, conf=confidence, verbose=False)
        
        # Frame anotado
        annotated_frame = results[0].plot()
        
        # Contar objetos
        for box in results[0].boxes:
            class_id = int(box.cls[0])
            class_name = model.names[class_id]
            detected_objects[class_name] = detected_objects.get(class_name, 0) + 1
        
        # Guardar frame
        out.write(annotated_frame)
        
        # Progreso
        frame_count += 1
        if frame_count % 30 == 0:  # Cada 30 frames
            progress = (frame_count / total_frames) * 100
            print(f"⏳ Progreso: {progress:.1f}% ({frame_count}/{total_frames} frames)")
    
    cap.release()
    out.release()
    
    print(f"\n✅ ¡Video procesado exitosamente!")
    print(f"💾 Guardado en: {output_path}")
    
    # Mostrar estadísticas
    if detected_objects:
        print(f"\n📊 OBJETOS DETECTADOS:")
        print("-" * 40)
        sorted_objects = sorted(detected_objects.items(), key=lambda x: x[1], reverse=True)
        for obj_name, count in sorted_objects:
            print(f"  {obj_name.capitalize()}: {count} detecciones")
    else:
        print("\n⚠️  No se detectaron objetos. Intenta reducir el umbral de confianza.")
    
    return detected_objects

def main():
    parser = argparse.ArgumentParser(
        description='Procesa videos para detectar objetos y personas usando YOLOv8'
    )
    parser.add_argument(
        '--input', '-i',
        required=True,
        help='Ruta del video de entrada'
    )
    parser.add_argument(
        '--output', '-o',
        required=True,
        help='Ruta donde guardar el video procesado'
    )
    parser.add_argument(
        '--confidence', '-c',
        type=float,
        default=0.5,
        help='Umbral de confianza (0.0 - 1.0, default: 0.5)'
    )
    parser.add_argument(
        '--model', '-m',
        default='yolov8n.pt',
        choices=['yolov8n.pt', 'yolov8s.pt', 'yolov8m.pt', 'yolov8l.pt', 'yolov8x.pt'],
        help='Modelo YOLO a usar (default: yolov8n.pt - más rápido)'
    )
    
    args = parser.parse_args()
    
    # Validar entrada
    if not Path(args.input).exists():
        print(f"❌ Error: El archivo {args.input} no existe")
        sys.exit(1)
    
    # Validar umbral
    if not 0.0 <= args.confidence <= 1.0:
        print(f"❌ Error: El umbral de confianza debe estar entre 0.0 y 1.0")
        sys.exit(1)
    
    # Procesar
    try:
        process_video_batch(
            args.input,
            args.output,
            args.confidence,
            args.model
        )
    except KeyboardInterrupt:
        print("\n⚠️  Procesamiento cancelado por el usuario")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error durante el procesamiento: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
