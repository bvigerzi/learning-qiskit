from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram
import os

root_dir = os.path.dirname(os.path.realpath(__file__))

n = 8
n_q = n # number of qubits in circuit
n_b = n # number of output bits
qc_output = QuantumCircuit(n_q,n_b)

for j in range(n):
    qc_output.measure(j,j)

figure = qc_output.draw(output='mpl')

figure.savefig('{}/first_circuit.png'.format(root_dir))

counts = execute(qc_output,Aer.get_backend('qasm_simulator')).result().get_counts()
histogram = plot_histogram(counts)
histogram.savefig('{}/probability_of_00000000.png'.format(root_dir))
