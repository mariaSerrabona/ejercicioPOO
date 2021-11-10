
class Libro:
#definimos todos los atributos que caracteizan a un libro

    isbn=0       #texto
    autor=0
    titito=0    #texto
    año_de_publicacion=0    #texto
    idioma=0   #texto
    editor=0
    ejemplares=0    #texto

    #ahora creamos el constructor

    def __init__(self, isbn,autor, titulo, año_de_publicacion, idioma,editor, ejemplares):
        self._isbn=isbn
        self._autor=autor
        self._titulo=titulo
        self._año_de_publicacion=año_de_publicacion
        self._idioma=idioma
        self._editor=editor
        self._ejemplares=ejemplares

    def getISBN(self):
        return self._isbn
    def setISBN(self, isbn):
        self._isbn=isbn

    def getAutor(self):
        return self._autor
    def setAutor(self, autor):
        self._autor=autor

    def getTitulo(self):
        return self._titulo
    def setTitulo(self, titulo):
        self._titulo=titulo

    def getAñoPublicacion(self):
        return self._año_de_publicacion
    def setAñoPublicacion(self, año_de_publicacion):
        self._año_de_publicacion=año_de_publicacion

    def getIdidoma(self):
        return self._idioma
    def setIdioma(self, idioma):
        self._idioma=idioma

    def getEditor(self):
        return self._editor
    def setEditor(self, editor):
        self._editor=editor

    def getEjemplares(self):
        return self._ejemplares
    def setEjemplares(self, ejemplares):
        self._ejemplares=ejemplares


