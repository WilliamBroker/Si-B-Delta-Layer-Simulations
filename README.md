# Si-B-Delta-Layer-Simulations
This is a repository of input scripts and associated documents that Dr. Juan Mendez (Sandia National Labs) and I wrote for simulating diffusion of boron delta layers within c-Si in the LAMMPS program. The following files are within this repository:
  
* SiB.sw: This is a file which stores the constants in the Stillinger-Weber pair potential. This potential is a classical model used to model group IV elements; in this case, Si-Si, Si-B and B-B interactions. This file is called upon in the LAMMPS input scripts. See J. Appl. Phys. 96, 1939 (2004).
* Inputmaker.py: This is a file that creates input scripts for an adjustable range of atomic molar fraction (xi) values, temperatures, and timestep (dt) values.
* Restartmaker.py: This is a file that creates restart input scripts for an adjustable range of atomic molar fraction (xi) values, temperatures, and timestep (dt) values. Restart scripts run previous simulations where they left off, using the "write_restart" command in LAMMPS.
* batch_submission_restarts.py and batch_submission_300_900K.py: These are python scripts that run restart and input scripts. When using, make sure the range of xi values, temperatures, and dt values match the ranges in the input and restart scripts. Encoded within these files are the number of cores to be used, the time limit, and the partition and qos styles.

The LAMMPS input scripts use a package called MXE, developed by Dr. Juan Mendez and Dr. Mauricio Ponga (see Computer Physics Communications 260, 2021 (2020)). MXE contains the physics used in diffusive molecular dynamics (DMD). MXE must be installed in the same place as all other LAMMPS packages in order for the simulation to run properly.
