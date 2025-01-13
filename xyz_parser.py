def parse(filename):
    try:
        with open(filename, "r") as file:
            number_of_atoms = 0
            atom_types = []
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
                    split = line.split()
                    atom = split[0]
                    coordinates = [float(split[1]), float(
                        split[2]), float(split[3])]

                    atom_types.append(atom)
                    atom_coordinates.append(coordinates)

    except FileNotFoundError:
        print("File not found")
        exit()

    return number_of_atoms, atom_types, atom_coordinates
