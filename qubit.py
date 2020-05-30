import matplotlib.pyplot as plt
from qiskit import BasicAer, Aer, QuantumCircuit, QuantumRegister, ClassicalRegister, execute, IBMQ
from qiskit.visualization import *
from qiskit.tools.monitor import job_monitor
import math

#########################################################
#########################################################
# #INIT

statevector_sim = Aer.get_backend("statevector_simulator")

nb_qubits = int(input("Sur combien de qubit veux-tu voir des interactions ? : 1, 2, 3, 4, 5 ? "))

#########################################################
#########################################################
# #Circuit

# Quantum Circuit
q = QuantumRegister(nb_qubits)
qc = QuantumCircuit(q)
for i in range(0, nb_qubits):
    print("Veux-tu poser plusieurs portes sur le qubit[", i, "] ?")
    many_gates = str(input("yes/no : "))
    play = True
    while play:
        print("Quelle porte veux-tu utiliser sur le qubit[", i, "] ?")
        if nb_qubits == 1:
            gate = str(input("h, x, y, none : "))
        else:
            gate = str(input("h, x, y, cx, none : "))
        if many_gates == 'no' or many_gates == 'n':
            play = False
        if gate == 'h':
            qc.h(i)
        elif gate == 'x':
            qc.x(i)
        elif gate == 'y':
            qc.y(i)
        elif gate == 'z':
            qc.z(i)
        elif gate == 'cx':
            print("Avec quel autre qubit veux-tu intriquer q[", i, "] ? : 0 -", nb_qubits - 1)
            intric = int(input())
            qc.cx(i, intric)
        else:
            play = False
        print(qc)

#########################################################
#########################################################
# #Visualization

statevector_job = execute(qc, statevector_sim)
statevector_result = statevector_job.result()
psi = statevector_result.get_statevector()

plot_bloch_multivector(psi)
plot_state_qsphere(psi)
plt.show()
