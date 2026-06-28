# --- EXPLICAÇÃO DIDÁTICA PARA FABIO ---
# O QUE FAZ: Este é o seu "Zelador Inteligente". Ele percorre as pastas de transcrições brutas, 
# organiza os nomes dos arquivos e usa a IA para criar um primeiro "lapidado" (resenha) 
# de cada documento encontrado.
# 
# POR QUE É NECESSÁRIO: Com centenas de arquivos brutos, é impossível ler um por um manualmente. 
# O Arquivista faz a triagem pesada para que você possa focar apenas nos conteúdos aprovados.
#
# COMO EXPLORAR NO DIA-A-DIA: Sempre que chegar uma pasta nova com 50 PDFs, peça ao agente: 
# "Rode o arquivista_recursivo_wtf.py na pasta X".

import os
import time
from google import genai

# 1. Configuração da API
client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))
MODEL_ID = "models/gemini-2.5-flash"

# 2. Configurações de Diretório
PASTA_RAIZ_INPUT = "04_PESQUISA_ANDAMENTO/ACERVO_DIGITAL_WTF/01_RAW_TRANSCRIPTS"
PASTA_RAIZ_OUTPUT = "04_PESQUISA_ANDAMENTO/ACERVO_DIGITAL_WTF/02_TECHNICAL_REVIEWS"

def gerar_review_ia(conteudo_slug, nome_original):
    prompt = f"""
    Atue como Bibliotecário Sênior e Analista de Bioeconomia.
    Analise o fragmento do documento '{nome_original}':
    {conteudo_slug[:8000]}
    
    Gere uma FICHA DE CATALOGAÇÃO:
    1. Título Curto e Padronizado.
    2. Resumo Técnico (3 parágrafos).
    3. Três palavras-chave (Ex: Biochar, Tanino, Bambu).
    4. Citação sugerida (Formato MQTF).
    """
    try:
        response = client.models.generate_content(model=MODEL_ID, contents=prompt)
        return response.text
    except Exception as e:
        return f"Erro no processamento: {e}"

def processar_recursivamente():
    for root, dirs, files in os.walk(PASTA_RAIZ_INPUT):
        for file in files:
            if file.endswith(".txt") or file.endswith(".md"):
                caminho_completo = os.path.join(root, file)
                print(f"📄 Processando: {file}...")
                with open(caminho_completo, 'r', encoding='utf-8') as f:
                    conteudo = f.read()
                
                review = gerar_review_ia(conteudo, file)
                
                # Criar estrutura de saída espelhada
                rel_path = os.path.relpath(root, PASTA_RAIZ_INPUT)
                dest_dir = os.path.join(PASTA_RAIZ_OUTPUT, rel_path)
                os.makedirs(dest_dir, exist_ok=True)
                
                nome_saida = f"REVIEW_{file.replace('.txt', '.md')}"
                with open(os.path.join(dest_dir, nome_saida), 'w', encoding='utf-8') as f_out:
                    f_out.write(review)
                print(f"✅ Review salvo: {nome_saida}")
                time.sleep(1)

if __name__ == "__main__":
    processar_recursivamente()
