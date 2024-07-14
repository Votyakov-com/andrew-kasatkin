class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    @staticmethod
    def length_check(self, other):
        if len(self.coords) != len(other.coords):
            raise ValueError('Vectors have different length')

    def __add__(self, other):
        Vector2.length_check(self, other)
        V = (n1 + n2 for n1, n2 in zip(self.coords, other.coords))
        V = list(V)
        return Vector2(V[0], V[1])

    def __neg__(self):
        self.coords = list(self.coords)
        self.coords.reverse()
        x, y = self.coords[0], self.coords[1]
        return Vector2(x, y)

    def __sub__(self, other):
        Vector2.length_check(self, other)
        V = (n1 - n2 for n1, n2 in zip(self.coords, other.coords))
        V = list(V)
        return Vector2(V[0], V[1])

    def __abs__(self):
        return list(map(lambda n: abs(n), self.coords))

    def __str__(self):
        return f"X coordinate: {self.coords[0]}\n" + \
            f"Y coordinate: {self.coords[1]}"

    def __eq__(self, other):
        Vector2.length_check(self, other)
        if self.coords == other.coords:
            return True
        else:
            return False

    def __ne__(self, other):
        Vector2.length_check(self, other)
        if self.coords != other.coords:
            return True
        else:
            return False

    def __mul__(self, other):
        Vector2.length_check(self, other)
        V = (n1 * n2 for n1, n2 in zip(self.coords, other.coords))
        V = list(V)
        return Vector2(V[0], V[1])


class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.coords = (self.x, self.y, self.z)

    def __add__(self, other):
        Vector2.length_check(self, other)
        V = (n1 + n2 for n1, n2 in zip(self.coords, other.coords))
        V = list(V)
        return Vector3(V[0], V[1], V[2])

    def __neg__(self):
        self.coords = list(self.coords)
        self.coords.reverse()
        x, y, z = self.coords[0], self.coords[1], self.coords[2]
        return Vector3(x, y, z)

    def __sub__(self, other):
        Vector2.length_check(self, other)
        V = (n1 - n2 for n1, n2 in zip(self.coords, other.coords))
        V = list(V)
        return Vector3(V[0], V[1], V[2])

    def __abs__(self):
        return list(map(lambda n: abs(n), self.coords))

    def __str__(self):
        return f"X coordinate: {self.coords[0]}\n" + \
            f"Y coordinate: {self.coords[1]}\n" + \
            f"Z coordinate: {self.coords[2]}"

    def __eq__(self, other):
        Vector2.length_check(self, other)
        if self.coords == other.coords:
            return True
        else:
            return False

    def __ne__(self, other):
        Vector2.length_check(self, other)
        if self.coords != other.coords:
            return True
        else:
            return False

    def __mul__(self, other):
        Vector2.length_check(self, other)
        V = (n1 * n2 for n1, n2 in zip(self.coords, other.coords))
        V = list(V)
        return Vector3(V[0], V[1], V[2])
