import pickle
from constants import label_to_encoded, rng, sleep, Registros_por_Distrito, Distritos1, Distritos2, Distritos3
from sklearn.ensemble import RandomForestRegressor
import numpy as np

# Cargar modelo desde el archivo pickle
with open("RF_modelo_entrenado.pkl", 'rb') as file:
    modelo_cargado = pickle.load(file)
rf_regressor = modelo_cargado["rf_regressor"]

label_encoders = label_to_encoded # Diccionario en fichero constants.py del label encoding que se hizo durante el modelado

def encode_solicitud(solicitud, label_encoders): # Encode las columnas categoricas de la solicitud input para uso en nuestro modelo RFR
    """
    Encode las columnas categoricas del input dict solicitud usando el dict de label_encoders en fichero constants.py
    
    Parametros:
    - solicitud: dict
        El input diccionary con los campos a ser encoded.
    - label_encoders: dict de objetos LabelEncoder
        Diccionario que contiene objetos LabelEncoder para cada campo categorico a ser encoded.

    Returns:
    - encoded_solicitud: dict
        La version encoded del input solicitud.
    """
    
    encoded_solicitud = solicitud.copy()

    # Loop atraves de las keys en la solicitud que requieren de encoding
    for key in ['Tipo', 'Distrito', 'Barrio']:
        if key in encoded_solicitud:
            encoded_solicitud[key] = label_encoders[key][encoded_solicitud[key]]
    
    return encoded_solicitud

def estimacion(encoded_solicitud, area): # Usar la encoded solicitud para hacer la estimacion de precio mensual
    """
    Utiliza la encoded_solicitud para hacer la prediccion usando modelo rf_regressor
    
    Parametros:
    - encoded_solicitud: dict
        El input diccionary con los campos categoricos encoded.

    Returns:
    - predicted_price: number
        La version encoded del input solicitud.
    """

    # Predecir el precio de renta para el nuevo_listing
    predicted_price = int(np.around(rf_regressor.predict([list(encoded_solicitud.values())])[0], -1))
    
    # Evaluar el precio por m2 de la prediccion y aplicar un ajuste si esta prediciendo al alza (identificar y modificar outliers)
    pred_m2 = predicted_price / area
    if pred_m2 > 50:
        predicted_price = predicted_price * .75
    elif 40 < pred_m2 < 50:
        predicted_price = predicted_price * .8
    elif 30 < pred_m2 < 40:
        predicted_price = predicted_price * .9
    else:
        predicted_price
        
    #Un pequeño delay en el calculo
    time_to_sleep = rng.uniform(1, 3)
    sleep(time_to_sleep)

    return predicted_price

def query(tipo, distrito, barrio, hab, banos, area, furnished):
    """
    Utiliza los inputs del usuario web para generar una solicitud encodificada
    
    Parametros:
    - tipo: texto
        El input de tipo de vivienda
    - distrito: texto
        El input de distrito de Madrid donde esta ubicada la vivienda
    - barrio: texto
        El input de barrio de Madrid donde esta ubicada la vivienda
    - hab: numero
        El input de numero de habitaciones de la vivienda
    - banos: numero
        El input de numero de banos de la vivienda
    - area: numero
        El input de area (en m2) de la vivienda
    - furnished: numero 
        1 = Amueblado y 0 = Sin Amueblar
        
    Returns:
    - encoded_solicitud: dict
        La version encoded del input solicitud.
    """

    # Se llena el diccionario solicitud con los inputs del usuario en la web.
    solicitud = {
        "Tipo" : tipo,
        "Distrito" : distrito,
        "Barrio" : barrio,
        "Habitaciones" : hab,
        "Banos" : banos,
        "Area" : area,
        "Furnished" : furnished
    }
    # Proceder con encoding la solicitud
    encoded_solicitud = encode_solicitud(solicitud, label_encoders)

    return encoded_solicitud   

def fiability(distrito, condicion , area , prediction):
    """
    Revisar el precio por m2 de la vivienda que ha predecido por el modelo. Validar ante los estandáres
    estipulados por m2 en base al distrito y condición de la vivienda.
    
    Parametros:
    - prediction: int
        El input de distrito de Madrid donde esta ubicada la vivienda
    - distrito: texto
        El input de distrito de Madrid donde esta ubicada la vivienda
    - condicion: texto
        El input de la condicion (estado) de la vivienda (normal/alta-calidad/lujosa)
    - area: int
        El area en m2 de la vivienda

    Returns:
    - fiabilidad: texto
        La metrica de fiabilidad (Alta/Media/Baja)
    """
    # Evaluar precio por m2
    pred_m2 = prediction / area

    # Identificar en que distrito esta la vivienda y evaluar ante el precio por m2 estandar
    if distrito in Distritos1:
        if pred_m2 >= 37:
            return "Fiabilidad Baja"
        elif 26 <= pred_m2 < 37 and condicion == "lujosa":
            return "Fiabilidad Media"
        elif 16 <= pred_m2 < 26 and (condicion == "alta-calidad" or condicion == "normal" or condicion == "lujosa"):
            return "Fiabilidad Alta"  
        elif 11 <= pred_m2 < 16 and (condicion == "normal" or condicion == "alta-calidad"):
            return "Fiabilidad Alta"
        else:
            return "Fiabilidad Baja"
        
    if distrito in Distritos2:
        if pred_m2 >= 41:
            return "Fiabilidad Baja"
        elif 28 <= pred_m2 < 41 and condicion == "lujosa":
            return "Fiabilidad Media"
        elif 20 <= pred_m2 < 28 and (condicion == "alta-calidad" or condicion == "normal" or condicion == "lujosa"):
            return "Fiabilidad Alta"  
        elif 15 <= pred_m2 < 20 and (condicion == "normal" or condicion == "alta-calidad"):
            return "Fiabilidad Alta"
        else:
            return "Fiabilidad Baja"
        
    if distrito in Distritos3:
        if pred_m2 >= 44:
            return "Fiabilidad Baja"
        elif 33 <= pred_m2 < 44 and condicion == "lujosa":
            return "Fiabilidad Media"
        elif 23 <= pred_m2 < 33 and (condicion == "alta-calidad" or condicion == "normal" or condicion == "lujosa"):
            return "Fiabilidad Alta"  
        elif 18 <= pred_m2 < 23 and (condicion == "normal" or condicion == "alta-calidad"):
            return "Fiabilidad Alta"
        else:
            return "Fiabilidad Baja"