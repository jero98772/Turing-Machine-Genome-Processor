# 🧬 Turing Machine Genome Processor 🦠

**Translations in**
[Español](https://github.com/jero98772/Turing-Machine-Genome-Processor/blob/main/docs/readme_es.md)
[Deutsch](https://github.com/jero98772/Turing-Machine-Genome-Processor/blob/main/docs/readme_de.md) 

Welcome to the **Turing Machine Genome Processor**! This project simulates a Turing Machine that navigates through genome sequences, processing based on start and stop codons. It's designed to work on sequences provided in FASTA format. 🚀

## 📝 Features
- Reads genome sequences from FASTA files 📄.
- Processes the sequences using a Turing Machine approach, respecting start codons (`ATG`, `AUG`) and stop codons (`UAA`, `UAG`, `UGA`) 🔬.
- Moves through the genome tape, executing commands and modifying memory based on nucleotide sequences 🎛️.

## Util stuff

there is a file for generate random dna, or rna 

there is data, for test this in data/ folder

## 🚀 How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/jero98772/Turing-Machine-Genome-Processor.git
   cd Turing-Machine-Genome-Processor/
   ```

2. **Prepare a FASTA file**: You need a FASTA file containing the genome sequences that you want to process. Each sequence should be in standard FASTA format:
   ```
   >sequence1
   ATGCGT...
   >sequence2
   ATGTTG...
   ```

3. **Run the program**:
   You can execute the program by passing the path to the FASTA file:
   ```bash
   python main.py your_genome_file.fasta
   ```

   Example:
   ```bash
   python main.py data/mouse_rRNAs.fa 
   ```

4. **Program Output**:
   - After running, you will see the final state of the **tape** (memory) and the position of the **pointer**.
   - The tape will show how the genome sequences were processed by the Turing Machine 🧠.

## 🛠️ Requirements

- Python 3.6 or higher 🐍.
- A genome sequence in FASTA format 📜. (see example data in data folder)

## 💻 Arguments

- **fasta_file**: Path to the FASTA file that contains genome sequences to be processed by the Turing Machine.

## ⚙️ How It Works

It is like [Brainfuck](https://es.wikipedia.org/wiki/Brainfuck)

- The Turing Machine starts at the first codon and moves through the genome following instructions based on nucleotide letters:
  - `A`, `T`, `U`: Moves the pointer to the next position on the tape.
  - `C`: Increases the value at the current tape position.
  - `G`: Decreases the value at the current tape position.

- Start codons (`ATG`/`AUG`) mark the beginning of a loop, while stop codons (`UAA`, `UAG`, `UGA`, etc.) indicate the end of the loop. If the machine encounters a stop codon while the memory pointer has a non-zero value, it jumps back to the start codon.

I do use c and g for  Decreases/Increases the value because the beheivor of skew diagram is in base of the information of citocine and guanide for find the position of replication 

## 👩‍💻 Example

Here is a sample output when running the Turing Machine with a small FASTA file:
```bash
python main.py example.fasta
Tape after processing: [0, 1, 1, 0, 2, 0, 0, 0, 0, 0]
Pointer position: 5
```

## 🔍 Exploring the Code

- **`read_fasta(file_path)`**: This function reads the FASTA file and returns a dictionary with sequence headers and their respective nucleotide sequences 🧬.
- **`TuringMachine`**: The main class responsible for processing genome sequences using Turing Machine logic 💡.
- **`load_program(program)`**: Loads the genome sequence into the Turing Machine.
- **`run()`**: Executes the program by moving through the genome, adjusting the tape and pointer accordingly.

## 🧪 Contribution

Feel free to open issues or submit pull requests! Contributions are welcome to expand the machine’s functionality or optimize performance 💡.

## 🧬 Credits

This project is inspired by the fascinating world of genomics and Turing Machines. Created by [jero98772](https://github.com/jero98772) 🌟.

---

Enjoy processing genomes with your custom Turing Machine! 🎉
