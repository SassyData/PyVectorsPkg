class Vector:
    """
    A class describing generic 2D & 3D vectors and their properties.
    """
    def __init__(self, i, j, k = None):
        self.i = i
        self.j = j
        self.k = k

    def dot_product(self, other):
        """
        Function which calculates the dot product of two vectors

        INPUTS:
        self - 2D or 3D vector

        OUTPUTS:
        dp - a value for the dot product
        insight - string statement, commenting on the size of the angle between these two vectors
        """
        dp = other.i * self.i + other.j * self.j + other.k * self.k

        if dp == 0:
            insight = "since the dot product is zero, the angle between these two vectors is Pi / 2"
        elif dp > 0:
            insight = "since the dot product is positive, the angle between these two vectors is less than Pi / 2"
        else:
            insight = "since the dot product is negative, the angle between these two vectors is greater than than Pi / 2"

        return(dp, insight)

