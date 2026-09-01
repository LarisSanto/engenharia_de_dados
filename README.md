# Pipeline de Engenharia de Dados: Da API à Nuvem e IaC
<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy">
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/Terra-7B42BC?style=for-the-badge&logo=terraform&logoColor=white" alt="Terraform">
  <img src="https://img.shields.io/badge/Amazon_AWS-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white" alt="AWS">
  <img src="https://img.shields.io/badge/GitHub_Codespaces-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Codespaces">
  <img src="https://img.shields.io/badge/DBeaver-382923?style=for-the-badge&logo=dbeaver&logoColor=white" alt="DBeaver">
</p>


Este projeto foi desenvolvido com uma abordagem prática ("hands-on") para simular um fluxo completo de Engenharia de Dados corporativo, cobrindo desde a extração de dados brutos até a modelagem relacional, estruturação de Data Lake e automação de infraestrutura. 


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
<br>

### Etapas do Pipeline

* Etapa 01 : Ingestão e Persistência Local (01_extracao_local/)
  - Consome dados meteorológicos em tempo real de uma API pública (Open-Meteo), trata o payload JSON utilizando Pandas e exporta os dados simultaneamente para três formatos diferentes (.csv, .xlsx e .parquet) para estudo de performance e armazenamento.
* Etapa 02 : Carga em Banco de Dados Relacional
  - Utiliza SQLAlchemy e Pandas para transformar o DataFrame extraído em uma tabela estruturada dentro de um banco de dados relacional, permitindo consultas e validações.
* Etapa 03 : Simulação de Cloud Data Lake
  - Simula a estruturação de dados em uma arquitetura de Data Lake corporativa, salvando o arquivo otimizado em formato colunar (Parquet), padrão utilizado na camada Bronze de ambientes em nuvem.
* Etapa 04 : Infraestrutura como Código - IaC
  - Contém o arquivo declarativo (main.tf) utilizando Terraform para provisionar de forma automatizada um banco de dados gerenciado em nuvem (AWS RDS), substituindo processos manuais por código versionável.
 
<br>

### Imagens do terminal.

<br>

Etapa 01 
<img width="1920" height="1060" alt="fase1_extracao png" src="https://github.com/user-attachments/assets/463cb184-4243-4814-98cb-48c32ca6dd2a" />

Etapa 02 
<img width="1920" height="1060" alt="fase2_banco png" src="https://github.com/user-attachments/assets/14ef074e-7667-41e8-b026-2125342f4daa" />

Etapa 03 
<img width="1920" height="1060" alt="fase3_s3 png" src="https://github.com/user-attachments/assets/edc44133-2082-4234-8561-0800ac369eda" />

Etapa 04  
<img width="1920" height="1060" alt="fase4_terraform png" src="https://github.com/user-attachments/assets/35e8629a-c665-4816-bb10-1f0f725d9d61" />

DBeaver
<img width="1920" height="1060" alt="dbeaver_tabela png" src="https://github.com/user-attachments/assets/f32a9c3a-9bc4-4e7b-a9bd-44f6f4bbff19" />


<br>

### Tecnologias Utilizadas
* Linguagem: Python (Pandas, Requests, SQLAlchemy, PyArrow)
* Bancos de Dados: SQLite (Relacional local) e arquitetura multi-banco
* Computação em Nuvem / Data Lake: Simulação de armazenamento em nuvem (Padrão Bronze em Parquet)
* Infraestrutura como Código (IaC): Terraform (AWS RDS)
* Ferramentas: GitHub Codespaces, DBeaver

<br>
#### OBS: Projeto desenvolvido como parte do aprendizado prático em Engenharia de Dados.
