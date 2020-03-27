from cqc.pythonLib import CQCConnection


#####################################################################################################
#
# main
#
def main():

    # Initialize the connection
    with CQCConnection("Bob") as Bob:

        # Get qubit from Alice
        qB = Bob.recvQubit()
        #DecisionMaking
        qB.Z()
        Bob.sendQubit(qB, "Alice")

def u3(q1, b, c, a):
    q1.rot_Z(af(a))
    q1.rot_Y(af(b))
    q1.rot_Z(af(c))
    return q1


##################################################################################################
main()
