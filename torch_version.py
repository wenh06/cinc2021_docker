"""
"""


if __name__ == "__main__":
    import torch
    cuda_is_available = " " if torch.cuda.is_available() else " not "
    print(f"torch version == {torch.__version__}")
    print("cuda is{}available")
