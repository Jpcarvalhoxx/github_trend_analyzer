# src/load/postgres_loader.py
from src.load.queries import UPSERT_OWNERS_QUERY, UPSERT_REPOS_QUERY, DROP_TEMPS_QUERY

def load_to_postgres(engine, df_owners, df_repos):
    print("📥 Sincronizando com o Postgres via Docker...")
    with engine.connect() as conn:
        df_owners.to_sql('temp_owners', engine, if_exists='replace', index=False)
        conn.execute(UPSERT_OWNERS_QUERY)
        
        df_repos.to_sql('temp_repos', engine, if_exists='replace', index=False)
        conn.execute(UPSERT_REPOS_QUERY)
        
        conn.execute(DROP_TEMPS_QUERY)
        conn.commit()