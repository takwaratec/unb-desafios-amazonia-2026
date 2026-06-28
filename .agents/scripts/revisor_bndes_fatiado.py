import os
import time
from google import genai

client = genai.Client(api_key="AIzaSyDnUer8X3QiY0dJtK26xL9z8hGxbtm3R8A")
MODEL_ID = "models/gemini-2.0-flash"

def ler_pasta(caminho):
    conteudo = ""
    if os.path.exists(caminho):
        for arq in os.listdir(caminho):
            if arq.endswith(".md"):
                try:
                    with open(os.path.join(caminho, arq), 'r', encoding='utf-8') as f:
                        conteudo += f.read()[:3000] # Leitura bem curta para economizar
                except: continue
    return conteudo

def executar_revisao():
    print("🚀 Iniciando Revisão Fatiada (Evitando Erro 429)...")
    
    caminho_rascunho = "docs/00_MODELO 1 - BNDES/03_CONSOLIDADO_TANIA_DRAFT.md"
    with open(caminho_rascunho, "r", encoding="utf-8") as f:
        rascunho = f.read()

    # Coleta de subsídios reduzida
    autos = ler_pasta("docs/01_GOVERNANCA/WTF_PROJETO_INTEGRADO.md") + ler_pasta("docs/03_DOSSIE_BNDES")

    # Dividir o rascunho em partes menores (ex: por títulos de seção ##)
    partes = rascunho.split("\n## ")
    revisado_total = ""

    for i, parte in enumerate(partes):
        print(f"🧠 Analisando bloco {i+1} de {len(partes)}...")
        
        prompt = f"""
        Aja como um Redator Sênior de Projetos para o BNDES/Fundo Amazônia.
        Sua tarefa é expandir o rascunho fornecido, utilizando os dados dos AUTOS para preencher as seções.

        ### REGRAS DE OURO:
        1. **Respeite os Limites:** Identifique no texto em vermelho o limite de caracteres (ex: "Máx 2000"). Escreva um texto denso e profissional que chegue o mais próximo possível desse limite, sem ultrapassá-lo.
        2. **Manutenção de Estilo:** Mantenha o texto e cores originais, mas substitua os marcadores de posição (ex: "Sônia escrever aqui...") por texto técnico real extraído dos autos.
        3. **Densidade Técnica:** Use os termos dos autos: "Bioeconomia Circular", "Tecnologia Social Livre", "NBR 16828-1", "PU Vegetal de Mamona".
        4. **Fluxo:** Avance com a narrativa de forma que ela seja contínua e persuasiva para um avaliador bancário.

        ### AUTOS DO PROJETO (Subsídios):
        {contexto_reduzido}

        ### SEÇÃO DO RASCUNHO PARA EXPANDIR:
        {secao}
        """

    with open("03_CONSOLIDADO_BNDES_REVISADO_V2.md", "w", encoding="utf-8") as f:
        f.write(revisado_total)
    print("✅ Concluído! Arquivo: 03_CONSOLIDADO_BNDES_REVISADO_V2.md")

if __name__ == "__main__":
    executar_revisao()
