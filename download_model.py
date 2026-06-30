from huggingface_hub import hf_hub_download
import os

os.makedirs("models", exist_ok=True)

model_path = hf_hub_download(
    repo_id="Qwen/Qwen2.5-3B-Instruct-GGUF",
    filename="qwen2.5-3b-instruct-q4_k_m.gguf",
    local_dir="models"
)

print("Model downloaded to:", model_path)