from qiskit import QuantumCircuit
import os

root_dir = os.path.dirname(os.path.realpath(__file__))

qc_cnot = QuantumCircuit(2)
qc_cnot.cx(0,1)
qc_cnot.draw()

figure = qc_cnot.draw(output='mpl')

figure.savefig('{}/cnot_gate.png'.format(root_dir))
