
# 📦 Sårbarhetssjekk for Debian Bookworm-pakker

## 👨‍💻 Laget av

Dette skriptet er utviklet av **Tarek Somak**.

## Introduksjon
Dette programmet er utviklet for å finne sårbare pakker i **Debian Bookworm** ved hjelp av **Open Source Vulnerabilities (OSV)**-databasen.  
Programmet analyserer pakkelisten for **amd64-arkitekturen** fra **main-repositoriet**, og sjekker hver pakke for kjente sårbarheter via OSV sitt API.

---

## 🚀 Hva programmet gjør

1. **Input**  
   Brukeren legger til en pakkeliste i prosjektmappen, som en fil kalt **Packages**.

2. **Analyse**  
   Programmet leser og tolker informasjon om hver pakke (navn og versjon) fra filen.

3. **Sårbarhetssjekk**  
   For hver pakke sjekker programmet om den har kjente sårbarheter ved å sende spørringer til OSV-databasen.

4. **Resultater**  
   Programmet returnerer følgende informasjon for hver pakke:
   - Navn og versjonsnummer.
   - Om pakken er sårbar eller ikke.
   - Hvis sårbar: CVE-ID og dato for siste oppdatering (hentet fra OSV).

5. **Output**  
   Resultatene lagres i en fil kalt **Resultat.txt**, som inneholder oversikt over både sårbare og ikke-sårbare pakker.

---

## 🧹 Filtrering av sårbare pakker

Hvis du **kun ønsker å se sårbare pakker**, kan du bruke følgende Linux-kommando for å filtrere resultatene:

```bash
grep -E "Package:|Vulnerabilities found:|CVE ID:" Resultat.txt | grep -v "has no known vulnerabilities" | grep -v "^$" > Vulnerable_Packages_Detailed.txt
```

Denne kommandoen vil:
- Filtrere ut linjer relatert til sårbare pakker.
- Ekskludere pakker uten kjente sårbarheter.
- Lagre resultatet i en ny fil kalt **Vulnerable_Packages_Detailed.txt**.

### 📊 Finne antall sårbare pakker

For å telle antall sårbare pakker, bruk følgende kommando:

```bash
grep -c "Package:" Vulnerable_Packages_Detailed.txt
```

Eksempel:  
> Resultatet kan f.eks. vise `541`, som betyr at 541 pakker er sårbare.  
Lykke til med å gå gjennom dem!

---

## ⚙️ Hvordan kjøre programmet?

1. **Legg inn stien til `Packages`-filen** i hovedfunksjonen i Python-koden (linje **48**).  
   Eksempel:
   ```python
   file_path = 'Packages'  # Endre denne hvis filen ligger et annet sted
   ```

2. **Kjør skriptet** med kommandoen:
   ```bash
   python3 vulns_in_Worm.py
   ```

3. **Resultater lagres** i en fil kalt **Resultat.txt** i prosjektmappen.

4. For en **filtrert oversikt over kun sårbare pakker**, bruk kommandoen nevnt over.


