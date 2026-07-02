# Project Guidelines

## Rules
- Do not modify files inside `datasets/raw/`.
- Save cleaned or transformed files inside `datasets/processed/` or the ticket `output/` folder.
- Use clear variable names.
- Validate your results using `.head()`, `.info()`, `.shape` and basic sanity checks.
- Prefer vectorized Pandas operations over loops.
- Keep your code readable.

## Suggested Git Commit Style
- `feat: complete ticket DA-001 customer revenue report`
- `fix: handle missing order quantities`
- `docs: update data dictionary`
