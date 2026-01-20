# J. Appl. Phys. 96, 1939 (2004);
#
# note that the parameters for this literature potential are pairwise
# so that there are some flexibility in the way the 
# parameters can be entered. As one way, we assume that 
# lambda_ijk is equal to lambda_ik and eps_ijk is 
# equal to sqrt(lambda_ij*eps_ij*lambda_ik*eps_ik)/lambda_ik, 
# and all other parameters in the ijk line are for ik.

# These entries are in LAMMPS "metal" units:
#   epsilon = eV; sigma = Angstroms
#   other quantities are unitless
#
#         eps      sigma   a       lambda   gamma    cos(theta)     A        B        p       q      tol
#
Si Si Si 2.171927 2.09510 1.8     21.0     1.2     -0.333333333333 7.049556 0.602224 4.0     0.0     0.0
B  B  B  1.891430 1.95754 1.53707 21.57076 1.65477 -0.4212         12.75998 0.57836  8.05849 0.01507 0.0
Si Si B  1.974759 0.0     0.0     21.0     0.0     -0.333333333333 0.0      0.0      0.0     0.0     0.0
Si B  B  1.795490 1.8080  2.1     21.0     1.2     -0.333333333333 7.049556 0.602224 4.0     0.0     0.0
B  Si Si 1.795490 1.8080  2.1     21.0     1.2     -0.333333333333 7.049556 0.602224 4.0     0.0     0.0
B  Si B  1.842836 0.0     0.0     21.2835  0.0     -0.3747         0.0      0.0      0.0     0.0     0.0
B  B  Si 1.842836 0.0     0.0     21.2835  0.0     -0.3747         0.0      0.0      0.0     0.0     0.0
Si B  Si 1.974759 0.0     0.0     21.0     0.0     -0.333333333333 0.0      0.0      0.0     0.0     0.0
