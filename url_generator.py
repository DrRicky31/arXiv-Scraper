import os

def count_files_in_folder(folder):
    # Contatore per il numero di file
    count = 0
    
    # Controlla se il percorso è valido
    if os.path.isdir(folder):
        # Itera attraverso i file nella folder
        for nome in os.listdir(folder):
            # Costruisce il percorso completo del file
            percorso_completo = os.path.join(folder, nome)
            
            # Verifica che sia un file e non una directory
            if os.path.isfile(percorso_completo):
                count += 1
    else:
        print(f"La cartella '{folder}' non esiste o non è valida.")
    
    return count

def file_name_extractor(folder):
    # Lista vuota per contenere i nomi dei file
    nomi_file = []
    
    # Controlla se il percorso è valido
    if os.path.isdir(folder):
        # Itera attraverso i file nella folder
        for nome in os.listdir(folder):
            # Costruisce il percorso completo del file
            percorso_completo = os.path.join(folder, nome)
            
            # Verifica che sia un file e non una directory
            if os.path.isfile(percorso_completo):
                # Rimuove la parte iniziale 'html-' e la parte finale '.html'
                if nome.endswith('.json'):
                    nome_modificato = nome[0:-5]
                    nomi_file.append(nome_modificato)
                else:
                    nomi_file.append(nome)
    else:
        print(f"La cartella '{folder}' non esiste o non è valida.")
    
    return nomi_file

# Percorso della cartella
path = 'extractions'
file_list = file_name_extractor(path)

# Output con prefisso e salva su file
output = [f"https://arxiv.org/html/{file}" for file in file_list]

# Percorso per salvare l'output nel file .txt
output_file = 'output.txt'

# Salva l'output nel file .txt
with open(output_file, 'w') as f:
    for line in output:
        f.write(line + '\n')

# Stampa l'output per conferma
print(output)

# Conta il numero di file nella cartella
file_count = count_files_in_folder(path)
print(f"Numero di file nella cartella '{path}': {file_count}")
