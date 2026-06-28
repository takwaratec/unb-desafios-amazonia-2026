import os
import time
from google import genai

client = genai.Client(api_key="AIzaSyDnUer8X3QiY0dJtK26xL9z8hGxbtm3R8A")
MODEL_ID = "models/gemini-2.0-flash"

def ler_arquivo(caminho):
    if os.path.exists(caminho):
        try:
            with open(caminho, 'r', encoding='utf-8') as f:
                return f.read()[:7000]
        except: return ""
    return ""

def executar_revisao():
    print("🚀 Iniciando Expansão de Texto (Respeitando Limites BNDES)...")
    
    # 1. Suas fontes reduzidas (Corrigido para usar ler_arquivo)
    f1 = ler_arquivo("docs/01_GOVERNANCA/WTF_PROJETO_INTEGRADO.md")
    f2 = ler_arquivo("docs/02_DIAGNOSTICO DE AREA/02_ESTUDOS_E_PESQUISAS/RES_pesquisa-bambu-indigenas-georreferenciamento.md")
    f3 = ler_arquivo("docs/02_DIAGNOSTICO DE AREA/WTF-DIAG-002_PARADIGMAS_BIOECONOMIA_AMAZONICA.md")
    autos = f1 + f2 + f3

    # 2. Carrega o rascunho da Tânia
    path_rascunho = "docs/00_MODELO 1 - BNDES/03_CONSOLIDADO_TANIA_DRAFT.md"
    with open(path_rascunho, "r", encoding="utf-8") as f:
        rascunho = f.read()

    # 3. Divide por seções (Título ##)
    secoes = rascunho.split("\n## ")
    revisado_final = ""

    for i, secao in enumerate(secoes):
        print(f"🧠 Redigindo Seção {i+1} de {len(secoes)}...")
        
        prompt = f"""
        Aja como redator sênior de projetos Fundo Amazônia/BNDES. 
        Sua tarefa é EXPANDIR o rascunho abaixo usando os dados dos AUTOS.

        REGRAS:
        1. Identifique o limite de caracteres nas tags vermelhas (ex: Máx 2000).
        2. Escreva um texto técnico denso que chegue próximo ao limite (ex: se o limite é 2000, escreva ~1800).
        3. Substitua marcas como "Sônia escrever aqui" por conteúdo real dos autos.
        4. MANTENHA as cores e formatação Markdown.
        5. Foco em: Bioeconomia, NBR 16828-1, Bambu e Mulheres.

        AUTOS: {autos}
        RASCUNHO DA SEÇÃO: {secao}
        """

        try:
            response = client.models.generate_content(model=MODEL_ID, contents=prompt)
            revisado_final += "\n## " + response.text if i > 0 else response.text
            time.sleep(12) # Pausa para evitar erro 429
        except Exception as e:
            print(f"⚠️ Erro na seção {i+1}: {e}")
            revisado_final += "\n## " + secao

    with open("03_CONSOLIDADO_BNDES_REVISADO_FINAL.md", "w", encoding="utf-8") as f:
        f.write(revisado_final)
    print("✅ Concluído! Verifique: 03_CONSOLIDADO_BNDES_REVISADO_FINAL.md")

if __name__ == "__main__":
    executar_revisao()
