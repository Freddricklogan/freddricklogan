# scripts

`update_readme.py` renders the Project Portfolio block of `../README.md` from `../projects.yml`
(between `<!-- portfolio:start -->` and `<!-- portfolio:end -->`). Run it after editing the data
file; CI fails when the README is stale (`--check`). Requires `pyyaml`.
