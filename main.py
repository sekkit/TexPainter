import argparse
import utils
from utils import device
from stable_diffusion_depth import StableDiffusionDepth
from texture import Texture

def main(args):
    port=7890
    utils.net_config(port)
    
    seed = args.seed
    utils.seed_everything(seed)

    mesh_dir = args.mesh_dir
    save_dir = args.save_dir
    
    text_prompt = args.text_prompt

    # diffusion configuration
    num_inference_steps = args.num_inference_steps

    sd = StableDiffusionDepth(device=device, num_inference_steps=num_inference_steps)
    print("[INFO] Stable Diffusion Loaded")

    text_embeddings = sd.text_encoding(text_prompt)

    latent_tex_size = args.latent_tex_size
    rgb_tex_size = args.rgb_tex_size
    tex_latent = Texture(size=(latent_tex_size, latent_tex_size), device=device, is_latent=True)
    tex_rgb = Texture(size=(rgb_tex_size, rgb_tex_size), device=device, is_latent=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mesh_dir', type=str)
    parser.add_argument('--save_dir', type=str)
    parser.add_argument('--text_prompt', type=str)
    parser.add_argument('--seed', type=int, default=0)
    parser.add_argument('--num_inference_steps', type=int, default=50)
    parser.add_argument('--end_step', type=int, default=35)
    parser.add_argument('--guidance_scale', type=float, default=7.5)
    parser.add_argument('--latent_tex_size', type=int, default=2000)
    parser.add_argument('--rgb_tex_size', type=int, default=600)
    parser.add_argument('--opt_eps', type=int, default=20)
    parser.add_argument('--opt_lr', type=float, default=0.1)

    parser.add_argument('--camera_num', type=int, default=8)
    parser.add_argument('--fov', type=int, default=35)
    parser.add_argument('--dist', type=float, default=1.5)
    parser.add_argument('--elev', type=float, default=30)
    
    args = parser.parse_args()

    main(args)