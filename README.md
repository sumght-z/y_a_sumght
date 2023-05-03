
# Environment
My envrionment uses python3.7
```
conda create -n apex python=3.7
conda activate apex
pip install pipwin
pipwin install pycuda
pip install -r requirements.txt
```
Install cuda11.8 with tensorrt following the [NVIDIA official instructions](https://docs.nvidia.com/deeplearning/tensorrt/install-guide/index.html)

1.可随意替换权重
训练方法：
使用yolov7的方法，然后训练完后把pt文件放进/utils下执行export_pt_to_onnx.py 会在当前文件夹生成best.onnx
把onnx文件放入weights文件夹。执行/apex.py即可自动转化为.trt
