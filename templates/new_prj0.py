# 18 10 - Ver intiale
# 19 10 - Modifie le contenu du fichier input

# TO DO : option "overwrite"
# TO DO : option 'template_dir"


from pathlib import Path
import sys

kTemplateDir ="./templates"
kTemplate1 = "000_template.py"
kTemplate2 = "000_template_Inputs.txt"
kReplace = "$$TXT_TO_REPLACE$$"

def main():
    if((len(sys.argv)==1) or (len(sys.argv[1])==0)) :
        print("You should at least pass the name of the project to be created.")
        print("Usage : >python ./templates/new_prj 089_NameOfProject")
        print("Generates 2 files in the directory from where new_project is called : 089_NameOfProject.py and 089_NameOfProject_Inputs.txt")
        exit()
    
    file_path = Path.cwd()
    src = Path(file_path, kTemplateDir, kTemplate1)

    prj_name = sys.argv[1]
    input_file = prj_name + ".py"
    dst = Path(input_file)
    # DONE - Vérifier si le fichier existe
    # DONE - Si oui demander confirmation de ré-écriture
    if (dst.exists()):
        ans = input(f"{dst} already exists. Overwrite ? y[N] :")
        ans = ans.upper() 
        if (ans!="Y"): # gere aussi le cas où ans==""
          print("The confirmation was not 'Y' or 'y'.")
          print("Operation cancelled.")              
          exit()
    dst.write_bytes(src.read_bytes())    

    src = Path(file_path, kTemplateDir, kTemplate2)
    input_file = prj_name + "_Inputs.txt"
    dst = Path(input_file)
    dst.write_bytes(src.read_bytes())    

    # Modification du fichier .py pour lire le bon fichier _Inputs.txt
    src_filename = prj_name + ".py"
    src = Path(src_filename)
    filedata = src.read_text()
    filedata = filedata.replace(kReplace, input_file)
    src.write_text(filedata)

    print("Done")
    
if __name__ == "__main__":
    main()