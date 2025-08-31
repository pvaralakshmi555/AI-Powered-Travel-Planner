import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

# Custom CSS for highlighting the form box
st.markdown("""
    <style>
    div[data-testid="stForm"] {
        border: 2px solid #4CAF50;
        border-radius: 15px;
        padding: 20px;
        background-color: #f9fff9;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="AI Travel Planner", page_icon="✈️", layout="wide")

st.title("🌍 AI-Powered Travel Planner")
st.markdown("Plan your trip smartly with **AI-powered suggestions** 🚕 🚆 🚌 ✈️")

# Input form
with st.form("travel_form"):
    col1, col2 = st.columns(2)
    with col1:
        source = st.text_input("🏙️ Source City", "Hyderabad")
    with col2:
        destination = st.text_input("📍 Destination City", "Bangalore")
    submitted = st.form_submit_button("🔍 Get Travel Options")

if submitted:
    # LangChain setup
    out_parser = StrOutputParser()

    # chat_template = ChatPromptTemplate.from_messages([
    #     ("system", 
    #      "You are an AI-Powered Travel Planner. "
    #      "Your job is to process user inputs  given source and destination and generate various travel choices such as cab, train, bus, and flights, along with their estimated costs. "
    #      "Format output as markdown cards for each travel mode."),
    #     ("human", "{Source} {Destination}")
    # ])
    chat_template = ChatPromptTemplate.from_messages([
        ("system", 
         "You are an AI-Powered Travel Planner. "
         "Given a source and destination, generate travel choices such as Flight, Train, Bus, and Cab. "
         "Provide comparison in a **Markdown table** with these columns:\n\n"
         "Mode of Transport| Airlines/Train Name/Operators/ | Estimated Travel Time | Estimated Cost | Notes\n\n"
         ),
        ("human", "Source: {Source}, Destination: {Destination}")
    ])
    
    chat_model = ChatGoogleGenerativeAI(
        api_key=Your_API_KEY,  # 🔑 Replace with your API key
        model="gemini-2.0-flash"
    )

    chain = chat_template | chat_model | out_parser

    # Run query
    raw_input = {"Source": source, "Destination": destination}
    result = chain.invoke(raw_input)
    
    # Correct way in Streamlit
    st.markdown(result, unsafe_allow_html=True)
        
