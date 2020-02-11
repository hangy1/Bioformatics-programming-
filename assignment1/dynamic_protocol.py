#!/usr/bin/env python3

final_vol =float( input("Please enter the final volume of the solution (ml): "))

NaCl_Cstock = float(input("Please enter the NaCl stock (mM): "))
NaCl_Cfinal = float(input("Please enter the NaCl final (mM): "))

#calculate inital volume from stock solutions, Ci * Vi = Cf * Vf
NaCl_Vstock = (NaCl_Cfinal * final_vol) / NaCl_Cstock
step1 = "add {} ml NaCl.\n".format(NaCl_Vstock)

MgCl2_Cstock = float(input("Please enter the MgCl2 stock: (mM): "))
MgCl2_Cfinal = float( input("Please enter the MgCl2 final: (mM): "))

#calculate initial volume from MgCl2 stock solution.
MgCl2_Vstock = (MgCl2_Cfinal * final_vol) / MgCl2_Cstock
step2 = "add {} ml MgCl2.\n".format(MgCl2_Vstock)

step3 = "Add water to a final volume of {:.2f} ml and mix.".format(final_vol)
print(step1 + step2 +step3)
