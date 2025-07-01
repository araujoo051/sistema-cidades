# Sistema de Grafos - Cidades e Conexões

Este projeto é uma aplicação em Python que simula um grafo não direcionado com cidades como vértices e conexões entre elas como arestas. É possível cadastrar cidades, adicionar conexões com distâncias, importar dados de um arquivo CSV e consultar informações através de um menu interativo.

## 🧩 Funcionalidades

- ✅ Cadastrar novas cidades
- ✅ Listar cidades cadastradas
- ✅ Criar conexões entre cidades com distância (em km)
- ✅ Listar todas as conexões existentes
- ✅ Ver vizinhos (cidades conectadas) de uma cidade
- ✅ Importar cidades e conexões de um arquivo CSV

## 📁 Estrutura do Projeto

- `grafo.py`: Contém a classe `Grafo` e `Cidade`, além do menu principal.
- `grafo.csv` *(opcional)*: Arquivo de entrada para importar cidades e conexões automaticamente.

### Formato do CSV esperado:

```csv
cidade1,cidade2,distancia
sao paulo, campinas, 100
campinas, rio de janeiro, 400
