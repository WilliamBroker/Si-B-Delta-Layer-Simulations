# -*- coding: utf-8 -*-
"""
Created on Sat Dec 13 13:53:30 2025

@author: wjbroke
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Dec 13 12:22:33 2025

@author: wjbroke
"""

import os
import numpy as np

parent_dir = os.getcwd()

xx = 4
yy = 10
zz = 4
Freq0 = 50.0

for xi in np.arange(0.2,1.2,0.2):
    xi = round(xi, 2)
    xicomplement = 1-xi
    for temp in np.arange(300,900,100):
        for dt0 in np.arange(10,20,10):
            
            os.chdir(parent_dir)
            
            file = open(f"inrestart.{xi}.{temp}.{dt0}.mxe_mt", "w")
            
            file.write(f"# Definition of variable\n")
            file.write(f"\n")
            file.write(f"variable	xx equal 4\n")
            file.write(f"variable	yy equal 10\n")
            file.write(f"variable	zz equal 4\n")
            file.write(f"variable	Temp0 equal {temp}\n")
            file.write(f"variable 	Freq0 equal 50.0\n")
            file.write(f"variable	Dt0 equal {dt0}\n")
            file.write(f"\n")
            
            file.write(f"# Simulation info\n")
            file.write(f"\n")
            file.write(f"units		metal\n")
            file.write(f"dimension       3\n")
            file.write(f"atom_style	atomic_mxe_mt\n")
            file.write(f"boundary        p p p\n")
            file.write(f"read_restart restart.{xi}.{temp}.{dt0}.*")
            file.write(f"\n")
            
            file.write(f"# Definition of region and atoms\n")
            file.write(f"\n")
            
            file.write(f"# Potential setting\n")
            file.write(f"\n")
            file.write(f"pair_style      sw_mxe_mt_binary\n")
            file.write(f"pair_coeff 	* * SiB.sw Si B\n")
            file.write(f"neigh_modify every 1\n")
            file.write(f"\n")
            file.write(f"mass            1       28.06\n")
            file.write(f"mass            2       10.811\n")
            file.write(f"\n")
            
            file.write(f"# Simulation setting\n")
            file.write(f"\n")
            file.write(f"compute {temp} all fe #Computes free entropy\n")
            file.write(f"thermo 100\n")
            file.write(f"\n")
            file.write(f"fix 0 all optfreq 200.0 0.5 0.0 wmin 10\n")
            file.write(f"fix 1 all npt temp 0.1 0.1 0.1 iso 1 1 1\n")
            file.write(f"#fix 1 all nvt temp 0.1 0.1 0.1\n")
    
            file.write(f"\n")
            file.write(f"fix diff all mass_transport/atom nu 10 Qm 0.69 dt {dt0} rdcut 5.0 substitutional 1 xmin 0.0 xmax 1.0 rescale 1\n")
            file.write(f"\n")
            file.write(f"dump 1 all custom 2000 dump.sim.{xi}.{temp}.{dt0}.* x y z frequency freq_force xi0 xi1 xi2 fxi0 fxi1 fxi2 fx fy fz\n")
            file.write(f"log log.{xi}.{temp}.{dt0}.lammps append\n")
            file.write(f"thermo_style custom step ke pe etotal press c_{temp} f_diff\n")
            file.write(f"\n")
            file.write(f"timestep	0.001\n")
            file.write(f"run 		10000\n")
            file.write(f"\n")
            file.write(f"unfix diff\n")
            file.write(f"\n")
            file.write(f"fix diff all mass_transport/atom nu 10 Qm 0.6 dt 1.0e3 rdcut 3.0 substitutional 1 xmin 0.0 xmax 1.0 rescale 1\n")
            file.write(f"run 100000\n")
            file.write(f"\n")
            file.write(f"unfix diff\n")
            file.write(f"\n")
            file.write(f"fix diff all mass_transport/atom nu 10 Qm 0.6 dt 1.0e5 rdcut 3.0 substitutional 1 xmin 0.0 xmax 1.0 rescale 1\n")
            file.write(f"run 100000\n")
            file.write(f"\n")
            file.write(f"unfix diff\n")
            file.write(f"\n")
            file.write(f"fix diff all mass_transport/atom nu 10 Qm 0.6 dt 1.0e7 rdcut 3.0 substitutional 1 xmin 0.0 xmax 1.0 rescale 1\n")
            file.write(f"run 100000\n")
            file.write(f"\n")
            file.write(f"unfix diff\n")
            file.write(f"\n")
            file.write(f"fix diff all mass_transport/atom nu 10 Qm 0.6 dt 1.0e9 rdcut 3.0 substitutional 1 xmin 0.0 xmax 1.0 rescale 1\n")
            file.write(f"run 100000\n")
            file.write(f"\n")
            file.write(f"unfix diff\n")
            file.write(f"\n")
            file.write(f"fix diff all mass_transport/atom nu 10 Qm 0.6 dt 1.0e12 rdcut 3.0 substitutional 1 xmin 0.0 xmax 1.0 rescale 1\n")
            file.write(f"run 1000000\n")
            file.write(f"\n")
            file.write(f"undump 1\n")
            file.write(f"undump 2\n")
            file.write(f"write_restart restart\n")
            
            
            file.close()
    
os.chdir(parent_dir)
    