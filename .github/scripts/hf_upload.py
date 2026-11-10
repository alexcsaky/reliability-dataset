"""Upload one release folder of this repository, the dataset card and the changelog to the Hugging Face dataset.

    HF_TOKEN=... python .github/scripts/hf_upload.py alexcsaky/reliability-dataset v1.1.2

Run from the repository root by .github/workflows/huggingface.yml. The card is this repository's README.md under the
Hugging Face header below, whose tables point at the release being uploaded. The token is read from HF_TOKEN and
never printed. The same steps as scripts/hf_upload.py in alexcsaky/reliability-api.
"""
import os
import re
import sys
from pathlib import Path

from huggingface_hub import HfApi

repo, version = sys.argv[1], sys.argv[2]
if not re.fullmatch(r"v\d+(\.\d+)*", version):
    sys.exit(f"not a release folder name: {version!r}")
folder = Path(version)
if not (folder / "claims.csv.gz").is_file():
    sys.exit(f"no release at {folder}/ (claims.csv.gz missing)")
token = os.environ.get("HF_TOKEN")
if not token:
    sys.exit("HF_TOKEN is not set: add a Hugging Face write token as the repository secret HF_TOKEN")

card = f"""---
license: cc-by-4.0
pretty_name: Reliability dataset
language:
- en
size_categories:
- 10K<n<100K
tags:
- fact-checking
- claims
- public-figures
- reliability
configs:
- config_name: subjects
  data_files: {version}/subjects.csv
- config_name: scores
  data_files: {version}/scores.csv
- config_name: claims
  data_files: {version}/claims.csv.gz
- config_name: changes
  data_files: {version}/changes.csv
---

""" + Path("README.md").read_text(encoding="utf-8")

api = HfApi(token=token)
api.upload_folder(repo_id=repo, repo_type="dataset", folder_path=str(folder), path_in_repo=version,
                  commit_message=f"Release {version}")
api.upload_file(repo_id=repo, repo_type="dataset", path_or_fileobj=card.encode("utf-8"), path_in_repo="README.md",
                commit_message=f"Dataset card for {version}")
api.upload_file(repo_id=repo, repo_type="dataset", path_or_fileobj="CHANGELOG.md", path_in_repo="CHANGELOG.md",
                commit_message="Changelog")
files = [f.path for f in api.list_repo_tree(repo, repo_type="dataset", path_in_repo=version)]
print(f"uploaded {version}: {len(files)} files")
