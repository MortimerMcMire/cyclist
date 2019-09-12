import random as rd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import cyclist as cy

def generate_data():
        p = list(range(0,1000))
        d1 = [0] * 1000
        d2 = [0] * 1000
        d3 = [0] * 1000
        t = [0] * 1000
        
        for x in p:
                t[x] = float(x+3)
                d1[x] = 5*np.sin(x)
                d2[x] = 5*np.cos(x)
                d3[x] = 5*np.tan(x)

        l = {'time':t, 'data1': d1, 'data2': d2, 'data3': d3}
        data = pd.DataFrame.from_dict(l)
        data.set_index('time', inplace=True)
        return data

#def main():
data = generate_data()
d = data.reset_index().drop(columns='time')
eventImport = [('start',3.0),('start',370.0),('end',30.0),('end',775.0)]

x = cy.parse_events(eventImport)
cycles = cy.create_cycles(d,x,'start','end')

print(cycles)
    
#if __name__ == "__main__":
#        main()
