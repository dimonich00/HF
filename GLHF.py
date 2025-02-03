import xyz_parser
import pyscf_run
import psi4_run
import argparse


def input_parse(file_path):
    """Parses an ORCA type input file to extract package, method, basis, charge, multiplicity, and molecular geometry."""
    with open(file_path, "r") as f:
        lines = f.readlines()

    package = None
    method, basis = None, None
    charge, multiplicity = None, None
    atoms = []

    for line in lines:
        line = line.strip()
        if line.startswith("# package:"):  # Extract package (pyscf or psi4)
            package = line.split(":")[1].strip().lower()
        elif line.startswith("!"):  # Extract method and basis set
            tokens = line.lstrip("!").split()
            method, basis = tokens[0].lower(), tokens[1] if len(
                tokens) > 1 else None
        elif line.startswith("* xyz"):  # Extract charge and multiplicity
            parts = line.split()
            charge, multiplicity = int(parts[2]), int(parts[3])
        elif line.startswith("*"):  # End of molecule section
            break
        elif line.startswith("path:"):
            path = line.split(":")[1]
            atoms = xyz_parser.parse(path)

        elif charge is not None:  # Capture atom coordinates
            atoms.append(line)

    if not package or not method or not basis or charge is None or multiplicity is None:
        raise ValueError("Invalid input file format.")

    # Convert atoms list into a formatted string
    molecule_str = "; ".join(atoms)
    return {
        "package": package,
        "method": method,
        "basis": basis,
        "charge": charge,
        "multiplicity": multiplicity,
        "atoms": molecule_str
    }


def main():
    parser = argparse.ArgumentParser(
        description="Run quantum chemistry calculations using PySCF or Psi4 from input file.")
    parser.add_argument(
        "input_file", help="Path to the ORCA input file (.inp)")
    args = parser.parse_args()

    # Parse ORCA input file
    data = input_parse(args.input_file)

    print(
        f"Running {data['method'].upper()} calculation with {data['package'].upper()}...")

    # Run the calculation with the specified package
    if data["package"] == "pyscf":
        energy = pyscf_run.run_pyscf(data, data["basis"], data["method"])
    elif data["package"] == "psi4":
        energy = psi4_run.run_psi4(data, data["basis"], data["method"])
    else:
        raise ValueError(
            "Invalid package. Choose 'pyscf' or 'psi4' in the input file.")

    print(f"Final {data['method'].upper()} energy: {energy:.6f} Hartree")


if __name__ == "__main__":
    main()
