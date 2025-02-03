def parse(filename):
    try:
        with open(filename, "r") as file:
            number_of_atoms = 0
            atom_coordinates = []

            for idx, line in enumerate(file):
                if idx == 0:
                    try:
                        number_of_atoms = int(line.strip())
                    except ValueError:
                        print("Wrong XYZ file structure")
                        exit()
                if idx == 1:
                    continue

                if idx != 0:
                    atom_coordinates.append(line.strip())

    except FileNotFoundError:
        print("File not found")
        exit()

    return atom_coordinates
