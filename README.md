# Pipeline de Engenharia de Dados: Da API à Nuvem e IaC

Este projeto foi desenvolvido com uma abordagem prática ("hands-on") para simular um fluxo completo de Engenharia de Dados corporativo, cobrindo desde a extração de dados brutos até a modelagem relacional, estruturação de Data Lake e automação de infraestrutura.

### Tecnologias Utilizadas
* Linguagem: Python (Pandas, Requests, SQLAlchemy, PyArrow)
* Bancos de Dados: SQLite (Relacional local) e arquitetura multi-banco
* Computação em Nuvem / Data Lake: Simulação de armazenamento em nuvem (Padrão Bronze em Parquet)
* Infraestrutura como Código (IaC): Terraform (AWS RDS)
* Ferramentas: GitHub Codespaces, DBeaver

---

### Estrutura do Repositório
O projeto é dividido em quatro fases modulares:
```text
engenharia_de_dados/
├── 01_extracao_local/     # Extração da API e salvamento em CSV, Excel e Parquet
├── 02_bancos_locais/      # Carga e persistência em banco de dados relacional
├── 03_cloud_s3/           # Simulação de armazenamento em Data Lake (Camada Bronze)
├── 04_terraform_iac/      # Código de infraestrutura para provisionar AWS RDS
└── README.md              # Documentação oficial do projeto
```

### Etapas do Pipeline

* Etapa 1: Ingestão e Persistência Local (01_extracao_local/)
  - Consome dados meteorológicos em tempo real de uma API pública (Open-Meteo), trata o payload JSON utilizando Pandas e exporta os dados simultaneamente para três formatos diferentes (.csv, .xlsx e .parquet) para estudo de performance e armazenamento.
* Etapa 2: Carga em Banco de Dados Relacional
  - Utiliza SQLAlchemy e Pandas para transformar o DataFrame extraído em uma tabela estruturada dentro de um banco de dados relacional, permitindo consultas e validações.
* Simulação de Cloud Data Lake
  - Simula a estruturação de dados em uma arquitetura de Data Lake corporativa, salvando o arquivo otimizado em formato colunar (Parquet), padrão utilizado na camada Bronze de ambientes em nuvem.
* Infraestrutura como Código - IaC
  - Contém o arquivo declarativo (main.tf) utilizando Terraform para provisionar de forma automatizada um banco de dados gerenciado em nuvem (AWS RDS), substituindo processos manuais por código versionável.
 



