from huggingface_hub import snapshot_download

# Download the entire repository
snapshot_download(
    repo_id="lerobot/aloha_static_cups_open",
    repo_type="dataset",
    local_dir="sample_lerobot_data"
)