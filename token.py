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
        # Conversión a minúsculas
        texto_norm = texto.lower()

        # Reemplazo de acentos
        reemplazos = {"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", "ü": "u"}
        for origen, destino in reemplazos.items():
            texto_norm = texto_norm.replace(origen, destino)

        # Quitar signos de puntuación comunes
        for signo in [".", ",", "!", "¡", "?", "¿", "(", ")", ";", ":"]:
            texto_norm = texto_norm.replace(signo, "")

        # Diccionario de abreviaciones (ejemplo con ~100 entradas)
        abreviaciones = {
            "epn": "escuela politécnica nacional",
            "unesco": "organización de las naciones unidas para la educación la ciencia y la cultura",
            "onu": "organización de las naciones unidas",
            "oms": "organización mundial de la salud",
            "oea": "organización de estados americanos",
            "ue": "unión europea",
            "eeuu": "estados unidos",
            "nasa": "national aeronautics and space administration",
            "fbi": "federal bureau of investigation",
            "cia": "central intelligence agency",
            "mit": "massachusetts institute of technology",
            "ai": "inteligencia artificial",
            "ml": "machine learning",
            "nlp": "procesamiento de lenguaje natural",
            "sql": "structured query language",
            "html": "hypertext markup language",
            "css": "cascading style sheets",
            "js": "javascript",
            "api": "application programming interface",
            "http": "hypertext transfer protocol",
            "ip": "internet protocol",
            "url": "uniform resource locator",
            "www": "world wide web",
            "pdf": "portable document format",
            "cpu": "unidad central de procesamiento",
            "gpu": "unidad de procesamiento gráfico",
            "ram": "memoria de acceso aleatorio",
            "rom": "memoria de solo lectura",
            "usb": "universal serial bus",
            "lan": "local area network",
            "wan": "wide area network",
            "vpn": "virtual private network",
            "iot": "internet de las cosas",
            "vr": "realidad virtual",
            "ar": "realidad aumentada",
            "mr": "realidad mixta",
            "ux": "experiencia de usuario",
            "ui": "interfaz de usuario",
            "qa": "quality assurance",
            "pm": "project manager",
            "ceo": "chief executive officer",
            "cfo": "chief financial officer",
            "cto": "chief technology officer",
            "hr": "recursos humanos",
            "kpi": "key performance indicator",
            "roi": "return on investment",
            "b2b": "business to business",
            "b2c": "business to consumer",
            "p2p": "peer to peer",
            "saas": "software as a service",
            "paas": "platform as a service",
            "iaas": "infrastructure as a service",
            "erp": "enterprise resource planning",
            "crm": "customer relationship management",
            "bi": "business intelligence",
            "etl": "extract transform load",
            "csv": "comma separated values",
            "json": "javascript object notation",
            "xml": "extensible markup language",
            "dl": "deep learning",
            "cv": "computer vision",
            "ocr": "optical character recognition",
            "rpa": "robotic process automation",
            "dns": "domain name system",
            "smtp": "simple mail transfer protocol",
            "ftp": "file transfer protocol",
            "ssh": "secure shell",
            "ssl": "secure sockets layer",
            "tls": "transport layer security",
            "mba": "master of business administration",
            "phd": "doctor of philosophy",
            "bsc": "bachelor of science",
            "msc": "master of science",
            "ba": "bachelor of arts",
            "ma": "master of arts",
            "llm": "master of laws",
            "jd": "juris doctor",
            "md": "doctor of medicine",
            "rn": "registered nurse",
            "ngo": "organización no gubernamental",
            "gdp": "producto interno bruto",
            "gnp": "producto nacional bruto",
            "unicef": "fondo de las naciones unidas para la infancia",
            "wto": "world trade organization",
            "imf": "international monetary fund",
            "wb": "world bank",
            "oecd": "organisation for economic co operation and development",
            "opec": "organization of the petroleum exporting countries",
            "cop": "conference of the parties",
            "ipcc": "intergovernmental panel on climate change",
            "sdg": "sustainable development goals",
            "csr": "corporate social responsibility"
        }

        # Expandir abreviaciones
        palabras = texto_norm.split()
        palabras_expandidas = [abreviaciones.get(p, p) for p in palabras]
        texto_final = " ".join(palabras_expandidas)

        mostrar_resultado("NORMALIZACIÓN", texto_final)


def aplicar_lematizacion():
    texto = obtener_texto()
    if texto:
        diccionario_lemas = {
            # Sustantivos básicos
            "niños": "niño", "niñas": "niño", "perros": "perro", "gatos": "gato",
            "parques": "parque",

            # Verbos comunes (formas conjugadas → infinitivo)
            "estaban": "estar","ladrando":"ladrar","ladro":"ladrar","estaba":"estar", "estoy": "estar", "estás": "estar", "está": "estar", "están": "estar",
            "era": "ser", "eres": "ser", "soy": "ser", "somos": "ser", "son": "ser", "fue": "ser",
            "iba": "ir", "vas": "ir", "voy": "ir", "vamos": "ir", "van": "ir", "fui": "ir",
            "tenía": "tener", "tengo": "tener", "tienes": "tener", "tiene": "tener", "tenemos": "tener", "tienen": "tener",
            "hacía": "hacer", "hago":("hacer"), 'haces':("hacer"), 'hace':("hacer"), 'hacemos':("hacer"), 'hacen':("hacer"),
            'decía':("decir"), 'digo':("decir"), 'dices':("decir"), 'dice':("decir"), 'decimos':("decir"), 'dicen':("decir"),
            "podía": "poder", "puedo": "poder", "puedes": "poder", "puede": "poder", "podemos": "poder", "pueden": "poder",
            "quería": "querer", "quiero": "querer", "quieres": "querer", "quiere": "querer", "queremos": "querer", "quieren": "querer",
            "sabía": "saber", "sé": "saber", "sabes": "saber", "sabe": "saber", "sabemos": "saber", "saben": "saber",
            "daba": "dar", "doy": "dar", "das": "dar", "da": "dar", "damos": "dar", "dan": "dar",
            "veía": "ver", "veo": "ver", "ves": "ver", "ve": "ver", "vemos": "ver", "ven": "ver",
            "comía": "comer", "como": "comer", "comes": "comer", "come": "comer", "comemos": "comer", "comen": "comer",
            "vivía": "vivir", "vivo": "vivir", "vives": "vivir", "vive": "vivir", "vivimos": "vivir", "viven": "vivir",
            "trabajaba": "trabajar", "trabajo": "trabajar", "trabajas": "trabajar", "trabaja": "trabajar", "trabajamos": "trabajar", "trabajan": "trabajar",
            "estudiaba": "estudiar", "estudio": "estudiar", "estudias": "estudiar", "estudia": "estudiar", "estudiamos": "estudiar", "estudian": "estudiar",
            "jugando": "jugar", "juego": "jugar", "juegas": "jugar", "juega": "jugar", "jugamos": "jugar", "juegan": "jugar",
            "disfrutaban": "disfrutar", "disfruto": "disfrutar", "disfrutas": "disfrutar", "disfruta": "disfrutar", "disfrutamos": "disfrutar", "disfrutan": "disfrutar",
            "corriendo": "correr", "corro": "correr", "corres": "correr", "corre": "correr", "corremos": "correr", "corren": "correr",
            "escribía": "escribir", "escribo": "escribir", "escribes": "escribir", "escribe": "escribir", "escribimos": "escribir", "escriben": "escribir",
            "leía": "leer", "leo": "leer", "lees": "leer", "lee": "leer", "leemos": "leer", "leen": "leer",
            "hablaba": "hablar", "hablo": "hablar", "hablas": "hablar", "habla": "hablar", "hablamos": "hablar", "hablan": "hablar",
            "pensaba": "pensar", "pienso": "pensar", "piensas": "pensar", "piensa": "pensar", "pensamos": "pensar", "piensan": "pensar",
            "sentía": "sentir", "siento": "sentir", "sientes": "sentir", "siente": "sentir", "sentimos": "sentir", "sienten": "sentir",
            "dormía": "dormir", "duermo": "dormir", "duermes": "dormir", "duerme": "dormir", "dormimos": "dormir", "duermen": "dormir",
            "abría": "abrir", "abro": "abrir", "abres": "abrir", "abre": "abrir", "abrimos": "abrir", "abren": "abrir",
            "cerraba": "cerrar", "cierro": "cerrar", "cierras": "cerrar", "cierra": "cerrar", "cerramos": "cerrar", "cierran": "cerrar"
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
            elif p.endswith("o") and len(p) > 4:
                p = p[:-1]
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
