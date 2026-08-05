#!/usr/bin/env python3
"""Organiza apostilas geradas em estrutura hierárquica no repositório.

Cria:
  apostilas/
    Nível 1 - Discípulo/
      Instituto 1 - Nome/
        Escola 1 - Nome/
          Curso 1 - Nome/
            Modulo 1 - Nome/
              001_apostila_titulo.docx
              ...
"""
import argparse
import json
import shutil
import sys
from pathlib import Path
from typing import Any


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    """Carrega JSONL com estrutura de apostilas."""
    with path.open("r", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def organizar_apostilas(
    manifesto: Path,
    gerados: Path,
    saida: Path = Path("apostilas"),
) -> None:
    """Organiza apostilas em estrutura hierárquica.
    
    Args:
        manifesto: Caminho para mapa_apostilas.jsonl
        gerados: Caminho para generated/ (onde estão os DOCX)
        saida: Diretório de saída (padrão: apostilas/)
    """
    if not manifesto.exists():
        print(f"❌ Manifesto não encontrado: {manifesto}")
        sys.exit(1)
    
    if not gerados.exists():
        print(f"❌ Diretório gerado não encontrado: {gerados}")
        sys.exit(1)
    
    apostilas = load_jsonl(manifesto)
    saida.mkdir(exist_ok=True, parents=True)
    
    copiadas = 0
    faltantes = 0
    
    for apostila in apostilas:
        nivel = apostila.get("nivel", "Desconhecido")
        instituto = apostila.get("instituto", "Desconhecido")
        escola = apostila.get("escola", "Desconhecido")
        curso = apostila.get("curso", "Desconhecido")
        modulo = apostila.get("modulo", "Desconhecido")
        num = apostila.get("numero", 0)
        titulo = apostila.get("titulo", "sem-titulo")
        
        # Construir caminho hierárquico
        caminho_saida = (
            saida
            / f"{nivel}"
            / f"{instituto}"
            / f"{escola}"
            / f"{curso}"
            / f"{modulo}"
        )
        caminho_saida.mkdir(exist_ok=True, parents=True)
        
        # Nome do arquivo DOCX: número_padronizado_titulo.docx
        nome_saida = f"{num:03d}_{titulo.replace('/', '_')}.docx"
        arquivo_saida = caminho_saida / nome_saida
        
        # Procurar arquivo DOCX nos gerados
        # Padrão esperado: generated/XXX_titulo.docx
        docx_candidates = list(gerados.glob(f"{num:03d}_*.docx")) or list(
            gerados.glob(f"{num}_*.docx")
        )
        
        if docx_candidates:
            arquivo_origem = docx_candidates[0]
            try:
                shutil.copy2(arquivo_origem, arquivo_saida)
                print(f"✅ {arquivo_saida}")
                copiadas += 1
            except Exception as e:
                print(f"⚠️  Erro ao copiar {arquivo_origem}: {e}")
                faltantes += 1
        else:
            print(f"⚠️  DOCX não encontrado para apostila {num}: {titulo}")
            faltantes += 1
    
    print(f"\n📊 Resumo:")
    print(f"  ✅ Copiadas: {copiadas}")
    print(f"  ⚠️  Faltantes: {faltantes}")
    print(f"  📁 Diretório de saída: {saida.resolve()}")


def main():
    parser = argparse.ArgumentParser(
        description="Organiza apostilas em estrutura hierárquica"
    )
    parser.add_argument(
        "--manifesto",
        type=Path,
        default=Path("generated/manifests/mapa_apostilas.jsonl"),
        help="Caminho para mapa_apostilas.jsonl",
    )
    parser.add_argument(
        "--gerados",
        type=Path,
        default=Path("generated"),
        help="Diretório com DOCX gerados",
    )
    parser.add_argument(
        "--saida",
        type=Path,
        default=Path("apostilas"),
        help="Diretório de saída",
    )
    args = parser.parse_args()
    
    organizar_apostilas(args.manifesto, args.gerados, args.saida)


if __name__ == "__main__":
    main()
