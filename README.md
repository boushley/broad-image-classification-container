# Broad Classifier
A broad image classifier that can run in docker. This assumes that you're
using NVIDIA GPU and that you have Docker configured with the [Nvidia
container toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html).

## Running
First create some directories for input/output
```
mkdir -p input output
```

Then build the docker container:
```
docker build -t broad-classifier .
```

Then run the docker container, mapping the input / output folders and
providing the flags to allocate GPUs and use NVIDIA runtime:
```
docker run --rm --runtime=nvidia --gpus all -v $(pwd)/input:/data/in -v $(pwd)/output:/data/out --name broad-classifier broad-classifier
```

Finally copy in some assets into the `input` folder. (Note the files put 
in this folder will be deleted once processed)

An annotated image with JSON sidecar file will be placed in the
`output` folder)
