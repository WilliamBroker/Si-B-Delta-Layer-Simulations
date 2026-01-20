# -*- coding: utf-8 -*-

import os
import numpy as np

parent_dir = os.getcwd()

for xi in np.arange(0.2,1.2,0.2):
    xi = round(xi,2)
    for temp in np.arange(300, 900, 100):
        for dt0 in np.arange(50, 150, 50):
        
            os.chdir(parent_dir)
            
            file = open(f"script.{xi}.{temp}.{dt0}.batch", "w")
        
            file.write(f"#!/bin/bash\n")
            file.write(f"## Do not put any commands or blank lines before the #SBATCH lines\n")
            file.write(f"#SBATCH --nodes=1\n")
            file.write(f"#SBATCH --time=36:00:00\n")
            file.write(f"#SBATCH --account=FY190140\n")
            file.write(f"#SBATCH --job-name=SiB_{xi}.{temp}.{dt0}\n")
            file.write(f"#SBATCH --partition=batch\n")
            file.write(f"###SBATCH --qos=long\n")
            file.write(f"nodes=$SLURM_JOB_NUM_NODES\n")
            file.write(f"cores=15\n")
            file.write(f"##export OMP_NUM_THREADS=36\n")
            #file.write(f"/ascldap/users/jpmende/Softwares/CBR3D_new_version_asym_delta_layer_test_2/./CBR3D 4K_x_{posX}nm_y_{posY}nm.txt\n")
            file.write(f"mpirun -np 15 /ascldap/users/wjbroke/lammps-stable_12Dec2018/src/lmp_mpi -in in.{xi}.{temp}.{dt0}.mxe_mt\n")
            
            file.close()
            
            os.system("export OMP_NUM_THREADS=36")
            os.system(f'sbatch script.{xi}.{temp}.{dt0}.batch')
            
            print(f'Job in.{xi}.{temp}.{dt0}.mxe_mt submitted')
    
os.chdir(parent_dir)

