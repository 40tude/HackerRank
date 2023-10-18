from pathlib import Path
import sys

# https://www.codium.ai/blog/building-user-friendly-python-command-line-interfaces-with-click/
#import click

kTemplateDir ="./templates"
kTemplate1 = "000_template.py"
kTemplate2 = "000_template_Inputs.txt"


# TO DO : option "overwrite"
# TO DO : option 'template_dir"

# @click.command()
# @click.argument('project_name')
# #@click.option('--greeting', '-g', default='Hello', help='The name of the project.', required=True, type=str)

# #def mycommand(name, greeting):
# def mycommand(prj_name):

#     '''
#     This command creates a new project to be used with HackerRank challenges.
#     '''
#     #click.echo(greeting + " " + name)
    
    

def main():

    if((len(sys.argv)==1) or (len(sys.argv[1])==0)) :
        print("You should at least pass the name of the project to be created.")
        print("Usage : >python ./templates/new_prj 089_NameOfProject")
        print("Generates 2 files in the directory from where new_project is called : 089_NameOfProject.py and 089_NameOfProject_Inputs.txt")
        exit()
    
    file_path = Path.cwd()
    src = Path(file_path, kTemplateDir, kTemplate1)

    prj_name = sys.argv[1]
    dst_filename = prj_name + ".py"
    dst = Path(dst_filename)
    # DONE - Vérifier si le fichier existe
    # DONE - Si oui demander confirmation de ré-écriture
    # TO DO : option "overwrite"
    if (dst.exists()):
        ans = input(f"{dst} already exists. Overwrite ? y[N] :")
        ans = ans.upper() 
        # if ans=="":
        #     ans="N"
        if (ans!="Y"):
          print("The confirmation was not 'Y' or 'y'.")
          print("Operation cancelled.")              
          exit()
    dst.write_bytes(src.read_bytes())    

    src = Path(file_path, kTemplateDir, kTemplate2)
    dst_filename = prj_name + "_Inputs.txt"
    dst = Path(dst_filename)
    dst.write_bytes(src.read_bytes())    
    print("Done")
    
if __name__ == "__main__":
    main()
    # mycommand()