import torch
print(torch.cuda.is_available())  # True if GPU detected
print(torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No GPU")
