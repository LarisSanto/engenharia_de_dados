# Definindo que vamos usar o provedor da AWS
provider "aws" {
  region = "us-east-1" # Região padrão da Amazon (Norte da Virgínia)
}

# 1. Criando um recurso de banco de dados relacional na nuvem (AWS RDS)
# No lugar de clicar no site da AWS, o Terraform lê este bloco e cria o banco sozinho
resource "aws_db_instance" "banco_dados_clima" {
  engine                 = "postgres"             # Motor do banco (pode ser mysql, postgres, oracle-se2, etc)
  engine_version         = "15.4"                 # Versão do banco de dados
  instance_class         = "db.t3.micro"          # Tamanho da máquina na nuvem (econômica para testes)
  allocated_storage      = 20                     # Espaço em disco em Gigabytes (20 GB)
  identifier             = "meu-banco-rds-clima"  # Nome do banco na AWS
  username               = "admin_engenharia"     # Usuário mestre de acesso
  password               = "SenhaSegura123!"      # Senha de acesso ao banco
  skip_final_snapshot    = true                   # Ignora backup final ao destruir o recurso (ótimo para testes)
  publicly_accessible    = true                   # Permite conexão externa (para fins didáticos)
}

# 2. Mostrando o endereço (endpoint) onde o Python vai se conectar depois de criado
output "endereco_do_banco_na_aws" {
  value       = aws_db_instance.banco_dados_clima.endpoint
  description = "Cole este endereço no seu código Python para enviar os dados direto para o RDS na nuvem!"
}