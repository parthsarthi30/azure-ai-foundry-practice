# Azure AI Foundry Practice

A practice exercise for provisioning an **Azure AI Foundry** workspace and making
a first call to a deployed chat model from Python.

---

## What this project does

`app.py` is a minimal Python script that:

1. Loads Azure OpenAI credentials from a local `.env` file.
2. Initializes an `AzureOpenAI` client.
3. Sends the prompt **"Explain what Azure AI Foundry is in one sentence."** to
   the deployed chat model.
4. Prints the model's reply.
5. Prints token-usage statistics (prompt / completion / total) for cost
   tracking.

---

## Prerequisites

- An active **Microsoft Azure** account with the $200 free trial credits
  activated.
- A **Hub** in [ai.azure.com](https://ai.azure.com) named `ent-agent-2026-hub`.
- A **Project** inside the Hub (e.g. `ent-agent-<yourname>`).
- A deployed chat model on the project's endpoint.
- **Python 3.9+** and the following packages:

  ```bash
  pip install openai python-dotenv
  ```

---

## Setup

1. **Clone the repository** and move into the project folder:

   ```bash
   git clone <your-repo-url>
   cd azure-ai-foundry-practice
   ```

2. **Create your `.env` file** based on the example template:

   ```bash
   cp .env.example .env
   ```

3. **Fill in your Azure OpenAI credentials** in `.env`:

   ```env
   AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com/
   AZURE_OPENAI_API_KEY=<your-api-key>
   ```

   > ⚠️ **Never commit your real `.env` file.** It is already listed in
   > `.gitignore`. The keys in `.env.example` are placeholders only — rotate
   > any key that has been shared publicly.

---

## Running the script

From the project root:

```bash
python app.py
```

You should see something like:

```
Endpoint: https://<your-resource>.openai.azure.com/
Key loaded: True
Azure AI Foundry is a unified platform for building, evaluating, and deploying
production-grade AI applications and agents on Azure.

--- Token Usage ---
Prompt tokens: 18
Completion tokens: 24
Total tokens: 42
```

The exact reply and token counts will vary per run.

---

## Resource mapping (from the exercise)

| Exercise step                       | Resource                                                                                     |
| ----------------------------------- | -------------------------------------------------------------------------------------------- |
| Step 2 — Hub                        | `ent-agent-2026-hub`                                                                         |
| Step 3 — Project                    | `ent-agent-<yourname>`                                                                       |
| Step 4 — Chat model deployment      | A chat completion deployment (the script targets the deployment name configured in `app.py`) |
| Step 5 — Embedding model deployment | `text-embedding-3-small` (provisioned for future RAG work)                                   |

> 📝 **Note on the chat model:** the original exercise calls for **GPT-4o** as
> a `Standard` deployment. The current `app.py` is wired to **`gpt-5-mini`**
> (`reasoning_effort="minimal"`), which is what was actually deployed in this
> workspace. To switch back to GPT-4o, deploy it in the Model Catalog and
> change the `model=` argument in `app.py` to match the new deployment name.
>
> 📝 **Note on the env var name:** the exercise spec uses
> `AZURE_OPENAI_KEY`, while the script reads `AZURE_OPENAI_API_KEY`. The
> `.env.example` and the script agree; if you need to match the spec
> literally, rename the variable in both places.

---

## Cost / token tracking

The script prints `prompt_tokens`, `completion_tokens`, and `total_tokens` on
every run. Keep a log of these to track consumption against the $200 trial
credit. A simple spreadsheet with the columns below is enough to get started:

| Date | Model | Prompt tokens | Completion tokens | Total tokens |
| ---- | ----- | ------------- | ----------------- | ------------ |

---

## Project structure

```
azure-ai-foundry-practice/
├── .env.example      # Template for local secrets — safe to commit
├── .gitignore        # Excludes .env so secrets stay local
├── README.md         # You are here
└── app.py            # Azure OpenAI call + token-usage logging
```

---

## Next steps

- Wire up `text-embedding-3-small` for a first **RAG** pipeline.
- Add streaming (`stream=True`) to the chat-completion call.
- Move secrets to **Azure Key Vault** or environment-managed credentials
  before deploying beyond local development.
