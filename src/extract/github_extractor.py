# src/extract/github_extractor.py
def fetch_top_java_repos(client, limit=50):
    print(f"📡 Buscando Top {limit} repositórios Java...")
    query = "language:Java stars:>5000"
    search_results = client.search_repositories(query, sort="stars", order="desc")
    return list(search_results[:limit])