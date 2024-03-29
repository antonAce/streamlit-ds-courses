import streamlit as st

st.set_page_config(
    page_title="Conclusions",
    page_icon="📒",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.title("Conclusions")

st.subheader("EDA Insights")
st.markdown(
    """
    1. The majority of the Data Science courses are dedicated to Beginners;
    2. The most common keywords in Data Science courses are: `Python`, `Machine learning`, `Data`, `R`, `Deep Learning`, `Statistics`, `TensorFlow` e.t.c.;
    3. `Udemy` is the most suitable platform for Beginners and General level students, and `Coursera` - for Intermediate and Expert;
    4. Among platforms with the most significant amount of content, `Coursera` has the highest average rating;
    5. Top tech organizations that have the highest average rating are `SAS`, `DeepLearning.AI`, `IBM`, and top educational organizations are `The University of Michigan`, `University of California`, `Johns Hopkins University`;
    6. The rating of the course may indeed depend on whether it is free or not;
    """
)

st.subheader("Techstack")
st.markdown(
    """
    Webcrawlers

    ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
    ![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=Selenium&logoColor=white)
    ![Zyte](https://img.shields.io/badge/Zyte-E10098?style=for-the-badge&logoColor=white)
    ![Scrapy+Splash](https://img.shields.io/badge/Scrapy+Splash-60a839?&style=for-the-badge&logoColor=white)

    Processing pipelines

    ![Conda](https://img.shields.io/badge/conda-342B029.svg?&style=for-the-badge&logo=anaconda&logoColor=white)
    ![Jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white)
    ![Apache Spark](https://img.shields.io/badge/Apache_Spark-FFFFFF?style=for-the-badge&logo=apachespark&logoColor=#E35A16)

    Dashboard

    ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
    ![Plotly](https://img.shields.io/badge/Plotly-239120?style=for-the-badge&logo=plotly&logoColor=white)
    ![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)

    """
)
