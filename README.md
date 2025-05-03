# MVHumanNet++: A Large-scale Dataset of Multi-view Daily Dressing Human Captures with Richer Annotations for 3D Human Digitization
## [Project Page](TODO) | [Paper (Arxiv)](TODO) | [Dataset](https://github.com/GAP-LAB-CUHK-SZ/MVHumanNet/)

<img src="./assets/Teaser.png" width="1080"/>

by Chenghong Li, Hongjie Liao, Yihao Zhi, Xihe Yang, Zhengwentai Sun, Jiahao Chang,
Shuguang Cui and [Xiaoguang Han*](https://gaplab.cuhk.edu.cn/) from [GAP-Lab](https://gaplab.cuhk.edu.cn/). 



## Introduction

MVHumanNet(https://github.com/GAP-LAB-CUHK-SZ/MVHumanNet/) contains **4,500** human identities,  **9,000** daily outfits,  **60,000** motion sequences,  **645 million** with extensive annotations, including human masks, camera parameters , 2D and 3D keypoints, SMPL/SMPLX parameters, and corresponding textual descriptions. 
As an extension of MVHumanNet(https://github.com/GAP-LAB-CUHK-SZ/MVHumanNet/), MVHumanNet++ is enhanced with newly processed normal maps and depth maps, significantly expanding its applicability and utility for advanced human-centric research.



### Folder structure 
```
|-- ROOT
    |-- outfits_ID # 100001
        |-- images    # Considering the limitation of storage space, we scaled the image to half the original size and masked some background.
            |-- camera_name
                |-- images  
            |-- camera_name
                |-- images
            ....
        |-- fmask   # corresponding masks.
            |-- camera_name
                |-- mask images 
            |-- camera_name
                |-- mask images 
            ....
        |-- annots # 2D image annotations by openpose.
            |-- camera_name
                |-- annotations  # json files
            |-- camera_name
                |-- annotations  # json files
            ....
        |-- openpose
            |-- camera_name
                |-- 2D keypoints  # json files
            |-- camera_name
                |-- 2D keypoints  # json files
            ....
        |-- smpl_param  #  optimizes from multi-view images
            |-- PKL files
        |-- smplx  #  optimizes from multi-view images
            |-- 3D keypoints
                |-- json files # 3D keypoints
            |-- smpl
                |-- json files 
            |-- smplx_mesh  
                |-- obj files  # smplx meshs
        |-- camera_extrinsics.json   # extrinsics of all cameras
        |-- camera_intrinsics.json   # intrinsics of all cameras
        |-- camera_scale.pkl

```

> [!tip]
> The camera extrinsics from `camera_extrinsics.json` represent world-to-camera matrix in OpenCV coordinate system.
> The translation should be multiplied by the camera scale from `camera_scale.pkl` to correct the scene scale.

If you find our work useful in your research, please consider citing:
```
@inproceedings{xiong2024mvhumannet,
  title={MVHumanNet: A Large-scale Dataset of Multi-view Daily Dressing Human Captures},
  author={Xiong, Zhangyang and Li, Chenghong and Liu, Kenkun and Liao, Hongjie and Hu, Jianqiao and Zhu, Junyi and Ning, Shuliang and Qiu, Lingteng and Wang, Chongjie and Wang, Shijie and others},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={19801--19811},
  year={2024}
}
```
and 
```
TODO
```



## License

The data is released under the MVHumanNet and MVHumanNet++ Terms of Use, and the code is released under the Attribution-NonCommercial 4.0 International License.

Copyright (c) 2025



