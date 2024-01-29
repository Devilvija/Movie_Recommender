import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=f9128014ddd148a9900e85721dea8a31&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies["movie_name"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].movie_name)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster


def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://i.pinimg.com/originals/52/92/ef/5292ef7dd72f9cf4a9b7001712f82bad.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )


add_bg_from_url()

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity (1).pkl', 'rb'))
data = pd.read_csv('data.csv')

st.title('Movie Recommender System')


Selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies['movie_name'].values)

if st.button('Recommend'):
    names, posters = recommend(Selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(posters[0], width=250)
        st.header(names[0])
        # Get director and cast information from the data DataFrame
        movie_info = data[data['movie_name'] == names[0]]
        st.markdown("---")
        st.subheader('Director:')
        st.write(movie_info['directors'].values[0])
        st.subheader('Cast:')
        st.write(movie_info['stars'].values[0])

    with col2:
        st.image(posters[1], width=250)
        st.header(names[1])
        # Get director and cast information from the data DataFrame
        movie_info = data[data['movie_name'] == names[1]]
        st.markdown("---")
        st.subheader('Director:')
        st.write(movie_info['directors'].values[0])
        st.subheader('Cast:')
        st.write(movie_info['stars'].values[0])

    with col3:
        st.image(posters[2], width=250)
        st.header(names[2])
        # Get director and cast information from the data DataFrame
        movie_info = data[data['movie_name'] == names[2]]
        st.markdown("---")
        st.subheader('Director:')
        st.write(movie_info['directors'].values[0])
        st.subheader('Cast:')
        st.write(movie_info['stars'].values[0])

    with col4:
        st.image(posters[3], width=250)
        st.header(names[3])
        # Get director and cast information from the data DataFrame
        movie_info = data[data['movie_name'] == names[3]]
        st.markdown("---")
        st.subheader('Director:')
        st.write(movie_info['directors'].values[0])
        st.subheader('Cast:')
        st.write(movie_info['stars'].values[0])

    with col5:
        st.image(posters[4], width=250)
        st.header(names[4])
        # Get director and cast information from the data DataFrame
        movie_info = data[data['movie_name'] == names[4]]
        st.markdown("---")
        st.subheader('Director:')
        st.write(movie_info['directors'].values[0])
        st.subheader('Cast:')
        st.write(movie_info['stars'].values[0])

        st.markdown("---")
        st.subheader(''':white[PROJECT DONE BY: 'Mr. Vijay Balnath Rawal']''')
        st.markdown("---")
