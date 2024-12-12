import os
import shutil
import string

def rename_and_copy_files(source_base_directory, destination_directory):
    # Vérifiez si le dossier de destination existe, sinon créez-le
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    
    # Parcourez chaque dossier dans le répertoire de base
    for base_folder in os.listdir(source_base_directory):
        base_folder_path = os.path.join(source_base_directory, base_folder)
        
        if os.path.isdir(base_folder_path):  # Assurez-vous que c'est un dossier
            # Parcourez les sous-dossiers dans chaque dossier de base
            for foldername in os.listdir(base_folder_path):
                folderpath = os.path.join(base_folder_path, foldername)
                
                if os.path.isdir(folderpath):  # Assurez-vous que c'est un sous-dossier
                    files = [f for f in os.listdir(folderpath) if os.path.isfile(os.path.join(folderpath, f))]
                    
                    # Suppose que chaque dossier contient 10 fichiers avec le même nom
                    file_names = set(f.split('.')[0] for f in files)  # Utilisation du nom sans extension
                    if len(file_names) == 1:  # Si tous les fichiers ont le même nom de base
                        base_name = list(file_names)[0]
                        
                        # Renommer et copier les fichiers
                        for i, filename in enumerate(files):
                            new_name = f"{base_name}_{string.ascii_uppercase[i]}.{filename.split('.')[-1]}"  # Nouveau nom avec lettre ajoutée
                            src_file = os.path.join(folderpath, filename)
                            dest_file = os.path.join(destination_directory, new_name)
                            
                            # Copier le fichier renommé dans le dossier de destination
                            shutil.copy(src_file, dest_file)
                            print(f"Copié: {src_file} -> {dest_file}")
                    else:
                        print(f"Les fichiers dans le dossier {foldername} n'ont pas le même nom de base.")
        else:
            print(f"{base_folder} n'est pas un dossier.")
            
# Exemple d'utilisation
source_base_directory = "C:/Users/admin/Documents/deo/.worspace/AI/class_vo/Handwritten_digit_project_L3_IA"   # Remplacez par votre chemin source
destination_directory = "C:/Users/admin/Documents/deo/.worspace/AI/class_vo/dataset"   # Remplacez par votre chemin de destination
rename_and_copy_files(source_base_directory, destination_directory)
