import click
@click.command()

def new_prj():
  '''
    Create a ready to use HackerRank .py file
  '''
  click.echo("Hello World")

if __name__ == '__main__':
  new_prj()