from sqlalchemy import text

# Query para inserir ou atualizar os Donos (Owners)
UPSERT_OWNERS_QUERY = text("""
    INSERT INTO dim_owners (owner_id, login, owner_type, avatar_url, owner_url, created_at_owner)
    SELECT owner_id, login, owner_type, avatar_url, owner_url, created_at_owner FROM temp_owners
    ON CONFLICT (owner_id) DO UPDATE SET
        owner_url = EXCLUDED.owner_url,
        created_at_owner = EXCLUDED.created_at_owner;
""")

# Query para inserir ou atualizar os Repositórios (Fato)
UPSERT_REPOS_QUERY = text("""
    INSERT INTO fact_repositories (
        repo_id, owner_id, name, full_name, description, 
        primary_language, stargazers_count, forks_count, 
        watchers_count, open_issues_count, size_kb, 
        created_at_github, last_push_github, extracted_at
    )
    SELECT 
        repo_id, owner_id, name, full_name, description, 
        primary_language, stargazers_count, forks_count, 
        watchers_count, open_issues_count, size_kb, 
        created_at_github, last_push_github, extracted_at
    FROM temp_repos
    ON CONFLICT (repo_id) DO UPDATE SET
        stargazers_count = EXCLUDED.stargazers_count,
        forks_count = EXCLUDED.forks_count,
        watchers_count = EXCLUDED.watchers_count,
        last_push_github = EXCLUDED.last_push_github,
        extracted_at = EXCLUDED.extracted_at;
""")



DASHBOARD_QUERY = """
    SELECT 
        r.full_name, 
        r.stargazers_count, 
        r.watchers_count, 
        r.forks_count, 
        r.size_kb, 
        r.open_issues_count,
        o.login as owner, 
        o.avatar_url,
        ROUND((r.watchers_count::numeric / r.stargazers_count::numeric) * 100, 2) as engagement_rate,
        ROUND((r.forks_count::numeric / r.stargazers_count::numeric) * 100, 2) as contribution_rate
    FROM fact_repositories r
    JOIN dim_owners o ON r.owner_id = o.owner_id
"""




# Query de limpeza das tabelas temporárias
DROP_TEMPS_QUERY = text("DROP TABLE IF EXISTS temp_owners; DROP TABLE IF EXISTS temp_repos;")