# --- EXPLICAÇÃO DIDÁTICA PARA FABIO ---
# O QUE FAZ: Este é o seu "Lapidador de Texto". Ele pega rascunhos ou transcrições brutas (.txt)
# e as transforma em Fichas Técnicas Profissionais com metadados e tabelas.
# 
# POR QUE É NECESSÁRIO: É essencial para manter a padronização e a sobriedade científica.
#
# COMO EXPLORAR NO DIA-A-DIA: Use para processar as suas anotações de campo.

import os
import time
from google import genai

client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))
MODEL_ID = "models/gemini-2.5-flash"

PASTA_BRUTA = "04_PESQUISA_ANDAMENTO/ACERVO_DIGITAL_WTF/01_RAW_TRANSCRIPTS"
PASTA_DESTINO = "docs/04_PESQUISA_ANDAMENTO/Fichas-Tecnicas"

def processar_arquivo(conteudo, nome):
    prompt = f"Converta este texto bruto em uma FICHA CIENTÍFICA MQTF:\n\n{conteudo}"
    try:
        response = client.models.generate_content(model=MODEL_ID, contents=prompt)
        return response.text
    except Exception as e: return str(e)

if __name__ == "__main__":
    os.makedirs(PASTA_DESTINO, exist_ok=True)
    for f in os.listdir(PASTA_BRUTA):
        if f.endswith(".txt"):
            with open(os.path.join(PASTA_BRUTA, f), 'r') as file:
                res = processar_arquivo(file.read(), f)
            with open(os.path.join(PASTA_DESTINO, f"FICHA_{f.replace('.txt', '.md')}"), 'w') as out:
                out.write(res)
            print(f"✅ Lapidado: {f}")
            time.sleep(1)
