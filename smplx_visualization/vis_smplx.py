import smplx
import numpy as np
import torch
import cv2

# Firstly, please install dependencies like smplx, opencv-python, pyrender, numpy, torch, trimesh, .etc


# Download SMPLX_NEUTRAL.npz from https://github.com/vchoutas/smplx#downloading-the-model and place it under the path './assets/smplx'
smplx_model = smplx.SMPLX(model_path = 'assets/smplx', gender = 'neutral', use_pca = True, num_pca_comps = 6, flat_hand_mean = True, batch_size = 1) # Note that different from MVHumanNet smplx saved format, MVHumanNet++ smplx follows the official MPI format.


img_path = f"./data/100842_0675_cam_00_img.jpg"
cam_path = f"./data/100842_cam_00_camera.npz"
frame_id = img_path.split("_")[-4] # 0675

# ================================================================================
smplx_file = np.load(f"./data/100842_smplx_params_all.npz") # corresponds to the smplx_params.npz file
smplx_data = {k: v for k, v in smplx_file.items()}
smplx_id = int(frame_id) // 25 - 1
out = smplx_model.forward(betas = torch.from_numpy(smplx_data['betas'][0][None]),
                          global_orient = torch.from_numpy(smplx_data['global_orient'][smplx_id][None]),
                          transl = torch.from_numpy(smplx_data['transl'][smplx_id][None]),
                          body_pose = torch.from_numpy(smplx_data['body_pose'][smplx_id][None]),
                          left_hand_pose = torch.from_numpy(smplx_data['left_hand_pose'][smplx_id][None]),
                          right_hand_pose = torch.from_numpy(smplx_data['right_hand_pose'][smplx_id][None]))

# # # ================= or load the individual smplx parameters =====================
# smplx_file = f"./data/100842_0675_smplx.npz" # corresponds to the 0675.npz file in 'smplx_params' folder
# smplx_data = np.load(smplx_file, allow_pickle=True)
# out = smplx_model.forward(betas = torch.from_numpy(smplx_data['betas']),
#                             global_orient = torch.from_numpy(smplx_data['global_orient']),
#                             transl = torch.from_numpy(smplx_data['transl']),
#                             body_pose = torch.from_numpy(smplx_data['body_pose']),
#                             left_hand_pose = torch.from_numpy(smplx_data['left_hand_pose']),
#                             right_hand_pose = torch.from_numpy(smplx_data['right_hand_pose']))
# # # ==============================================================================

vertices = out['vertices'].detach().numpy()
faces = smplx_model.faces

camera = np.load(cam_path)
render_data = {}
cameras = {}
K = camera['intrinsic'][None]
R = camera['extrinsic'][:3, :3][None]
T = camera['extrinsic'][:3, 3:4][None]

cameras['K'] = K
cameras['R'] = R
cameras['T'] = T

images = cv2.imread(img_path)

vertices = np.array(vertices[0])

pid = 0
render_data = {'vertices': vertices, 'faces': faces, 'vid': pid, 'name': 'human'}

render_data_input = {"0":render_data}
from renderer import Renderer
render = Renderer(height=1024, width=1024, faces=None)
render_results = render.render(render_data_input, cameras, [images])


cv2.imwrite(f"projected_smplx.png", render_results[0].astype(np.uint8))
print("Projected SMPL-X mesh saved as projected_smplx.png")