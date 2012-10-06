Make sure all script files are executable. (chmod +x <filename>)

Add custom cleaning to clean.sh
(You might also want to alter the chapter.py which splits files into chapters)

When done run:
./epub_cleaner.sh <your epub file>

The output file will be called 'clean.epub'. Rename it as you like.

NOTE: A tmp folder is used and will be deleted when running the script. The tmp folder is named 'tmp' and you will not be prompted before it is deleted.

Linux/OSX only. (should run fine in Cygwin though)
