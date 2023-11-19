### LoaderScript

LoaderScript is a Python script that creates a hierarchical directory structure with specified levels of depth and 
populates the directories with random files.

### Guideline

1. Install Python: Make sure you have Python installed on your system.
2. Have a sufficeint amount of space to handle this file system creation, I recommend for depth of 5 and file 
   range from 10kb to 1 mb ateleast reserve 100 TB of space.
3. Expect code to take long time to run as there are recursive calls and random file generation is taking place. 
   (Given the depth is on higher level and consolidated FS size is large)
4. Use the script responsibly and consider testing on a smaller scale before creating a massive filesystem.

