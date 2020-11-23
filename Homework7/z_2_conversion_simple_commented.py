import re
import yaml

"""
1. load bibtex file
    - bibliography should be curated in Zotero (one can program cleaning procedures into the script, but this is not as reliable);
    - loading bibtex data, keep only those records that have PDFs;
    - some processing might be necessary (like picking one file out of two and more)
2. convert into other formats
    - csv
    - json
    - yml
"""

###########################################################
# VARIABLES ###############################################
###########################################################

settingsFile = "z_config.yml" #to define your settings file
settings = yaml.load(open(settingsFile), Loader = yaml.FullLoader) # to define the settings you need
bibKeys = yaml.load(open("zotero_biblatex_keys.yml"), Loader = yaml.FullLoader) #to define your newly created YAML file with the keys you need

###########################################################
# FUNCTIONS ###############################################
###########################################################

# load bibTex Data into a dictionary
def bibLoad(bibTexFile):

    bibDic = {} #create an empty dictionary

    with open(bibTexFile, "r", encoding="utf8") as f1: #open your BibTex file
        records = f1.read().split("\n@") #read your file as one big string and split it into single records

        for record in records[1:]: #loop through each of these records except for the first one 
            # let process ONLY those records that have PDFs
            if ".pdf" in record.lower(): # #record.lower so that there won't be any issues with case sensitivity

                record = record.strip().split("\n")[:-1] #get rid of the white spaces and split each record into key-value-pairs

                rType = record[0].split("{")[0].strip() #split the first element of the list to get the type of the record
                rCite = record[0].split("{")[1].strip().replace(",", "") #split the first element to get the Citation Key

                bibDic[rCite] = {} #specify your empty dictionary
                bibDic[rCite]["rCite"] = rCite #add a record into your dictionary using citationKey as a key value
                bibDic[rCite]["rType"] = rType #add recordType into the newly created record
                #process the rest of the record
                for r in record[1:]: #loop through the rest of the record
                    key = r.split("=")[0].strip() #get the key of each key-value-pair of your record
                    val = r.split("=")[1].strip() #get the value of each key-value-pair of your record
                    val = re.sub("^\{|\},?", "", val) #get rid of unwanted characters

                    fixedKey = bibKeys[key] #get the fixed keys from your YAML file

                    bibDic[rCite][fixedKey] = val #get the value according to the fixed key


    print("="*80) #print a line of equal signs
    print("NUMBER OF RECORDS IN BIBLIGORAPHY: %d" % len(bibDic)) #print the number of records in your dictionary
    print("="*80) #print a line of equal signs
    return(bibDic) #return your function

# CONVERSION FUNCTIONS

import json #import the json library
def convertToJSON(bibTexFile): #define a function to convert your bibTexfile to JSON
    data = bibLoad(bibTexFile) #load your data
    with open(bibTexFile.replace(".bib", ".json"), 'w', encoding='utf8') as f9: #replace the extension of your file
        json.dump(data, f9, sort_keys=True, indent=4, ensure_ascii=False) #save your dictionary into a JSON file


import yaml #import the yaml library
def convertToYAML(bibTexFile): #define a function to convert your bibTexfile to YAML
    data = bibLoad(bibTexFile) #load your data
    with open(bibTexFile.replace(".bib", ".yaml"), 'w', encoding='utf8') as f9: #replace the extension of your file
        yaml.dump(data, f9) #save your dictionary into a YAML file

# CSV is the trickest because bibTeX is not symmetrical
def convertToCSV(bibTexFile): #define a function to convert your bibTexfile to CSV
    data = bibLoad(bibTexFile) #load your data
    # let's handpick fields that we want to save: citeKey, type, author, title, date
    headerList = ['citeKey', 'type', 'author', 'title', 'date'] #create a list with keys you want to save
    header = "\t".join(headerList) #add that list

    dataNew = [header] #turn that list into a string

    for k,v in data.items(): #loop through the key-value-pairs
        citeKey = k #define your citation key as key

        if 'rType' in v: #check for the type of the record
            rType = v['rType'] #add the type of the record
        else:
            rType = "NA" #add 'no data'

        if 'author' in v: #check for the author
            author = v['author'] #add the author
        else:
            author = "NA" #add 'no data'

        if 'title' in v: #check for the title
            title = v['title'] #add the title
        else:
            title = "NA" # add 'no data'

        if 'date' in v: #check for the date
            date = v['date'] #add the date
        else:
            date = "NA" #add 'no data'

        tempVal = "\t".join([citeKey, rType, author, title, date]) #create a temporary variable to create all actual values in the same way
        dataNew.append(tempVal) #add this temporary variable to your string

    finalData = "\n".join(dataNew) #create a new variable
    with open(bibTexFile.replace(".bib", ".csv"), 'w', encoding='utf8') as f9: #replace the extension of your file
        f9.write(finalData) #create a CSV file


###########################################################
# RUN EVERYTHING ##########################################
###########################################################

print(settings["bib_all"]) #print your settings

#convertToJSON(settings["bib_all"])
#convertToYAML(settings["bib_all"])
#convertToCSV(settings["bib_all"])
    #call your functions

print("Done!")