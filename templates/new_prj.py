# 18 10 - Ver intiale
# 19 10 - Modifie le contenu du fichier input
# 21 10 - levarage click (Excelent !!!!)

# DONE : option "overwrite"
# DONE  : option 'verbose"
# TO DO : option 'template_dir"
# TO DO : manage multiple prj_name ? What would be the use case?

from pathlib import Path
import sys

# https://realpython.com/python-click/
import click

kTemplateDir ="./templates"
kTemplate1 = "000_template.py"
kTemplate2 = "000_template_Inputs.txt"
kReplace = "$$TXT_TO_REPLACE$$"

# ##############################################################################
@click.command("new_prj")
@click.version_option("0.1.0", prog_name="new_prj")

@click.option(
  "-v", 
  "--verbose", 
  is_flag=True,
  help="Display information while the command runs.",
)

@click.option(
  "-o", 
  "--overwrite", 
  is_flag=True,
  help="Overwrite existing PRJ_NAME.py and PRJ_NAME_Inputs.txt files.",
)  # default value is False

@click.argument(
  "prj_name",
  nargs=1,         # only one prj_name can be managed so far
)

# ##############################################################################
def cli(prj_name, verbose, overwrite):
  '''
    Create a ready to use HackerRank project consisting of two files (.py and _Inputs.txt files).
    PRJ_NAME is a valid filename.
    PRJ_NAME.py and PRJ_NAME_Inputs.txt files will be created in the directory from where this command is called.
  '''

  file_path = Path.cwd()
  src = Path(file_path, kTemplateDir, kTemplate1)
  python_filename = prj_name + ".py"
  dst = Path(python_filename)
  # DONE - Check if the file exists
  # DONE - If yes ask for confirmation before overwrite
  if (dst.exists() and overwrite==False):
      if not click.confirm(f"'{dst}' already exists. Overwrite?"):
        click.echo("Operation aborted.")              
        raise SystemExit(1)
  
  dst.write_bytes(src.read_bytes())   
  if verbose:
    click.echo(f"{python_filename} created.")

  src = Path(file_path, kTemplateDir, kTemplate2)
  inputs_file = prj_name + "_Inputs.txt"
  dst = Path(inputs_file)
  dst.write_bytes(src.read_bytes())
  if verbose:  
    click.echo(f"{inputs_file} created.")
  
  # Modify the content of prj_name.py in order to open prj_name_Inputs.txt
  src_filename = prj_name + ".py"
  src = Path(src_filename)
  filedata = src.read_text()
  filedata = filedata.replace(kReplace, inputs_file)
  src.write_text(filedata)
  if verbose:
    click.echo(f"Content of {src_filename} updated.")
  
  click.echo("Done.")

# ##############################################################################
if __name__ == '__main__':
  cli()