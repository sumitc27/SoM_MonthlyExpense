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
def inject_styles():
  # Purely presentational. No application/business logic is affected.
  # Restyles the BaseWeb sliders that st.select_slider renders into:
  #   thicker rounded track, indigo->violet gradient fill, larger thumb with ring.
  st.markdown(
    """
    <style>
      :root {
        --kk-accent-a: #6366f1;   /* indigo */
        --kk-accent-b: #8b5cf6;   /* violet */
        --kk-track-bg: rgba(148, 163, 184, 0.28);
        --kk-ease: cubic-bezier(0.16, 1, 0.3, 1);
      }

      /* ============================================================
         CARD: center the inputs in a ~60vw panel instead of a full
         page-width column. Purely visual — no layout logic changes.
         ============================================================ */
      .block-container {
        max-width: 60vw !important;
        margin-left: auto !important;
        margin-right: auto !important;
        padding: 2.2rem 2.4rem !important;
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(148, 163, 184, 0.18);
        border-radius: 20px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.25);
        backdrop-filter: blur(6px);
      }
      /* On small screens a 60vw card is too cramped — widen it back. */
      @media (max-width: 900px) {
        .block-container { max-width: 92vw !important; padding: 1.4rem 1.2rem !important; }
      }

      /* ============================================================
         SHORT BINARY SLIDERS
         The Yes/No and Single/Mingle sliders only have two options, so
         the thumb shouldn't travel the whole card. Each is wrapped (in
         Python) in a container keyed "kk-binary"; we shrink the slider
         inside it. A tiny drag now flips it end-to-end.
         ============================================================ */
      .st-key-kk-binary-mess [data-baseweb="slider"],
      .st-key-kk-binary-rel [data-baseweb="slider"] {
        max-width: 170px;
      }
      /* Keep the min/max tick labels under the short track aligned to it */
      .st-key-kk-binary-mess [data-testid="stSliderTickBar"],
      .st-key-kk-binary-rel [data-testid="stSliderTickBar"] {
        max-width: 170px;
      }

      /* ---- The track: thicker + fully rounded ----
         BaseWeb renders the track as nested divs with inline styles, so we
         match the bars by height and force our look with !important. */
      [data-testid="stSlider"] [data-baseweb="slider"] [role="slider"] {
        /* Bigger, cleaner thumb */
        height: 22px !important;
        width: 22px !important;
        background: #ffffff !important;
        border: 2px solid var(--kk-accent-a) !important;
        box-shadow: 0 2px 6px rgba(0,0,0,0.18),
                    0 0 0 0 rgba(99,102,241,0.0) !important;
        transition: box-shadow 160ms var(--kk-ease),
                    transform 160ms var(--kk-ease) !important;
        will-change: transform;
        cursor: grab;
      }
      [data-testid="stSlider"] [role="slider"]:hover {
        transform: scale(1.08);
        box-shadow: 0 2px 8px rgba(0,0,0,0.22),
                    0 0 0 7px rgba(99,102,241,0.16) !important;
      }
      [data-testid="stSlider"] [role="slider"]:active {
        cursor: grabbing;
        transform: scale(1.12);
        box-shadow: 0 2px 10px rgba(0,0,0,0.25),
                    0 0 0 10px rgba(99,102,241,0.22) !important;
      }
      [data-testid="stSlider"] [role="slider"]:focus-visible {
        outline: none;
        box-shadow: 0 2px 8px rgba(0,0,0,0.22),
                    0 0 0 8px rgba(99,102,241,0.28) !important;
      }

      /* The two horizontal bars inside the slider (base track + filled range).
         BaseWeb gives them inline background + height. We thicken & round them,
         and recolor the FILLED part (the one that isn't the gray base) with a
         gradient. The base track is forced to a soft neutral. */
      [data-testid="stSlider"] [data-baseweb="slider"] > div > div {
        height: 8px !important;
        border-radius: 999px !important;
      }
      /* Base (unfilled) track */
      [data-testid="stSlider"] [data-baseweb="slider"] > div > div {
        background: var(--kk-track-bg) !important;
      }
      /* Filled range: the inner highlighted segment gets the gradient */
      [data-testid="stSlider"] [data-baseweb="slider"] > div > div > div {
        background: linear-gradient(90deg, var(--kk-accent-a), var(--kk-accent-b)) !important;
        border-radius: 999px !important;
        height: 8px !important;
      }

      /* The value number above the thumb: match the new accent, not red */
      [data-testid="stSliderThumbValue"] {
        color: var(--kk-accent-a) !important;
        font-weight: 700 !important;
      }
      /* Min/max tick labels: subtle */
      [data-testid="stSliderTickBar"] {
        opacity: 0.75;
      }

      @media (prefers-reduced-motion: reduce) {
        [data-testid="stSlider"] [role="slider"] {
          transition: none !important;
        }
        [data-testid="stSlider"] [role="slider"]:hover,
        [data-testid="stSlider"] [role="slider"]:active {
          transform: none !important;
        }
      }
    </style>
    """,
    unsafe_allow_html=True,
  )

def main():
    # Adding GitHub icon and link

  # Presentational styles only — injected before widgets render (no FOUC).
  inject_styles()

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
  with st.container(key="kk-binary-mess"):
    MessTaken = st.select_slider('Have you opted for Mess?',['Yes✅','No❌'])
  CanteenVisit = st.select_slider('No. of days you go Canteen/Hexa/Nescafe in a week.',[0,1,2,3,4,5,6,7])
  with st.container(key="kk-binary-rel"):
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
   
  
  


