import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open('DT_car.pkl','rb'))


st.title('Fill up the details of your car')

present_price=int(st.number_input('Enter the Present Price of your car',min_value=0))
km_driven=int(st.number_input('Enter the kms Driven by your car',min_value=0))
make_year=int(st.number_input('Enter the year of purchase of your car',min_value=1900,max_value=2021))
fuel_type=st.selectbox('Fuel Type',options=['Petrol','Diesel','CNG'])
transmission_type=st.selectbox('Transmission Type',options=['Manual','Automatic'])
seller_type=st.selectbox('Seller Type',options=['Dealer','Individual'])

if seller_type == 'Dealer':
    seller_individual = 0
else:
    seller_individual = 1

if transmission_type == 'Manual':
    trans_manual = 1
else:
    trans_manual = 0


if fuel_type == 'Petrol':
    fuel_type_petrol = 1
    fuel_type_diesel = 0

elif fuel_type == 'Diesel':
    fuel_type_petrol = 0
    fuel_type_diesel = 1

else:
    fuel_type_petrol = 0
    fuel_type_diesel = 0



if st.button('Predict'):
    age_of_car=2021-make_year

    prediction=model.predict(pd.DataFrame([present_price,km_driven,age_of_car,fuel_type_diesel,fuel_type_petrol,seller_individual,trans_manual]).T.values)
    st.title(round(prediction[0]))



