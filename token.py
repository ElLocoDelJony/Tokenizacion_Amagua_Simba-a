import tkinter as tk
from tkinter import messagebox

# --- FUNCIONES DE PROCESAMIENTO PLN ---

def obtener_texto():
    texto = entrada_texto.get().strip()
    if not texto:
        messagebox.showwarning("Entrada vacía", "Por favor, ingresa un texto primero.")
        return None
    return texto

def aplicar_tokenizar():
    texto = obtener_texto()
    if texto:
        # Tokenización básica separando por espacios
        for signo in [".", ",", "!", "¡", "?", "¿"]:
            texto = texto.replace(signo, f" {signo} ")
        tokens = [t for t in texto.split() if t]
        mostrar_resultado("TOKENIZACIÓN", tokens)

def aplicar_normalizacion():
    texto = obtener_texto()
    if texto:
        texto_norm = texto.lower()
        reemplazos = {"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", "ü": "u"}
        for origen, destino in reemplazos.items():
            texto_norm = texto_norm.replace(origen, destino)
        for signo in [".", ",", "!", "¡", "?", "¿", "(", ")"]:
            texto_norm = texto_norm.replace(signo, "")
        mostrar_resultado("NORMALIZACIÓN", texto_norm)

def aplicar_lematizacion():
    texto = obtener_texto()
    if texto:
        diccionario_lemas = {
            "niños": "niño", "niñas": "niño", "perros": "perro", "gatos": "gato",
            "estaban": "estar", "jugando": "jugar", "parques": "parque",
            "disfrutaban": "disfrutar", "corriendo": "correr", "corre": "correr"
        }
        palabras = texto.lower().replace(".", "").replace(",", "").split()
        lemas = [diccionario_lemas.get(p, p) for p in palabras]
        mostrar_resultado("LEMATIZACIÓN (Lemas reales)", lemas)

def aplicar_stemming():
    texto = obtener_texto()
    if texto:
        palabras = texto.lower().replace(".", "").replace(",", "").split()
        stems = []
        for p in palabras:
            if p.endswith("ando") or p.endswith("endo"):
                p = p[:-4]
            elif p.endswith("aban"):
                p = p[:-4]
            elif p.endswith("os") and len(p) > 4:
                p = p[:-2]
            elif p.endswith("es") and len(p) > 4:
                p = p[:-2]
            elif p.endswith("an") and len(p) > 4:
                p = p[:-2]
            stems.append(p)
        mostrar_resultado("STEMMING (Raíces truncadas)", stems)

def mostrar_resultado(etapa, datos):
    caja_salida.delete("1.0", tk.END)
    caja_salida.insert(tk.END, f"--- {etapa} ---\n\n")
    if isinstance(datos, list):
        caja_salida.insert(tk.END, str(datos))
    else:
        caja_salida.insert(tk.END, datos)

# --- INTERFAZ ---

ventana = tk.Tk()
ventana.title("Aplicación Básica PLN")
ventana.geometry("550x380")
ventana.configure(bg="#D4E6F1")

lbl_entrada = tk.Label(ventana, text="Ingresar Texto", font=("Arial", 11, "bold"), bg="#D4E6F1")
lbl_entrada.pack(anchor="w", padx=20, pady=(15, 2))

entrada_texto = tk.Entry(ventana, font=("Arial", 11), width=55)
entrada_texto.pack(padx=20, pady=5)
entrada_texto.insert(0, "Los niños estaban jugando en los parques.")

contenedor = tk.Frame(ventana, bg="#D4E6F1")
contenedor.pack(fill="both", expand=True, padx=20, pady=15)

marco_botones = tk.Frame(contenedor, bg="#D4E6F1")
marco_botones.pack(side="left", fill="y", padx=(0, 20))

btn_tokenizar = tk.Button(marco_botones, text="Tokenizar", bg="#7DCEA0", width=15, font=("Arial", 10, "bold"), command=aplicar_tokenizar)
btn_tokenizar.pack(pady=5)

btn_normalizar = tk.Button(marco_botones, text="Normalización", bg="#F5B7B1", width=15, font=("Arial", 10, "bold"), command=aplicar_normalizacion)
btn_normalizar.pack(pady=5)

btn_lematizar = tk.Button(marco_botones, text="Lematización", bg="#AED6F1", width=15, font=("Arial", 10, "bold"), command=aplicar_lematizacion)
btn_lematizar.pack(pady=5)

btn_stemming = tk.Button(marco_botones, text="Stemming", bg="#F9E79F", width=15, font=("Arial", 10, "bold"), command=aplicar_stemming)
btn_stemming.pack(pady=5)

marco_salida = tk.Frame(contenedor, bg="#D4E6F1")
marco_salida.pack(side="right", fill="both", expand=True)

lbl_salida = tk.Label(marco_salida, text="Salida", font=("Arial", 11, "bold"), bg="#D4E6F1")
lbl_salida.pack(anchor="w")

caja_salida = tk.Text(marco_salida, font=("Arial", 10), width=30, height=10, bg="white", wrap="word")
caja_salida.pack(fill="both", expand=True, pady=5)

ventana.mainloop()
