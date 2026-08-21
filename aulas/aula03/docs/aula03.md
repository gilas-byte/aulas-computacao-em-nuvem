# Respostas da aula 03

> Aula pratica de python com docker.

## 1. O que foi necessario instalar e configurar para executar a aplicação sem Docker?

Ter o Python instalado no pc, configurar um ambiente virtual e utilizar um gerenciador de pacotes (como o pip) para instalar as dependências, como o Flask.

## 2. O que o Docker passou a empacotar ou padronizar?

O Docker passou a empacotar todo o ambiente de execução da aplicação. Python, a biblioteca Flask, o interpretador Python e até as dependências do sistema operacional necessárias para rodar o código, garantindo que ele funcione da mesma forma em qualquer computador.

## 3. Se o container for executado em uma VM IaaS, quais responsabilidades ainda ficam com a equipe?

A equipe fica responsável pela aplicação, pelos dados, e também pelo gerenciamento do Sistema Operacional da VM (atualizações, segurança) e pela instalação e manutenção do próprio motor do Docker dentro dessa VM.

## 4. O que um PaaS poderia assumir automaticamente?

O container todo, a VM e o runtime.

## 5. Porque Docker não pode ser classificado, sozinho, como IaaS, PaaS ou SaaS?

Porque o docker é uma ferramenta que empacota o processo em si, o código, a infraestrutura, o banco de dados, e precisa ser gerenciado ou pelo provedor, ou pelo cliente.