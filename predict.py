import pickle
from constants import label_to_encoded, rng, sleep, Registros_por_Distrito
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

def estimacion(encoded_solicitud): # Usar la encoded solicitud para hacer la estimacion de precio mensual
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

def fiability(distrito, condicion):
    """
    Revisar el numero de registros de viviendas en el distrito solicitado en el query para dar una metrica
    de fiabilidad del modelo.
    
    Parametros:
    - distrito: texto
        El input de distrito de Madrid donde esta ubicada la vivienda

    Returns:
    - fiabilidad: texto
        La metrica de fiabilidad (Alta/Media/Baja)
    """
    # Revisar numero de registros en el distrito del query
    number = Registros_por_Distrito[distrito]

    if number >= 1000:
        return "Fiabilidad Alta"
    elif 300 < number < 1000:
        return "Fiabilidad Media"
    elif number < 300:
        return "Fiabilidad Baja"