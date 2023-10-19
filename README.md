# Predicción de Precios de Viviendas Media Estancia en Madrid, España

Este proyecto de data science se centra en predecir los precios de las viviendas a Media Estancia en Madrid, España, utilizando el algoritmo de Random Forest Regressor. Se han aplicado diversas técnicas y procesos para obtener predicciones precisas, que incluyen web scraping para recopilar datos, análisis de importancia de características, codificación de etiquetas para datos categóricos y ajuste de precios según estándares locales.

## Objetivo

El objetivo principal de este proyecto es desarrollar un modelo predictivo que pueda estimar con precisión los precios de las viviendas en Madrid. Esto puede ser de gran utilidad para los compradores, vendedores y profesionales del mercado inmobiliario que deseen tomar decisiones informadas.

## Datos

Los datos utilizados en este proyecto se obtuvieron mediante web scraping de diversas fuentes en línea que proporcionan información sobre las viviendas en Madrid. Estos datos incluyen características como el tamaño de la vivienda, la ubicación, el número de habitaciones, el número de baños y más.

## Procesamiento de Datos

### Importancia de Características

Se realizó un análisis de feature importance para determinar qué columnas de datos son más relevantes para la predicción de precios. Esto nos ayudó a seleccionar las características más influyentes y eliminar las que no contribuyen significativamente al modelo.

### Codificación de Etiquetas

Para manejar datos categóricos, se aplicó label encoding. Esto convirtió las categorías en valores numéricos, lo que facilita su inclusión en el modelo de Random Forest Regression.

## Modelo de Random Forest Regressor

El modelo utilizado en este proyecto es el Random Forest Regressor. Este algoritmo es conocido por su capacidad para manejar conjuntos de datos complejos y proporcionar predicciones sólidas.

## Validación de Precios

Para obtener predicciones que reflejen de manera más precisa los estándares de precios locales en Madrid, se aplicó una validacion, y si fuese necesario ajuste, de precios utilizando información sobre el mercado inmobiliario en la región.

## Resultados

Se proporcionarán los resultados y las métricas de rendimiento del modelo, lo que permitirá evaluar su precisión y eficacia.

## Instalación

Para ejecutar este proyecto en tu entorno local, sigue estos pasos:

1. Clona el repositorio:

   ```bash
   git clone https://github.com/gbiskandar/Prediccion_Alquiler.git
   ```

2. Instala las dependencias necesarias:

   ```bash
   pip install -r requirements.txt
   ```

3. Ejecuta el código principal para realizar predicciones.

## Contribuciones

Agradezco a mis colegas de The Bridge Digital Talent Accelerator en Madrid: [Antonio de la Macorra](https://github.com/adlmacorra), Diana Luzuriaga y Alfonso Caballero por sus contribuciones a la elaboracion del proyecto.

## Contacto

Para cualquier pregunta o comentario, no dudes en ponerte en contacto conmigo en [info@invex.pro](mailto:info@invex.pro).

## Licencia

Este proyecto está bajo la licencia [Licencia MIT](LICENSE).