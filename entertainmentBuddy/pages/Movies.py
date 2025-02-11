import streamlit as st
import pandas as pd
import pickle
import requests


def fatch_poster(movie_id):
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3MzM1NjMwMzkwZWQ0ODg3YmUwZWQyNTA0MmU0NjZkYiIsIm5iZiI6MTczMzE2MjE2OS40Mywic3ViIjoiNjc0ZGY0YjllYmI5MmU0YTdlMDQ5YWEyIiwic2NvcGVzIjpbImFwaV9yZWFkIl0sInZlcnNpb24iOjF9.m7ooLZj4W_EPGVbxrEUkl2lBVblTnBXoVxvctBhQFxM"
    }
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    response = requests.get(url, headers=headers)
    data = response.json()
    return "http://image.tmdb.org/t/p/w500/"+data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)),reverse=True,key = lambda x:x[1])[1:6]

    recommended_movies_list = []
    recommended_movies_poster = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].id

        recommended_movies_list.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fatch_poster(movie_id))

    return recommended_movies_list,recommended_movies_poster



movies_dict = pickle.load(open('Dataset\movie\movie_dic.pkl','rb'))
movies = pd.DataFrame(movies_dict)
movies_list = movies['title'].values

similarity= pickle.load(open('Dataset\movie\similarity.pkl','rb'))
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

st.title('Movie Recommender')

st.sidebar.success("Select Any Page from here") 

movie_name = st.selectbox('Find your movie here:',movies_list)
if st.button('Recommend'):
    movie_name,movies_poster = recommend(movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(movie_name[0])
        st.image(movies_poster[0])

    with col2:
        st.text(movie_name[1])
        st.image(movies_poster[1])

    with col3:
        st.text(movie_name[2])
        st.image(movies_poster[2])
    
    with col4:
        st.text(movie_name[3])
        st.image(movies_poster[3])
    
    with col5:
        st.text(movie_name[4])
        st.image(movies_poster[4])


st.text("Experience the magic of cinema like never before with our movie recommendation engine. Using a dedicated ML model trained on an extensive dataset of blockbuster hits, indie gems, and timeless classics, we deliver quick and accurate recommendations. Let us guide you to your next cinematic adventure")

st.write(f"**© 2025 Entertainment Buddy. All Rights Reserved.**"+
"**© 2025 Entertainment Buddy. Anime, TV Show, and Movie Recommender System. All Rights Reserved.**")