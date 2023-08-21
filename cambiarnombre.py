import os

def rename_files():
    # Obtener la ruta de la carpeta actual
    folder_path = "C:/Users/hp/Documents/entrevistas 2023/GATechSolutions/errors"

    # Obtener una lista de todos los archivos en la carpeta actual
    files = os.listdir(folder_path)

    for file in files:
        # Verificar si el archivo tiene la extensión ".fct_error"
        if file.endswith(".fct_error"):
            # Generar el nuevo nombre del archivo quitando la parte ".error" de la extensión
            new_name = file.replace(".fct_error", ".fct")

            # Renombrar el archivo
            os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_name))

rename_files()
