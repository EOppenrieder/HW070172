import os, yaml

###########################################################
# VARIABLES ###############################################
###########################################################

settingsFile = "z_config.yml" #to define the file with the settings for the BibTex-files
vars = yaml.load(open(settingsFile), Loader = yaml.FullLoader) #to define the variables you need


###########################################################
# FUNCTIONS ###############################################
###########################################################

# analyze bibTeX data; identify what needs to be fixed

def bibAnalyze(bibTexFile):
#to analyze your BibTexFile which you exported from
#Zotero to see what you need to fix
    tempDic = {} #create an empty dictionary to be filled

    with open(bibTexFile, "r", encoding="utf8") as f1: #open your BibTexFile, do not forget about the Unicode encodings!
        records = f1.read() #read the file as one big string
        records = records.split("\n@") #split into single records

        for record in records[1:]: #loop through each of these records
            # let process ONLY those records that have PDFs
            if ".pdf" in record.lower(): #record.lower so that there won't be any issues with case sensitivity
                record = record.strip() #to get rid of the white spaces
                record = record.split("\n")[:-1] #to split each record into key-value-pairs

                for r in record[1:]: #loop through the key-value-pairs
                    r = r.split("=")[0].strip() #extract the key

                    if r in tempDic: 
                        tempDic[r] += 1 #add one occurrence of a key
                    else:
                        tempDic[r] = 1 #add the first occurrence of a key

    results = [] #create an empty list
    for k,v in tempDic.items(): 
        result = "%010d\t%s" % (v, k) #create a variable for the occurrences-key-pairs
        results.append(result) #add the results

    results = sorted(results, reverse=True) #sort the results, beginning with the key with the most occurrences
    results = "\n".join(results) #add the results

    with open("bibtex_analysis.txt", "w", encoding="utf8") as f9:
        f9.write(results) #create a file where you store the results

bibAnalyze(vars['bib_all']) #call the function with the settings you defined in your settings file



