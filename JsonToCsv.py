import json
import numpy as np
import pandas as pd

jsondata = ""

filename = input("Enter Input Filename : ")
with open(filename, "r") as jsonfile:
    jsondata = json.load(jsonfile)

data = []
headers = []

truearr = []

arrheader = ""

for key in jsondata:
    if (isinstance(jsondata[key], list)):
        for subdata in jsondata[key]:
            data1 = data.copy()
            for key1 in subdata:
                if (isinstance(subdata[key1], list)):
                    for subsubdata in subdata[key1]:
                        data2 = data1.copy()
                        for key2 in subsubdata:
                            if (isinstance(subsubdata[key2], list)):
                                for subsubsubdata in subsubdata[key2]:
                                    data3 = data2.copy()
                                    for key3 in subsubsubdata:
                                        if(isinstance(subsubsubdata[key3], list)):
                                            pass
                                        else:
                                            if ((key + "__" + key1 + "__" + key2 + "__" + key3) not in headers):
                                                headers.append(key + "__" + key1 + "__" + key2 + "__" + key3)
                                            if (subsubsubdata[key3] == None):
                                                data3.append("null")
                                            else:
                                                data3.append(subsubsubdata[key3])
                                    truearr.append(data3)
                            else:
                                if ((key + "__" + key1 + "__" + key2) not in headers):
                                    headers.append(key + "__" + key1 + "__" + key2)
                                if (subsubdata[key2] == None):
                                    data2.append("null")
                                else:
                                    data2.append(subsubdata[key2])
                else:
                    if ((key + "__" + key1) not in headers):
                        headers.append(key + "__" + key1)
                    if (subdata[key1] == None):
                        data1.append("null")
                    else:
                        data1.append(subdata[key1])
    else:
        if (key not in headers):
            headers.append(key)
        if (jsondata[key] == None):
            data.append("null")
        else:
            data.append(jsondata[key])

numpy_data = np.array(truearr)
df = pd.DataFrame(data=numpy_data, columns=headers)

output = input("Enter Output Filename : ")

df.to_csv(output, index=False)