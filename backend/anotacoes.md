# Anotações

Esse arquivo vai ajudar a armazenar as informações referentes as bibliotecas utilizadas dentro desse projeto.

## Supabase

.table("tabela") -> Seleciona a tabela
.select(* | "coluna")
.eq("campo", informação_a_ser_filtrdada) -> Permite a utilização de filtros. Equivalente ao where
.execute() -> Executa a consulta

``` python
supabase.table("nome_tabela").select(* | "coluna").eq("campo", informação_a_ser_filtrdada).execute()
```

---

Ao criar um produto e definirmos sua quantidade, devemos inserir suas informações dentro da tabela "TABELA_ENTRADA". De forma que só seja possível fazer isso caso o produto exista.

Não permitir que produtos repetidos (nome, categoria) sejam criados.

---

### Lógicas

#### Lógica para a criação de um produto
Determinado produto já existe? Se sim, não criar o produto e lançar um erro. Se não, solicitar as informações do produto e realizar sua criação.

#### Lógica para o registro das entradas de produtos de dentro do almoxarifado
    Determinado produto existe? Se sim, solicitar nome do produto, a quantidade de produtos a darem entrada no sistema e criar um registro com essas informações dentro da tabela entradas, além disso, fazer um altertable e somar a quantidade de entradas com a quantidade do estoque atual de produtos. Se não, não realizar a entrada e solicitar que o usuário crie o produto para que sua entrada possa ser registrada no sistema.

#### Lógica para o registo de saída dos produtos de dentro do almoxarifado
    Determinado produto existe? Se sim, solicitar o nome do produto, a quantidade de produtos a serem retirados do sistema e criar um registr com essas informações dentro da tabela saídas, além disso, fazer um altertable e subtrair a quantidade de saídas com a quantidade do estoque atual de produtos. Se não, não realizar a saída e solicitar que o usuário crie o produto para que sua retirada possa ser registrada dentro do sistema.