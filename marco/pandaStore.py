## Red Bird program (store each recording) <Hermia>
import numpy as np
import pandas as pd

"""
param inputdict --> dict input (x to be updated here)
param inputtodf --> dataframe input
dataframe df--> dataframe input appeds to df
param storedict --> temporary store the dictonary in each recording to b undated later to elsewhere
"""

class Record():
    def __init__(self, columns=[], storeDict = False):
        self.dataFrame = pd.DataFrame(columns=columns)
        self.storeDict = storeDict
        self.dicts = []



    ## input type: dictionary (nested)
    ## return type: dictionary
    ## function action: Convert nested dictionry input to dictionary (internal function --> used in appendData)
    def flattendData(self, data):
        flattened_data = data["data"]
        flattened_data["time"] = data["time"]   
        return flattened_data

    
    ## input type: dictionary
    ## return type: /
    ## function action: If have dictonary, append new dictionary to dataframe
    ## Can print out the dictionary
    def appendData(self, data, verbose = False):

        self.dataFrame = pd.concat([
            self.dataFrame, 
            pd.DataFrame(self.flattendData(data), 
            index = [len(self.dataFrame)])
        ])

        if self.storeDict:
            self.dicts.append(data)

        if verbose:
            print(self.dataFrame)

    
    ## input type: /
    ## output type: /
    ## function action: print first 5 rows of the pd dataframe (for viewing purpose)
    def showDataHead(self):
        print(self.dataFrame.head())



    ## input type: /
    ## output type: /
    ## function action: print all columns of the pd dataframe(for viewing purpose)
    def showAllData(self):
        pd.set_option("display.max_rows", len(self.dataFrame))
        print(self.dataFrame)
        pd.reset_option("display.max_rows")



    ## input type: json file name (in same folder)
    ## output type: / 
    ## function action: load in dataframe to the program and update/rewrite/OVERWRITE!!! self.df(dataframe) aft the same time
    def loadData(self, path):
        """
        Caution: Overwrites existing dataframe.
        """
        self.dataFrame = pd.read_json(path)


    ## input type: json file name (in same folder)
    ## output type: /
    ## function action: save updated dataframe/json file
    def saveData(self, path):
        self.dataFrame.to_json(path)