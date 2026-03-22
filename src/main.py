# src/main.py
from src.utils.db import get_engine, get_github_client
from src.extract.github_extractor import fetch_top_java_repos
from src.transform.github_transformer import transform_repos_data
from src.load.postgres_loader import load_to_postgres


def run_pipeline():
    try:
        # Conexões
        engine = get_engine()
        client = get_github_client()

        # Fluxo ETL
        raw_data = fetch_top_java_repos(client, limit=50)
        df_owners, df_repos = transform_repos_data(raw_data)
        load_to_postgres(engine, df_owners, df_repos)

        print("✅ Pipeline executado com sucesso e modularizado!")
    except Exception as e:
        print(f"❌ Falha no Pipeline: {e}")

if __name__ == "__main__":
    run_pipeline()