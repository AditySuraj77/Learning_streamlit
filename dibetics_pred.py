import numpy as np
import streamlit as st
import pickle

loading_model = pickle.load(open('model.pkl','rb'))

def dibetics_prediction(input_data):
    # converting input_data into numpy asarray
    input_data_numpy_asarray = np.asarray(input_data)
    # reshape the input_numpy_array_data
    input_data_reshape = input_data_numpy_asarray.reshape(1, -1)

    prediction = loading_model.predict(input_data_reshape)
    print(prediction)

    if prediction[0] == 0:
        return 'The Person is Non - Diabetics'
    else:
        return 'The Person is Diabitecs'


# take input from user
def main():
    st.title('Dibetics Predictions')

Pregnancies = st.text_input('Pregnancies')
Glucose = st.text_input('Glucose')
BloodPressure = st.text_input('BloodPressure')
SkinThickness = st.text_input('SkinThickness')
Insulin = st.text_input('Insulin')
BMI = st.text_input('BMI')
DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction')
Age = st.text_input('Age')

digonosis = ''

if st.button('Predict'):
    digonosis = dibetics_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,
                                     DiabetesPedigreeFunction,Age ])
st.success(digonosis)

if __name__ == '__main__':
    main()