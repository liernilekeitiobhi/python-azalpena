from PIL import Image
import os

def redimensionar_imagen(ruta_entrada, ruta_salida=None, escala=0.5):
    """
    Redimensiona una imagen a un porcentaje de su tamaño original.
    
    Args:
        ruta_entrada (str): Ruta de la imagen original.
        ruta_salida (str, optional): Ruta para guardar la imagen redimensionada. 
                                    Si es None, se sobrescribe la original.
        escala (float, optional): Porcentaje de escalado (0.7 = 70%).
    """
    try:
        # Abrir la imagen original
        with Image.open(ruta_entrada) as img:
            # Calcular nuevo tamaño
            ancho, alto = img.size
            nuevo_ancho = int(ancho * escala)
            nuevo_alto = int(alto * escala)
            
            # Redimensionar
            img_redimensionada = img.resize((nuevo_ancho, nuevo_alto), Image.LANCZOS)
            
            # Guardar la imagen
            if ruta_salida is None:
                ruta_salida = ruta_entrada
            
            img_redimensionada.save(ruta_salida)
            print(f"✅ Imagen redimensionada al {escala*100}% y guardada en: {ruta_salida}")
    
    except Exception as e:
        print(f"❌ Error: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    # Configuración
    ruta_imagen_original = "docs/img/vsc-logo.png"  # Cambia esto por tu ruta
    ruta_imagen_redimensionada = "docs/img/vsc-logo-redim.png"  # Opcional: None para sobrescribir
    
    # Redimensionar al 70%
    redimensionar_imagen(ruta_imagen_original, ruta_imagen_redimensionada, escala=0.5)