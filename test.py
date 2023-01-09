import torch

if torch.cuda.is_available():
    print("CUDA is available!")
else:
    print("CUDA is not available.")

if torch.cuda.device_count() > 0:
    print("Number of GPUs:", torch.cuda.device_count())
else:
    print("No GPUs available.")