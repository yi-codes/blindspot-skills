#!/usr/bin/env bash
# Send a prompt (read from stdin) to another model's CLI and print its final answer.
#
# Usage:
#   ask_other_model.sh --list            # show which backends are available
#   ask_other_model.sh claude < prompt   # Claude Code, print mode, web tools only
#   ask_other_model.sh codex  < prompt   # Codex CLI, read-only sandbox
#   ask_other_model.sh custom < prompt   # $CROSS_CHECK_CMD, which must read the prompt on stdin
#
# The other model runs in an empty temporary directory so it cannot read the
# current project, and its session is not persisted.
set -euo pipefail

backend="${1:-}"

list_backends() {
  command -v claude >/dev/null 2>&1 && echo "claude"
  command -v codex >/dev/null 2>&1 && echo "codex"
  [ -n "${CROSS_CHECK_CMD:-}" ] && echo "custom"
  return 0
}

if [ "$backend" = "--list" ]; then
  list_backends
  exit 0
fi

case "$backend" in
  claude|codex|custom) ;;
  *)
    echo "usage: $0 --list | claude | codex | custom  (prompt on stdin)" >&2
    exit 2
    ;;
esac

if [ -t 0 ]; then
  echo "error: pipe the prompt on stdin" >&2
  exit 2
fi

prompt="$(cat)"
if [ -z "$prompt" ]; then
  echo "error: empty prompt" >&2
  exit 2
fi

work_dir="$(mktemp -d "${TMPDIR:-/tmp}/cross-check.XXXXXX")"
trap 'rm -rf "$work_dir"' EXIT
cd "$work_dir"

case "$backend" in
  claude)
    command -v claude >/dev/null 2>&1 || { echo "error: claude CLI not found" >&2; exit 127; }
    # Only web tools: the second model may research, but cannot run commands or edit files.
    printf '%s' "$prompt" | claude -p \
      --tools "WebSearch,WebFetch" \
      --allowedTools "WebSearch,WebFetch" \
      --no-session-persistence
    ;;
  codex)
    command -v codex >/dev/null 2>&1 || { echo "error: codex CLI not found" >&2; exit 127; }
    out_file="$work_dir/answer.md"
    log_file="$work_dir/codex.log"
    # Codex prints progress and warnings on stderr; keep them out of the answer
    # and show them only if the run fails.
    if ! printf '%s' "$prompt" | codex exec \
      --sandbox read-only \
      --skip-git-repo-check \
      --ephemeral \
      --color never \
      -o "$out_file" \
      - >/dev/null 2>"$log_file"; then
      tail -n 40 "$log_file" >&2
      exit 1
    fi
    cat "$out_file"
    echo
    ;;
  custom)
    [ -n "${CROSS_CHECK_CMD:-}" ] || { echo "error: CROSS_CHECK_CMD is not set" >&2; exit 2; }
    # CROSS_CHECK_CMD is user-configured, e.g. 'llm -m <model-name>'.
    printf '%s' "$prompt" | bash -c "$CROSS_CHECK_CMD"
    ;;
esac
