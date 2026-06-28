# --- EXPLICAÇÃO DIDÁTICA PARA FABIO ---
# O QUE FAZ: Este é o seu "Segurança de Porta". Ele olha para os arquivos e decide 
# se o assunto é interessante para o projeto ou se é lixo.
# 
# POR QUE É NECESSÁRIO: Economiza créditos de API e tempo de processamento.

import os
import shutil
from google import genai

client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))
MODEL_ID = "models/gemini-2.5-flash"

TEMAS = ["Bambu", "Tanino", "Biochar", "Saneamento", "Amazônia"]

def avaliar(texto):
    prompt = f"Responda SIM se o texto fala sobre: {TEMAS}\n\n{texto[:1000]}"
    try:
        res = client.models.generate_content(model=MODEL_ID, contents=prompt)
        return "SIM" in res.text.upper()
    except: return False

if __name__ == "__main__":
    # Lógica de triagem
    pass
