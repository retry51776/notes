
gitmsg() {
  ENDPOINT="${LMSTUDIO_ENDPOINT:-http://localhost:1234/v1/chat/completions}"
  API_KEY="${LMSTUDIO_API_KEY:-lm-studio}"
  MODEL="${LMSTUDIO_MODEL:-openai/gpt-oss-120b}"

  DIFF="$(git diff --cached -U0)"
  if [ -z "$DIFF" ]; then
    DIFF="$(git diff -U0)"
  fi

  if [ -z "$DIFF" ]; then
    echo "No changes detected."
    return 1
  fi

  SYSTEM_PROMPT="You are a senior engineer generating concise Conventional Commits..."
  USER_PROMPT="Generate a commit message for this diff:\n$DIFF"

  COMMIT_MSG=$(curl -s "$ENDPOINT" \
    -H "Authorization: Bearer $API_KEY" \
    -H "Content-Type: application/json" \
    -d "$(jq -n \
      --arg sys "$SYSTEM_PROMPT" \
      --arg usr "$USER_PROMPT" \
      --arg model "$MODEL" \
      '{model: $model, temperature: 0.7, max_tokens: -1, messages: [{role:"system", content:$sys},{role:"user", content:$usr}]}')" \
    | jq -r '.choices[0].message.content')

  echo "$COMMIT_MSG" | pbcopy
  echo "📋 Commit message copied to clipboard:"
  echo "$COMMIT_MSG"
}