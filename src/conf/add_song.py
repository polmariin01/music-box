import json
import os
import directories as dir
import sys
import random as r
import shutil

'''


'''

#same_name : bool = True


# Options

def reset_json(name = "IDs.json", name2 = "existent.json"):
    dir.goto(dir.PATH_CONF)
    json_file = open(name, "w")
    json_start = {"songs": [] }
    json_file.write(json.dumps(json_start, indent=4))
    print(json.dumps(json_start))
    json_file.close()
    json_ids = open(name2,"w")
    json_ids.write("[]")
    json_ids.close()


def write_json(id=0, file_name : str =0, name = "IDs.json"):
    dir.goto(dir.PATH_CONF)
    print(os.listdir())
    #json_file = open(name)
    #print(str(json_file) + "\n" + name)
    #json_dict = json.load(json_file)
    dict_piece = {id : file_name}
    with open(name, 'r+') as j:
        contents = json.loads(j.read())
#        print(contents["songs"])
        contents["songs"].append(dict_piece)
#        print(contents)
        j.close()
    with open(name, 'w') as j:
        j.write(json.dumps(contents, indent=4))
        j.close()    
    
    return
    json_dict = json.load(json_file)
    dict_piece = json.dump({id : file_name})
    print(dict_piece)
#    print(json_dict)
    # Mirar si ja existeix
    json_file.close()


def IDexists(id, file_name="existent.json"):
    
    with open(dir.PATH_CONF + file_name, 'r') as j:
        contents = json.loads(j.read())
        j.close()
        if id not in contents:
            contents.append(id)
            with open(dir.PATH_CONF + file_name, 'w') as j:
                j.write(json.dumps(contents))
                j.close()
            return False
        return True


def generate_ID(random = True, file_name = "existent.json"):

    #id = random.randint(0,999999)
    if random:
        id = format(r.randint(0,999999), '06d') #TODO else hash of name

    while(IDexists(id)):        
        id = format(r.randint(0,999999), '06d')
    print("Nova ID: " + id)
    return id

def isTypeFile(file: str, ftype = "mp3"):
    #Default .mp3
    if len(file) > 4:
        return file.endswith(ftype)
    return False

def all_sort(v = False):
    dir.goto(dir.PATH_UNFILTERED)
#   os.chdir(dir.PATH_UNFILTERED)
    arxius = os.listdir()
    if len(arxius) < 1:
        print("Unfiltered directory empty.")
        return
    arxius_mp3 = list(filter( isTypeFile, arxius))
    if v:
        print("Llista arxius:\n" + str(arxius) + "\n")
        print("Llista arxius filtrats:\n" + str(arxius_mp3) + "\n")
    for files in arxius_mp3:
        dir.goto()
        pdf_name = files.replace(".mp3",".pdf")
        if os.path.exists(dir.PATH_UNFILTERED + pdf_name):
            id = generate_ID()
            write_json(id = id, file_name = files)
            dir.goto()
            #TODO actually moure i tal els arxius
            shutil.move(dir.PATH_UNFILTERED + files, dir.PATH_AUDIO + id + ".mp3")
            shutil.move(dir.PATH_UNFILTERED + pdf_name , dir.PATH_PDF + id + ".pdf")
        else:
            print(files + " has no PDF\n")


def main():
    args = sys.argv[1:]
    #all_sort()
    all_list = ['all']
    print("MAIN\n****")
    # 1. Check for the arg pattern:
    #   python3 affirm.py -affirm Bart
    #   e.g. args[0] is '-affirm' and args[1] is 'Bart'
    print(args)
    if len(args) >= 1:
        if args[0] in all_list:
            print("ADD ALL SONGS")
            all_sort()
            # Funció principal, extreure tot

        elif args[0] in ['start','init','s','restart','reset']:
            # Select random nice phrase
            # affirmation = random.choice(AFFIRMATIONS)
            # Print with the name in args[1]
            #print(affirmation, args[1])
            print("RESTART JSONS")
            reset_json()
        elif args[0] in all_list:
            print("all")
        else:
            print("No opció correcta")
    # .. later if statements for -hello and -n ...

#all_sort()

#random.randint()

#create_json()
#write_json("asdasdff", 12223)
#write_json()
main()