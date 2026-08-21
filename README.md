# ☁️ Aulas de Computação em Nuvem 🐳

> Meu repositório pessoal de estudos da matéria de Computação em Nuvem

## ☁️ O que é Computação em Nuvem?

Computação em Nuvem é a entrega de recursos de TI (servidores, armazenamento, banco de dados, rede) pela internet, pagando somente pelo que se usa, ao invés de comprar e manter máquinas físicas.

**`IaaS, PaaS e SaaS são os modelos de serviço da nuvem, e a diferença entre eles está em quanto da infraestrutura o provedor assume e quanto continua sendo responsabilidade da sua equipe.`**

## Por que este repositório existe?

Este é um repositório público das minhas **aulas de Computação em Nuvem**, para que você possa ver todos os códigos que estou fazendo nas aulas, e aprender com eles também.

O projeto que vai sendo construído aula após aula é o **Radar ENEM**, uma API em Flask que consulta notas e é usada como cobaia para os testes de containerização, carga e custo.

`Todas as pastas das aulas têm uma pasta docs/ com as respostas e observações da aula`

## 🗂️ Quadro de aulas

| Aula | Descrição |
| --- | --- |
| [Aula 03](aulas/aula03) | 🐳 API Flask do Radar ENEM empacotada em Docker + respostas sobre IaaS, PaaS e SaaS. |
| [Aula 04](aulas/aula04) | 📊 Monitoramento de container sob carga (`docker stats`), requisitos do serviço e simulação de custos. |
| **`(Aguarde...)`** | **`(Aguarde...)`** |

## 🛠️ Tecnologias e Ferramentas

* **Linguagem:** Python 3.12
* **API:** Flask
* **Containers:** Docker
* **Testes de carga:** `requests` + threads, com coleta via `docker stats`
* **Sistema:** Desenvolvido e testado rodando liso no Linux (CachyOS) 🐧

## 🚀 Como rodar o Radar ENEM

Suba o container da aplicação:

```bash
cd aulas/aula03

docker build -f dockerfile -t radar-enem .

docker run -d -p 5000:5000 --name radar-enem radar-enem
```

E teste os endpoints:

```bash
curl http://localhost:5000/health
curl http://localhost:5000/nota/650
curl http://localhost:5000/aluno/guilherme
```

Com o container de pé, dá pra gerar carga e monitorar o consumo:

```bash
cd ../aula04

python gerar_carga.py
```

## Sinta-se à vontade para clonar o repositório

```bash
git clone "https://github.com/gilas-byte/aulas-computacao-em-nuvem"
```

e se o repositório tiver alguma atualização:

```bash
git pull
```

**Obrigado pela visita, bons estudos!**
