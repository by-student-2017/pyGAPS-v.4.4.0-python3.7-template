#import pygaps
import pygaps.characterisation as pgc
import pygaps.parsing as pgp
import matplotlib.pyplot as plt

# create the path
path = r'case.csv'
#path = r'ref_ngcb.csv'

# import the isotherm
isotherm = pgp.isotherm_from_csv(path)
#isotherm.print_info()

pgc.area_BET(isotherm, verbose=True)
#pygaps.area_BET(isotherm, limits=(0.05, 0.2), verbose=True)
fig1 = plt.figure(1)
fig1.savefig('./plot/BET-plot.jpg')
fig2 = plt.figure(2)
fig2.savefig('./plot/BET-plot_Rouquerol-plot.jpg')
#plt.show()
