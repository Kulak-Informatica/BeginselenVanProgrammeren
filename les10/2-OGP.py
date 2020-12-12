# WAS BUSY WITH SOMETHIN ELSE JOINED LATE DIDN'T HAV TIME FOR 1 SOZ

class Prison:
    def __init__(self, cells, prisoners):
        self.cells = cells
        self.prisoners = prisoners

    def get_prisoners(self):
        return self.prisoners

    def get_cells(self):
        return self.cells

    def add_prisoners(self, prisoners):
        if type(prisoners) == Prisoner:
            self.prisoners.append(prisoners)
        else:
            self.prisoners.extend(prisoners)

    def release_prisoner(self, prisoner):
        self.prisoners.remove(prisoner)


class Prisoner:
    def __init__(self, name, cell, diet, visitorsdays, prisoner_id, internet_access):
        self.name = name
        self.cell = cell
        self.diet = diet
        self.visitorsdays = visitorsdays
        self.prisoner_id = prisoner_id
        self.internet_access = internet_access

    def get_name(self):
        return self.name

    def get_cell(self):
        return self.cell

    def get_diet(self):
        return self.diet

    def get_visitorsdays(self):
        return self.visitorsdays

    def get_internet_access(self):
        return self.internet_access

    def set_internet_acces(self, internet_access=-1):
        if internet_access == -1:
            self.internet_access = not self.internet_access
        elif type(internet_access) != bool:
            raise TypeError("internet_access should be bool or not specified")
        else:
            self.internet_access = internet_access

    def __repr__(self):
        return "Prisoner [" + self.prisoner_id + "]: " + self.name


class Cell:
    cell_id = 0

    def __init__(self, size, internet_connection, prisoners):
        if size not in (4, 6, 8):
            raise ValueError("Cell does not have valid size of 4, 6 or 8")
        self.size = size
        self.internet_connection = internet_connection
        self.cell_id = Cell.cell_id
        Cell.cell_id += 1
        self.prisoners = prisoners

    def get_size(self):
        return self.size

    def get_internetconnection(self):
        return self.internet_connection

    def __repr__(self):
        return f"Cell {self.cell_id:03d}"
