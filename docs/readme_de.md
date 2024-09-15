# 🧬 Turing-Maschine Genom-Prozessor 🦠

**Translations in**
[Español](https://github.com/jero98772/Turing-Machine-Genome-Processor/blob/main/docs/readme_es.md)
[Deutsch](https://github.com/jero98772/Turing-Machine-Genome-Processor/blob/main/docs/readme_de.md) 


Willkommen beim **Turing-Maschine Genom-Prozessor**! Dieses Projekt simuliert eine TuringMaschine, die durch GenomSequenzen navigiert und auf Basis von Start- und Stopp-Codons verarbeitet. Es ist dafür konzipiert, mit Sequenzen im FASTA-Format zu arbeiten. 🚀

## 📝 Funktionen
- Liest GenomSequenzen aus FASTA-Dateien 📄.
- Verarbeitet die Sequenzen mit einem Turing-Maschinen-Ansatz und berücksichtigt Start-Codons (`ATG`, `AUG`) und Stopp-Codons (`UAA`, `UAG`, `UGA`) 🔬.
- Bewegt sich durch das Genom-Band, führt Befehle aus und ändert den Speicher basierend auf Nukleotid-Sequenzen 🎛️.

## Nützliche Sachen

- Es gibt eine Datei zum Generieren zufälliger DNA oder RNA.
- Es gibt Testdaten im `data/`-Ordner.

## 🚀 Wie man es ausführt

1. **Klone das Repository**:
   ```bash
   git clone https://github.com/jero98772/Turing-Machine-Genome-Processor.git
   cd Turing-Machine-Genome-Processor/
   ```

2. **Bereite eine FASTA-Datei vor**: Du brauchst eine FASTA-Datei, die die Genom-Sequenzen enthält, die du verarbeiten möchtest. Jede Sequenz sollte im Standard-FASTA-Format vorliegen:
   ```
   >sequence1
   ATGCGT...
   >sequence2
   ATGTTG...
   ```

3. **Führe das Programm aus**:
   Du kannst das Programm ausführen, indem du den Pfad zur FASTA-Datei übergibst:
   ```bash
   python main.py deine_genom_datei.fasta
   ```

   Beispiel:
   ```bash
   python main.py data/mouse_rRNAs.fa 
   ```

4. **Programmausgabe**:
   - Nach der Ausführung siehst du den Endzustand des **Bands** (Speicher) und die Position des **Zeigers**.
   - Das Band zeigt, wie die Genom-Sequenzen von der Turing-Maschine verarbeitet wurden 🧠.

## 🛠️ Anforderungen

- Python 3.6 oder höher 🐍.
- Eine Genom-Sequenz im FASTA-Format 📜. (siehe Beispiel-Daten im Ordner `data`)

## 💻 Argumente

- **fasta_file**: Pfad zur FASTA-Datei, die die Genom-Sequenzen enthält, die von der Turing-Maschine verarbeitet werden sollen.

## ⚙️ So funktioniert es

Es ist ähnlich wie [Brainfuck](https://de.wikipedia.org/wiki/Brainfuck)

- Die Turing-Maschine startet am ersten Codon und bewegt sich durch das Genom, indem sie Anweisungen auf Grundlage der Nukleotid-Buchstaben befolgt:
  - `A`, `T`, `U`: Bewegt den Zeiger zur nächsten Position auf dem Band.
  - `C`: Erhöht den Wert an der aktuellen Bandposition.
  - `G`: Verringert den Wert an der aktuellen Bandposition.

- Start-Codons (`ATG`/`AUG`) markieren den Beginn einer Schleife, während Stopp-Codons (`UAA`, `UAG`, `UGA`, etc.) das Ende der Schleife anzeigen. Wenn die Maschine auf ein Stopp-Codon stößt, während der Speicherzeiger einen Wert ungleich null hat, springt sie zurück zum Start-Codon.

Ich benutze `C` und `G` zum Verringern/Erhöhen des Wertes, weil das Verhalten des Skew-Diagramms auf der Information von Cytosin und Guanin basiert, um die Replikationsposition zu finden.

## 👩‍💻 Beispiel

Hier ist eine Beispielausgabe, wenn die Turing-Maschine mit einer kleinen FASTA-Datei ausgeführt wird:
```bash
python main.py example.fasta
Band nach der Verarbeitung: [0, 1, 1, 0, 2, 0, 0, 0, 0, 0]
Zeigerposition: 5
```

## 🔍 Den Code erkunden

- **`read_fasta(file_path)`**: Diese Funktion liest die FASTA-Datei und gibt ein Wörterbuch mit Sequenzüberschriften und den jeweiligen Nukleotid-Sequenzen zurück 🧬.
- **`TuringMachine`**: Die Hauptklasse, die für die Verarbeitung von Genom-Sequenzen mit der Turing-Maschinen-Logik verantwortlich ist 💡.
- **`load_program(program)`**: Lädt die Genom-Sequenz in die Turing-Maschine.
- **`run()`**: Führt das Programm aus, indem es sich durch das Genom bewegt und entsprechend das Band und den Zeiger anpasst.

## 🧪 Beitrag

Du kannst gerne Issues eröffnen oder Pull-Requests einreichen! Beiträge sind willkommen, um die Funktionalität der Maschine zu erweitern oder die Leistung zu optimieren 💡.

## 🧬 Danksagungen

Dieses Projekt ist inspiriert von der faszinierenden Welt der Genomik und Turing-Maschinen. Erstellt von [jero98772](https://github.com/jero98772)  🌟.

---

Viel Spaß beim Verarbeiten von Genomen mit deiner eigenen TuringMaschine! 🎉

