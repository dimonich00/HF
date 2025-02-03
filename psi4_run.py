import psi4

psi4.set_memory('500 MB')


def run_psi4(molecule, basis, method):

    psi4.set_options({"basis": basis})
    mol_str = f"{molecule['charge']} {molecule['multiplicity']}\n" + \
        molecule["atoms"].replace(";", "\n")
    mol = psi4.geometry(mol_str)
    energy = psi4.energy(method.upper())
    return energy
