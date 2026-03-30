from huggingface_hub import snapshot_download

# model_path = "/data/phd/wsun/checkpoint_LaVIT/VideoLaVIT-v1"
# snapshot_download(
#     "rain1011/Video-LaVIT-v1",
#     local_dir=model_path,
#     local_files_only=False,
#     local_dir_use_symlinks=False
#     )

from huggingface_hub import hf_hub_download

model_path = '/data/phd/wsun/checkpoint_LaVIT/playground-v2'   # The local directory to save playground v2 checkpoint
snapshot_download(
    "playgroundai/playground-v2-1024px-aesthetic",
    local_dir=model_path,
    local_dir_use_symlinks=False,
    repo_type='model'
    )