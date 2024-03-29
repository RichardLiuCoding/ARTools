# ARTools
A collection of Python codes to analyze and visualize SPM data acquired on AR machines, including MFP3D, Cypher, Jupier SPM.

Designed for users who just want to quickly analyze and visualize SPM data in large batch with Python.

For more advanced analysis of SPM and other microscopy data, please have a look at [SciFiReaders](https://github.com/pycroscopy/SciFiReaders) project.

# Installation:

```Python
pip install aespm
```

Use of artools:

```Python
import aespm.tools as at
```

# Example uses:
* Load and display a single ibw image:
```Python
import aespm.tools as at
file_name = 'ibw/H120009.ibw'
t = at.display_ibw(file_name, key=['Height'], titles='Height', save='test')
```
* Load and display all the ibw images in a folder:
```Python
# If mode and key are both None, every channel in every image file will be displayed
folder = 'ibw'
fnames, ibw_data = at.display_ibw_folder(folder=folder, mode=None, key=None)
```
* Load and display only "AC Mode" in a folder with different color maps:
```Python
# Only the AC mode and the Height Phase and ZSensor channels will be displayed
# Save the image
at.display_ibw(file = ibw_data[-1], key=['Height', 'Phase'], titles=['Height', 'Phase'], 
               cmaps=[plt.cm.viridis, plt.cm.Blues], save="test")
```
* Load and display all the DART switching spectroscopy (hysteresis loop):
```Python
folder = 'ibw'
for ix in os.listdir(folder):
    if ix.endswith('.ibw'):
        t = at.load_ibw(file=os.path.join(folder, ix))
        if t.mode == 'Spec':
            fig, ax=plt.subplots(1, 2, figsize=[9,4])
            ax[0].plot(t.bias, t.amp_off, '.-')
            ax[1].plot(t.bias, t.phase1_off, '.-')    
            ax[0].set_title('Piezo response (a.u.)')
            ax[1].set_title('Phase 1')
            for axis in ax:
                axis.set_xlabel('Bias (V)')
```

# Usages:

* Working on colab:
  ```Python
  !pip install aespm
  import aespm.tools as at
  ```
* Example notebook: Copy [link](https://drive.google.com/file/d/1oQNA_NjmEttzpAH3-2YDk8XcsrdZWWW2/view?usp=sharing) to your google drive.
* Either import your data folder using gdown or mount your drive to this notebook.
* Working locally:
  ```Python
  !pip install aespm
  import aespm.tools as at
  ```
  and start having fun!

# Functions:

* load_ibw(): load ibw file with header and channels automatically parsed from the data file.
  * Currently support "AC Mode", "Contact Mode", "PFM Mode", "DART Mode" and "Spec" (spectroscopy files).
* display_ibw(): visualize a single ibw file with specified channels and options to save the image.
* display_ibw_folder(): visualize all the ibw files in a folder with the option to specify imaging mode and channels to display

# To-do:
* Add support for SKPM mode
* Add option to display the specified parameter (like surface voltage, tip voltage, etc.) on the figure
* Add support for more spectroscopy data format
