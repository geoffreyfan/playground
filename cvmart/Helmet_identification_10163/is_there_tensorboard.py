import os
if os.path.exists('/project/train/tensorboard'):
    # os.system('cp -r /project/train/models/train/exp/weights/* /project/train/tensorboard/')
    os.system('rm -rf /project/train/tensorboard')
else:
    os.system('mkdir /project/train/tensorboard')
    # os.system('cp -r /project/train/tensorboard/* /project/train/models/train/exp/weights/')