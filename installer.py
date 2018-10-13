import os
import subprocess
from glob import glob

def env_error():
    with open('errors.txt', 'w') as log:
        log.write('''Local App Data Enviornment Variable Not Found. \n
                     Please place your chrome intsall directory in the config.txt file.''')

def plexamp_dir_error():
    with open('errors.txt', 'w') as log:
        log.write('Plexamp directory not found.\n Please update your plex directory in the config.txt file.')

def default_plexamp_dir():
    try:
        local_app_data = os.environ.get('LOCALAPPDATA')
    except KeyError:
        env_error()
        return False
    
    plexamp_dir = os.path.join(local_app_data,'Programs','plexamp')
    if not os.path.exists(plexamp_dir):
        return False
    
    return plexamp_dir

def check_dir(path):
    if not os.path.exists(path):
        plexamp_dir_error()
        return False
    return True

def plexamp_config():
    if not os.path.exists('config'):
        with open('config.txt' ,'w') as config:
            config.write('Chrome=\n')
            config.write('Plexamp=\n')
    
    with open('config.txt', 'r') as config:
        paths = config.readlines()
        plexamp_dir = ''
        chrome_dir = ''
        for path in paths:
            if 'Plexamp' in path:
                plexamp_dir = path[path.find('=')+1:].strip()
            if 'Chrome' in path:
                chrome_dir = path[path.find('=')+1:].strip()
        
    with open('config.txt', 'w') as config:
        config.write('Chrome=%s\n'%chrome_dir)
        config.write('Plexamp=%s\n'%plexamp_dir)    
        
    return plexamp_dir

def main():
    plexamp_dir = plexamp_config()
    if not bool(plexamp_dir):
        plexamp_dir = default_plexamp_dir()
    
    
    plexamp_dir = os.path.join(plexamp_dir,'Plexamp.exe')
    if not check_dir(plexamp_dir):
        return
    
    
    current_path = os.path.abspath(os.getcwd())
    if len(glob(os.path.join(current_path,'*.py'))) > 0:
        fix_keys = os.path.join(current_path,'update_chrome_files.py')
        with open('launch.bat', 'w') as launcher:
            launcher.write('python %s start\n'%fix_keys)
            launcher.write('start /b /wait "" %s\n'%plexamp_dir)
            launcher.write('python %s close'%fix_keys)
    else:
        fix_keys = os.path.join(current_path,'update_chrome_files.exe')
        with open('launch.bat', 'w') as launcher:
            launcher.write('start /b /wait %s start\n'%fix_keys)
            launcher.write('start /b /wait "" %s\n'%plexamp_dir)
            launcher.write('start /b /wait %s close'%fix_keys)
    
    with open('Plexamp (Media Key Fix).vbs', 'w') as vbs:
        vbs.write('Set oShell = CreateObject ("Wscript.Shell")\n')
        vbs.write('Dim StrArgs\n')
        bat = os.path.join(current_path,'launch.bat')
        vbs.write('StrArgs = "cmd /c %s"\n'%bat)
        vbs.write('oShell.Run strArgs, 0, false')
    
    shortcut_link = os.path.join(current_path,'Plexamp (Media Key Fix).vbs')
    with open('make_shortcut.vbs', 'w') as short:
        short.write('Set WshShell = CreateObject("Wscript.shell")\n')
        short.write('strDesktop = WshShell.SpecialFolders("Desktop")\n')
        short.write('set oMyShortcut = WshShell.CreateShortcut(strDesktop & "\\Plexamp (Media Key Fix).lnk")\n')
        short.write('oMyShortcut.WindowStyle = 1\n')
        short.write('oMyShortcut.IconLocation = "%s,0"\n'%plexamp_dir)
        short.write('oMyShortcut.TargetPath = "%s"\n'%shortcut_link)
        short.write('oMyShortcut.Description = "Shortcut to the Streamkeys Plexamp Fix"\n')
        short.write('oMyShortcut.WorkingDirectory = "%s"\n'%current_path)
        short.write('oMyShortcut.Save')
    subprocess.call('cmd /c make_shortcut.vbs')
    os.remove('make_shortcut.vbs')
            
if __name__ == '__main__':
    main()
    
    
