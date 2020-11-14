from qiskit import QuantumCircuit
import os

root_dir = os.path.dirname(os.path.realpath(__file__))

qc_ha = QuantumCircuit(4,2)
# encode inputs in qubits 0 and 1
qc_ha.x(0) # invert qubit 0 (now is value 1)
qc_ha.x(1) # invert qubit 1 (now is value 1)
qc_ha.barrier()
# use cnots to write the XOR of the inputs on qubit 2
qc_ha.cx(0,2) # qubit 0 is CNOT to qubit 2
qc_ha.cx(1,2) # qubit 1 is CNOT to qubit 2
qc_ha.barrier()
# extract outputs
qc_ha.measure(2,0) # extract XOR value
qc_ha.measure(3,1)

figure = qc_ha.draw(output='mpl')

figure.savefig('{}/half_adder.png'.format(root_dir))
