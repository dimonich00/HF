from pyscf import gto, scf


def run_pyscf(molecule, basis, method):
    """Runs a calculation using PySCF."""

    mol = gto.M(atom=molecule["atoms"], charge=molecule["charge"],
                spin=molecule["multiplicity"] - 1, basis=basis)
    mf = scf.HF(mol) if method.lower() == "hf" else None
    energy = mf.kernel()
    return energy
# mol is an object to hold molecule information.
# mol = pyscf.M(
#    verbose=4,
#    output='out_h2o',
#    atom='''
#      o     0    0       0
# h     0    -.757   .587
#      h     0    .757    .587''',
#    basis='6-31g',
# )
# For more details, see pyscf/gto/mole.py and pyscf/examples/gto

#
# The package follow the convention that each method has its class to hold
# control parameters.  The calculation can be executed by the kernel function.
# Eg, to do Hartree-Fock, (1) create HF object, (2) call kernel function
# mf = mol.RHF()
# print('E(HF)=%.15g' % mf.kernel())##
