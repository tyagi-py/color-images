mkdir models
wget https://github.com/richzhang/colorization/blob/master/colorization/resources/pts_in_hull.npy?raw=true -O ./models/pts_in_hull.npy
wget https://raw.githubusercontent.com/richzhang/colorization/master/colorization/models/colorization_deploy_v2.prototxt -O ./models/model_prototext.prototxt
wget http://eecs.berkeley.edu/~rich.zhang/projects/2016_colorization/files/demo_v2/colorization_release_v2.caffemodel -O ./models/model.caffemodel
