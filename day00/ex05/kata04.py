# Expected output format : module_00, ex_04 : 132.42, 1.00e+04, 1.23e+04

tup = (0, 4, 132.42222, 10000, 12345.67)

print(f"module_{tup[0]:02}, ex_{tup[1]:02} : {tup[2]:.2f}, {tup[3]:.2e}, {tup[4]:.2e}")
