# 📊 Residual Value

Este repositorio recopila todo el material relacionado con el Trabajo de Fin de Máster (TFM) titulado:
**"Consideraciones en el cálculo de valor residual de vehículos financiados, con foco en nuevos vehículos eléctricos"**.

A continuación, se describen los archivos principales organizados por temática:

---

## 📈 Modelización

* **`residual_value_model.ipynb`**
  Jupyter Notebook que contiene la implementación y documentación del **modelo de cálculo de valor residual** propuesto.

* **`used_car_price_prediction_model.ipynb`**
  Jupyter Notebook con la implementación y documentación del **modelo de predicción del precio de vehículos de segunda mano**, utilizado como componente del modelo de cálculo de valor residual.

* **`xgboost_model.json`**
  Archivo que exporta el modelo de predicción de precios seleccionado.

* **`make_te_dictionary.xlsx`**, **`model_te_dictionary.xlsx`**, **`aux_model_te_dictionary.xlsx`**
  Diccionarios que asocian a cada marca o modelo la codificación por objetivo aplicada sobre la muestra de entrenamiento.

---

## 🌐 Extracción de Datos

* **`web_scraping.py`**
  Script en Python para la extracción de datos desde la página web **cars.com** utilizando técnicas de *web scraping*.

* **`create_directories.py`**
  Script en Python para generar la estructura de directorios donde se almacenan los datos extraídos.

* **`cars/`**
  Directorio que contiene toda la información extraída de **cars.com** mediante el archivo `web_scraping.py`.

* **`raw_data.xlsx`**
  Archivo que unifica y consolida los datos almacenados en el directorio `cars/`.

* **`price_scraping.py`**
  Script en Python para la extracción de datos desde la página web **kbb.com** utilizando técnicas de *web scraping*.

* **`data_treatment.py`**
  Script en Python para el preprocesamiento de los datos extraídos de **kbb.com**.

* **`raw_data_OV.xlsx`**
  Versión modificada de `raw_data.xlsx` que incluye la variable *original value*.

---

## 🛠️ Procesamiento de Datos

* **`car_classification_prompt.txt`**
  Prompt utilizado en un modelo de lenguaje (LLM) para automatizar la clasificación de vehículos por tipo (SUV, compacto, deportivo, camioneta, etc.).

* **`model_vehicle:type.txt`**
  Diccionario que asocia cada modelo de coche con su correspondiente tipo de vehículo.

* **`color_codification_prompt.txt`**
  Prompt utilizado en una LLM para automatizar la codificación RGB de colores descritos en lenguaje natural.

* **`colors/`**
  Directorio que contiene diccionarios de colores convertidos de lenguaje natural a codificación RGB, generados mediante LLM y validados manualmente.

* **`excel_color_macro.txt`**
  Macro de Excel para verificar que la codificación automática de colores ha sido correcta.

* **`preprocessed_dataset.xlsx`**
  Archivo resultante del preprocesamiento de `raw_data_OV.xlsx`, utilizando el código de `used_car_price_prediction_model.ipynb`.

---

### 👥 Autores y contribuciones

Este proyecto ha sido desarrollado en colaboración con un equipo de seis personas en el marco del Trabajo de Fin de Máster, veánse Lucía Bravo Dalmau, Carmen Fernández Casal, Paula Florián Júlvez, Lucía García de Santos, Juan Carlos Llamas Núñez y Ana Villoria Jiménez. No obstante, la implementación del código, el diseño de los modelos y la preparación del repositorio han sido realizados principalmente por Juan Carlos Llamas Núñez, contando con contribuciones de Lucía García de Santos. El resto del equipo ha contribuido en otras áreas del proyecto no relacionadas con la codificación y la modelización.

---

📌 **Nota:** Todos los archivos y scripts han sido desarrollados como parte del análisis y modelización para el TFM anteriormente mencionado. Su uso y distribución están sujetos a las condiciones del autor.
