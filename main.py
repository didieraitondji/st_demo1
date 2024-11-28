# main.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Nom et prénom du créateur
st.title(":blue[TP sur la base de données IRIS !]")

# Titre de l'application
st.title("TP sur la base de données IRIS !")

selected_option = st.radio("Sélectionnez La méthode que vous préférez :", 
["Auto", "Téléverser manuellement IRIS"])

if selected_option == "Auto":
    # Affichage des premières lignes du dataframe
    df = pd.read_csv("IRIS.csv")
    st.subheader("Affichage des premières lignes du dataframe")
    st.write(df.head())
    
    # Statistiques descriptives
    st.subheader("Statistiques descriptives")
    st.write(df.describe())
    
    # Choix d'une colonne pour l'analyse
    st.subheader("Affichage de l'histogramme d'une colonnes :")
    selected_column = st.selectbox("Sélectionnez une colonne à afficher", df.columns)
    
    # Affichage de l'histogramme de la colonne sélectionnée
    st.subheader(f"Histogramme de {selected_column}")
    fig, ax = plt.subplots()
    sns.histplot(df[selected_column], kde=True, ax=ax)
    st.pyplot(fig)
    
    # Graphique en nuage de points pour comparer deux colonnes
    st.subheader("Graphique en nuage de points pour comparer deux colonnes")
    col1 = st.selectbox("Sélectionnez la colonne X", df.columns, index=0)
    col2 = st.selectbox("Sélectionnez la colonne Y", df.columns, index=1)
    
    fig, ax = plt.subplots()
    sns.scatterplot(x=df[col1], y=df[col2], hue=df["setosa"], ax=ax)
    st.pyplot(fig)
    
else:
    file = st.file_uploader("Importer vos données ici", type=["csv"])
    if file is not None:
        
        # Affichage des premières lignes du dataframe
        df = pd.read_csv(file)
        st.subheader("Affichage des premières lignes du dataframe")
        st.write(df.head())
        
        # Statistiques descriptives
        st.subheader("Statistiques descriptives")
        st.write(df.describe())
        
        # Choix d'une colonne pour l'analyse
        st.subheader("Affichage de l'histogramme d'une colonnes :")
        selected_column = st.selectbox("Sélectionnez une colonne à afficher", df.columns)
        
        # Affichage de l'histogramme de la colonne sélectionnée
        st.subheader(f"Histogramme de {selected_column}")
        fig, ax = plt.subplots()
        sns.histplot(df[selected_column], kde=True, ax=ax)
        st.pyplot(fig)
        
        # Graphique en nuage de points pour comparer deux colonnes
        st.subheader("Graphique en nuage de points pour comparer deux colonnes")
        col1 = st.selectbox("Sélectionnez la colonne X", df.columns, index=0)
        col2 = st.selectbox("Sélectionnez la colonne Y", df.columns, index=1)
        
        fig, ax = plt.subplots()
        sns.scatterplot(x=df[col1], y=df[col2], hue=df["setosa"], ax=ax)
        st.pyplot(fig)
