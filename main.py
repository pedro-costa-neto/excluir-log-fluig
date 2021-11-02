import click
import os
import sqlite3
import getpass
from datetime import datetime
from tabulate import tabulate
from peewee import *

db = SqliteDatabase('database.db')

class BaseModel(Model):
    class Meta:
        database = db

class Storages(BaseModel):
    id = AutoField(primary_key = True, null = False, unique = True)
    user = CharField(null = False)
    path = TextField(null = False)

class Log(BaseModel):
    id = AutoField(primary_key = True, null = False, unique = True)
    user = CharField(null = False)
    path = TextField(null = False)
    date = DateField(null = False)
    size = DoubleField(null = False)


@click.group()
def main():
    db.connect()
    db.create_tables([Storages, Log])

@main.command()
def storage_list():
    storage = Storages.select()
    click.echo(tabulate(storage.tuples(), headers=["ID", "USER", "PATH"]))

@main.command()
@click.option("--path", help="Informar o caminho da pasta")
def storage_insert(path):
    record = {
        "user": getpass.getuser(),
        "path": path
    }
    Storages.insert(record).execute()
    click.echo("Storage criado com suacesso!")

@main.command()
@click.option("--id", prompt="ID", help="Informar o ID do Path")
@click.option("--path", prompt="Path", help="Informar o Path")
def storage_update(id, path):
    Storages.update({Storages.path: path}).where(Storages.id == id).execute()
    click.echo("Storage atualizado com suacesso!")

@main.command()
@click.option("--id", prompt="ID", help="Informar o ID do Path")
def storage_delete(id):
    Storages.delete().where(Storages.id == id).execute()
    click.echo("Storage excluído com sucesso!")

@main.command()
def run():
    storages = Storages.select()

    for storage in storages:
        if os.path.isdir(storage.path):
            for file in os.listdir(storage.path):
                if (file.find("server-") >= 0 and (file.find(".log") >= 0 or file.find(".zip") >= 0)):
                    file_path = os.path.join(storage.path, file)
                    file_size = os.path.getsize(file_path) / (1024 ** 2)

                    record = {
                        "user": getpass.getuser(),
                        "path": file_path,
                        "date": datetime.now(),
                        "size": file_size
                    }

                    Log.insert(record).execute()
                    os.remove(file_path)
    click.echo("Arquivos excluídos com sucesso!")
    click.echo("Para visualizar a lista de arquivos excluídos, executar o comando log-list --date aaaa-mm-dd")

if __name__ == "__main__":
    main()