# ARTools
A collection of Python codes to analyze and visualize SPM data acquired on AR machines.

Designed for users who just want to quickly analyze and visualize SPM data in large batch with Python.

For more advanced analysis of SPM and other microscopy data, please have a look at [SciFiReaders](https://github.com/pycroscopy/SciFiReaders) project.

# Example uses:
* Load and display a single ibw image:
```Python
file_name = 'ibw/H120009.ibw'
t = display_ibw(file_name, key=['Height'], titles='Height', save='test')
```
* Load and display all the ibw images in a folder:
```Python
# If mode and key are both None, every channel in every image file will be displayed
folder = 'ibw'
fnames, ibw_data = display_ibw_folder(folder=folder, mode=None, key=None)
```
* Load and display only "AC Mode" in a folder:
```Python
# Only the AC mode and the Height Phase and ZSensor channels will be displayed
folder = 'ibw'
fnames, ibw_data = display_ibw_folder(folder=folder, mode='AC Mode', key=['Height', 'Phase', 'ZSensor'])
```
* Load and display a single DART switching spectroscopy (hysteresis loop):
```Python
t = load_ibw(file, ss=True)
fig, ax=plt.subplots(1,2,figsize=[9,4])
ax[0].plot(t.bias, t.phase1_off)
ax[0].set_title('Phase1_off')
ax[1].plot(t.bias, t.amp_off)
ax[1].set_title('Amp_off')
```

# Insllation:

* Working on colab: copy this notbook ([link](https://colab.research.google.com/drive/1hvjodEQ5AKng_S1Sr_u-DvzeF41jMDZ9?usp=sharing]) to your google drive and either import your data folder using gdown or mount your drive to this notebook.
* Working locally: download the IBW_file_explorer.ipynb to where your data folder lives on your local computer and start having fun!

# Functions:

* load_ibw(): load ibw file with header and channels automatically parsed from the data file.
* display_ibw(): visualize a single ibw file with specified channels and options to save the image.
* display_ibw_folder(): visualize all the ibw files in a folder with the option to specify imaging mode and channels to display

# To-do:
* Add support for SKPM mode
* Add option to display the specified parameter (like surface voltage, tip voltage, etc.) on the figure
* Add support for more spectroscopy data format
