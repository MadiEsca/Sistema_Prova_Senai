# Realizando a importação das bibliotecas que serão utilizadas
import os
from supabase import create_client, Client
from dotenv import load_dotenv
from datetime import datetime, timezone

load_dotenv() # Carregando o arquivo de .env

# Utilizar try, exception e finally
# Realizando a conexão com o banco de dados
def __server_connection():
    try:
        supabase: Client = create_client(
        os.environ.get("SUPABASE_URL"),
        os.environ.get("SUPABASE_KEY")
        )
        print("Conexão realizada com sucesso")
        return supabase
    except Exception as erro:
        print(f"Erro ao realiazar a conexão com o banco de dados: {erro}")
        return erro

# Criando as operações CRUD

# Operações relacionadas a tabela de produtos
def create_product(): # Realiza a criação de um produto dentro do sistema
    supabase = __server_connection()
    
    try:
        if supabase: # Funciona apenas se o servidor estiver conectado
            categorias = ("A","B","C") #Tupla com as categorias aceitas

            #Solicitando as informações a serem acrescentadas no banco de dados
            quantidade: int = int(input("Digite a quantidade no estoque: "))
            nome: str = str(input("Digite o nome do produto: "))
            categoria_escolhida: str = str(input("Digite a categoria (a, b, c): "))
            valor_unitario: float = float(input("Digite o preço unitário do produto: "))

            #Validação do campo de categoria
            if categoria_escolhida not in categorias:
                print("Categoria inválida")
                print("Selecione uma das seguites categorias: 'A', 'B', 'C'")
                return Exception("Categoria inválida")

            dados = {
                "quantidade":quantidade, 
                "nome": nome, 
                "categoria": categoria_escolhida, 
                "valor_unitario": valor_unitario
            }
            
            response = (
                supabase.table("tabela_produtos")
                .insert(dados)
                .execute()
                )
            
            register_entrace(quantidade_produto_entrada=quantidade, nome_produto=nome)
        return response
    except Exception as erro:
        print(f"Não funciona, {erro}")
        return erro

#Lista todos os produtos da tabela
def list_products():
    supabase = __server_connection()
    try:
        response = (
        supabase.table("tabela_produtos")
        .select("*")
        .execute()
        )
        print("Deu certo")
        print(response.data)
        return response.data
    except Exception as erro:
        print(f"Deu erro aqui, {erro}")
        return erro

def list_products_categories():
    supabase = __server_connection()
    #Solicitar uma categoria | Enviar para a consulta dentro do banco de dados | Retornar os dados
    try:
        categorias: tuple = ("A", "B", "C")

        categoria_busca: str = str(input("Digite a categoria (A, B, C): ")).upper()
        if categoria_busca not in categorias:
            print("Categoria inválida")
            print("Selecione uma das seguites categorias: 'A', 'B', 'C'")
            return Exception("Categoria inválida")
        
        response = (
            supabase.table("tabela_produtos")
            .select("*")
            .eq("categoria", categoria_busca)
            .execute()
        )

        # Realizar o tratamento quando a informação retornada for 
        print(f"As informações foram retornadas com sucesso: \n{response.data}")
        return response.data
    
    except Exception as erro:
        print(f"Houve um erro: {erro}")
        return erro

# Listar todos os produtos - ok
# Listar os produtos com base em sua categoria - ok


#Operações referentes a tabela de entrada de produtos
#Função que irá registrar a entrada de um produto

def list_individual_product(termo_pesquisa): # Busca um produto de forma individual
    supabase = __server_connection()
    try:
        if not termo_pesquisa:
            termo_pesquisa = input("Digite o nome do produto: ")
        
        response = (
            supabase.table("tabela_produtos")
            .select("*")
            .eq("nome", termo_pesquisa)
            .execute()
        )

        if not response.data: # Verifica se a requisição retorna algum dado
            print("Sem dados")
            return Exception("Sem dados por aqui")
        else: 
            #print(f"Os dados foram retornados com sucesso! \n {response.data}")
            return response.data

    except Exception as erro:
        print(f"Não foi possível realizar a consulta devido aos seguintes erros: {erro}")
        return erro

def register_entrace(quantidade_produto_entrada, nome_produto):
    #id_produto será um valor proveniente de uma consulta sql, que irá buscar pelo nome especificado pelo usuario
    supabase = __server_connection()
    try:
        if supabase:
            # Função utilizada para retornar os registros que correspondem ao nome especificado
            produto_busca = list_individual_product(nome_produto)

            data_entrada = datetime.now(timezone.utc).isoformat() # Pega a data e a hora atual
            quantidade = quantidade_produto_entrada # Pega a quantidade a de entrada do produto
            # Com base no valor retornado pela função list_individual_product, é selecionado apenas o id
            # do primeiro produto (0), já que só existe um único com o mesmo nome
            id_produto: int = produto_busca[0]["id"] 

            dados = {
                "data_entrada":data_entrada,
                "quantidade":quantidade,
                "id_produto":id_produto
            }

            response = (
                supabase.table("tabela_entradas")
                .insert(dados)
                .execute()
            )

            print("Cadastro realizado com sucesso")
            return response.data
    except Exception as erro:
        print(f"Não foi possível realizar o cadastro pelo seguinte motivo, {erro}")

# Listar todas as saídas de produtos com base data em ordem decrescente
def register_exits(quantidade_produto_saida, nome_produto):

    # Realizar a decrementação da quantidade de dentro do estoque


    #id_produto será um valor proveniente de uma consulta sql, que irá buscar pelo nome especificado pelo usuario
    supabase = __server_connection()
    try:
        if supabase:
            # Função utilizada para retornar os registros que correspondem ao nome especificado
            produto_busca = list_individual_product(nome_produto)

            data_saidas = datetime.now(timezone.utc).isoformat() # Pega a data e a hora atual
            quantidade = quantidade_produto_saida # Pega a quantidade a de entrada do produto
            # Com base no valor retornado pela função list_individual_product, é selecionado apenas o id
            # do primeiro produto (0), já que só existe um único com o mesmo nome
            id_produto: int = produto_busca[0]["id"]
            quantidade_produto: int = produto_busca[0]["quantidade"]

            dados = {
                "data_saida":data_saidas,
                "quantidade":quantidade,
                "id_produto":id_produto
            }

            # Realizando a subtração da tabela principal
            response_2 = (
                supabase.table("tabela_produtos")
                .update({"quantidade": f"{quantidade_produto - quantidade_produto_saida}"})
                .eq("id", 1)
                .execute()
            )

            # Realizando a inserção dentro da tabela de saídas
            response = (
                supabase.table("tabela_saidas")
                .insert(dados)
                .execute()
            )

            print("Retirada realizada com sucesso")
            return response.data
    except Exception as erro:
        print(f"Não foi possível realizar a solicitação pelo seguinte motivo, {erro}")


#list_products_categories()
print(datetime.now())
#list_products()
#register_exits(2, "Raquelly")

# Criar um painel solicitando qual o tipo de funcionalidade que o usuário quer

print("""
      1 - Listar produtos cadastrados no sistema
      2 - Cadastrar um produto no sistema
      3 - Retirar um produto

""")
escolha: int = int(input("Digite o que você quer fazer: "))
match escolha:
    case 1:
        list_products()
    case 2:
        create_product()
    case 3:
        register_exits()
    case 4:
        pass
    case _:
        print("Opção inválida")

#
if __name__ == "__main__":
    print("tudo funciona")