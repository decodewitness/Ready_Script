# Readyscript-1

This script will read your documents out loud.
Change the input file which is stored in the "filename" variable, to whatever document you want to have the program read out loud.

----------

E.g.:

    filename = "my_document.txt"

(to read 'my_document.txt' from the same directory)



If you want for instance to read the 'my_document.txt' file and it's in your Windows Downloads folder you can use the full path like (don't forget to change <your username> to the name of your Windows user username, e.g. "Administrator"):

    filename = "C:\Users\<your username>\Downloads\my_document.txt"

---------
Project: Readyscript-1<br>
Version: v.0.1-2b<br>
---------
Filename: 07.Readyscript-1.ipynb<br>
Author: Vera Lo<br>
Date: 05/05/2022<br>
Email: <N/A><br>

---------<br>
Run with Jupyter Notebook, first install Jupyter Notebook, then open our file from the Jupyter Notebook program<br>.
<br>
E.g.:

    # To install Anaconda3 download it from the Anaconda website.
    
    # Install Anaconda3...
    
    # Then run the Anaconda Prompt from the start menu, by opening the menu, and typing the first letters of Anaconda.
    # if installed correctly it should pop up in about 3-4 keystrokes.
    
    # From the Anaconda Prompt, navigate to the folder where your "07.Readyscript-1.ipynb" is located.
    # Type the following in your Home directory, which ends with your username:
    
    cd Documents
    dir
    
    
    # If everything is okay, you should see the script in your Documents folder, or any other folder,
    # where you downloaded it.
    
    Example:
    ------------
(ml) C:\Users\user_name\Documents>dir<br>
Volume in drive C has no label.<br>
Volume Serial Number is 1027-DF85<br>
<br>
Directory of C:\Users\user_name/Documents\<br>
<br>
05/05/2023  10:04    <DIR>          .<br>
23/04/2023  22:57    <DIR>          ..<br>
05/05/2023  09:58    <DIR>          .ipynb_checkpoints<br>
05/05/2023  10:04            10.485 07.Readyscript-1.ipynb<br>
05/05/2023  09:53           158.422 Readyscript-1.ipynb<br>
05/05/2023  09:31           154.755 my_text_file.txt<br>
              3 File(s)        323.662 bytes<br>
              3 Dir(s)  55.155.699.712 bytes free<br>
<br>
    
    -----------
    
    # Switch into your Python environment, if you're using Anaconda3 Prompt.
    # Change <workspace name> into the name of your workspace, e.g. "ml".
    
    conda activate <workspace name>
    
    # or, to switch to a workspace name called "ml", type:
    
    conda activate ml
    
    ----------
    
    # To install Jupyter Notebook type the following:
    pip install jupyter
    
    # To run Jupyter Notebook type the following:
    jupyter notebook

    ----------
    
    # To start the program, make sure it is in the same directory you're starting Jupyter Notebook from,
    
    # If you have our file Ready Script-1 in your "Documents" folder, e.g.:
    # inside: "C:/Users/Administrator/Documents/07.Readyscript.ipynb".
    # Then you open Jupyter Notebook from "Documents", so that our script is in the same folder as where
    # you are working.
    
    ----------
    
    # Select the script from the main Jupyter Notebook window, which should open in your browser,
    # after starting the Jupyter Notebook program.
    
    # Or, try pressing CTRL and the mouse on the link i.e.: (CTRL + left-mouse-button).
    # Click on one of the bottom links in the console to open the window for Jupyter Notebook in your browser.
