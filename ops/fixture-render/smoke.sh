#!/usr/bin/env bash
set -euo pipefail

export LC_ALL=C.UTF-8
export COMPOSE_ENV_FILES="${COMPOSE_ENV_FILES:-.env.fixture.example}"
output="${1:-logs/render-fixture}"
mkdir -p -- "$(dirname -- "$output")"
mkdir -- "$output"
output="$(cd -- "$output" && pwd)"
preview="$(mktemp -d)"
trap 'rm -rf -- "$preview"' EXIT

renderer=(docker compose --profile render run --rm --no-deps -T)
curl --fail --silent --show-error --max-time 10 \
  -H 'Authorization: Bearer local-driver-a' \
  http://127.0.0.1:8000/api/v1/local-fixtures/current \
  | "${renderer[@]}" --user "$(id -u):$(id -g)" --volume "$output:/out" renderer /out

libreoffice -env:UserInstallation="file://$preview/profile" --headless \
  --convert-to pdf --outdir "$preview" "$output/synthetic-mean.docx"

cat > "$preview/expected.txt" <<'EOF'
RAFIQ Synthetic Calculation
This fixture compares PDF and Word output from one stored R result.
Measure Fixture result
Samples 2, 4, 6 (unitless)
Sample count 3 samples
Mean 4 (unitless)
Method synthetic-mean-v1
Result version 1
EOF

check_page() {
  local format="$1" pdf="$2"
  test "$(pdfinfo "$pdf" | awk '$1 == "Pages:" { print $2 }')" = 1
  pdftotext -layout -nopgbrk "$pdf" - \
    | awk '{$1 = $1; if (NF) print}' > "$preview/$format.txt"
  diff -u "$preview/expected.txt" "$preview/$format.txt"
  pdffonts "$pdf" > "$preview/$format-fonts.txt"
  awk 'NR > 2 {
    name = tolower($1)
    gsub(/[^a-z]/, "", name)
    if (name !~ /dejavusans/ || $(NF-4) != "yes") exit 1
    if (name ~ /bold/) bold = 1; else regular = 1
  } END { if (!regular || !bold) exit 1 }' "$preview/$format-fonts.txt"
  pdftoppm -png -r 144 -singlefile "$pdf" "$output/$format-page"
}

check_page pdf "$output/synthetic-mean.pdf"
check_page word "$preview/synthetic-mean.pdf"

{
  echo 'PDF and Word each have one page. Both match the expected labels, values, and units.'
  cat "$preview/expected.txt"
  echo
  echo 'Embedded PDF fonts'
  cat "$preview/pdf-fonts.txt"
  echo
  echo 'Embedded fonts in the PDF preview rendered from Word'
  cat "$preview/word-fonts.txt"
} | tee "$output/comparison.txt"

{
  git rev-parse HEAD
  docker image inspect --format '{{.Os}}/{{.Architecture}} {{.Id}}' rafiq-fixture-renderer:local
  sha256sum server/Dockerfile server/uv.lock
  libreoffice --version
  pdftoppm -v 2>&1
  "${renderer[@]}" --entrypoint sh renderer -ec '
    cat /etc/os-release
    python --version
    uv --version
    uv pip freeze
    dpkg-query -W
    sha256sum /usr/share/fonts/truetype/dejavu/DejaVuSans.ttf \
      /usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf
  '
  (cd "$output" && sha256sum synthetic-mean.pdf synthetic-mean.docx)
} > "$output/dependencies.txt"
