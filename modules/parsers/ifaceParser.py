from pandas import DataFrame

def parse_brief(result):

    result = result.split("\n")
    del result[0]
    
    for i in range(len(result)):
    
        result[i] = result[i].split(" ")
    
        while("" in result[i]):
            result[i].remove("")
    
        if("administratively" in result[i]):
            result[i].remove("administratively")
    
        del result[i][2]
        del result[i][2]
    print(result)
    
    df = DataFrame(result, columns=['iname', 'address', 'status', 'protocol'])
    
    return df