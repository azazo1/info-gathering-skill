[private]
default:
    @just --list

# just index .research/<slug>
# 扫描证据库并生成 index.md.
index dir:
    python3 "{{justfile_directory()}}/scripts/evidence_index.py" "{{dir}}"

# 用临时样例自检索引脚本, 不改动任何真实证据库.
self-test:
    python3 "{{justfile_directory()}}/scripts/evidence_index.py" --self-test
