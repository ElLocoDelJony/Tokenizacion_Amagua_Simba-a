import tkinter as tk
from tkinter import scrolledtext
import spacy
from nltk.stem import SnowballStemmer
import nltk


import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')


# Descargar recursos necesarios
nltk.download('punkt')

# Cargar modelo de spaCy en español
nlp = spacy.load("es_core_news_sm")
stemmer = SnowballStemmer("spanish")

# Funciones de procesamiento
def tokenizar():
    texto = entrada.get("1.0", tk.END)
    doc = nlp(texto)
    tokens = [token.text for token in doc]
    salida.delete("1.0", tk.END)
    salida.insert(tk.END, "Tokens:\n" + str(tokens))

def normalizar():
    texto = entrada.get("1.0", tk.END)
    texto_norm = texto.lower().strip()
    salida.delete("1.0", tk.END)
    salida.insert(tk.END, "Texto normalizado:\n" + texto_norm)

def lematizar():
    texto = entrada.get("1.0", tk.END)
    doc = nlp(texto)
    lemas = [token.lemma_ for token in doc]
    salida.delete("1.0", tk.END)
    salida.insert(tk.END, "Lemas:\n" + str(lemas))

def stemming():
    texto = entrada.get("1.0", tk.END)
    palabras = nltk.word_tokenize(texto)
    stems = [stemmer.stem(palabra) for palabra in palabras]
    salida.delete("1.0", tk.END)
    salida.insert(tk.END, "Stems:\n" + str(stems))

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Aplicación Básica PLN")
ventana.geometry("500x400")
ventana.configure(bg="#cce7f0")

# Etiqueta y campo de texto
tk.Label(ventana, text="Ingresar Texto", bg="#cce7f0", font=("Arial", 12, "bold")).pack()
entrada = scrolledtext.ScrolledText(ventana, width=50, height=5)
entrada.pack(pady=5)

# Botones
tk.Button(ventana, text="Tokenizar", bg="lightgreen", command=tokenizar).pack(pady=3)
tk.Button(ventana, text="Normalización", bg="pink", command=normalizar).pack(pady=3)
tk.Button(ventana, text="Lematización", bg="lightgray", command=lematizar).pack(pady=3)
tk.Button(ventana, text="Stemming", bg="yellow", command=stemming).pack(pady=3)

# Área de salida
tk.Label(ventana, text="Salida", bg="#cce7f0", font=("Arial", 12, "bold")).pack()
salida = scrolledtext.ScrolledText(ventana, width=50, height=8)
salida.pack(pady=5)

ventana.mainloop()
