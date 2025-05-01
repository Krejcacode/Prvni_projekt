"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Martin Krejčiřík
email: krejcirikmartin9@gmail.com
"""


# Import modulu pro odstranění interpunkce
import string


# Seznam textů k analýze
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]


# Slovník s přihlašovacími údaji
uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Oddělovač pro vizuální přehlednost
odelovac = "-" * 50

# Přihlášení uživatele
uzivatelske_jmeno = input("Zadej své uživatelské jméno: ")
heslo = input("Zadej své heslo: ")
print(odelovac)

# Počet textů pro výběr uživatele
pocet_textu = len(TEXTS)

# Kontrola přihlašovacích údajů
if uzivatelske_jmeno in uzivatele and uzivatele[uzivatelske_jmeno] == heslo:
    print(f"Vítej v aplikaci, {uzivatelske_jmeno}")
    print(f"Máme {pocet_textu} texty k analýze.")
    print(odelovac)
    
     # Výběr textu
    volba_textu = input(f"Vyber si číslo textu mezi 1 a {pocet_textu}, který chceš analyzovat:  ")
    
    # Kontrola volby textu a případné ukončení programu
    if not volba_textu.isdigit() or int(volba_textu) not in range(1,pocet_textu + 1):
        print("Zadal jste vstup, který nebyl ve volbě. Ukončuji program ..")
        exit()
    
    # Převedení volby textu na číslo a výběr textu
    volba_textu = int(volba_textu)
    vybrany_text = TEXTS[volba_textu - 1]
    
    # Očištění textu od interpunkce 
    slova_textu = [slovo.strip(string.punctuation) for slovo in vybrany_text.split()]

    # Přehled statistik slov
    statistiky_textu = {
        "titlecase_slova": 0,
        "uppercase_slova": 0,
        "lowercase_slova": 0,
        "numeric_slova": 0,
        "suma_stringu": 0
    }
    # Slovník pro uchování četnosti dle délky slova
    cetnosti = {}

    # Analýza slov
    for slovo in slova_textu:
        if slovo.istitle():
            statistiky_textu["titlecase_slova"] += 1
        elif slovo.isupper() :
            statistiky_textu["uppercase_slova"] += 1
        elif slovo.islower():
            statistiky_textu["lowercase_slova"] += 1
        elif slovo.isnumeric() :
            statistiky_textu["numeric_slova"] += 1
            statistiky_textu["suma_stringu"] += int(slovo)
        
        # Výpočet četnosti dle délky slova
        delka = len(slovo)
        if delka in cetnosti:
            cetnosti[delka] += 1
        else:
            cetnosti[delka] = 1
    
    # Výpis počtu slov
    pocet_slov = len(slova_textu)
    print(f"Je zde {pocet_slov} slov ve vybraném textu")
    
    # Výpis statistik slov
    print(f"Je zde {statistiky_textu['titlecase_slova']} slov začínajících velkým písmenem.")
    print(f"Je zde {statistiky_textu['uppercase_slova']} slov psaných velkými písmeny.")
    print(f"Je zde {statistiky_textu['lowercase_slova']} slov psaných malými písmeny.")
    print(f"Počet čísel: {statistiky_textu['numeric_slova']}")
    print(f"Součet všech čísel: {statistiky_textu['suma_stringu']}")
    print(odelovac)
    
    # Výpis grafu četnosti délek slov
    print("Délka| Výskyty           | Počet")
    print(odelovac)
    for delka in sorted(cetnosti):
        pocet = cetnosti[delka]
        print(f"{delka:<5}| {'*' * pocet:<18}| {pocet:<5}")

# Ukončení programu v případě neplatného uživatelského jména nebo hesla
else :
    print("Neregistrovaný uživatel, ukončuji program ..")
