# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 12:08:07 2026

@author: wjbroke
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 11:37:47 2026

@author: wjbroke
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Dec 13 12:22:33 2025

@author: wjbroke
"""
#This is a file to make LAMMPS input files using bash commands in terminal. It makes files for differing atomic molar concentration (xi) values,
#temperatures, and diffusive timesteps (note that LAMMPS uses a different timestep, under the timestep command, to actually run the simulation).
#The commands used here can be looked up in the LAMMPS docs or MXE manual.

import os
import numpy as np

parent_dir = os.getcwd()

xx = 4 #xx, yy and zz define the simulation box. These are for my own sanity when looking at this code---change the numbers in the "Definition of variable" lines
yy = 10
zz = 8
Freq0 = 50.0
width = 1.0 #This defines the width of the delta layer. 1 unit here = 4.7nm


for xi in np.arange(0.2,1.2,0.2):
    xi = round(xi, 2)
    xicomplement = 1-xi
    for temp in np.arange(300,900,100):
        for dt0 in np.arange(0.0001,0.0002,0.0001): #This is the range of the initial timestep
            
            os.chdir(parent_dir)
            
            file = open(f"in.{xi}.{temp}.{dt0}.{width}.mxe_mt", "w")
            
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
            file.write(f"atom_style	atomic_mxe_mt\n") #Mxe used here
            file.write(f"boundary        p p p\n")
            file.write(f"\n")
            file.write(f"# Definition of region and atoms\n")
            file.write(f"\n")
            file.write(f"lattice	diamond 5.431\n") #This is the lattice parameter used
            file.write(f"region	box   block -{xx} {xx} -{yy} {yy} -{zz} {zz}\n")
            file.write(f"region	doped block -{xx} {xx} -1 1 -{zz} {zz}\n")
            file.write(f"\n")
            file.write(f"create_box	2 box\n") #We create the simulation box
            file.write(f"create_atoms	1 box\n") #We create the atoms in the box
            file.write(f"\n")
            file.write(f"group doped region doped\n") #We create the delta layer
            file.write(f"\n")
            file.write(f"set type 1 mxe_temperature {temp}\n") #Mxe used here
            file.write(f"set type 1 frequency {Freq0}\n")
            file.write(f"set type 1      xi 0.999 0.001 0.00\n") #We don't use 0 for non-vacancies in order to avoid computational errors
            file.write(f"set group doped xi {xicomplement} {xi} 0.00\n")
            file.write(f"\n")
            file.write(f"# Potential setting\n")
            file.write(f"\n")
            file.write(f"pair_style      sw_mxe_mt_binary\n") #Mxe used here
            file.write(f"pair_coeff 	* * SiB.sw Si B\n")
            file.write(f"neigh_modify every 1\n")
            file.write(f"\n")
            file.write(f"mass            1       28.06\n")
            file.write(f"mass            2       10.811\n")
            file.write(f"\n")
            file.write(f"# Simulation setting\n")
            file.write(f"\n")
            file.write(f"compute {temp} all fe\n") #Computes free entropy
            file.write(f"thermo 100\n")
            file.write(f"\n")
            file.write(f"fix 0 all optfreq 200.0 0.5 0.0 wmin 10\n")
            file.write(f"fix 1 all npt temp 0.1 0.1 0.1 iso 1 1 1\n")
            file.write(f"#fix 1 all nvt temp 0.1 0.1 0.1\n")
            file.write(f"\n")
## fix ID-fix all transport/atom nu [hopping frequency] Qm [barrier energy] dt [time step] rdcut [cutoff radius] interstitial(o subtitutional) [type atoms] rescale [1/0]\n")
## Dimension analysis: [nu = 1.0e13 1/sec] [dt = 1.0e-2  sec]\n")
## Dimension analysis: [nu = 10    1/psec] [dt = 1.0e10 psec] (THIS IS IMPORTANT!!! DONT MIX UNITS!!!)
            file.write(f"restart 10000 restart.{xi}.{temp}.{dt0}.{width}.*\n") #We create the restart files here
            file.write(f"dump 1 all custom 100 dump.prelim.{xi}.{temp}.{dt0}.{width}.* x y z frequency freq_force xi0 xi1 xi2 fxi0 fxi1 fxi2 fx fy fz\n") #This is the dump for the prerun, where we relax the system.
            file.write(f"log log.prelim.{xi}.{temp}.{dt0}.{width}.lammps append\n") #The log of the prerun
            file.write(f"thermo_style custom step ke pe etotal press c_{temp}\n")
            file.write(f"\n")
            file.write(f"timestep   0.001\n")
            file.write(f"run 		1000\n") #We let the system relax and the volume to adjust
            file.write(f"\n")
            file.write(f"fix diff all mass_transport/atom nu 10 Qm 0.69 dt {dt0} rdcut 5.0 substitutional 1 xmin 0.0 xmax 1.0 rescale 1\n") #Mxe used here
            file.write(f"\n")
            file.write(f"dump 2 all custom 100 dump.sim.{xi}.{temp}.{dt0}.{width}.* x y z frequency freq_force xi0 xi1 xi2 fxi0 fxi1 fxi2 fx fy fz\n") #Now we let diffusion happen
            file.write(f"log log.{xi}.{temp}.{dt0}.{width}.lammps append\n")
            file.write(f"thermo_style custom step ke pe etotal press c_{temp} f_diff\n")
            file.write(f"\n")
            file.write(f"timestep	0.001\n")
            file.write(f"run 		100000\n")
              
            file.write(f"\n")
            file.write(f"undump 1\n")
            file.write(f"undump 2\n")
            file.write(f"write_restart restart\n")
                    
                    
            file.close()
    
os.chdir(parent_dir)
    