from qiskit import QuantumCircuit
import os

root_dir = os.path.dirname(os.path.realpath(__file__))

n = 8
qc_encode = QuantumCircuit(n)
qc_encode.x(7)

figure = qc_encode.draw(output='mpl')

figure.savefig('{}/encoding_input.png'.format(root_dir))
