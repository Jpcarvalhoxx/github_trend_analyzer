-- 1. Dimensão de Owners
CREATE TABLE dim_owners (
    owner_id BIGINT,
    login VARCHAR(100) NOT NULL,
    owner_url VARCHAR(255),
    owner_type VARCHAR(50),
    avatar_url VARCHAR(255),
    created_at_owner TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Definição da Chave Primária como Constraint
    CONSTRAINT pk_owner PRIMARY KEY (owner_id)
);

-- 2. Tabela Fato de Repositórios
CREATE TABLE fact_repositories (
    repo_id BIGINT,
    owner_id BIGINT,
    name VARCHAR(150) NOT NULL,
    full_name VARCHAR(255),
    description TEXT,
    primary_language VARCHAR(50),
    
    -- Métricas
    stargazers_count INTEGER DEFAULT 0,
    forks_count INTEGER DEFAULT 0,
    watchers_count INTEGER DEFAULT 0,
    open_issues_count INTEGER DEFAULT 0,
    size_kb INTEGER,
    license_name VARCHAR(100),
    has_wiki BOOLEAN DEFAULT FALSE,
    has_pages BOOLEAN DEFAULT FALSE,
    
    -- Timestamps
    created_at_github TIMESTAMP,
    last_push_github TIMESTAMP,
    extracted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- --- SEÇÃO DE CONSTRAINTS ---
    
    -- Define a Chave Primária
    CONSTRAINT pk_repo PRIMARY KEY (repo_id),

    -- Define a CHAVE ESTRANGEIRA explicitamente
    -- Se o dono for deletado, os repositórios dele também são (CASCADE)
    CONSTRAINT fk_repo_owner 
        FOREIGN KEY (owner_id) 
        REFERENCES dim_owners (owner_id) 
        ON DELETE CASCADE
);

-- ⚡ Índices de Performance
CREATE INDEX idx_repo_language ON fact_repositories(primary_language);
CREATE INDEX idx_repo_stars ON fact_repositories(stargazers_count DESC);
