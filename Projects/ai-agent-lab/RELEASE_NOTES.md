# Release Notes - Sprint 8.0 - 2026-07-24

This release focuses on polish, usability, and operational visibility for the AI Agent Lab CLI.

## UX Improvements
- **Redesigned CLI Banner**: Now dynamically detects and displays the actual LLM provider and model, providing clear runtime context.
- **Terminal Report Display**: Added Executive Summary and Key Findings display directly in the terminal upon pipeline completion, improving feedback loop speed.
- **Structured Progress Reporting**: Unified stage-based progress reporting (`▶ Research`, `✓ Completed`), removing duplicate and noisy logging.
- **Report Formatting**: Improved PDF report layout with correct pagination and section heading spacing.
- **Timezone Awareness**: PDF generation time now displays in local IST (UTC+5:30).

## Security Improvements
- **Secret Masking**: Implemented comprehensive API key and credential masking in HTTP request logging.
- **Verbosity Control**: Refactored `httpx` and internal logging to ensure verbose mode shows diagnostics *only* when requested, and always without exposing secrets.

## Developer Experience (DX)
- **Structured Verbose Mode**: Refactored verbose diagnostics into distinct, readable sections (Runtime, Research, Summarization, PDF).
- **Graceful Error Handling**: Improved error handling for common CLI misuse (e.g., running verbose mode without a prompt).
- **Performance**: Removed redundant logging, resulting in a cleaner and faster execution path.
