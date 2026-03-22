# src/transform/github_transformer.py
import pandas as pd
from datetime import datetime

def transform_repos_data(raw_repos):
    owners_list, repos_list = [], []

    for repo in raw_repos:
        # Dados do Dono
        owners_list.append({
            'owner_id': repo.owner.id, 'login': repo.owner.login,
            'owner_type': repo.owner.type, 'avatar_url': repo.owner.avatar_url,
            'owner_url': repo.owner.html_url, 'created_at_owner': repo.owner.created_at 
        })
        # Dados do Repositório
        repos_list.append({
            'repo_id': repo.id, 'owner_id': repo.owner.id, 'name': repo.name,
            'full_name': repo.full_name, 'description': repo.description[:255] if repo.description else "",
            'primary_language': repo.language, 'stargazers_count': repo.stargazers_count,
            'forks_count': repo.forks_count, 'watchers_count': repo.subscribers_count,
            'open_issues_count': repo.open_issues_count, 'size_kb': repo.size,
            'created_at_github': repo.created_at, 'last_push_github': repo.pushed_at,
            'extracted_at': datetime.now()
        })

    df_owners = pd.DataFrame(owners_list).drop_duplicates(subset=['owner_id'])
    df_repos = pd.DataFrame(repos_list)
    return df_owners, df_repos