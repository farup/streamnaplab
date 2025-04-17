<div align="center">
  <h1>StreamMapNet and NAPLab</h1>
  
  <h3>[WACV 2024] StreamMapNet: Streaming Mapping Network for Vectorized Online HD Map Construction </h3>
  
  [![arXiv](https://img.shields.io/badge/arXiv-Paper-<COLOR>.svg)](https://arxiv.org/abs/2308.12570)
  
  <img src="./resources/pipeline_newnew.png" width="950px">
</div>

## Introduction
This repository contains the adaption of StreamMapNet to NAPLab data.

## Getting Started StreamMapNet and NapLab 

**Step 1.** Load Anaconda Module
```
module load Anaconda3/2023.09-0
```

### 1. Environment
**Step 1.** Create conda environment and activate it.

```
conda create --name streammapnet python=3.8 -y
conda activate streammapnet
```

**Step 2.** Install PyTorch.

```
pip install torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html
```

**Step 3.** Install MMCV series.

```
# Install mmcv-series
pip install mmcv-full==1.6.0
pip install mmdet==2.28.2
pip install mmsegmentation==0.30.0
git clone https://github.com/open-mmlab/mmdetection3d.git
cd mmdetection3d
git checkout v1.0.0rc6 
pip install -e .
```

**Step 4.** Install other requirements.

```
pip install -r requirements.txt
```

### 2. Data Preparation

To use data from NAPLab, the dataset needs to be generated in NAPLab format (close to NuScenes), and images frames extracted. Clone [this](https://github.com/farup/naplab) and follow the env setup. Use the notebooks examples to format and extract https://github.com/farup/naplab/notebooks

- **Step 1.** Generate the dataset format from a selected trip with 01_parsing_example.ipynb
- **Step 2.** Extract frames from the same trip (01_parsing_example.ipynb)
- **Step 3.** Convert the dataset to .pkl file with 03_converting_example


### 3. Test with NapLab Data: 

To test and visualzie StreamMapNet with data from NapLab, you can either request an interactive job from [IDUN ](https://www.hpc.ntnu.no/idun/documentation/running-jobs/) or submit slurm jobs. The follwoing steps utilize interactive jobs and lauch scripts with python debugger. launch_example.json is provided, copy the content and change the paths your vscode/launche.json file. 

Interactive job can be requested in the cmd: 
```
 salloc --partition=GPUQ --account=share-ie-idi --time=4:00:00 --nodes=1 --ntasks-per-node=4 --gres=gpu:1 --mem=80G
```

Proxy jump need to be added in the ssh.config (example node): 

```
Host idun-09-06
  HostName idun-09-06
  ProxyJump idun-login1.hpc.ntnu.no
  User terjenf
```


In the config file HD-Maps/plugin/configs/nusc_newsplit_480_60x30_24e_naplab.py, set the following variables: 

**Step 1** Setup config file.

- **ann_file:** path to the converted .pkl file
- **sample_end:** path to parent folder of trips with extracted images. 

If not all images are extracted, we need to adjust the sample start and sample end. Each scene has by defeault 40 images:

- **sample_start:** 40*starte scene number (e.g. 40 * 8) 
- **sample_end:**  40*end scene number (e.g. 40 * 10)

**Step 2** Predict

*Run "Python: Test StreamMapNet NapLab" from the python debugger (launch.json).*


**Step 3** Visualize

To visualzie the predictions, first need to comment out the module import in the first init file in the naplab libary, as their dependecies are not compatibel with the python verison of StreamMapNet (non ideal way): 

```
>>  naplab/naplab/__init__.py

print("naplab")
# from .naplab_processing import NapLabParser
# from .naplab_processing.parsers import CamParser, GNSSParser
# from .naplab_processing.utils import f_theta_utils

from .naplab_devkit import NapLab
# from .converters import create_naplab_infos_map

__all__ = ["NapLab"]

```
Remeber to uncomment, if used later to parse another trip. 

*Run "Python: Visualize StreamMapNet NapLab" from the python debugger (launch.json).*


**Step 4** Generate Video

*Run "Python: Generate StreamMapNet NapLab Video" from the python debugger (launch.json).*

















