import os

# Define the full structure: (dir or file, relative path, initial content for files or None for dirs)
STRUCTURE = [
    # Root-level files/folders
    ('dir', 'research_papers', None),
    ('dir', 'notebooks', None),
    ('file', '.gitignore', '# Byte-compiled / optimized / DLL files\n__pycache__/\n*.py[cod]\n'),
    ('file', 'LICENSE', 'MIT License\n\nCopyright (c) 2025'),
    ('file', 'requirements.txt', '# Add your Python dependencies here\n'),
    ('file', 'README.md', '# Deep Learning Research Paper Implementations & Explanations\n'),
    # Notebooks
    ('file', 'notebooks/ResNet_Quick_Demo.ipynb', '{}\n'),
    ('file', 'notebooks/FlashAttention_Integration_Test.ipynb', '{}\n'),
    # DenseNet
    ('dir', 'research_papers/densenet/code/models', None),
    ('dir', 'research_papers/densenet/code/scripts', None),
    ('dir', 'research_papers/densenet/summary', None),
    ('dir', 'research_papers/densenet/results', None),
    ('file', 'research_papers/densenet/README.md', '# DenseNet Landing Page\n'),
    ('file', 'research_papers/densenet/code/models/densenet.py', '# DenseNet core architecture\n'),
    ('file', 'research_papers/densenet/code/scripts/train.py', '# Training script for DenseNet\n'),
    ('file', 'research_papers/densenet/code/scripts/evaluate.py', '# Evaluation script for DenseNet\n'),
    ('file', 'research_papers/densenet/summary/01_core_concept.md', '# Feature Reuse, Concatenation\n'),
    ('file', 'research_papers/densenet/summary/02_architecture.md', '# Dense Block & Transition Layer\n'),
    ('file', 'research_papers/densenet/results/densenet_121_cifar.png', ''),  # Placeholder,
    # FlashAttention
    ('dir', 'research_papers/flash_attention/code/layers', None),
    ('dir', 'research_papers/flash_attention/summary', None),
    ('dir', 'research_papers/flash_attention/results', None),
    ('file', 'research_papers/flash_attention/README.md', '# FlashAttention Landing Page\n'),
    ('file', 'research_papers/flash_attention/code/layers/flash_attention.py', '# FlashAttention layer (custom CUDA/PyTorch)\n'),
    ('file', 'research_papers/flash_attention/summary/01_io_awareness.md', '# Memory Hierarchy, HBM vs. SRAM\n'),
    ('file', 'research_papers/flash_attention/summary/02_tiling_logic.md', '# Tiling and Recomputation\n'),
    ('file', 'research_papers/flash_attention/results/speed_benchmark.csv', 'run,method,speedup\n'),
    # ResNet
    ('dir', 'research_papers/resnet/code/models', None),
    ('dir', 'research_papers/resnet/code/scripts', None),
    ('dir', 'research_papers/resnet/summary', None),
    ('dir', 'research_papers/resnet/results', None),
    ('file', 'research_papers/resnet/README.md', '# ResNet Landing Page\n'),
    ('file', 'research_papers/resnet/code/models/resnet.py', '# ResNet model definition\n'),
    ('file', 'research_papers/resnet/code/models/blocks.py', '# Residual and Bottleneck blocks\n'),
    ('file', 'research_papers/resnet/code/scripts/train.py', '# Training script for ResNet\n'),
    ('file', 'research_papers/resnet/summary/01_degradation_problem.md', '# Degradation Problem\n'),
    ('file', 'research_papers/resnet/summary/02_residual_connection.md', '# Residual Connections\n'),
    ('file', 'research_papers/resnet/results/resnet_50_accuracy.txt', 'Top-1 Accuracy: \n'),
]

def main():
    for typ, path, content in STRUCTURE:
        if typ == 'dir':
            os.makedirs(path, exist_ok=True)
            print(f"Directory created: {path}")
        elif typ == 'file':
            folder = os.path.dirname(path)
            if folder and not os.path.exists(folder):
                os.makedirs(folder, exist_ok=True)
                print(f"Directory created for file: {folder}")
            if not os.path.exists(path):
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content or '')
                print(f"File created: {path}")

if __name__ == '__main__':
    main()
