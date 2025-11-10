# ==============================
# Imports et variables globales
# ==============================
import math
from point2d import Point2D  # On suppose que Point2D est défini dans ce fichier

# ==============================
# Définition de la classe Vector2D
# ==============================
class Vector2D:
    """
    Classe représentant un vecteur 2D défini par deux points (origine et extrémité).
    
    >>> p1 = Point2D(1, 2)
    >>> p2 = Point2D(4, 6)
    >>> v = Vector2D(p1, p2)
    >>> print(v)
    Vector2D(x=3, y=4)
    >>> abs(v)
    5.0
    >>> -v
    Vector2D(x=-3, y=-4)
    >>> v2 = Vector2D(Point2D(0,0), Point2D(3,4))
    >>> v == v2
    True
    >>> v3 = Vector2D(Point2D(1,1), Point2D(2,2))
    >>> v + v3
    Vector2D(x=4, y=6)
    >>> v - v3
    Vector2D(x=2, y=2)
    """

    def __init__(self, start_point, end_point):
        """
        Initialise un vecteur à partir de deux points.
        start_point et end_point doivent être des instances de Point2D.
        """
        self.x = end_point.x - start_point.x
        self.y = end_point.y - start_point.y

    def __abs__(self):
        """Retourne la norme du vecteur."""
        return math.hypot(self.x, self.y)

    def __str__(self):
        """Affichage clair du vecteur."""
        return f"Vector2D(x={self.x}, y={self.y})"

    def __eq__(self, other):
        """Comparaison entre vecteurs."""
        return self.x == other.x and self.y == other.y

    def __neg__(self):
        """Retourne l'opposé du vecteur."""
        return Vector2D(Point2D(0,0), Point2D(-self.x, -self.y))

    def __add__(self, other):
        """Addition de deux vecteurs."""
        return Vector2D(Point2D(0,0), Point2D(self.x + other.x, self.y + other.y))

    def __sub__(self, other):
        """Soustraction de deux vecteurs."""
        return Vector2D(Point2D(0,0), Point2D(self.x - other.x, self.y - other.y))

# ==============================
# Définition de la fonction principale
# ==============================
def main():
    # Création de points
    p1 = Point2D(1, 2)
    p2 = Point2D(4, 6)
    p3 = Point2D(1, 1)
    p4 = Point2D(2, 2)

    # Création de vecteurs
    v1 = Vector2D(p1, p2)
    v2 = Vector2D(Point2D(0,0), Point2D(3,4))
    v3 = Vector2D(p3, p4)

    print("Vecteur v1 :", v1)
    print("Norme de v1 :", abs(v1))
    print("Opposé de v1 :", -v1)
    print("v1 == v2 ?12211²1", v1 == v2)
    print("v1 + v3 =", v1 + v3)
    print("v1 - v3 =", v1 - v3)

# ==============================
# Appel protégé de la fonction principale
# ==============================
if __name__ == "__main__":
    main()
