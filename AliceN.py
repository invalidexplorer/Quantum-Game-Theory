from cqc.pythonLib import CQCConnection, qubit
import math
#####################################################################################################
#
# main
#
pi = math.pi

def main():
    # Initialize the connection
    with CQCConnection("Alice") as Alice:
        # Create qubits
        q1 = qubit(Alice)
        q2 = qubit(Alice)
        J(q1, q2)
        q1.Z()
        Alice.sendQubit(q2, "Bob")
        q3 = Alice.recvQubit()
        JD(q1,q3)
        # Measure the qubits

        a = q1.measure()
        b = q3.measure()
        to_print = "App {}: Measurement outcomes are: Alice={}, Bob={}".format(Alice.name, a, b)
        print("|" + "-" * (len(to_print) + 2) + "|")
        print("| " + to_print + " |")
        print("|" + "-" * (len(to_print) + 2) + "|")


def af(x):

    if x>=2*pi:
        return af(x-(2*pi))
    if x < 0:
        return af(x+(2*pi))
    for i in range(0, 255):
        if x==(i*2*pi)/256:
            #print(i)
            return i


def u3(q1,b,c,a):
    q1.rot_Z(af(a))
    q1.rot_Y(af(b))
    q1.rot_Z(af(c))
    return q1


def cu3(q1, q2, a, b, c): #controlled c3 gate
    q2.rot_Z(af(-(c - b) / 2))
    q1.cnot(q2)
    u3(q2, - a / 2, 0, -(b + c) / 2)
    q1.cnot(q2)
    u3(q2, a / 2, b, 0)
    return q1,q2

def J(q1, q2): # J gate
    cu3(q1, q2, 0, pi / 2, pi / 2)
    cu3(q2, q1, pi, 2 * pi, 0)
    cu3(q1, q2, pi / 2, 2 * pi, 0, )
    q1.X()
    cu3(q1, q2, pi / 2, 3 * pi, pi, )
    q1.X()
    cu3(q2, q1, pi, 2 * pi, 0)
    cu3(q1, q2, 0, pi / 2, pi / 2)
    return q1, q2

def JD(q1, q2):
    cu3(q1 , q2, 0, pi * 3 / 2, pi * 3 / 2)
    cu3(q2 , q1, pi, 0, 0)
    q1.X()
    cu3(q1, q2, pi / 2, 0, 0)
    q1.X()
    cu3(q1, q2, pi / 2, pi, pi)
    cu3(q2, q1, pi, 0, 0)
    cu3(q1, q2, 0, pi * 3 / 2, pi * 3 / 2)
    return q1,q2
##################################################################################################
main()
