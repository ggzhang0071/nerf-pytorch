import os
import argparse

device=torch.device("cuda" if torch.cuda.is_available() else "cpu")
np.random.seed(0)


def train():
    

    K=None
    if args.dataset_type='llff':
        images, poses, bds, render_poses, i_test = load_llff_data(args.datadir, args.factor,
                                                                    recenter=True, bd_factor=.75, spherify=args.spherify)
        hwf=poses[0,:3,-1]
        poses=poses[:,:3,:4]
        print('Loaded llff', images.shape, render_poses.shape, hwf, args.datadir)
        if  not isinstance(i_test, list):
            i_test=[i_test] 
        if args.llffhold>0:
            print('Auto LLFF holdout,', args.llffhold)
            i_test=[int(i) for i in args.llffhold.split(',')]

        i_val=i_test
        i_train=[i for i in np.arange(images.shape[0]) if (i not in i_test)]
        print('DEFINING BOUNDS')
        if args.no_ndc:
            near=np.ndarray.min(bds) * .9   
            far=np.ndarray.max(bds) * 1
        else:
            near=0.
            far=1.
        print('NEAR FAR', near, far)

        H, W, focal=hwf
        H, W, focal=int(H), int(W), float(focal)
        hwf=[H, W, focal]


def get_embedder(multiers, i=0):
    if i==-1:
        return nn.Identity(), 3
    embed_kwargs={
        'include_input':True,
        'input_dims':3,
        'max_freq_log2':10,
        'num_freqs':10,
        'log_sampling':True,
        'predict_pos':[Torch.sin, torch.cos],
    }

    embed_obj=Emedder(**embed_kwargs)
    embed= lambda x, eo=embed_obj: eo(x)
    return embed, embed_obj.out_dim


def create_nerf(args):
    """ Instantiate NeRF's MLP model.
    """
    embed_fn, input_ch = get_embedder(args.multires, args.i_embed)



        

        


if __name__=='__main__':
    args=argparse.ArgumentParser()
    args.add_argument('--config', type=str, default='configs/llff_data.txt')
    args.add_argument('--expname', type=str, default='default') # name of experiment
                

    train()