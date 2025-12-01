#!/bin/bash

diller=("russian" "chinese" "english" "german")



curl -s https://raw.githubusercontent.com/cem-ali152/winoptimize-tools/refs/heads/main/tr_md/how_to_make_custom_profil_tr.md > ./how_to_make_custom_profil_tr.md
dosya="./how_to_make_custom_profil_tr.md"
echo "how_to_make_custom_profil_tr.md indirildi"

git_raw=$(<"$dosya")

for ((i=0; i<${#diller[@]}; i++)); do
    prompt="$git_raw bunu ${diller[i]} çevir"

    dosya_adi=$(echo "${diller[i]}" | tr ' ' '_')
    safe_prompt=$(printf '%s' "$prompt" | jq -Rs .)

    curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent" \
      -H "Content-Type: application/json" \
      -H "X-goog-api-key: $1" \
      -X POST \
      -d "{
        \"contents\": [
          {
            \"parts\": [
              {
                \"text\": $safe_prompt
              }
            ]
          }
        ]
      }" -sS | jq -r '.candidates[0].content.parts[0].text' >> "how_to_make_custom_profil_${dosya_adi}.md"

done
