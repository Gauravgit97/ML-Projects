import streamlit as st
import pandas as pd
import pickle
import requests


def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)),reverse=True,key = lambda x:x[1])[1:6]

    recommended_movies_list = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].MAL_ID

        recommended_movies_list.append(movies.iloc[i[0]].title)

    return recommended_movies_list




movies_dict = pickle.load(open('Dataset\\anime\\anime_dic.pkl','rb'))
movies = pd.DataFrame(movies_dict)
movies_list = movies['title'].values

similarity= pickle.load(open('Dataset\\anime\\similarity_anime.pkl','rb'))

page_bg_img = f"""
<style>
[data-testid="stMain"]{{
background-image: url("https://images.unsplash.com/photo-1501426026826-31c667bdf23d");
background-size: 180%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stSidebar"]{{
background-image: url("https://images.unsplash.com/photo-1501426026826-31c667bdf23d");
background-size: 180%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title('Anime Recommender')

st.sidebar.success("Select Any Page from here") 

movie_name = st.selectbox('Find your movie here:',movies_list)
if st.button('Recommend'):
    movie_name = recommend(movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(movie_name[0])

    with col2:
        st.text(movie_name[1])

    with col3:
        st.text(movie_name[2])
    
    with col4:
        st.text(movie_name[3])
    
    with col5:
        st.text(movie_name[4])


st.write(f"**© 2025 Entertainment Buddy. All Rights Reserved.**"+
"**© 2025 Entertainment Buddy. Anime, TV Show, and Movie Recommender System. All Rights Reserved.**")