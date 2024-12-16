



def main():
    from pathlib import Path

    folder_path = Path("path")
    files = [f.name for f in folder_path.iterdir()] 
    try:
        for i in files:
            old_name = Path("path\{}".format(i))  
            new_name = Path("path\{}".format("backup_new" + i))  
    
            old_name.rename(new_name)
    except:
        raise "Error"
    
    
    






if __name__ == "__main__":
    main()