import numpy as np
import pickle
import streamlit as st

#Loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

#creating a function for prediction
def monthlyexp_prediction(input_data):
    # Sample new data (replace with your actual data)

# Reshape the input data to match the model's input shape
  new_data = np.array(input_data).reshape(1, -1)

# Make predictions on the new data
  predictions = loaded_model.predict(new_data)
  for i, prediction in enumerate(predictions):
# Print the prediction
   if(prediction>400):
    return f"Your predicted Monthly Expense = ₹ {prediction:.0f}"
   else:
     return f"Your predicted Monthly Expense = Around ₹500"
def main():
    # Adding GitHub icon and link

  #giving a title
  st.title('Monthly Expenses Predictior💸 namely "KharchaKitna"')
 
  st.write("""
    ## Welcome to the "KharchaKitna"!
           You ever wonder how much money is required to surive between Dumna & Airport!!!
                    Just Kidding!!! I means in our IIITDMJ🏫 :)
    This tool helps students at our IIITDMJ Campus to predict their monthly expenses based on various factors such as:
    - Mess Taken
    - Canteen Visits
    - Relationship Status
    - Online Food Orders
    - City Visits

    NOTE:- If you have opted for mess then your monthly mess amount will be not included with the MonthlyExpense, since it is already paid at the start of the Semester.
    
    Simply input your details below and click 'Predict' to see your estimated monthly expenses.
    """)

  #getting the input data from the user
  #MessTaken CanteenVisit RelationshipStatus OnlineFood CityVisit MonthlyExpense		
  MessTaken = st.select_slider('Have you opted for Mess?',['Yes✅','No❌'])
  CanteenVisit = st.select_slider('No. of days you go Canteen/Hexa/Nescafe in a week.',[0,1,2,3,4,5,6,7])
  RelationshipStatus = st.select_slider('Your Relationship Status',['Single🗿', 'Mingle😁'])
  OnlineFood = st.select_slider('No. of times you order food online in a month.',[0,1,2,3,4,5,6,7,8,9,10])
  CityVisit = st.select_slider('No. of days you go out to city in a month',[0,1,2,3,4,5,6,7])
  if(MessTaken=='Yes✅'):
    MessTaken = 1
  else :
    MessTaken = 0
  if(RelationshipStatus=='Single🗿'):
    RelationshipStatus = 0
  else :
    RelationshipStatus = 1
  #Code for prediction
  predicted = ''
  #Creating a button for Prediction
  if st.button('Predict'):
    predicted = monthlyexp_prediction([MessTaken,CanteenVisit,RelationshipStatus,OnlineFood,CityVisit])

  st.success(predicted)
  st.markdown('---')
  st.write("""If you are not satisfied by the prediction.
           
OR
           
Want to know more about this project. 
           
Checkout the GitHub Repo of this project the link is mentioned below.""")
  st.write("https://github.com/sumitc27/SoM_MonthlyExpense")
  st.markdown('---')
  st.write("This ML Project is a product of Summer of ML, which is part of TPC’s summer open-source program BSOC")
  st.markdown("""
    <a href="https://github.com/sumitc27" target="_blank">
        <img src="https://img.icons8.com/ios-glyphs/30/000000/github.png" alt="GitHub icon"/>
    </a>
    """, unsafe_allow_html=True) 
  st.write('Link to My GitHub Account')
  st.write("Made with ❤️ by Sumit")

if __name__ == '__main__':
  main()
   
  
  


