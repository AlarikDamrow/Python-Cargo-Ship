#Alarik Damrow
def count_items(crate): #Counts number of particular item and stores
    return crate.count('t'), crate.count('w'), crate.count('d')

def cargo(crates, T, W, D):
    # Count items in crates
    item_counts = [count_items(crate) for crate in crates]
    # Array to be used to detemine how many crates can be fitted
    table = {}
    def dp(index, T, W, D): #Function to look through crates and determine best case scenario
        if index == len(crates): # If there is no way to hold any crates
            return 0
        if (index, T, W, D) in table: #If there is a capacity to carry these crates
            return table[(index, T, W, D)]
        # Iterate through the crates and output the number of toasters, washers, and dryers in the current crate
        t, w, d = item_counts[index]
        # Skip the current crate
        best = dp(index + 1, T, W, D)
        # Take the current crate only if it does not exceed the capacities given
        if t <= T and w <= W and d <= D:
            best = max(best, 1 + dp(index + 1, T - t, W - w, D - d))
        # Take record and return the best way to maximize capacity
        table[(index, T, W, D)] = best
        return best
    # Start at the first crate and recusively iterate till capacity is filled
    return dp(0, T, W, D)

# Cases on Assignment PDF
'''
print( cargo(["d"],21,22,23))
print( cargo(["d"],1,1,1)
)
print( cargo(['twwddwwdtdtdddddwwwtwtttdddwwtdwt', 'td', 'wddddwwwwwttwwdwdtddwttdww', 
'ddtttwwwwwwwtttwwdwdwwttdwtwdwwtdwt', 'wtt', 'ttdtdtdddwtdtwtwwtwtwwwdwwwtdddtwtd', 
'dwwtwtdwddddt', 'twtttw', 'ddttdwwttdtwwdwtddddddwttdddwdtwwwddwddtdw', 'ddtdddttt', 
'wttdttdddwdttwtww', 't', 'ttwttdtwdtwwd', 'wdtwdwdttdwwdwdwtwtt', 
'twwwdtttttdwttdttdtdwdwdwwtwdttwwddt', 'dwtwtwwttdtdwwdwddttwtwwtwtwttdwdtwtwtddwdttt', 
'twtwdddttwtwtdwwwddwdttwwwtddwdtwtdddwd', 
'wtttwwtwwwdwddwtddwwwwdwttwwdttdtdwttw', 'twtwdddtwddttttddwtddwwtddtwdwtt', 
'wtdwwwddtttwtddtdwwdwwwdtddd', 'wwwt', 'ddtttwwdw', 'ttdwwwwwwwdddttttddwwd', 'd', 
'dwwwwddwwdddtwtwdttwtdw', 'tddddtwtttwttttt', 
'dtwwtdwtddddwdddwwwdwwwwwdtdddtdwwdtdddwtd', 'wdttwwwtwtwt', 
'tdtwwwwwwtwttdtwdddd', 'dwwwddwddddtttwdwtdwttdtdtdtd', 
'wwdtddtdwdtdwwtdttddwttdwwtwwtwdtwttwwwddtddt', 
'wtdddtttwdtdddwwtddtdwdtdwwdtwttdddwtwtwtttdtdwtd', 
'wdwdddtdddtddtdwtdtdtwwttwtwwwwwtdddwwdddwdtwwt', 
'wdwtdwttdddwwwwtwdddtdtdwdtwwddttt', 'dtddtttwdtw', 'dwwddwwdwtdwd', 
'twwtdwdwtwtttwddwttdwtddwtdwwttwddwwtdtttdttddt', 'ttwtwddtwdwdt', 
'wdwwdddddtwdwwddwdtttwwttdwdwttdwttddttwtdww', 'tddddwwtdwddd', 
'dtwwdttdttdwwwtdtdwtwwwdwdddtdd', 'twwwddwtdtdttddtwdtwtdtd', 
'ttttwtdwwwtddwdwddwdwdwdwtwtdtwddttw', 'dwddtdwwwtdwwwtddtwdtdddtwtdww', 
'dwdwwtwwdddttdwdwtw', 'wwwtwdddwdtddwddddddwddttdwwt', 'wtttttttddwwtdwdtd', 
'dwwwddwttwdwtwddtdwddtdddddwddddwwddwdt', 'dwwwwwdttdtwtwwtttdddwwtwtwwwdt', 
'wdtwtwdwtttwddtwdwwwwwddddddtwdwttw'],20,20,20)
)
print(cargo(['twwddwwdtdtdddddwwwtwtttdddwwtdwt', 'td', 'wddddwwwwwttwwdwdtddwttdww', 
'ddtttwwwwwwwtttwwdwdwwttdwtwdwwtdwt', 'wtt', 'ttdtdtdddwtdtwtwwtwtwwwdwwwtdddtwtd', 
'dwwtwtdwddddt', 'twtttw', 'ddttdwwttdtwwdwtddddddwttdddwdtwwwddwddtdw', 'ddtdddttt', 
'wttdttdddwdttwtww', 't', 'ttwttdtwdtwwd', 'wdtwdwdttdwwdwdwtwtt', 
'twwwdtttttdwttdttdtdwdwdwwtwdttwwddt', 'dwtwtwwttdtdwwdwddttwtwwtwtwttdwdtwtwtddwdttt', 
'twtwdddttwtwtdwwwddwdttwwwtddwdtwtdddwd', 
'wtttwwtwwwdwddwtddwwwwdwttwwdttdtdwttw', 'twtwdddtwddttttddwtddwwtddtwdwtt', 
'wtdwwwddtttwtddtdwwdwwwdtddd', 'wwwt', 'ddtttwwdw', 'ttdwwwwwwwdddttttddwwd', 'd', 
'dwwwwddwwdddtwtwdttwtdw', 'tddddtwtttwttttt', 
'dtwwtdwtddddwdddwwwdwwwwwdtdddtdwwdtdddwtd', 'wdttwwwtwtwt', 
'tdtwwwwwwtwttdtwdddd', 'dwwwddwddddtttwdwtdwttdtdtdtd', 
'wwdtddtdwdtdwwtdttddwttdwwtwwtwdtwttwwwddtddt', 
'wtdddtttwdtdddwwtddtdwdtdwwdtwttdddwtwtwtttdtdwtd', 
'wdwdddtdddtddtdwtdtdtwwttwtwwwwwtdddwwdddwdtwwt', 
'wdwtdwttdddwwwwtwdddtdtdwdtwwddttt', 'dtddtttwdtw', 'dwwddwwdwtdwd', 
'twwtdwdwtwtttwddwttdwtddwtdwwttwddwwtdtttdttddt', 'ttwtwddtwdwdt', 
'wdwwdddddtwdwwddwdtttwwttdwdwttdwttddttwtdww', 'tddddwwtdwddd', 
'dtwwdttdttdwwwtdtdwtwwwdwdddtdd', 'twwwddwtdtdttddtwdtwtdtd', 
'ttttwtdwwwtddwdwddwdwdwdwtwtdtwddttw', 'dwddtdwwwtdwwwtddtwdtdddtwtdww', 
'dwdwwtwwdddttdwdwtw', 'wwwtwdddwdtddwddddddwddttdwwt', 'wtttttttddwwtdwdtd', 
'dwwwddwttwdwtwddtdwddtdddddwddddwwddwdt', 'dwwwwwdttdtwtwwtttdddwwtwtwwwdt', 
'wdtwtwdwtttwddtwdwwwwwddddddtwdwttw'],50,50,50))
print(cargo(["tdwwddt", "t", "dwww", "ddww", "wwww"],3,5,4))
print(cargo(["dwtd", "td", "td", "ddd", "www"],2,1,1))
print(cargo(["d", "t", "w", "wdw", "tdt"],2,1,2)
)
print(cargo(['tdtwttdwwwwwwdtttwtwdddwwdwwtw', 'tdddwwtwdtwwtwtwwdddtdwdwdwdddww', 
'wwttwtwwtwwwwdtdtdwttdwdttdw', 'ddwdwwttwtwdwddtdt', 
'dddtddttwdwwwtdwdwddwwddtdtttwwwwwwtddtwwwtwtwtwdt', 
'ttttdwddddwdtddwdwddtttttttdwtwtdwwtwdt', 
'wttwddtdddtdwddtttttdttwtwdwtdttwtwwttwwdtwwwtdww', 
'dwwwdwdtwtttwwwttttttwdwwwwtdwtddwttdwtwtdtwwtwd', 'dddtwdwdtdtddddtdwwwtddtw', 
'wtwdtdwwwtdttwddttddwwtwddttttdttttttwdwt'],12,25,8))
print(cargo(['tdtwttdwwwwwwdtttwtwdddwwdwwtw', 'tdddwwtwdtwwtwtwwdddtdwdwdwdddww', 
'wwttwtwwtwwwwdtdtdwttdwdttdw', 'ddwdwwttwtwdwddtdt', 
'dddtddttwdwwwtdwdwddwwddtdtttwwwwwwtddtwwwtwtwtwdt', 
'ttttdwddddwdtddwdwddtttttttdwtwtdwwtwdt', 
'wttwddtdddtdwddtttttdttwtwdwtdttwtwwttwwdtwwwtdww', 
'dwwwdwdtwtttwwwttttttwdwwwwtdwtddwttdwtwtdtwwtwd', 'dddtwdwdtdtddddtdwwwtddtw', 
'wtwdtdwwwtdttwddttddwwtwddttttdttttttwdwt'],1,1,1))
print(cargo(['wwttddddddddwtdttddddtdwtdtdwdttwtwdddwtwwtwddwddt', 
'ddtttddtwwtwwwwwwddttdddtdtwdtttdwwddwwtddtdwwddtd', 
'tdtwddtdwwddtwwtdtwdwtwwwwdwtdwwdwddddwdtttddtttdd', 
'ddwtwwddttddttttdtwwwdtdtdwdwdtwdtttdwdwwtwdtdttwd', 
'ttddwwdwttdwdwwdwwddwwtwtdwddwddtddttdwdttdwdwttwd', 
'tdttwwtddwwwddttdttddttwwwwtwdwwtdwdtwttdtdwttwwtt', 
'ddwtwtwtttttwtwwdwttwdwdddddwtdddddtwwdtdwddwtdwww', 
'tddtwdwttdddtwtwtttwtwdtwtddtwwttwwwddddddwdwtwwdt', 
'twwddddtttwttdtdtwdtwddtdwtdwttwwwdwddtwdwwwddttdw', 
'ttddtddtttwwdwwtdwwdddddttwddtwdwtdtwtwwdttwtdtwdt', 
'tdwttwwdwwddddwwdwdtdwddtdtwttdttdtwwwwdwtddttwdwt', 
'ddddtwdwtttddddtwwtdttdtdtwtddwtwdwtwwwdttwtwwwwwt', 
'ttdtdwwwtddwwwdwddwwtwtdddttddddtddwwdtwdwdtdwdtdw', 
'ttwddwwdttdtdddttdtdtddddtddtwwdddddwtddtwttwdwttd', 
'tdwtdttdddwtwdttwwdwwtwttdtwdddddwtdwdtwddwdwtwwtt', 
'dttdtdtddtddtwtwtwtddwtwtwdtdwddwtttttwwtdtttwwttd', 
'twtwdtwddtwwtdtwtdwdwdwttwwdwtdttdwddwtdtdwdwwtwtd', 
'wtwwdtwwtdwdwdtddtdwdwdttddwwdwtddwttwdddtwwwdddtd', 
'dwdtdwtttwwdddtwdwdttwdddwwtddddtttdwtddwwtwtdttdd', 
'dtwwtddtwwttwtwtddddddtdwwwdtwwtwtdwddwtdtwdtdwwdd', 
'twdddwttwtttdwttdwdwdttdtddtwwdtdttdwddtwdtwtttttw', 
'wtwttwdwwdwtttddwtdwdtwdddwttdwtwwdttwtwdwtwttdwww', 
'wdtdwtdwdtdwddttddwwtdtwttwtwttdwwwwtwttdtwtwtwwwd', 
'ttdwwwwtttddwddwwtwtttwwwdddttdwttdddwdwwwwddttddw', 
'tddttdtwddtwwwdwdtwddtdwdwtdtddtwtdwwwtwdwwdwtdwtt', 
'twtdttwdddtwdttwwwwwttwdwtwtdwddtddttddtwddtddwddd', 
'wtdwtttttdwttdwdddwwddttwtdtwwdwtddtwttdwtwttdwttd', 
'ddddwttwwtwwtttdttwddtddwttdwdtwdtwdtddtwttwwwtwww', 
'dwwwdwdwwdwdwdwdtttddtddttdwwttwwwdtwttddtwddddwwd', 
'wwdtwwtttwttdwwddwtdttwwwdwwwttttwttwwdwtddwttwttw', 
'dttddwdwdtddddttdwdddtwdddtdtdwddtdddtdwdwdtddtwdw', 
'wddwdddtdwdtttddwtwdttdddtttwdwwtddttwdwwdtwdwtwdt', 
'wdtwdwwddwwwwtdtddtwwdwtdwwwtdwtwtdwwttdwdtwddtdwd',
'dtttwwttttdwtddtttddtdwtdwtwtdtddtdtwddwdtwttwdwtw', 
'dwwdddwdwwttwtdtwttddwtdttwwttdwddddtwtwdwtddwdtwt', 
'ddtwwttwdttttwtwttdtwddtdwwdwdwtwttdwtdtwwdwdddttt', 
'tdttdwwwwtwtwddddtwdtdwwwttwdtwdtdwtdtdwwddwwwddtw', 
'wddwwttdtdtwwwwdwddwtdttdtwdddtddtwdwtwwwttwdtdwwt', 
'twwdtddwtdwdddwtdwwtttdwddwdtwdtddwtdwtwwdtttdtdtt', 
'wwdwdtdddwwttttwddwtttwdtddwddttwddwdwdwtdtttwwtwd', 
'ddwtwtdwtwddwwtwwttwddttddddtwdtwtwwtwwttdtwtdwwtt', 
'wwwtwwtwwwwtddwtwwtdttdwwttddtdwtwttddddtwtddwdwww', 
'tttdtwdwdwwtdtwtwdtdddwtdtwwtwdttwdtwttdwttdwtddww', 
'ttwdttdtwwwwdttdtwdtdwdwddwwdwwwttdtdwwdwwdtdddttd', 
'ttdwwdwddtdwtdwddddtdddttwwdtwtwdwtdtdttwtdwwdtdtd', 
'wwdddwttwwdttttdtdtdtdtwtwdwwdtwdttwwttwdttddttwwd', 
'ttdddwdwdtwtwttwwwwtwdwtttddwtwdwdddwwwddwdwtdtwtw', 
'tdttwdwtwwdttdtttdttwttwdtwwwdwdtdtwwwttdtwdwtdtww', 
'tdwttwwwwwdttdwwwdtwwtttwtwtdwdwdtwttwwdwddddtttwd', 
'tdwdwtwttddwttdddwttddwtwddwdtttdwtwtwtwtddwttwddt'],50,50,50))
'''
