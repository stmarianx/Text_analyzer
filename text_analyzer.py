#!/usr/bin/env python3

import sys
import re
from collections import Counter

def main():
    if len(sys.argv) < 2:
        print("Utilizare: python text_analyzer.py <cale_catre_fisier.txt>")
        sys.exit(1)

    fisier_intrare = sys.argv[1]

    # 1. Citim textu
    try:
        with open(fisier_intrare, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Eroare: Fisierul '{fisier_intrare}' nu a fost gasit.")
        sys.exit(1)

    # 2. numarul de cuvinte
    cuvinte = re.findall(r'\S+', text)
    numar_cuvinte = len(cuvinte)

    # 3. numarul de propozitii
    propozitii = re.split(r'[.!?]+', text)
    propozitii = [p.strip() for p in propozitii if p.strip()]   # eliminam spatiile
    numar_propozitii = len(propozitii)

    # 4. CNP-urile (13 cifre consecutive).
    cnp_pattern = r'\b\d{13}\b'
    cnp_gasite = re.findall(cnp_pattern, text)
    cnp_unice = set(cnp_gasite)

    # 5. 07 (urmate de 8 cifre)
    phone_pattern = r'\b07\d{8}\b'
    telefoane_gasite = re.findall(phone_pattern, text)
    telefoane_unice = set(telefoane_gasite)

    # 6. Statistica pentru fiecare litera
    litere = re.findall(r'[a-zA-Z]', text)
    numar_total_litere = len(litere)
    counter_litere = Counter(ch.lower() for ch in litere)

    # 7. Afisare rezultate
    print(f"Cuvinte = {numar_cuvinte}")
    print(f"Propozitii = {numar_propozitii}")

    print(f"CNP(uri) = {len(cnp_unice)} {list(cnp_unice)}")
    print(f"Telefoane = {len(telefoane_unice)} {list(telefoane_unice)}")

    print("Litere:")
    for litera in sorted(counter_litere):
        numar_aparitii = counter_litere[litera]
        procent = (numar_aparitii / numar_total_litere) * 100 if numar_total_litere else 0
        print(f"   {litera.upper()} = {numar_aparitii} ({procent:.2f}%)")


if __name__ == "__main__":
    main()
