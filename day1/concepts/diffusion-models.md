# Diffusion Models

Reference for how diffusion models generate images by removing noise, and how a text prompt steers the result.

---

## The Core Idea

A diffusion model learns to turn noise into data one small step at a time. Generation starts from a field of pure random noise, removes a little noise guided by what the model learned, and repeats until a clean image appears. It is the reverse of gradually destroying an image by adding noise.

## Forward and Reverse Processes

- **Forward process (training):** take a real image and add a little noise, step by step, until it becomes pure noise. This is easy to do and needs no learning.
- **Reverse process (generating):** start from noise and run a learned denoiser backward, removing a little noise at each step, until an image emerges.

The model is trained on pairs from the forward process. At each step it learns to predict the noise that was added, so it can subtract it during generation.

## Why Small Steps

Adding noise is cheap and gives the model perfect practice pairs for free. Learning many small denoising steps is far easier than learning one giant jump from noise to a finished image. Breaking generation into small steps is what makes diffusion output sharp and stable.

## Text-to-Image Pipeline

A text-to-image diffusion pipeline has a few parts:

1. **Text encoder:** turns the prompt into an embedding.
2. **Noise:** a random starting field.
3. **UNet denoiser:** removes noise over many steps, steered by the text embedding.
4. **Decoder:** in a latent diffusion model (such as Stable Diffusion), a VAE decoder turns the denoised latent into a viewable image.

The text embedding is what steers the denoising toward your description. Latent diffusion runs the denoising in a compressed latent space for speed, then decodes to pixels at the end. A pixel-space diffusion model skips the decoder and denoises the image directly.

## Key Generation Settings

| Setting | Effect |
| :--- | :--- |
| **Steps** | More steps: more refinement, slower runs |
| **Guidance scale** | Higher: sticks closer to the prompt, less variety |
| **Seed** | Fixes the starting noise so a result repeats |

## Diffusion vs VAE

| | VAE | Diffusion |
| :--- | :--- | :--- |
| How it generates | Decode one latent sample | Denoise over many steps |
| Speed | Fast, single pass | Slower, many steps |
| Image quality | Softer | Sharp, detailed |
| Typical role | Teaching, representations | Modern image generators |

## Where Diffusion Is Used

- Text-to-image tools such as Stable Diffusion, DALL-E, and Midjourney.
- Image editing: inpainting, outpainting, and upscaling.
- A growing role in audio and video generation.

The same denoising idea carries across all of these. In Lab 1.4 you run a pre-trained pipeline for inference only, so no training is required.
