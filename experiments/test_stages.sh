#!/usr/bin/env bash
set -euo pipefail

MODEL_NAME_STAGE1="deepvk/RuModernBERT-base"

DATA_PATH="./benchmarks/raw/hr"
INDEX_PATH="./benchmarks/faiss/hr"

RUN_NAME_STAGE1="deepvk_RuModernBERT_base_v1"

mkdir -p "$DATA_PATH" "$INDEX_PATH"

run_stage1() {
  local result_path="./benchmarks/result/stage1"
  local log_dir="./logs/stage1"
  local checkpoint_dir="./checkpoints/stage1"

  mkdir -p "$result_path" "$log_dir" "$checkpoint_dir"

  accelerate launch --num_processes=1 -m stage1.main \
    --model_name "$MODEL_NAME_STAGE1" \
    --run_name "$RUN_NAME_STAGE1" \
    --data_path "$DATA_PATH" \
    --index_path "$INDEX_PATH" \
    --result_path "$result_path" \
    --log_dir "$log_dir" \
    --checkpoint_dir "$checkpoint_dir" \
    --extension "flat" \
    --fp16 \
    --hard_negative_strategy "in_batch" \
    --seed 42 \
    --test_only
}

usage() {
  cat <<EOF
Usage:
  $0 stage1
  $0 all

You can pass several stages:
  $0 stage1
EOF
}

if [[ $# -eq 0 ]]; then
  usage
  exit 1
fi

for stage in "$@"; do
  case "$stage" in
    all|stage1)
      run_stage1
      ;;
    *)
      echo "Unknown stage: $stage"
      usage
      exit 1
      ;;
  esac
done