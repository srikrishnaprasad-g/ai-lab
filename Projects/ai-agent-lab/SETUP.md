# Setup Guide

This guide explains how to install, configure, and run AI Agent Lab in a local development environment.

---

# System Requirements

## Supported Operating Systems

AI Agent Lab is designed to run on:

| Platform | Status |
|----------|--------|
| Windows 10 / 11 | ✅ Supported |
| macOS | ✅ Supported |
| Ubuntu 22.04+ | ✅ Supported |

---

## Python

Python 3.11 or later is recommended.

Verify your installation:

```bash
python --version
```

Expected output:

```text
Python 3.11.x
```

---

## Git

Verify Git is installed:

```bash
git --version
```

---

## Recommended Tools

The following tools improve the development experience:

- Visual Studio Code
- GitHub Desktop (optional)
- Claude Code
- Claude Code Router
- PowerShell 7 (Windows)
- Windows Terminal

---

# Clone the Repository

```bash
git clone https://github.com/srikrishnaprasad-g/ai-lab.git
```

Navigate to the project:

```bash
cd AI-Lab/Projects/ai-agent-lab
```

---

# Create a Virtual Environment

## Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

---

## macOS / Linux

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

# Install Dependencies

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

Install project dependencies:

```bash
pip install -r requirements.txt
```

---

# Verify Installation

Run:

```bash
pytest
```

Expected output:

```text
======================

XX passed

======================
```

(The exact number of tests will increase over time.)

---

# API Keys

AI Agent Lab uses external services for LLM inference and search.

Current integrations include:

| Service | Required |
|----------|----------|
| Gemini | Yes |
| Tavily | Yes |
| Groq | Optional |
| OpenRouter | Optional |

---

# Create a .env File

Create a file named:

```text
.env
```

Example configuration:

```text
##########################################
# LLM
##########################################

DEFAULT_PROVIDER=gemini
DEFAULT_MODEL=gemini-2.5-flash

##########################################
# API Keys
##########################################

GEMINI_API_KEY=YOUR_KEY

TAVILY_API_KEY=YOUR_KEY

##########################################
# Runtime
##########################################

LOG_LEVEL=INFO

OUTPUT_DIR=output
```

Never commit the `.env` file to version control.

---

# Configuration Variables

| Variable | Description |
|----------|-------------|
| DEFAULT_PROVIDER | Default LLM provider |
| DEFAULT_MODEL | Default model |
| GEMINI_API_KEY | Gemini authentication |
| TAVILY_API_KEY | Search provider key |
| LOG_LEVEL | Logging verbosity |
| OUTPUT_DIR | Report destination |

---

# Running the Application

Launch the runtime:

```bash
python main.py
```

The CLI will initialize the runtime, load configuration, and prompt for a request.

Example:

```
Analyze the impact of AI coding assistants on software engineering.
```

---

# Output

Reports are written to:

```text
output/
```

Typical artifacts include:

```
report.md

report.pdf
```

Future releases may introduce timestamped execution directories and execution metadata.

---

# Updating Dependencies

To upgrade project dependencies:

```bash
pip install --upgrade -r requirements.txt
```

After upgrading, execute the full test suite:

```bash
pytest
```

before committing changes.
---

# Provider Configuration

AI Agent Lab is designed around a provider abstraction layer, allowing different LLM providers to be used with minimal configuration changes.

## Gemini

Example configuration:

```text
DEFAULT_PROVIDER=gemini
DEFAULT_MODEL=gemini-2.5-flash

GEMINI_API_KEY=YOUR_API_KEY
```

Gemini is the recommended default provider for development due to its balance of performance, cost, and ease of integration.

---

## Groq

Example configuration:

```text
DEFAULT_PROVIDER=groq

GROQ_API_KEY=YOUR_API_KEY
DEFAULT_MODEL=qwen/qwen3-32b
```

Groq provides high-speed inference and is useful for latency-sensitive workloads.

Model availability may change over time. Refer to the Groq documentation for supported models.

---

## OpenRouter

Example configuration:

```text
DEFAULT_PROVIDER=openrouter

OPENROUTER_API_KEY=YOUR_API_KEY

DEFAULT_MODEL=openai/gpt-4.1-mini
```

OpenRouter enables access to multiple providers through a unified interface.

Your selected model must be available under your OpenRouter account and billing plan.

---

# Search Configuration

AI Agent Lab currently integrates with Tavily for web search.

Example:

```text
TAVILY_API_KEY=YOUR_API_KEY
```

The search provider is initialized automatically when the Research Agent requires external information.

Future releases may support additional search providers.

---

# Logging Configuration

The logging level controls the amount of diagnostic information produced during execution.

Supported levels:

| Level | Description |
|--------|-------------|
| DEBUG | Detailed runtime diagnostics |
| INFO | Standard execution information |
| WARNING | Potential issues |
| ERROR | Execution failures |

Example:

```text
LOG_LEVEL=INFO
```

Verbose CLI mode complements logging by displaying additional runtime information during execution.

---

# Output Configuration

Reports are written to the configured output directory.

Example:

```text
OUTPUT_DIR=output
```

Future releases may support:

- Timestamped execution folders
- Custom report templates
- Multiple output destinations
- Cloud storage integration

---

# Troubleshooting

## Missing API Key

Typical error:

```text
API key not found
```

Resolution:

- Verify the `.env` file exists.
- Confirm the variable name is correct.
- Restart the application after updating environment variables.

---

## Provider Initialization Failure

Possible causes:

- Invalid API key
- Unsupported model
- Network connectivity issues
- Provider service outage

Recommended actions:

1. Verify credentials.
2. Check internet connectivity.
3. Confirm the selected model is available.
4. Review runtime logs for additional details.

---

## Search Errors

If search requests fail:

- Verify the Tavily API key.
- Confirm internet access.
- Check Tavily service availability.
- Retry the request.

The application should continue operating where possible, although responses may contain less external context.

---

## Dependency Issues

If packages fail to install:

```bash
pip install --upgrade pip

pip install -r requirements.txt
```

If problems persist:

```bash
pip freeze

python --version
```

Compare the installed versions with the project's supported requirements.

---

## Test Failures

Run:

```bash
pytest
```

If tests fail:

- Ensure dependencies are installed.
- Verify Python version compatibility.
- Remove stale virtual environments if necessary.
- Reinstall project dependencies.

---

# Validation Checklist

Before using AI Agent Lab, confirm the following:

- [ ] Python 3.11+ installed
- [ ] Git installed
- [ ] Repository cloned
- [ ] Virtual environment created
- [ ] Dependencies installed
- [ ] `.env` file configured
- [ ] API keys added
- [ ] Tests pass successfully
- [ ] Runtime launches without errors
- [ ] Markdown report generated
- [ ] PDF generation verified (if enabled)

Completing this checklist helps ensure a consistent development environment.

---

# Frequently Asked Questions

## Can I use a different LLM provider?

Yes.

The provider abstraction layer allows switching providers through configuration without modifying agent logic.

---

## Can multiple providers be configured?

Yes.

Multiple API keys may be stored in the `.env` file. The active provider is selected using the `DEFAULT_PROVIDER` configuration.

---

## Is a search provider mandatory?

Current implementations benefit from web search for research-oriented prompts.

If search is unavailable, some workflows may continue with reduced capabilities depending on implementation.

---

## Should the virtual environment be committed?

No.

The virtual environment should remain local to your development machine and should be excluded from version control.

---

## Where are reports stored?

Reports are written to the directory specified by `OUTPUT_DIR`.

By default:

```text
output/
```

---

# Next Steps

Your environment is now ready.

Recommended reading order:

1. `README.md`
2. `docs/ARCHITECTURE.md`
3. `docs/CLI.md`
4. `docs/PROVIDERS.md`
5. `docs/OBSERVABILITY.md`
6. `docs/ROADMAP.md`

These documents provide a deeper understanding of the project's architecture, runtime behavior, and future direction.

---

# Need Help?

If you encounter issues:

1. Review the troubleshooting section.
2. Verify your configuration.
3. Check the runtime logs.
4. Execute the test suite.
5. Consult the project documentation.

Maintaining a reproducible development environment is essential for reliable AI engineering and simplifies future upgrades.