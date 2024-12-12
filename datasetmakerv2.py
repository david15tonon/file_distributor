import os
import shutil

source_directory = "C:/Users/admin/Documents/deo/.worspace/AI/class_vo/Handwritten_digit_project_L3_IA"
destination_directory = "C:/Users/admin/Documents/deo/.worspace/AI/class_vo/dataset"

def rename_and_copy_files(source_directory, destination_directory):
    # Vérifiez si le dossier de destination existe, sinon créez-le
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    
    # Dictionnaire pour regrouper les fichiers par nom
    files_dict = {}

    # Parcourez chaque dossier dans le répertoire source
    for foldername in os.listdir(source_directory):
        folderpath = os.path.join(source_directory, foldername)
        
        if os.path.isdir(folderpath):  # Assurez-vous que c'est un dossier
            # Parcourez les fichiers du dossier
            for filename in os.listdir(folderpath):
                file_path = os.path.join(folderpath, filename)
                
                if os.path.isfile(file_path):  # Si c'est bien un fichier
                    base_name = filename.split('.')[0]  # Récupérer le nom de base sans l'extension
                    
                    if base_name not in files_dict:
                        files_dict[base_name] = []
                    files_dict[base_name].append(file_path)  # Ajoutez le chemin complet du fichier dans le dictionnaire

    # Maintenant, traitez chaque groupe de fichiers ayant le même nom de base
    for base_name, file_paths in files_dict.items():
        if len(file_paths) > 1:  # Si plusieurs fichiers ont le même nom de base
            for i, file_path in enumerate(file_paths):
                # Construire un nouveau nom avec un compteur numérique
                new_name = f"{base_name}_{i+1}.{file_path.split('.')[-1]}"  # Ajouter un numéro à la fin du nom de base
                dest_file = os.path.join(destination_directory, new_name)
                
                # Copier le fichier dans le dossier de destination
                shutil.copy(file_path, dest_file)
                print(f"Copié: {file_path} -> {dest_file}")
        else:
            print(f"Le fichier {base_name} n'a pas plusieurs instances, il n'est donc pas traité.")

# Exemple d'utilisation
rename_and_copy_files(source_directory, destination_directory)
