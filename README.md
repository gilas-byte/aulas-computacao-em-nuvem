# Aulas de Computação em Nuvem

![License: MIT](https://img.shields.io/badge/License-MIT-blue) ![Python](https://img.shields.io/badge/Python-3.12-blue)

Cloud computing coursework using a Flask API to study containers, load monitoring and cost estimation.
Repositório de aulas de Computação em Nuvem com uma API Flask para estudar containers, monitoramento de carga e estimativa de custos.

## What it does / O que faz

**EN:** This public study repository shares code and notes from cloud computing classes. **Radar ENEM** is a Flask API developed across lessons to practice containerization, load monitoring and cost estimation. Each lesson has a `docs/` folder with answers and observations.

**PT-BR:** Este repositório público reúne códigos e notas das **aulas de Computação em Nuvem**. O projeto desenvolvido aula após aula é o **Radar ENEM**, uma API Flask usada nos exercícios de containerização, carga e custo. Todas as pastas das aulas têm uma pasta `docs/` com as respostas e observações.

**Limitations / Limitações:** The API uses fixed example data, without an ENEM data integration or database; the cost script only multiplies user-provided values. A API usa dados fixos de exemplo, não consulta dados reais do ENEM e não possui banco de dados; o script de custos apenas multiplica os valores informados pelo usuário. Os exemplos usam o servidor de desenvolvimento do Flask e não constituem uma implantação de produção. / The examples use Flask's development server and do not constitute a production deployment.

### What is cloud computing? / O que é Computação em Nuvem?

**EN:** Cloud computing delivers IT resources (servers, storage, databases and networking) over the internet, paying for usage rather than buying and maintaining physical machines. IaaS, PaaS and SaaS differ in how much infrastructure the provider manages and what remains the team's responsibility.

**PT-BR:** Computação em Nuvem é a entrega de recursos de TI (servidores, armazenamento, banco de dados, rede) pela internet, pagando somente pelo que se usa, ao invés de comprar e manter máquinas físicas.

**IaaS, PaaS e SaaS são os modelos de serviço da nuvem, e a diferença entre eles está em quanto da infraestrutura o provedor assume e quanto continua sendo responsabilidade da sua equipe.**

### Lessons / Quadro de aulas

| Lesson / Aula | Description / Descrição |
| --- | --- |
| [Lesson 03 / Aula 03](aulas/aula03) | Docker-packaged Radar ENEM Flask API and answers about IaaS, PaaS and SaaS. / API Flask do Radar ENEM empacotada em Docker + respostas sobre IaaS, PaaS e SaaS. |
| [Lesson 04 / Aula 04](aulas/aula04) | Container load monitoring (`docker stats`), service requirements and cost simulation. / Monitoramento de container sob carga (`docker stats`), requisitos do serviço e simulação de custos. |

### Technologies / Tecnologias e ferramentas

- **Language / Linguagem:** Python 3.12 (Docker image / imagem Docker).
- **API:** Flask (`Flask>=3.0,<4.0`).
- **Containers:** Docker.
- **Load tests / Testes de carga:** `requests` + threads, with collection via / com coleta via `docker stats`.
- **Original development environment / Ambiente original de desenvolvimento:** Linux (CachyOS).

## Repository structure / Estrutura do repositório

- [`aulas/aula03/`](aulas/aula03): Flask API (`app.py`), `dockerfile`, `requirements.txt` and an average calculation example (`teste.py`). / API Flask, container, dependências e exemplo de cálculo de média.
- [`aulas/aula03/docs/`](aulas/aula03/docs): lesson answers and evidence. / Respostas e evidências da aula.
- [`aulas/aula04/`](aulas/aula04): `gerar_carga.py` (load and monitoring / carga e monitoramento), `carga_menor.py` (1,000 requests / 1.000 requisições) and / e `custos.py` (monthly cost / custo mensal).
- [`aulas/aula04/docs/`](aulas/aula04/docs) and / e [`media/`](aulas/aula04/media): observations and screenshots; `stats.json` and `requisicoes.json` in the lesson folder contain recorded measurements. / Observações e capturas; `stats.json` e `requisicoes.json` na pasta da aula contêm medições registradas.

## Running / Como rodar

### Get the repository / Obter o repositório

```bash
git clone https://github.com/gilas-byte/aulas-computacao-em-nuvem
cd aulas-computacao-em-nuvem
```

To update an existing clone, run `git pull` inside it. / Para atualizar um clone existente, execute `git pull` dentro dele.

### Radar ENEM

Requires Docker installed and running. From the repository root: / Requer Docker instalado e em execução. A partir da raiz do repositório:

```bash
cd aulas/aula03

docker build -f dockerfile -t radar-enem .

docker run -d -p 127.0.0.1:5000:5000 --name radar-enem radar-enem
```

Test the endpoints in another terminal: / Teste os endpoints em outro terminal:

```bash
curl http://localhost:5000/health
curl http://localhost:5000/nota/650
curl http://localhost:5000/aluno/guilherme
```

Other routes / Outras rotas: `/`, `/professor/<nome>` and / e `/nota/aluno/<nome>/media`. The average route always uses the same four example grades. / A rota de média sempre usa as mesmas quatro notas de exemplo.

### Load monitoring / Monitoramento de carga

Requires the running `radar-enem` container, Docker CLI access and Python with `requests` installed on the host. The lesson 03 `requirements.txt` declares only Flask; it does not install `requests`. / Requer o container `radar-enem` em execução, acesso ao comando Docker e Python com `requests` instalado na máquina. O `requirements.txt` da aula 03 declara apenas Flask; não instala `requests`.

From the repository root: / A partir da raiz do repositório:

```bash
cd aulas/aula04

python gerar_carga.py
```

The script sends 100 requests, captures `docker stats` and prints a report. It **overwrites** `stats.json` and `requisicoes.json` in the current directory, storing one JSON object per line. / O script envia 100 requisições, coleta `docker stats` e imprime um relatório. Ele **sobrescreve** `stats.json` e `requisicoes.json` no diretório atual, gravando um objeto JSON por linha.

### Cost estimation / Estimativa de custos

Requires Python only. From the repository root: / Requer apenas Python. A partir da raiz do repositório:

```bash
python aulas/aula04/custos.py
```

Enter the hourly price, hours per day and days per month; use a decimal point for fractional values. / Informe o preço por hora, as horas por dia e os dias por mês; use ponto como separador decimal.

## Status

Study / Estudo — coursework and educational experiments. / Aulas e experimentos didáticos.

## License / Licença

[MIT](LICENSE).
