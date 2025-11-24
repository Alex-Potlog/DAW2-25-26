"""
SOLUCIONS DELS EXERCICIS DE TRACTAMENT DE FITXERS EN PYTHON
============================================================

EXERCICIS BÀSICS
----------------
"""

# 1. LLEGIR I MOSTRAR
def exercici_1():
    try:
        with open('text_simple.txt', 'r', encoding='utf-8') as f:
            contingut = f.read()
            print(contingut)
    except FileNotFoundError:
        print("El fitxer no existeix")

# 2. COMPTAR LÍNIES
def exercici_2():
    try:
        with open('text_simple.txt', 'r', encoding='utf-8') as f:
            linies = f.readlines()
            print(f"El fitxer té {len(linies)} línies")
    except FileNotFoundError:
        print("El fitxer no existeix")

# 3. ESCRIURE TEXT
def exercici_3():
    frases = []
    print("Introdueix 5 frases:")
    for i in range(5):
        frase = input(f"Frase {i+1}: ")
        frases.append(frase)
    
    with open('frases_usuari.txt', 'w', encoding='utf-8') as f:
        for frase in frases:
            f.write(frase + '\n')
    print("Frases guardades a 'frases_usuari.txt'")

# 4. COPIAR FITXER
def exercici_4():
    try:
        with open('text_simple.txt', 'r', encoding='utf-8') as f_origen:
            contingut = f_origen.read()
        
        with open('text_simple_copia.txt', 'w', encoding='utf-8') as f_desti:
            f_desti.write(contingut)
        
        print("Fitxer copiat correctament")
    except FileNotFoundError:
        print("El fitxer origen no existeix")

"""
EXERCICIS INTERMEDIS
--------------------
"""

# 5. BUSCAR PARAULA
def exercici_5():
    paraula = input("Quina paraula vols buscar? ")
    try:
        with open('text_simple.txt', 'r', encoding='utf-8') as f:
            for num_linia, linia in enumerate(f, 1):
                if paraula.lower() in linia.lower():
                    print(f"Línia {num_linia}: {linia.strip()}")
    except FileNotFoundError:
        print("El fitxer no existeix")

# 6. ESTADÍSTIQUES DE TEXT
def exercici_6():
    try:
        with open('text_simple.txt', 'r', encoding='utf-8') as f:
            contingut = f.read()
            linies = contingut.split('\n')
            paraules = contingut.split()
            caracters = len(contingut)
            
            print(f"Estadístiques del fitxer:")
            print(f"- Línies: {len(linies)}")
            print(f"- Paraules: {len(paraules)}")
            print(f"- Caràcters: {caracters}")
    except FileNotFoundError:
        print("El fitxer no existeix")

# 7. FILTRAR LÍNIES
def exercici_7():
    paraula_clau = input("Paraula clau per filtrar: ")
    try:
        with open('text_simple.txt', 'r', encoding='utf-8') as f_entrada:
            linies = f_entrada.readlines()
        
        with open('text_filtrat.txt', 'w', encoding='utf-8') as f_sortida:
            for linia in linies:
                if paraula_clau.lower() in linia.lower():
                    f_sortida.write(linia)
        
        print(f"Línies amb '{paraula_clau}' guardades a 'text_filtrat.txt'")
    except FileNotFoundError:
        print("El fitxer no existeix")

# 8. INVERTIR CONTINGUT
def exercici_8():
    try:
        with open('text_simple.txt', 'r', encoding='utf-8') as f:
            linies = f.readlines()
        
        with open('text_invertit.txt', 'w', encoding='utf-8') as f:
            for linia in reversed(linies):
                f.write(linia)
        
        print("Contingut invertit guardat a 'text_invertit.txt'")
    except FileNotFoundError:
        print("El fitxer no existeix")

"""
EXERCICIS AVANÇATS
------------------
"""

# 9. PROCESSAR CSV
def exercici_9():
    try:
        with open('notes_estudiants.csv', 'r', encoding='utf-8') as f:
            linies = f.readlines()
        
        with open('mitjanes_estudiants.txt', 'w', encoding='utf-8') as f_sortida:
            # Saltem la capçalera
            for linia in linies[1:]:
                parts = linia.strip().split(',')
                nom = parts[0]
                notes = [float(parts[1]), float(parts[2]), float(parts[3])]
                mitjana = sum(notes) / len(notes)
                f_sortida.write(f"{nom}: {mitjana:.2f}\n")
                print(f"{nom}: {mitjana:.2f}")
    except FileNotFoundError:
        print("El fitxer CSV no existeix")
    except ValueError:
        print("Error en el format de les notes")

# 10. FUSIONAR FITXERS
def exercici_10():
    fitxers = ['fitxer1.txt', 'fitxer2.txt', 'fitxer3.txt']
    
    with open('fitxer_fusionat.txt', 'w', encoding='utf-8') as f_sortida:
        for nom_fitxer in fitxers:
            try:
                f_sortida.write(f"\n{'='*50}\n")
                f_sortida.write(f"CONTINGUT DE: {nom_fitxer}\n")
                f_sortida.write(f"{'='*50}\n\n")
                
                with open(nom_fitxer, 'r', encoding='utf-8') as f:
                    contingut = f.read()
                    f_sortida.write(contingut)
                    f_sortida.write('\n')
            except FileNotFoundError:
                f_sortida.write(f"[ERROR: Fitxer {nom_fitxer} no trobat]\n")
    
    print("Fitxers fusionats a 'fitxer_fusionat.txt'")

# 11. REGISTRE D'ERRORS
def exercici_11():
    try:
        comptadors = {'ERROR': 0, 'WARNING': 0, 'INFO': 0}
        
        with open('sistema.log', 'r', encoding='utf-8') as f:
            for linia in f:
                if '[ERROR]' in linia:
                    comptadors['ERROR'] += 1
                elif '[WARNING]' in linia:
                    comptadors['WARNING'] += 1
                elif '[INFO]' in linia:
                    comptadors['INFO'] += 1
        
        print("Resum del fitxer de log:")
        print(f"- Errors: {comptadors['ERROR']}")
        print(f"- Warnings: {comptadors['WARNING']}")
        print(f"- Info: {comptadors['INFO']}")
    except FileNotFoundError:
        print("El fitxer de log no existeix")

# 12. GESTIÓ DE CONTACTES
import json

def carregar_contactes():
    try:
        with open('contactes.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def guardar_contactes(contactes):
    with open('contactes.json', 'w', encoding='utf-8') as f:
        json.dump(contactes, f, ensure_ascii=False, indent=2)

def afegir_contacte(nom, telefon, email):
    contactes = carregar_contactes()
    contactes.append({'nom': nom, 'telefon': telefon, 'email': email})
    guardar_contactes(contactes)
    print(f"Contacte '{nom}' afegit correctament")

def buscar_contacte(nom):
    contactes = carregar_contactes()
    for contacte in contactes:
        if contacte['nom'].lower() == nom.lower():
            print(f"Nom: {contacte['nom']}")
            print(f"Telèfon: {contacte['telefon']}")
            print(f"Email: {contacte['email']}")
            return
    print(f"Contacte '{nom}' no trobat")

def esborrar_contacte(nom):
    contactes = carregar_contactes()
    contactes_nous = [c for c in contactes if c['nom'].lower() != nom.lower()]
    if len(contactes_nous) < len(contactes):
        guardar_contactes(contactes_nous)
        print(f"Contacte '{nom}' esborrat")
    else:
        print(f"Contacte '{nom}' no trobat")

def exercici_12():
    while True:
        print("\n=== GESTIÓ DE CONTACTES ===")
        print("1. Afegir contacte")
        print("2. Buscar contacte")
        print("3. Esborrar contacte")
        print("4. Sortir")
        opcio = input("Tria una opció: ")
        
        if opcio == '1':
            nom = input("Nom: ")
            telefon = input("Telèfon: ")
            email = input("Email: ")
            afegir_contacte(nom, telefon, email)
        elif opcio == '2':
            nom = input("Nom a buscar: ")
            buscar_contacte(nom)
        elif opcio == '3':
            nom = input("Nom a esborrar: ")
            esborrar_contacte(nom)
        elif opcio == '4':
            break

"""
EXERCICIS DE CODIFICACIÓ (amb encode i decode)
-----------------------------------------------
"""

import codecs

# 13. DETECTAR CODIFICACIÓ
def exercici_13():
    nom_fitxer = input("Nom del fitxer a analitzar: ")
    codificacions = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
    
    try:
        # Llegir els bytes del fitxer
        with open(nom_fitxer, 'rb') as f:
            bytes_fitxer = f.read()
        
        for codificacio in codificacions:
            try:
                # Intentar decodificar els bytes amb cada codificació
                text = bytes_fitxer.decode(codificacio)
                print(f"✓ La codificació {codificacio} funciona!")
                print(f"Primeres 100 caràcters: {text[:100]}")
                return
            except UnicodeDecodeError:
                print(f"✗ La codificació {codificacio} no funciona")
        
        print("No s'ha pogut detectar la codificació")
    except FileNotFoundError:
        print("El fitxer no existeix")

# 14. CONVERTIR CODIFICACIÓ
def exercici_14():
    try:
        # Llegir bytes del fitxer
        with open('text_latin1.txt', 'rb') as f:
            bytes_fitxer = f.read()
        
        # Decodificar amb latin-1 (obtenir text)
        text = bytes_fitxer.decode('latin-1')
        print(f"Text decodificat: {text}")
        
        # Codificar amb utf-8 (obtenir bytes)
        bytes_utf8 = text.encode('utf-8')
        
        # Guardar els bytes en utf-8
        with open('text_utf8.txt', 'wb') as f:
            f.write(bytes_utf8)
        
        print("Fitxer convertit de latin-1 a utf-8")
    except FileNotFoundError:
        print("El fitxer no existeix")
    except UnicodeDecodeError:
        print("Error al decodificar amb latin-1")

# 15. FITXER AMB ACCENTS
def exercici_15():
    caracters_catalans = ['à', 'è', 'é', 'í', 'ò', 'ó', 'ú', 'ç', 'ï', 'ü', '·']
    comptadors = {c: 0 for c in caracters_catalans}
    
    try:
        # Llegir bytes del fitxer
        with open('text_catala.txt', 'rb') as f:
            bytes_fitxer = f.read()
        
        # Intentar decodificar amb utf-8
        try:
            contingut = bytes_fitxer.decode('utf-8')
        except UnicodeDecodeError:
            # Si falla, provar amb latin-1
            print("⚠ UTF-8 ha fallat, provant amb latin-1...")
            contingut = bytes_fitxer.decode('latin-1')
        
        # Comptar caràcters
        for caracter in contingut.lower():
            if caracter in comptadors:
                comptadors[caracter] += 1
        
        print("Recompte de caràcters especials catalans:")
        for caracter, quantitat in comptadors.items():
            if quantitat > 0:
                print(f"  {caracter}: {quantitat}")
                
    except FileNotFoundError:
        print("El fitxer no existeix")

# 16. NETEJA DE CODIFICACIÓ
def exercici_16():
    nom_fitxer = input("Nom del fitxer a netejar: ")
    
    try:
        # Llegir bytes del fitxer
        with open(nom_fitxer, 'rb') as f:
            bytes_fitxer = f.read()
        
        # Amb 'replace' - substitueix per '?'
        text_replace = bytes_fitxer.decode('utf-8', errors='replace')
        bytes_replace = text_replace.encode('utf-8')
        
        with open('fitxer_net_replace.txt', 'wb') as f:
            f.write(bytes_replace)
        print("Fitxer netejat amb 'replace' guardat")
        print(f"Mostra: {text_replace[:100]}")
        
        # Amb 'ignore' - elimina els caràcters problemàtics
        text_ignore = bytes_fitxer.decode('utf-8', errors='ignore')
        bytes_ignore = text_ignore.encode('utf-8')
        
        with open('fitxer_net_ignore.txt', 'wb') as f:
            f.write(bytes_ignore)
        print("\nFitxer netejat amb 'ignore' guardat")
        print(f"Mostra: {text_ignore[:100]}")
        
        print(f"\nDiferència de mida: {len(text_replace)} vs {len(text_ignore)} caràcters")
        
    except FileNotFoundError:
        print("El fitxer no existeix")

# 17. COMPARAR CODIFICACIONS
def exercici_17():
    nom_fitxer = input("Nom del fitxer: ")
    
    try:
        # Llegir bytes del fitxer
        with open(nom_fitxer, 'rb') as f:
            bytes_fitxer = f.read()
        
        # Decodificar amb UTF-8
        try:
            text_utf8 = bytes_fitxer.decode('utf-8')
            print("=== CONTINGUT AMB UTF-8 ===")
            print(text_utf8[:200])
        except UnicodeDecodeError:
            print("=== UTF-8 ===")
            print("Error al decodificar amb UTF-8")
            text_utf8 = None
        
        # Decodificar amb Latin-1
        text_latin1 = bytes_fitxer.decode('latin-1')  # latin-1 sempre funciona
        print("\n=== CONTINGUT AMB LATIN-1 ===")
        print(text_latin1[:200])
        
        # Comparar
        if text_utf8 and text_utf8 != text_latin1:
            print("\n⚠ Hi ha diferències entre les dues codificacions!")
            print(f"UTF-8: {len(text_utf8)} caràcters")
            print(f"Latin-1: {len(text_latin1)} caràcters")
        elif text_utf8:
            print("\n✓ El contingut és idèntic")
            
    except FileNotFoundError:
        print("El fitxer no existeix")

# 18. FITXER MULTIIDIOMA
def exercici_18():
    fitxers = ['text_catala.txt', 'multiidioma.txt']
    
    contingut_total = []
    
    for nom_fitxer in fitxers:
        try:
            # Llegir bytes
            with open(nom_fitxer, 'rb') as f:
                bytes_fitxer = f.read()
            
            # Intentar amb diferents codificacions
            text = None
            codificacio_usada = None
            
            for enc in ['utf-8', 'latin-1', 'cp1252']:
                try:
                    text = bytes_fitxer.decode(enc)
                    codificacio_usada = enc
                    break
                except UnicodeDecodeError:
                    continue
            
            if text:
                contingut_total.append(f"\n{'='*50}\n")
                contingut_total.append(f"Fitxer: {nom_fitxer} (codificació: {codificacio_usada})\n")
                contingut_total.append(f"{'='*50}\n\n")
                contingut_total.append(text)
                contingut_total.append('\n')
                
        except FileNotFoundError:
            contingut_total.append(f"[Fitxer {nom_fitxer} no trobat]\n")
    
    # Guardar tot en UTF-8
    text_final = ''.join(contingut_total)
    bytes_final = text_final.encode('utf-8')
    
    with open('multiidioma_utf8.txt', 'wb') as f:
        f.write(bytes_final)
    
    print("Fitxers multiidioma consolidats en UTF-8")

# 19. REPARAR BOM
def exercici_19():
    try:
        # Llegir bytes del fitxer
        with open('text_amb_bom.txt', 'rb') as f:
            bytes_fitxer = f.read()
        
        # Verificar si té BOM
        if bytes_fitxer[:3] == b'\xef\xbb\xbf':
            print("✓ El fitxer original té BOM UTF-8: \\xef\\xbb\\xbf")
            # Eliminar els 3 primers bytes (el BOM)
            bytes_sense_bom = bytes_fitxer[3:]
        else:
            print("✗ El fitxer NO té BOM")
            bytes_sense_bom = bytes_fitxer
        
        # Decodificar el text
        text = bytes_sense_bom.decode('utf-8')
        
        # Guardar sense BOM (codificar normalment amb utf-8)
        bytes_final = text.encode('utf-8')
        with open('text_sense_bom.txt', 'wb') as f:
            f.write(bytes_final)
        
        print("Fitxer guardat sense BOM")
        
        # Verificar el nou fitxer
        with open('text_sense_bom.txt', 'rb') as f:
            bytes_nou = f.read(3)
            if bytes_nou != b'\xef\xbb\xbf':
                print("✓ El fitxer nou NO té BOM")
            
    except FileNotFoundError:
        print("El fitxer no existeix")
    except UnicodeDecodeError:
        print("Error al decodificar el fitxer")

# 20. ERRORS AMB REPLACE
def exercici_20():
    nom_fitxer = input("Nom del fitxer: ")
    
    try:
        # Llegir bytes del fitxer
        with open(nom_fitxer, 'rb') as f:
            bytes_fitxer = f.read()
        
        # Decodificar amb 'replace'
        text_replace = bytes_fitxer.decode('utf-8', errors='replace')
        
        # Decodificar amb 'ignore'
        text_ignore = bytes_fitxer.decode('utf-8', errors='ignore')
        
        print("=== AMB errors='replace' ===")
        print(text_replace[:300])
        print(f"\nLongitud: {len(text_replace)} caràcters")
        print(f"Nombre de '�' (caràcters substituïts): {text_replace.count('�')}")
        
        print("\n=== AMB errors='ignore' ===")
        print(text_ignore[:300])
        print(f"\nLongitud: {len(text_ignore)} caràcters")
        
        diferencia = len(text_replace) - len(text_ignore)
        if diferencia > 0:
            print(f"\n⚠ 'replace' té {diferencia} caràcters més (els '�' substituïts)")
        else:
            print("\n✓ No hi ha diferències - el fitxer és UTF-8 vàlid")
        
    except FileNotFoundError:
        print("El fitxer no existeix")

# Menú principal per provar els exercicis
def menu_principal():
    print("\n=== SOLUCIONS EXERCICIS DE FITXERS ===")
    print("Tria un exercici per executar (1-20) o 0 per sortir:")
    
    exercicis = {
        1: exercici_1, 2: exercici_2, 3: exercici_3, 4: exercici_4,
        5: exercici_5, 6: exercici_6, 7: exercici_7, 8: exercici_8,
        9: exercici_9, 10: exercici_10, 11: exercici_11, 12: exercici_12,
        13: exercici_13, 14: exercici_14, 15: exercici_15, 16: exercici_16,
        17: exercici_17, 18: exercici_18, 19: exercici_19, 20: exercici_20
    }
    
    while True:
        try:
            opcio = int(input("\nExercici: "))
            if opcio == 0:
                break
            elif opcio in exercicis:
                print(f"\n--- Executant exercici {opcio} ---")
                exercicis[opcio]()
            else:
                print("Número d'exercici no vàlid")
        except ValueError:
            print("Si us plau, introdueix un número")
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    menu_principal()

# 21. ROT13 - Xifrat simple
def exercici_21():
    """
    ROT13 és un xifrat simple que desplaça cada lletra 13 posicions.
    Amb codecs.encode i codecs.decode és molt fàcil!
    """
    text = input("Escriu un text per xifrar amb ROT13: ")
    
    # Xifrar amb ROT13 (només funciona amb text, no bytes)
    text_xifrat = codecs.encode(text, 'rot13')
    print(f"Text xifrat: {text_xifrat}")
    
    # Desxifrar (ROT13 és reversible aplicant-lo dues vegades)
    text_desxifrat = codecs.decode(text_xifrat, 'rot13')
    print(f"Text desxifrat: {text_desxifrat}")
    
    # Guardar en un fitxer
    with open('text_rot13.txt', 'w', encoding='utf-8') as f:
        f.write(f"Original: {text}\n")
        f.write(f"Xifrat: {text_xifrat}\n")
    
    print("Resultat guardat a 'text_rot13.txt'")

# 22. HEX - Representació hexadecimal
def exercici_22():
    """
    Convertir text a representació hexadecimal i viceversa.
    Útil per veure els bytes d'un text.
    """
    text = input("Escriu un text (amb accents si vols): ")
    
    # Primer convertim text a bytes
    bytes_text = text.encode('utf-8')
    print(f"Bytes UTF-8: {bytes_text}")
    
    # Codificar a hexadecimal
    hex_text = codecs.encode(bytes_text, 'hex')
    print(f"Hexadecimal: {hex_text.decode('ascii')}")
    
    # Decodificar des de hexadecimal
    bytes_recuperats = codecs.decode(hex_text, 'hex')
    text_recuperat = bytes_recuperats.decode('utf-8')
    print(f"Text recuperat: {text_recuperat}")
    
    # Exemple amb caràcter català
    print("\n--- Exemple amb 'ç' ---")
    c_bytes = 'ç'.encode('utf-8')
    c_hex = codecs.encode(c_bytes, 'hex')
    print(f"'ç' en UTF-8: {c_bytes}")
    print(f"'ç' en hexadecimal: {c_hex.decode('ascii')}")

# 23: Codificació ROT13
def encriptar_rot13(text):
    """
    Encripta text utilitzant ROT13
    """
    # ROT13 és una codificació que rota les lletres 13 posicions
    # A->N, B->O, ..., N->A, O->B, etc.
    # És reversible: aplicar ROT13 dues vegades retorna l'original
    text_encriptat = codecs.encode(text, 'rot_13')
    return text_encriptat


# 24: Decodificació ROT13
def desencriptar_rot13(text_encriptat):
    """
    Desencripta text ROT13
    """
    # Com que ROT13 és simètric, desencriptar és igual que encriptar
    # Podem usar encode o decode, el resultat és el mateix
    text_original = codecs.decode(text_encriptat, 'rot_13')
    return text_original

# 25. PROCESSAR UN FITXER (ROT13)
def processar_document(fitxer_entrada, fitxer_sortida) -> str:
    try:
        with open(fitxer_entrada, 'r', encoding='utf-8') as file:
            contingut = file.readlines()
        
        # Desxifrar cada línia amb ROT13
        # La següent línia ens decodifica utilitzant "rot_13", retornant una còpia amb espais eliminats
        contingut_desxifrat = [codecs.decode(linia.strip(), 'rot_13') for linia in contingut if linia.strip()]
        
        # Ordenar alfabèticament
        contingut_ordenat = sorted(contingut_desxifrat)
        
        # Mostrar per pantalla
        print("Linies desxifrades i ordenades:")
        for linia in contingut_ordenat:
            print(f"  {linia}")
        
        # Guardar al fitxer de sortida
        with open(fitxer_sortida, 'w', encoding='utf-8') as file_w:
            for linia in contingut_ordenat:
                file_w.write(linia + '\n')
        
        print(f"\n✓ Document processat i guardat a '{fitxer_sortida}'")
        return fitxer_sortida
        
    except FileNotFoundError:
        print(f"Error: El fitxer '{fitxer_entrada}' no existeix!")
        raise
    except Exception as e:
        print(f"Error inesperat: {e}")
        raise