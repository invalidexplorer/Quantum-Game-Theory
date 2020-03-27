### QuantumGameTheory

Quantum game theory has been implemented via EWL Scheme using Quantum Networks in SimulaQron.

## Description

Here alice prepares two qubits, pass them through J gate and then sents one of the qubits to Bob. Alice and Bob applies respective gates of their choice (U1, U2) without notifying the each other. Here U1 and U2 represent their quantum choices. Bob sends his qubit to Alice and Reverse J gate is applied to both of the qubits before measurement. 

## Sample test cases are as follows:

Gates: *U1  U2
    1. *I   I -> result should be |00>
    2. *I   X -> result should be |01>
    3. *X   I -> result should be |10>
    4. *X   X -> result should be |11>

Requirements
Be sure to have SimulaQron installed and running on your computer (see  guide).

## Usage

1) The decisions are hard coded for testing, though they can be for sure be accepted on the go from the user. 
2) After changing the decisions, the simulaqron network must be reset, else it will show unpredictable results.
   It can be reset by the following command on the terminal : simulaqron reset
3) Before starting simulaqron on the terminal, the backend must be changed to either projectq or qutip, as the default               stabilizers do not have single qubit rotation gates.

It can be changed by the following command on terminal: 
* simulaqron set backend projectq
 > Hence before executing and after changing the decisions, the following commands must be used.
* simulaqron reset
* simulaqron set backend projectq
* simulaqron start
* sh run.sh
