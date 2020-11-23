import re
import yaml
import os
import shutil

###########################################################
# VARIABLES ###############################################
###########################################################

settingsFile = "z_config_new.yml" #to define your settings file
settings = yaml.load(open(settingsFile), Loader = yaml.FullLoader) # to define the settings you need
bibKeys = yaml.load(open("bibtex_Habsburg_newkeys.yml"), Loader = yaml.FullLoader) #to define your newly created YAML file with the keys you need

###########################################################
# FUNCTIONS ###############################################
###########################################################
def bibLoad(bibTexFile):
# load bibTex Data into a dictionary
    bibDic = {} #create an empty dictionary

    with open("Habsburg.bib", "r", encoding="utf8") as f1: #open your BibTex file
        records = f1.read().split("\n@") #read your file as one big string and split it into single records

        for record in records[1:]: #loop through each of these records except for the first one
            # let process ONLY those records that have PDFs
            if ".pdf" in record.lower(): #record.lower so that there won't be any issues with case sensitivity
                completeRecord = "\n@" + record #create a new variable for the complete record

                record = record.strip().split("\n")[:-1] #get rid of the white spaces and split each record into key-value-pairs

                rType = record[0].split("{")[0].strip() #split the first element of the list to get the type of the record
                rCite = record[0].split("{")[1].strip().replace(",", "") #split the first element to get the Citation Key

                bibDic[rCite] = {} #specify your empty dictionary
                bibDic[rCite]["rCite"] = rCite #add a record into your dictionary using citationKey as a key value
                bibDic[rCite]["rType"] = rType #add recordType into the newly created record
                bibDic[rCite]["completeR"] = completeRecord #add the complete record
                #process the rest of the record
                for r in record[1:]: #loop through the rest of the record
                    key = r.split("=")[0].strip() #get the key of each key-value-pair of your record
                    val = r.split("=")[1].strip() #get the value of each key-value-pair of your record
                    val = re.sub("^\{|\},?", "", val) #get rid of unwanted characters

                    fixedKey = bibKeys[key] #get the fixed keys from your YAML file
                    if fixedKey == "file": #check for the file value
                        if ";" in val:
                            temp = val.split(";") #split if there are two values 
                            for i in temp:
                                if i.endswith(".pdf"): #keep only the one with pdf
                                    val = i
                                    break
                                


                    bibDic[rCite][fixedKey] = val #get the value according to the fixed key

    
    print(bibDic) #print your dictionary 
    return(bibDic) #return your dictionary
    
dictionary = bibLoad(settings["bib_all"]) #choose your predefined settings

def folderMaker(rCite): #define a function to create your folders
    temppath = os.path.join(settings["memex_path"], rCite[0], rCite[:2], rCite) #define how to create your folderpath
    if not os.path.exists(temppath):
            os.makedirs(temppath) #create your folderpath 
    print(temppath) #print your folderpath
    return temppath #return your folderpath

def copySafe(metadata): 
    for k, v in metadata.items(): #loop through the key-value-pairs
        publpath = folderMaker(k) #create the path according to the citation key
        tempFile = open(publpath + "\\" + k + ".bib", "w", encoding="utf8") #create a bib-file
        print(v["completeR"], file= tempFile) #print your bib-File
        pdfPath = v["file"] #get the previous path of your pdf
        pdfPath = pdfPath.replace("\\\\", "\\") #get rid of the backlashes
        pdfPath = pdfPath.replace("\\:", ":") #get rid of the backlashes
        #print(pdfPath)
        #print(publpath+k+".pdf")
        if not os.path.isfile(publpath):
            shutil.copyfile(pdfPath, publpath + "\\" +k+".pdf") #copy your PDF to the new destination

copySafe(dictionary) 






