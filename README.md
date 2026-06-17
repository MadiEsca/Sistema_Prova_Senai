# SENAI - Situação-Problema: Sistema de Controle de Almoxarifado

## Contextualização

Uma empresa de médio porte do setor industrial possui um almoxarifado central que utiliza uma planilha para o controle e distribuição de materiais de limpeza utilizados diariamente.

Com o crescimento da empresa, tornou-se inviável esse controle manual, gerando inconsistências, perdas e dificuldade na tomada de decisão.

Diante desse cenário, a empresa decidiu implantar um sistema informatizado de estoque, capaz de registrar entradas (contendo data inicial) e saídas (contendo data final) dos produtos (contendo nome, categoria, quantidade e valor unitário), com atualização automática do saldo de estoque e geração de relatórios para apoiar o planejamento de compras e a tomada de decisão.

---

## Desafio

Você foi contratado como programador júnior e ficará responsável pela primeira etapa da implantação do sistema informatizado de controle de almoxarifado.

Esta primeira etapa está focada exclusivamente na integridade e consistência das informações, concentrando-se na lógica de negócio e na persistência em banco de dados.

---

## Resultados e Entregas Esperadas

| Nº | Nome da Entrega |
|----|-----------------|
| 1 | Implementação do Banco de Dados (Script) |
| 2 | Codificação Back-End (Implementação das regras de negócio com interação no banco de dados) |

---

## Regras de Negócio

### Banco de Dados

- Desenvolver o Diagrama Entidade-Relacionamento (DER), representando adequadamente as entidades, atributos, relacionamentos e cardinalidades, conforme a situação-problema.
- O script do banco de dados deverá conter, no mínimo, três registros em cada uma das tabelas criadas.
- Respeitar os tipos de dados definidos.
- Implementar corretamente as restrições de chaves primárias e estrangeiras.
- Criar uma *view* denominada `vw_estoque`, responsável por calcular e apresentar o valor total por item de produto, considerando a quantidade registrada e o respectivo valor unitário.

### Back-End

A codificação Back-End deverá ser apresentada por meio de uma das seguintes formas:

- Terminal/Console (logs de execução);
- Endpoints (API) utilizando Postman ou Insomnia (requisição e resposta);
- Retorno/saída da função exibida no console.

### Funcionalidades Obrigatórias

#### Consultas

- Listar o valor total por categoria do produto, considerando a quantidade registrada e o valor unitário.
- Listar todos os produtos cadastrados. **OK**
- Listar todas as saídas de produtos em ordem decrescente por data.

#### Cadastro e Movimentação

- Cadastrar novos produtos contendo validações para: **OK**
  - Valor unitário;
  - Quantidade;
  - Categoria (A, B, C). **OK**
- Registrar entradas de produtos no estoque. **ok**

#### Relatórios

- Listar movimentações de entrada e saída em um período informado (data inicial e data final), apresentando os seguintes campos:

  - Nome do produto;
  - Unidade de medida (ml, kg, g);
  - Total de entradas;
  - Total de saídas;
  - Saldo no período;
  - Valor total financeiro das entradas;
  - Valor total financeiro das saídas.

- Listar os produtos com maior volume de saída em um período informado (data inicial e data final), apresentando:

  - Nome do produto;
  - Quantidade total de saída;
  - Valor total financeiro das saídas.

#### Controle de Estoque

- Identificar produtos que tenham atingido os limites:
  - Mínimo: 0;
  - Máximo: 100.

- Exibir o percentual do nível de estoque atingido para cada produto.

---

## Observação

Durante toda a implementação do sistema, devem ser utilizadas boas práticas de TI, garantindo organização, qualidade, segurança e manutenibilidade do código.