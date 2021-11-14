#las linkedlist están creadas por cabeceras y nodos que la siguen
#creamos el constructor de un nodo y de una cabecera

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval      #la cabecera de la lista
        self.nextval = None         #el elemento siguiente a la cabecera

class LinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):            #imprimir una lista enlazada
        printval = self.headval
        while printval is not None: #mientras el elemento de la cabecera no sea nulo, se imprimirán los datos
            print (printval.dataval)
            printval = printval.nextval     #se pasa al siguiente por la función next


    def add_value (self, value):
        self.headval.nextval=value #se añade como un segundo elemento, el valor pasado por parámetro

    def get_first(self):
        return self.headval     #retorna el elemento de la cabecera

    def get_value(self):
        return self.headval.nextval     #retorna el segundo elemento de la lista




#lista doblemente encadenada para poder recorrerla en los dos sentidos
#además cada celda podrá obtener al información tanto de su celda anterior como de su posterior

#generamos los mismos constructores perp haciendo referencias tmabién a los alementos anteriores

class Node:
    def __init__(self, data):
        self.data = data #cabecera
        self.next = None    #siguiente a la cabecera
        self.prev = None    #anterior a la cabecera

class doubly_linked_list:
    def __init__(self):
        self.head = None

    def add (self, value):  #añadir elemenentos a la lista
        value=Node(value)   #llamamos al constructo del nodo
        value.next=self.head    #lo ponemos como el primer elemento de la lista
        if self.head is not None:   #si la cabecera de la lista no es nulo, lo ponemos como el elemento previon a la cabecera (en última posición)
            self.head.prev=value
        self.head=value #si el elemento de la cebcera sí es nulo, lo ponemos como el elemento de la cabecera

    #de este modo, cada vez que se llame al método, entrarán los valores por el final de la lista

    def get_prev(self), value:
        return self.value.prev

    def remove (self):      #eliminamos un dato el principio de la lista
        if self.head.next is not None:
            self.head = None    #si la cabecera no es nula, la eliminamos poniéndola a null
            return
        self.head = self.head.next  #reordenamos la lista llamando al siguiente y al anterior (null)
        self.head.prev = None;