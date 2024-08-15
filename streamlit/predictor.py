import streamlit as st
import requests

# Definir la URL base de la API
API_URL = "http://paramapi:8585"

# Obtener los datos de la API
def fetch_data(endpoint):
    response = requests.get(f"{API_URL}/{endpoint}")
    if response.status_code == 200:
        return response.json()
    return []

# Mock de la función que simula una API para predecir el precio estimado
def mock_predict_price(data):
    # Simulando una predicción basada en los datos recibidos (en realidad solo devuelve un valor fijo o calculado simple)
    estimated_price = data['operation_amount'] * 1.1  # Ejemplo: aplicar un incremento del 10%
    return {"estimated_price": estimated_price}

# Opciones extraídas
operation_types = fetch_data("operationtypes")
currencies = fetch_data("currencies")
cities = fetch_data("cities")
states = fetch_data("states")
countries = fetch_data("countries")

# Formulario principal
def main():
    st.title('Property Form')

    with st.form(key='property_form'):
        # Campos de texto
        id = st.text_input('ID')
        name = st.text_input('Name')
        publisher_id = st.text_input('Publisher ID')
        publisher_name = st.text_input('Publisher Name')
        address = st.text_input('Address')
        latitude = st.text_input('Latitude')
        longitude = st.text_input('Longitude')
        url = st.text_input('URL')

        # Combos
        operation_type = st.selectbox('Operation Type', operation_types)
        operation_currency = st.selectbox('Operation Currency', currencies)
        expenses_currency = st.selectbox('Expenses Currency', currencies)
        city = st.selectbox('City', cities)
        state = st.selectbox('State', states)
        country = st.selectbox('Country', countries)

        # Campos numéricos
        operation_amount = st.number_input('Operation Amount', min_value=0.0, step=0.01)
        expenses_amount = st.number_input('Expenses Amount', min_value=0.0, step=0.01)
        total_mts = st.number_input('Total Meters', min_value=0.0, step=0.01)
        covered_mts = st.number_input('Covered Meters', min_value=0.0, step=0.01)
        rooms = st.number_input('Rooms', min_value=0)
        bedrooms = st.number_input('Bedrooms', min_value=0)
        bathrooms = st.number_input('Bathrooms', min_value=0)
        garages = st.number_input('Garages', min_value=0)
        antique = st.number_input('Antique', min_value=0)
        number_of_floors = st.number_input('Number of Floors', min_value=0)
        apartments_per_floor = st.number_input('Apartments per Floor', min_value=0)
        publication_antiquity = st.number_input('Publication Antiquity', min_value=0)

        # Botón para enviar
        submitted = st.form_submit_button('Submit')

        # Enviar datos a la API mock y obtener el precio estimado
        if submitted:
            # Crear un diccionario con los datos del formulario
            property_data = {
                'id': id,
                'name': name,
                'operation_type': operation_type,
                'operation_currency': operation_currency,
                'operation_amount': operation_amount,
                'expenses_currency': expenses_currency,
                'expenses_amount': expenses_amount,
                'total_mts': total_mts,
                'covered_mts': covered_mts,
                'rooms': rooms,
                'bedrooms': bedrooms,
                'bathrooms': bathrooms,
                'garages': garages,
                'antique': antique,
                'building_layout': None,  # Placeholder, no incluimos este campo
                'orientation': None,  # Placeholder, no incluimos este campo
                'number_of_floors': number_of_floors,
                'apartments_per_floor': apartments_per_floor,
                'real_estate_type': None,  # Placeholder, no incluimos este campo
                'posting_type': None,  # Placeholder, no incluimos este campo
                'publisher_id': publisher_id,
                'publisher_name': publisher_name,
                'address': address,
                'city': city,
                'state': state,
                'country': country,
                'latitude': latitude,
                'longitude': longitude,
                'reserved': None,  # Placeholder, no incluimos este campo
                'publication_antiquity': publication_antiquity,
                'url': url
            }

            # Simular llamada a la API para predecir el precio
            prediction = mock_predict_price(property_data)
            estimated_price = prediction['estimated_price']

            # Mostrar el precio estimado
            st.success(f'El precio estimado de la propiedad es: {estimated_price} {operation_currency}')

if __name__ == '__main__':
    main()
