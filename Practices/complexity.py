from time import *
from math import *


class CustomerNode:
    def __init__(self, ticket_num, cust_name, server_name, next):
        '''(IntNode, int, str, str, CustomerNode) -> NoneType
        Create a new CustomerNode with ticket number ticket_num,
        customer name cust_name, server name server_name and
        pointing to next.
        REQ: server_name must be either "Anna" or "Brian".
        '''
        self._ticket_num = ticket_num
        self._cust_name = cust_name
        self._server_name = server_name
        self.next = next

    def __repr__(self):
        """(CustomerNode) -> str
        Return a string representing self.
        """
        return ("CustomerNode(" + repr(self._ticket_num) + ", " +
                repr(self._cust_name) + ", " + repr(self._server_name) +
                ", " + repr(self.next) + ")")

    def get_ticket_num(self):
        return self._ticket_num

    def get_cust_name(self):
        return self._cust_name

    def get_server_name(self):
        return self._server_name


def reclistmerge(L1, L2):
    ''' (CustomerNode, CustomerNode) -> CustomerNode
    '''
    #
    #
    if L1 == None:
        return L2
    if L2 == None:
        return L1
    # debug printing
    print(L1.get_ticket_num(), L2.get_ticket_num())
    #
    #
    if L1.get_ticket_num() < L2.get_ticket_num():
        #
        #
        L1.next = reclistmerge(L1.next, L2)
        return L1
    else:
        #
        #
        L2.next = reclistmerge(L1, L2.next)
        return L2

if __name__ == "__main__":
    L_A = CustomerNode(2, "Alice", "Anna",
                       CustomerNode(3, "Bob", "Anna",
                                    CustomerNode(5, "Carol", "Anna", None)))
    L_B = CustomerNode(1, "Ziggy", "Brian",
                       CustomerNode(4, "Yaz", "Brian",
                                    CustomerNode(6, "Xavier", "Brian", None)))
    L = reclistmerge(L_A, L_B)
    print(L)
