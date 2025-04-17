<div align="center">
  <h1>StreamMapNet</h1>
  
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

To use data from NapLab car, frames from a trip need to be extracted, and the dataset structured in NapLab format (close NuScenes). Use the notebooks here: https://github.com/farup/naplab/notebooks

- **Step 1.** Generate the dataset format from a selected trip with 01_parsing_example.ipynb, or used pre-created file for trip:
- **Step 2.** Extract frames from the same trip (01_parsing_example.ipynb): 

```
naplab_parser.extract_images(scenes=(8,10)) # extraction example
```

### 3. Test with NapLab Data: 


In the config file HD-Maps/plugin/configs/nusc_newsplit_480_60x30_24e_naplab.py, set the following variables: 


- **ann_file**: path to the converted .pkl file
- **sample_end.**: path to parent folder of trips with extracted images. 

If not all images are extracted, we need to adjust the sample start and sample end. Each scene has by defeault 40 images:

- **sample_start** 40*starte scene number (e.g. 40 * 8) 
- **sample_end.**  40*end scene number (e.g. 40 * 10)

```








