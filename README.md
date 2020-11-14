# Learning Qiskit

## Quick Start

### Step Zero

The following steps are specified for a Linux development environment. Each command specified may require slight adjustments to get working for your particular environment, and further adjustments outside of a Linux environment.

### Step One

Create virtual Python environment

```bash
python3 -m venv venv
```

### Step Two

Enable virtual environment

```bash
source venv/bin/activate
```

### Step Three

Install requirements

```bash
python3 -m pip install -r requirements.txt
```

### Common Issues and Solutions

NotFoundError: no lapack/blas resources found

```bash
sudo apt-get install gfortran libopenblas-dev liblapack-dev
```

<stdin>:1: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.

```bash
sudo apt-get install python3-tk
```

### Step Four

You are now ready to begin!
