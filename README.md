# Hartree-Fock Energy Calculator for Simple Molecules

## What does this project do?

One of the primary methods in a chemist's toolkit for predicting the properties of chemical compounds is quantum-chemical calculations. These calculations are usually performed using specialized software packages (Gaussian, Orca, Gammes). There are also Python packages designed for these purposes, such as [PySCF](https://pyscf.org/index.html) and [Psi4](https://psicode.org/). However, using each of these requires knowledge of specific syntax, which can be challenging to navigate. Therefore, the goal of this project is to develop a Python wrapper that accepts an executable file containing the name of the software package to be used and the description of the method to be applied for the molecular calculation. This executable file is based on the structure of the executable files used by the Orca package, making it familiar to computational chemists.

The tool will:
- Accept input file with parameters (package, method, basis set and molecule).
- Call chosen library with parameters from input file.
- Print results in a console output or output file.

---

## What kind of input data does it expect?
- **Input file**: Examples can be found inside folder
- **Molecular structure**: A list of atoms and their 3D Cartesian coordinates (e.g., in [XYZ format](https://en.wikipedia.org/wiki/XYZ_file_format)).  

---

## What kind of output can the user expect?

- The computed energy of the molecule in atomic units (Hartree).  
- Convergence information for the SCF optimization process.  
- Optionally, a visualization of molecular orbitals and electron densities (if visualization tools are integrated).  

---

## Technologies

### Programming Language:
- Python.  

### Dependencies:
- `conda` for installation of packages
- `pyscf`, `psi4`: For numerical computations.  
- `matplotlib`: For optional visualization.  

### How to run it:
1. Clone the repository:  
   ```bash
   git clone https://github.com/dimonich00/HF.git
   cd HF
   ```
2. Install dependencies:
   ```bash
   conda install psi4 python=3.10 -c conda-forge
   conda install -c pyscf -c conda-forge pyscf
   ```

   or
     
   ```bash
   conda install -c requirements.txt
   ```
4. Run the tool with an input file:  

   python3 GLHF.py /path/to/input/file

   Molecular geometry can be specified insida an input file (see test.input or test2.input) or added as a link using "path:path/to/file/" (see test3.input)

---

## Why is this project useful?

This tool simplifies interaction with python-based quantum packages and allows to easily use them for chemists who usually use classical quantum chemistry programs 

---

## Acknowledgments

This project was developed as part of the course WIS Python course. For more information, visit the course repository [https://github.com/szabgab/wis-python-course-2024-11].
