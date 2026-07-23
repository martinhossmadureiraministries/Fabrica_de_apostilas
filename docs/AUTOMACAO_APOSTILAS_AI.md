# Automação de geração de apostilas EBE com Gemini + Groq

Esta automação prepara a produção em massa das **1.029 apostilas** do mapa oficial da Escola Bíblica Epignósis, preservando a hierarquia curricular e a identidade institucional.

## O que já está definido

- Fonte curricular: `EBE_Mapa_Completo_Apostilas-2.pdf`.
- Total esperado: **1.029 apostilas**.
- Hierarquia extraída automaticamente:
  - Nível formativo;
  - Instituto;
  - Escola;
  - Curso;
  - Módulo;
  - Apostila.
- Saída estruturada por pastas:

```text
generated/apostilas/
  nivel-1-discipulo-conhecer/
    instituto-de-formacao-crista/
      escola-de-fundamentos-da-fe/
        salvacao-e-novo-nascimento/
          modulo-1-fundamentos-da-salvacao/
            EBE-APO-0001_o-estado-de-perdicao-do-ser-humano.docx
```

## Divisão de trabalho entre Gemini e Groq

Modo recomendado: `gemini_groq`.

1. **Groq — planeamento rápido**
   - Define a ideia única da apostila.
   - Lista textos bíblicos, termos-chave e riscos de repetição.
   - Ajuda a impedir que todas as apostilas fiquem genéricas.

2. **Gemini — redacção principal**
   - Redige a apostila completa em JSON estruturado.
   - Mantém o conteúdo coerente com título, matéria, módulo e curso.
   - Produz apresentação, objectivos, desenvolvimento, exercícios, glossário e bibliografia.

3. **Groq — revisão rápida**
   - Verifica coerência título-conteúdo.
   - Aponta problemas de repetição, superficialidade ou desalinhamento.
   - Emite parecer pedagógico/doutrinário.

4. **Validação local — sem API**
   - Confere tamanho mínimo.
   - Verifica termos do título presentes no conteúdo.
   - Detecta parágrafos repetidos.
   - Calcula similaridade aproximada entre apostilas do mesmo lote.

## Secrets necessários

No GitHub, configure em:

`Settings → Secrets and variables → Actions → New repository secret`

Crie:

- `GEMINI_API_KEY`
- `GROQ_API_KEY`

Opcionalmente, em `Variables`, pode definir:

- `GEMINI_MODEL`
- `GROQ_MODEL`

> Nunca coloque chaves de API no código, no chat, em commits ou em ficheiros `.env` versionados.

## Sobre o `GITHUB_TOKEN`

O `GITHUB_TOKEN` é criado automaticamente pelo GitHub Actions. Não é necessário criar um token manual para executar o workflow.

O workflow `Gerar apostilas EBE com IA` usa:

```yaml
permissions:
  contents: write
```

Isso permite, se a opção `publicar_manifesto` for activada, comitar apenas o manifesto e o índice de qualidade. Por padrão, os ficheiros `.docx` gerados ficam como **artefactos da execução**, não como commits no repositório.


## Instalação manual dos workflows

Como a GitHub App do Arena pode não ter a permissão `workflows: write`, os workflows foram guardados numa pasta alternativa:

```text
workflows-para-instalar/
  gerar-apostilas-ai.yml
  validar-automacao-apostilas.yml
```

Para activar no GitHub Actions, copie manualmente estes dois ficheiros para:

```text
.github/workflows/
```

Depois faça commit directamente no GitHub ou a partir de um ambiente com permissão para editar workflows.

## Como executar manualmente

Abra no GitHub:

`Actions → Gerar apostilas EBE com IA → Run workflow`

Campos principais:

- `modo`: `gemini_groq`, `gemini`, `groq` ou `offline`.
- `inicio`: número inicial da apostila no mapa, de 1 a 1029.
- `limite`: quantidade do lote.
- `instituto`, `escola`, `curso`, `modulo`: filtros opcionais.
- `dry_run`: apenas lista o lote, sem gerar.
- `offline_if_missing`: usa modo técnico offline caso os secrets não existam.

Exemplos:

### Gerar as 3 primeiras apostilas

```text
modo: gemini_groq
inicio: 1
limite: 3
```

### Gerar 5 apostilas de um curso específico

```text
modo: gemini_groq
curso: Salvação e Novo Nascimento
inicio: 1
limite: 5
```

### Testar sem API

```text
modo: offline
inicio: 1
limite: 1
```

## Limites e recomendação prática

As camadas gratuitas de Gemini, Groq e GitHub Actions têm limites. Portanto, a produção das 1.029 apostilas deve ser feita por lotes.

Recomendação inicial:

- Teste técnico: `offline`, limite `1`.
- Teste com IA: `gemini_groq`, limite `1`.
- Produção moderada: lotes de `3` a `10` apostilas.
- Produção grande: usar `self-hosted runner` e controlar pausas/rate limit.

## Ficheiros principais

- `scripts/importar_mapa_apostilas.py` — extrai o mapa PDF para JSONL com 1.029 apostilas.
- `scripts/gerar_apostilas_ai.py` — gera DOCX com identidade visual EBE.
- `config/gerador_apostilas.yml` — parâmetros de identidade, IA, qualidade e saída.
- `workflows-para-instalar/gerar-apostilas-ai.yml` — workflow manual de geração; mover manualmente para `.github/workflows/` quando houver permissão.
- `workflows-para-instalar/validar-automacao-apostilas.yml` — validação técnica sem IA; mover manualmente para `.github/workflows/` quando houver permissão.

## Política de armazenamento

A pasta `generated/` está no `.gitignore` porque a geração das 1.029 apostilas pode criar muitos ficheiros pesados. Os resultados devem ser baixados como artefactos do GitHub Actions ou guardados em armazenamento externo.
