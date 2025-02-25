# Web Vulnerability Scanner

Este es un script en **Python** diseñado para analizar vulnerabilidades en sitios web de manera masiva. Permite identificar puertos abiertos, revisar cabeceras de seguridad, detectar posibles inyecciones SQL y obtener información sobre el servidor.

## 🔹 Características
✅ **Escaneo de puertos abiertos** (80, 443, 8080, 3306, 21, 22).  
✅ **Verificación de cabeceras de seguridad** faltantes.  
✅ **Detección de vulnerabilidad de inyección SQL** en parámetros de URL.  
✅ **Obtención de información del servidor y tecnologías utilizadas**.  
✅ **Sugerencias de seguridad para mitigar riesgos**.  

## 📌 Requisitos
Para ejecutar este script, necesitas tener **Python 3** instalado y las siguientes librerías:

```bash
pip install requests bs4
```

## 🚀 Uso
1. Clona o descarga este repositorio.
2. Abre una terminal y navega hasta la carpeta del proyecto.
3. Ejecuta el script con:

```bash
python script.py
```

4. Ingresa la URL del sitio web sin `http/https` cuando se te solicite.
5. Observa el análisis y sigue las recomendaciones proporcionadas.

## ⚠️ Advertencia
Este script debe utilizarse **únicamente** con fines educativos y en sitios web de los cuales tengas autorización. No nos hacemos responsables por el mal uso de esta herramienta.

## 📌 Mejoras futuras
🔹 Implementación de escaneo de subdominios.  
🔹 Detección de vulnerabilidades XSS.  
🔹 Integración con bases de datos de exploits conocidos.  

Si tienes ideas o mejoras, ¡haz un **pull request** o contactame! 🚀

