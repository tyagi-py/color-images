# color-images

This is a python script that fill colors in Black & White images. 
It uses Caffe (A Deep Learning framework) model and OpenCV.


![Grey Apple](https://raw.githubusercontent.com/TyagiSumit/color-images/master/sample/gray.jpeg) 
![Colored Apple](https://raw.githubusercontent.com/TyagiSumit/color-images/master/sample/graycolor.png)

![Grey Rose](https://raw.githubusercontent.com/TyagiSumit/color-images/master/sample/rose.jpg) 
![Colored Rose](https://raw.githubusercontent.com/TyagiSumit/color-images/master/sample/rosecolor.png)



## Installation

To prevent the dependencies of this project from messing with your core python installation, you can create a [virtualenv](https://virtualenv.pypa.io/en/latest/).

Now, use pip to install the dependencies using:
```
pip install -r requirements.txt
```

Now, we need to download the models, which can be done by the following:

for linux:
```bash
chmod +x get_models.sh
./get_models.sh
```
for windows:
run [get_models.bat](https://github.com/TyagiSumit/color-images/blob/master/get_model.bat) file


## Usage
```bash
python fill_color.py --input /path/to/input/image 
```
output will be saved in same folder 

## Model used:

http://eecs.berkeley.edu/~rich.zhang/projects/2016_colorization/files/demo_v2/colorization_release_v2.caffemodel

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

