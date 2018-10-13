import json
import sys
import os
from glob import glob
from distutils.version import StrictVersion

def env_error():
    with open('errors.txt', 'w') as log:
        log.write('''Local App Data Enviornment Variable Not Found. \n
                     Please place your chrome intsall directory in the config.txt file.''')
    return

def stream_keys_error():
    with open('errors.txt', 'w') as log:
        log.write('Stream Keys install directory not found.\n Please make sure this is the directory for your current chrome installation')
    return
    
def chrome_dir_error():
    with open('errors.txt', 'w') as log:
        log.write('Chrome directory not found.\n Please place your chrome directory in the config.txt file.')
    return

def find_chrome_default():
    try:
        local_app_data = os.environ.get('LOCALAPPDATA')
    except KeyError:
        env_error()
        return False
    
    default_chrome = os.path.join(local_app_data,'Google','Chrome','User Data', 'Default')
        
    if not os.path.exists(default_chrome):
        chrome_dir_error()
        return False
    
    return default_chrome

def find_json_files(default_chrome):
    if not os.path.exists(default_chrome):
        chrome_dir_error()
        return False
    
    stream_keys_default = os.path.join(default_chrome,'Extensions','ekpipjofdicppbepocohdlgenahaneen')
    
    if not os.path.exists(stream_keys_default):
        stream_keys_error()
        return False
    
    versions = []
    for version_directory in glob(os.path.join(stream_keys_default,'*','')):
        version = os.path.basename(os.path.normpath(version_directory))
        version = version[:version.find('_')]
        versions.append(StrictVersion(version))
    
    if not bool(versions):
        stream_keys_error()
        return False
    
    stream_keys_manifest = os.path.join(stream_keys_default, str(max_version(versions)), 'manifest.json')
    
    if not os.path.exists(stream_keys_manifest):
        stream_keys_error()
        return False
    
    preferences = os.path.join(default_chrome, 'Preferences')
    if not os.path.exists(preferences):
        chrome_dir_error()
        return False

    
    return (stream_keys_default,preferences)


def chrome_dir_config():
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
        
    return chrome_dir

def max_version(versions):
    for i,version in enumerate(versions):
        if i == 0:
            max_vers = version
        if version > max_vers:
            max_vers = version
    return max_vers
def main():    
    chrome_dir = chrome_dir_config()
    print (chrome_dir)
    if not bool(chrome_dir):
        chrome_dir = find_chrome_default()
        print (chrome_dir)
        if not bool(chrome_dir):
            return
    
    paths = find_json_files(chrome_dir)
    if not bool(paths):
        return
    
    streamkeys_manifest, preferences = paths 
    
    if sys.argv[1] == 'start':
        val = False
    if sys.argv[1] == 'close':
        val = True
    

    with open(streamkeys_manifest, 'r+') as sk:
        data = json.load(sk)
        for _,item in data['commands'].items():
            item['global'] = val
        sk.seek(0)
        json.dump(data, sk, indent=4)
        sk.truncate()
    
    with open(preferences, 'r+') as pref:
        data = json.load(pref)
        for _, item in data['extensions']['commands'].items():
            item['global'] = val
        pref.seek(0)
        json.dump(data, pref)
        pref.truncate()

if __name__ == '__main__':
    main()