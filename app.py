import streamlit as st
st.set_page_config(page_title='My Streamlit App', layout='wide', initial_sidebar_state='auto')
from streamlit_option_menu import option_menu
from predictor_dashboard import main

st.markdown("<h1 style='text-align:center; padding-top: 0rem; color:black;'>Predictor</h1>", unsafe_allow_html=True)

selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Dashboard", "About"],  # required
            icons=["house", "bi bi-speedometer2", "bi bi-info-circle"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )


if selected == "Home":
    st.title("Welcome to our Predictor: ML web app!")

    # Highlight the benefits
    st.markdown("<h5>Get accurate estimates for the prices of used cars and salaries of software developers based on various factors such as location, experience, and more.</h5>",unsafe_allow_html=True)

    # Use clear and concise language
    st.markdown("<h5>Our easy-to-use app provides accurate predictions for used car prices and software developer salaries based on advanced machine learning algorithms.</h5>",unsafe_allow_html=True)

    # Provide clear instructions
    st.markdown("<h5>Simply input key parameters such as the make and model of the car, or the developer's years of experience and location, and our app will provide an estimated price or salary.</h5>",unsafe_allow_html=True)


    image2 = "image2.jpg"
    image4 = "imageSD.jpg"
    
    # set the text for each image
    text1 = ("<p style='text-align:center;'>Get the best value for your car!</p>")
    text2 = ("<p style='text-align:center;'>Get the proper salary!<p>")

    col1, col2 = st.columns(2)

    # Display the images in each column
    with col1:
        st.image(image2, use_container_width=True, width=100)
        st.markdown(text1, unsafe_allow_html=True)

    with col2:
        st.image(image4, use_container_width=True, width=100)
        st.markdown(text2, unsafe_allow_html=True)
    
    text_block1, text_block2 = st.columns(2)
    with text_block1:
        # st.markdown("<p style="font-size:";>Introducing our predictor web app! Our app is designed to help you predict the prices of used cars and salaries of software developers, based on various factors that influence these markets. By inputting key parameters such as the make and model of the car or the developer's years of experience and location, our app will provide an estimated price or salary.</p>", unsafe_allow_html=True)
        st.subheader("Introducing our predictor web app! Our app is designed to help you predict the prices of used cars and salaries of software developers, based on various factors that influence these markets. By inputting key parameters such as the make and model of the car or the developer's years of experience and location, our app will provide an estimated price or salary.")
    
    text_block3, text_block4 = st.columns(2)
    with text_block3:
        st.subheader("")

    with text_block4:
        st.subheader("Our user-friendly interface makes it easy to input and adjust the relevant parameters, and our prediction model is based on advanced machine learning algorithms that have been trained on large datasets. With this app, you can make more informed decisions when buying or selling a used car or negotiating a salary as a software developer.")
    
    text_block3, text_block4 = st.columns(2)
    with text_block3:
        st.subheader("Whether you are in the market for a used car or looking to hire or be hired as a software developer, our predictor web app is a powerful tool to help you make informed decisions. Try it out today and experience the benefits of our cutting-edge prediction technology.")

if selected == "Dashboard":
    main()

if selected == "About":
    st.title("About")
    st.write("""Welcome to Predictor, a web app that predicts used car prices and software developer salaries with the help of machine learning algorithms.

Our team has built a sophisticated predictive model using a variety of data sources, including historical sales data, demographic information, and job market trends. This model takes into account a wide range of factors that can influence the price of a used car or the salary of a software developer, such as location, age, make and model of the car, years of experience, education level, and more.

With Predictor, you can quickly and easily get an estimate of the value of a used car or the salary you might expect to earn as a software developer. Simply enter the relevant information into the app, and our predictive model will do the rest. You'll receive a detailed report that shows you how we arrived at our estimate, along with a range of possible values based on different scenarios.

Our goal with Predictor is to provide you with a fast, reliable, and accurate tool for making informed decisions about buying or selling a used car, or negotiating your salary as a software developer. We believe that machine learning can be a powerful tool for solving real-world problems, and we're excited to share our work with you.

Thank you for using Predictor, and we hope you find our web app helpful and informative.""")

