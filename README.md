## (Fluig) Exclusão de logs

Rotina para excluir os arquivos de logs ".log" e ".zip" que são baixados durante o desenvolvimento e monitoramento do sistema.

A rotina foi desenvolvida para ser um **command-line interface** (CLI) simples, permitindo o gerenciamento das pastas que serão monitoradas para buscar os arquivos de logs.



#### Cadastrar um storage

Para cadastrar um storage é necessário informar o parâmetro "--path", onde é referenciado o caminho da pasta.

```
python main.py storage-insert --path C:\Users\usuario\Downloads
```



#### Listar storages

```
python main.py storage-list
```

O comando retornará uma tabela com as informações abaixo.

```
  ID  USER      PATH
----  --------  --------------------------
   1  usuario   C:\Users\usuario\Downloads
   2  usuario   C:\Users\usuario\Desktop
```



#### Atualizar um storage

Para atualizar o storage é necessário informar os parâmetros "--id" e "--path".

- "--id" é o ID informado no retorno do comando que lista os storages cadastrados;
- "--path" é informado o novo caminho da pasta;

```
python main.py storage-update --id 2 --path C:\Users\usuario\Documents
```



#### Excluir um storage

Para excluir o storage é necessário informar o parâmetro "--id", referenciando o ID apresentando no retorno do comando que lista os storages cadastrados.

```
python main.py storage-delete --id 2
```



#### Executar a rotina para excluir os logs

O comando abaixo inicia a rotina que excluirá os arquivos de log e grava as informações "User", "Path", "Date" e "Size" de cada arquivo excluído na tabela log. 

```
python main.py run
```

