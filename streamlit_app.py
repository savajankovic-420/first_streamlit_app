import streamlit
import pandas as pd

streamlit.title('My Moms New Healthy Diner') 


streamlit.header('Breakfast Menu')
streamlit.text('π₯£ Omega 3 & Blueberry Oatmeal')
streamlit.text('π₯ Kale, Spinach & Rocket Smoothie')
streamlit.text('πHard-Boiled Free-Range Egg')
streamlit.text('π₯π Avocado Toast')
  
streamlit.header('ππ₯­ Build Your Own Fruit Smoothie π₯π')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# The fruit list is indexed and will show which fruits are in the table
my_fruit_list = my_fruit_list.set_index('Fruit')

#Creating a pick list for the user to filter the table. 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected] # the loc function finds the fruits

#displaying the table on the page
streamlit.dataframe(fruits_to_show)
