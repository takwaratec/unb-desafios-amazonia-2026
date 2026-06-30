# AGENTS.md — unb-desafios-amazonia-2026

> Repositório da proposta UnB + Tecnologia Takwara para o Edital Desafios da Amazônia
> (Amazônia+10 / CONFAP / BNDES / Fundo Amazônia)
> Mantido pelo Hermes Agent

## Identidade
Repositório de trabalho para estruturar a proposta de pesquisa e inovação da Rede UnB + Tecnologia Takwara, voltada a solucionar desafios concretos de cadeias produtivas da sociobioeconomia amazônica (Açaí, Castanha, Cacau, Babaçu, Pesca).

## Objetivo do Agente
1. Baixar e processar o edital, regulamento e anexos
2. Analisar enquadramento — o que pode ser pleiteado com as tecnologias existentes
3. Redigir a pré-proposta (Fase 1) e proposta final (Fase 2)
4. Manter documentação organizada para compartilhamento com parceiros
5. Criar fichas científicas no Acervo para materiais não fichados do MQTF

## Estrutura
```
├── AGENTS.md
├── README.md
├── .gitignore
├── .agents/scripts/       ← Scripts portados do MQTF
├── TRIAGEM-BRUTA/
│   ├── 01_REUNIOES/       # Áudios, transcrições, atas
│   ├── 02_DOCUMENTOS/     # PDFs, DOCX dos parceiros
│   ├── 03_REGULAMENTOS/   # Edital + anexos baixados
│   └── 04_REFERENCIAS/    # Artigos de apoio
└── docs/
    ├── index.md           # Home / Raio-X de enquadramento
    ├── edital/            # Ficha do edital
    ├── proposta/          # Rascunho da proposta
    ├── rede/              # Membros da Rede
    └── anexos-obrigatorios/
```

## Repositórios Irmãos
- **MQTF (Mulheres Que Tecem a Floresta):** https://github.com/takwaratec/Mulheres-Tecem-Amazonia
- **Acervo Científico:** https://takwaratec.github.io/Analises-e-escrita-cientifica/

> ⛔ **NÃO misturar com:** ECOSALA, Mentoria, Vaga Lúmen, MSTJS — são ecossistemas separados.

## Convenções

### ❌ Regras absolutas
- **NUNCA** inflar TRL em propostas
- **NUNCA** fabricar citações de figuras públicas
- **NUNCA** citar documentos internos (LAB_, ENG_, RES_, SCI_, TAK_) como evidência
- **NUNCA** usar "biosoberano" ou termos metafóricos internos em textos públicos
- **NUNCA** criar fichas científicas sem autor, DOI/ISBN/ISSN identificados
- **NUNCA** publicar documentos incompletos

### ✅ Regras de conduta
- **Única fonte de referências:** Acervo Científico (Analises-e-escrita-cientifica)
- **Proposta impessoal** — sem marcas pessoais, linguagem técnica institucional
- **Toda ficha** segue método Cavichioli (2025): 8 seções obrigatórias
- **Atribuição correta** — cada autor com seu crédito
- **TRL honesto** — tecnologia descrita pelo que faz, não por codificação interna
- **Protocolo de governança** — trabalhos de campo só após observância das diretrizes do protocolo CANCU (Salvaguardas de Cancún, REDD+), disponível na [documentação de governança](https://github.com/takwaratec/Mulheres-Tecem-Amazonia/blob/main/docs/01_GOVERNANCA/GOV_PROTOCOLO_SEGURANCA_CANCUN.md)

### Fluxo de trabalho
1. `git pull` — sincronizar com remoto
2. Fazer alterações (processar TRIAGEM, redigir proposta)
3. `git add <arquivos> && git commit -m "tipo: descrição" && git push`

## Scripts disponíveis

Em `.agents/scripts/`:
- `triagem_inteligente.py` — Processa materiais da TRIAGEM, extrai informações estruturadas
- `revisor_bndes_expansor.py` — Expande e revisa rascunhos de proposta conforme formulário BNDES
- `extract_reviews.py` — Extrai resenhas de documentos técnicos
- `lapidar_lote.py` — Revisão em lote de documentos .md
- `arquivista_recursivo_wtf.py` — Catalogação recursiva de diretórios

## Fichas Científicas

Quando identificar material do MQTF ainda não fichado no Acervo Científico:
1. Extrair texto do PDF original com PyMuPDF
2. Criar ficha seguindo método Cavichioli (8 seções)
3. Salvar em `Analises-e-escrita-cientifica/docs/analises/tecnologia-takwara/`
4. Referenciar na proposta como "Acervo Científico — Ficha Técnica [autor/ano]"
