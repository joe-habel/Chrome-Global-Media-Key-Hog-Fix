from cx_Freeze import setup, Executable
# NOTE: you can include any other necessary external imports here aswell
 
includefiles = ['config.txt','readme.md'] # include any files here that you wish
includes = []
excludes = []
packages = []
 
chrome = Executable(
 # what to build
   script = "update_chrome_files.py", # the name of your main python script goes here 
   targetName = "update_chrome_Files.exe", # this is the name of the executable file
)

installer = Executable(
 # what to build
   script = "installer.py", # the name of your main python script goes here 
   targetName = "Setup.exe", # this is the name of the executable file
)
 
setup(
 # the actual setup & the definition of other misc. info
    name = "Global Chrome Fixer", # program name
    version = "0.1",
    author = "Joe Habel",
    options = {"build_exe": {"excludes":excludes,"packages":packages,
      "include_files":includefiles}},
    executables = [chrome,installer]
)
