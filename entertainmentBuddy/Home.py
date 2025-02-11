import streamlit as st

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

st.title('Entertainment Buddy')

st.sidebar.success("Select Any category from here") 

st.title('Movies')
movie_name,movies_poster = ['The Dark Knight','Firefox','Independence Day','Skyfall','Quantum of Solace'],['http://image.tmdb.org/t/p/w500//qJ2tW6WMUDux911r6m7haRef0WH.jpg','http://image.tmdb.org/t/p/w500//xP6VaKdFEriMzPXe3j5YyDF3ryS.jpg','http://image.tmdb.org/t/p/w500//p0BPQGSPoSa8Ml0DAf2mB2kCU0R.jpg','http://image.tmdb.org/t/p/w500//d0IVecFQvsGdSbnMAHqiYsNYaJT.jpg','http://image.tmdb.org/t/p/w500//e3DXXLJHGqMx9yYpXsql1XNljmM.jpg']

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

st.title('TV Show')
movie_name,movies_poster = ['Game of Thrones','Money Heist','Stranger Things','The Walking Dead','Squid Game'],['http://image.tmdb.org/t/p/w500//1XS1oqL89opfnbLl8WnZY1O1uJx.jpg','http://image.tmdb.org/t/p/w500//reEMJA1uzscCbkpeRJeTT2bjqUp.jpg','http://image.tmdb.org/t/p/w500//49WJfeN0moxb9IPfGn8AIqMGskD.jpg','http://image.tmdb.org/t/p/w500//n7PVu0hSz2sAsVekpOIoCnkWlbn.jpg','http://image.tmdb.org/t/p/w500//dDlEmu3EZ0Pgg93K2SVNLCjCSvE.jpg']

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


st.title("About Us")
st.text("Our system is designed to cater to your unique tastes with dedicated machine learning models for each category: Anime, TV Shows, and Movies. Each model is optimized with its own dataset, carefully curated to include thousands of titles spanning diverse genres and styles. Whether you're exploring the world of anime, binging on TV shows, or diving into cinematic masterpieces, our recommendation engine ensures lightning-fast results. By using category-specific models, we deliver precise and personalized suggestions, ensuring every recommendation feels just right for you.")

st.write(f"**© 2025 Entertainment Buddy. All Rights Reserved.**"+
"**© 2025 Entertainment Buddy. Anime, TV Show, and Movie Recommender System. All Rights Reserved.**")