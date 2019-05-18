mkdir models
cd models
powershell -command "& { [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 ; iwr  http://eecs.berkeley.edu/~rich.zhang/projects/2016_colorization/files/demo_v2/colorization_release_v2.caffemodel -OutFile model.caffemodel; iwr https://github.com/richzhang/colorization/blob/master/colorization/resources/pts_in_hull.npy?raw=true -OutFile pts_in_hull.npy; iwr https://raw.githubusercontent.com/richzhang/colorization/master/colorization/models/colorization_deploy_v2.prototxt -OutFile model_prototext.prototxt }"
