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
        recommended_movies_poster.append("http://image.tmdb.org/t/p/w500/"+movies.iloc[i[0]].poster_path)

    return recommended_movies_list,recommended_movies_poster




movies_dict = pickle.load(open('Dataset\show\show_dic.pkl','rb'))
movies = pd.DataFrame(movies_dict)
movies_list = movies['title'].values

similarity= pickle.load(open('Dataset\show\similarity_tv.pkl','rb'))

st.title('TV Show Recommender')
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


st.text("Uncover your next favorite TV series with our TV show recommendation system. Built on a powerful ML model trained with thousands of top-rated and trending shows, we ensure personalized suggestions tailored to your viewing preferences. Whether you love gripping dramas, hilarious comedies, or edge-of-your-seat thrillers, we've got you covered.")

st.write(f"**© 2025 Entertainment Buddy. All Rights Reserved.**"+
"**© 2025 Entertainment Buddy. Anime, TV Show, and Movie Recommender System. All Rights Reserved.**")