# 🧬 Procesador de Genomas con Máquina de Turing 🦠

**Traducciones en:**
[Español](https://github.com/Semillero-Inteligencia-Artificial-EAFIT/airedellin/blob/main/docs/readme_es.md)
[Deutsch](https://github.com/Semillero-Inteligencia-Artificial-EAFIT/airedellin/blob/main/docs/readme_de.md) 

¡Bienvenido al **Procesador de Genomas con Máquina de Turing**! Este proyecto simula una Máquina de Turing que navega por secuencias genómicas, procesando con base en codones de inicio y de parada. Está diseñado para trabajar con secuencias en formato FASTA. 🚀

## 📝 Características
- Lee secuencias genómicas desde archivos FASTA 📄.
- Procesa las secuencias usando un enfoque de Máquina de Turing, respetando los codones de inicio (`ATG`, `AUG`) y los codones de parada (`UAA`, `UAG`, `UGA`) 🔬.
- Se mueve a través de la cinta del genoma, ejecutando comandos y modificando la memoria en función de las secuencias de nucleótidos 🎛️.

## Cosas útiles

- Hay un archivo para generar ADN o ARN aleatorio.
- Hay datos de prueba en la carpeta `data/`.

## 🚀 Cómo Ejecutar

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/jero98772/Turing-Machine-Genome-Processor.git
   cd Turing-Machine-Genome-Processor/
   ```

2. **Prepara un archivo FASTA**: Necesitas un archivo FASTA que contenga las secuencias genómicas que deseas procesar. Cada secuencia debe estar en formato FASTA estándar:
   ```
   >sequence1
   ATGCGT...
   >sequence2
   ATGTTG...
   ```

3. **Ejecuta el programa**:
   Puedes ejecutar el programa pasando la ruta del archivo FASTA:
   ```bash
   python main.py tu_archivo_genoma.fasta
   ```

   Ejemplo:
   ```bash
   python main.py data/mouse_rRNAs.fa 
   ```

4. **Salida del programa**:
   - Después de ejecutarse, verás el estado final de la **cinta** (memoria) y la posición del **puntero**.
   - La cinta mostrará cómo las secuencias genómicas fueron procesadas por la Máquina de Turing 🧠.

## 🛠️ Requisitos

- Python 3.6 o superior 🐍.
- Una secuencia genómica en formato FASTA 📜. (consulta los datos de ejemplo en la carpeta `data`)

## 💻 Argumentos

- **fasta_file**: Ruta del archivo FASTA que contiene las secuencias genómicas a procesar por la Máquina de Turing.

## ⚙️ Cómo Funciona

Es similar a [Brainfuck](https://es.wikipedia.org/wiki/Brainfuck)

- La Máquina de Turing comienza en el primer codón y se mueve a través del genoma siguiendo instrucciones basadas en las letras de los nucleótidos:
  - `A`, `T`, `U`: Mueve el puntero a la siguiente posición en la cinta.
  - `C`: Aumenta el valor en la posición actual de la cinta.
  - `G`: Disminuye el valor en la posición actual de la cinta.

- Los codones de inicio (`ATG`/`AUG`) marcan el comienzo de un bucle, mientras que los codones de parada (`UAA`, `UAG`, `UGA`, etc.) indican el final del bucle. Si la máquina encuentra un codón de parada mientras el puntero de memoria tiene un valor distinto de cero, vuelve al codón de inicio.

Utilizo `C` y `G` para aumentar/disminuir el valor debido al comportamiento del diagrama de sesgo basado en la información de la citocina y guanina para encontrar la posición de replicación.

## 👩‍💻 Ejemplo

Aquí tienes una salida de ejemplo al ejecutar la Máquina de Turing con un pequeño archivo FASTA:
```bash
python main.py example.fasta
Cinta después del procesamiento: [0, 1, 1, 0, 2, 0, 0, 0, 0, 0]
Posición del puntero: 5
```

## 🔍 Explorando el Código

- **`read_fasta(file_path)`**: Esta función lee el archivo FASTA y devuelve un diccionario con los encabezados de secuencia y sus respectivas secuencias de nucleótidos 🧬.
- **`TuringMachine`**: La clase principal responsable de procesar las secuencias genómicas usando la lógica de la Máquina de Turing 💡.
- **`load_program(program)`**: Carga la secuencia genómica en la Máquina de Turing.
- **`run()`**: Ejecuta el programa moviéndose a través del genoma, ajustando la cinta y el puntero según corresponda.

## 🧪 Contribuciones

¡Siéntete libre de abrir issues o enviar pull requests! Las contribuciones son bienvenidas para expandir la funcionalidad de la máquina o mejorar el rendimiento 💡.

## 🧬 Créditos

Este proyecto está inspirado en el fascinante mundo de la genómica y las Máquinas de Turing. Creado por [jero98772](https://github.com/jero98772)  🌟.

---

¡Disfruta procesando genomas con tu propia Máquina de Turing! 🎉