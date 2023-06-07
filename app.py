import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image
import json
import urllib.request
import base64
import textwrap


#   Título de la página
st.set_page_config(page_title="Canchita reviews", page_icon="🍿", layout="wide")

######################################
# Definicion de Funciones de la Página
######################################

# Request el lottie interactivo para utilizar en el website
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Request el API creado para utilizar en el website
def descarga_api_videos(urlapi):
    r = requests.get(urlapi)
    if r.status_code != 200:
        return None
    data = r.json()
    return data


# utiliza archivo CSS local para modificar boxes en el website
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Insert imagen CSV
def render_svg(svg_file):
    b64 = base64.b64encode(svg_file.encode('utf-8')).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
    st.write(html, unsafe_allow_html=True)

######################################
# Recursos a utilizar en el website
######################################

local_css("style/style.css")

#Fetch de LottieFiles
premios = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_4ftwog8c.json")
resenhas = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_yetxuujw.json")
trailers = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_j1adxtyb.json")

#SVG
star =  """<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="yellow" class="bi bi-star-fill" viewBox="0 0 24 24">
                <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
           </svg>"""

#Fetch del API creado
peliculas_base_datos = descarga_api_videos("https://curious-fedora-calf.cyclic.app/canchita/api/movies/movies")

#Imágenes
Fondo = Image.open("images/Fondo.jpg")

urllib.request.urlretrieve(
  'https://image.tmdb.org/t/p/w500'+ peliculas_base_datos[0]["poster_path"],
   "fondo0.png")
urllib.request.urlretrieve(
  'https://image.tmdb.org/t/p/w500'+ peliculas_base_datos[1]["poster_path"],
   "fondo1.png")
urllib.request.urlretrieve(
  'https://image.tmdb.org/t/p/w500'+ peliculas_base_datos[2]["poster_path"],
   "fondo2.png")
img_fondo0 = Image.open('fondo0.png')
img_fondo1 = Image.open('fondo1.png')
img_fondo2 = Image.open('fondo2.png')


#Overview
overview0 = peliculas_base_datos[0]["overview"]
overview1 = peliculas_base_datos[1]["overview"]
overview2 = peliculas_base_datos[2]["overview"]

#Nombres de las Peliculas
title0 = peliculas_base_datos[0]["original_title"]
title1 = peliculas_base_datos[1]["original_title"]
title2 = peliculas_base_datos[2]["original_title"]

#Calificación promedio
average0 = peliculas_base_datos[0]["vote_average"]
average1 = peliculas_base_datos[1]["vote_average"]
average2 = peliculas_base_datos[2]["vote_average"]

#Video Trailer
video_0 = peliculas_base_datos[0]["video"]
video_1 = peliculas_base_datos[1]["video"]
video_2 = peliculas_base_datos[2]["video"]


######################################
# Estructura del Website
###################################### 
# Header
with st.container():
    st.title(':blue[_Canchita reviews_] 🍿')

    feature1,feature2,feature3 = st.columns((1, 1, 1))
    with feature1:
        st_lottie(resenhas, height=300, key="fe1")
        st.write(
            """
            Unlock the reel magic and dive into a world of captivating cinema 🎬 with our 
            comprehensive movie reviews 🖍, where every frame comes alive!
            """
        )
    with feature2:
        st_lottie(premios, height=300, key="fe2")
        st.write(
            """
            Witness the glitz and glamour ✨ of the awards season 🏆 right from your screen,
            as we bring you exclusive access to watch the most prestigious ceremonies and 
            celebrate the finest in cinema!
            """
        )
    with feature3:
        st_lottie(trailers, height=300, key="fe3")
        st.write(
            """
            Get a sneak peek into the world of cinema with our collection of captivating movie trailers 🎬,
            igniting your excitement for the big screen experience! 💥
            """
        )
    st.markdown("""<hr style="height:5px;border:none;color:#1CA7E2;background-color:#1CA7E2;" /> """, unsafe_allow_html=True)    

# About US
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Live the experience _Canchita Reviews_")
        st.write("##")
        st.write(
            """
            Welcome to our movie haven, where cinematic wonders come alive! 
            Immerse yourself in a world of film exploration, where you'll find comprehensive reviews,
            captivating trailers, and exclusive access to prestigious awards ceremonies. From timeless
            classics to the latest blockbusters, our website is your gateway to unlocking the magic 
            of cinema. Discover hidden gems, engage in lively discussions, and fuel your passion for the 
            silver screen. Join our community of movie enthusiasts and embark on a thrilling journey through 
            the captivating realm of film. Don't just watch movies – experience them with us!
            """
        )
    with right_column:
        st.image(Fondo)


# ---- Primera película ----
with st.container():
    st.header(title0)
    #Rating de la pelicula
    rating, value ,icon = st.columns((8,1,1)) 
    with rating:
        st.subheader(':violet[Rating]')
    with value:
        st.subheader(average0)
    with icon:
        render_svg(star)
        
    #Trailer + poster
    image_column, video_column = st.columns((1, 2)) #Radio de 1 a 2
    with image_column:
        st.image(img_fondo0)
    with video_column:
        st.video(video_0)
    #Review
    st.subheader(":violet[Review]")
    st.write(overview0)
    st.markdown("""<hr style="height:5px;border:none;color:#1CA7E2;background-color:#1CA7E2;" /> """, unsafe_allow_html=True)  

# ---- Segunda película ----
with st.container():
    st.header(title1)
    #Rating de la pelicula
    rating, value ,icon = st.columns((8,1,1)) 
    with rating:
        st.subheader(':violet[Rating]')
    with value:
        st.subheader(average1)
    with icon:
        render_svg(star)
        
    #Trailer + poster
    image_column, video_column = st.columns((1, 2)) #Radio de 1 a 2
    with image_column:
        st.image(img_fondo1)
    with video_column:
        st.video(video_1)
    #Review
    st.subheader(":violet[Review]")
    st.write(overview1)
    st.markdown("""<hr style="height:5px;border:none;color:#1CA7E2;background-color:#1CA7E2;" /> """, unsafe_allow_html=True)  

# ---- Tercera película ----
with st.container():
    st.header(title2)
    #Rating de la pelicula
    rating, value ,icon = st.columns((8,1,1)) 
    with rating:
        st.subheader(':violet[Rating]')
    with value:
        st.subheader(average2)
    with icon:
        render_svg(star)
        
    #Trailer + poster
    image_column, video_column = st.columns((1, 2)) #Radio de 1 a 2
    with image_column:
        st.image(img_fondo2)
    with video_column:
        st.video(video_2)
    #Review
    st.subheader(":violet[Review]")
    st.write(overview2)
    st.markdown("""<hr style="height:5px;border:none;color:#1CA7E2;background-color:#1CA7E2;" /> """, unsafe_allow_html=True)     


# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Us!")
    st.text("Tell us any recommendation to improve our service for you")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/gonzales.omar@pucp.edu.pe" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your recommendation here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()