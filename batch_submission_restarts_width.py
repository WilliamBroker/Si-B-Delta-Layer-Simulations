# -*- coding: utf-8 -*-
"""
Created on Fri Jan 23 15:52:21 2026

@author: wjbroke
"""

# -*- coding: utf-8 -*-

import os
import numpy as np

parent_dir = os.getcwd()

for width in np.arange(1,2.5,0.5):
    for xi in np.arange(0.2,1.2,0.2):
        xi = np.round(xi,2)
        for temp in np.arange(300, 900, 100):
            for dt0 in np.arange(10, 20, 10):
            
                os.chdir(parent_dir)
                
                file = open(f"script.restart.{xi}.{temp}.{dt0}.{width}.batch", "w")
            
                file.write(f"#!/bin/bash\n")
                file.write(f"## Do not put any commands or blank lines before the #SBATCH lines\n")
                file.write(f"#SBATCH --nodes=1\n")
                file.write(f"#SBATCH --time=36:00:00\n")
                file.write(f"#SBATCH --account=FY190140\n")
                file.write(f"#SBATCH --job-name=SiB_restart{xi}.{temp}.{dt0}.{width}\n")
                file.write(f"#SBATCH --partition=batch\n")
                file.write(f"###SBATCH --qos=long\n")
                file.write(f"nodes=$SLURM_JOB_NUM_NODES\n")
                file.write(f"cores=15\n")
                file.write(f"##export OMP_NUM_THREADS=36\n")
                #file.write(f"/ascldap/users/jpmende/Softwares/CBR3D_new_version_asym_delta_layer_test_2/./CBR3D 4K_x_{posX}nm_y_{posY}nm.txt\n")
                file.write(f"mpirun -np 15 /ascldap/users/wjbroke/lammps-stable_12Dec2018/src/lmp_mpi -in inrestart.{xi}.{temp}.{dt0}.{width}.mxe_mt\n")
                
                file.close()
                
                os.system("export OMP_NUM_THREADS=36")
                os.system(f'sbatch script.restart.{xi}.{temp}.{dt0}.{width}.batch')
                
                print(f'Job inrestart.{xi}.{temp}.{dt0}.{width}.mxe_mt submitted')
    
os.chdir(parent_dir)

