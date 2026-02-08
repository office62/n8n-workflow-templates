# n8n Workflow Catalog

**Total workflow-uri:** 740 (740 valide, 0 cu erori)
**Categorii:** 24

## Cuprins

- [AI Research RAG and Data Analysis](#ai-research-rag-and-data-analysis) (41 workflow-uri)
- [Airtable](#airtable) (5 workflow-uri)
- [Database and Storage](#database-and-storage) (5 workflow-uri)
- [Discord](#discord) (3 workflow-uri)
- [Forms and Surveys](#forms-and-surveys) (4 workflow-uri)
- [Gmail and Email Automation](#gmail-and-email-automation) (21 workflow-uri)
- [Google Drive and Google Sheets](#google-drive-and-google-sheets) (17 workflow-uri)
- [HR and Recruitment](#hr-and-recruitment) (4 workflow-uri)
- [Instagram Twitter Social Media](#instagram-twitter-social-media) (10 workflow-uri)
- [Notion](#notion) (10 workflow-uri)
- [OpenAI and LLMs](#openai-and-llms) (82 workflow-uri)
- [Other Integrations and Use Cases](#other-integrations-and-use-cases) (30 workflow-uri)
- [PDF and Document Processing](#pdf-and-document-processing) (18 workflow-uri)
- [Slack](#slack) (11 workflow-uri)
- [Telegram](#telegram) (20 workflow-uri)
- [WhatsApp](#whatsapp) (5 workflow-uri)
- [WordPress](#wordpress) (6 workflow-uri)
- [analytics](#analytics) (6 workflow-uri)
- [api-webhooks](#api-webhooks) (20 workflow-uri)
- [automation](#automation) (252 workflow-uri)
- [communication](#communication) (41 workflow-uri)
- [data-integration](#data-integration) (75 workflow-uri)
- [data-transformation](#data-transformation) (24 workflow-uri)
- [document-processing](#document-processing) (30 workflow-uri)

---

## AI Research RAG and Data Analysis

### Autonomous AI crawler

> Se declanșează manual. folosește Sub-workflow Tool, folosește OpenAI Chat, folosește Parser Structurat, citește date din Supabase (+5 altele). Detalii: ⚠️ Note

1. Complete video guide for this workflow is available [on my YouTube](https://youtu.be/2W09puFZwtY). 
2. Remember to add your credentials and configure nodes.
3. If you like this workflow, please subscribe to [my YouTube...

- **Noduri:** 38
- **Conexiuni:** 25
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, HTML, HTTP API, Markdown, OpenAI Chat, Parser Structurat, Sub-workflow Tool, Supabase

### Build Your Own Image Search Using AI Object Detection, CDN and ElasticSearchBuild Your Own Image Search Using AI Object Detection, CDN and ElasticSearch

> Se declanșează manual. folosește HTTP API, folosește Editor Imagine, creează înregistrări în Elasticsearch. Detalii: 2. Use Detr-Resnet-50 Object Classification
[Learn more about Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/)

Not all AI workflows need an LLM! As in this example, we're using a non-LLM vision model to parse the source image...

- **Noduri:** 17
- **Conexiuni:** 9
- **Declanșare:** 👆 Manual
- **Integrări:** Editor Imagine, Elasticsearch, HTTP API

### Build a Financial Documents Assistant using Qdrant and Mistral.ai

> Se declanșează de Monitor Fișiere Locale. folosește Fișier Local, folosește Mistral Embeddings, folosește Document Loader, folosește Text Splitter (+5 altele). Detalii: Step 3. When files are updated, the vector point is updated.
[Learn how to delete points using the Qdrant API](https://qdrant.tech/documentation/concepts/points/delete-points)

Similarly to the files deleted branch, when we encounter a change in a...

- **Noduri:** 29
- **Conexiuni:** 20
- **Declanșare:** 👆 Manual
- **Integrări:** Document Loader, Fișier Local, HTTP API, LangChain Retrieval QA, Mistral AI, Mistral Embeddings, Qdrant, Text Splitter, Vector Retriever

### Build a Tax Code Assistant with Qdrant, Mistral.ai and OpenAI

> Se declanșează manual. folosește Mistral Embeddings, folosește Document Loader, folosește Text Splitter, folosește HTTP API (+7 altele). Detalii: Step 3. Save into Qdrant VectorStore
[Read more about using the Qdrant Vectorstore](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant)

We'll save our data into a Qdrant collection being mindful...

- **Noduri:** 38
- **Conexiuni:** 28
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, Buffer Memory, Compresie, Document Loader, Extracție Fișier, HTTP API, Mistral Embeddings, OpenAI Chat, Qdrant, Sub-workflow Tool (+1 altele)

### Building RAG Chatbot for Movie Recommendations with Qdrant and Open AI

> Se declanșează manual. obține date din GitHub, folosește Extracție Fișier, folosește OpenAI Embeddings, folosește Document Loader (+7 altele). Detalii: Tool, calling Qdrant's recommendation API based on user's request, transformed by AI agent

- **Noduri:** 27
- **Conexiuni:** 22
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, Buffer Memory, Document Loader, Extracție Fișier, GitHub, HTTP API, OpenAI Chat, OpenAI Embeddings, Qdrant, Sub-workflow Tool (+1 altele)

### Chat with GitHub OpenAPI Specification using RAG (Pinecone and OpenAI)

> Se declanșează manual. folosește HTTP API, folosește Pinecone, folosește Document Loader, folosește Text Splitter (+5 altele). Detalii: RAG workflow in n8n

This is an example of how to use RAG techniques to create a chatbot with n8n. It is an API documentation chatbot that can answer questions about the GitHub API. It uses OpenAI for generating embeddings, the gpt-4o-mini LLM for...

- **Noduri:** 17
- **Conexiuni:** 12
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, Buffer Memory, Document Loader, HTTP API, OpenAI Chat, OpenAI Embeddings, Pinecone, Text Splitter, Vector Store Tool

### Customer Insights with Qdrant, Python and Information Extractor

> Se declanșează manual. folosește HTML, folosește Document Loader, folosește Text Splitter, folosește OpenAI Embeddings (+6 altele). Detalii: Try It Out!

 This workflow generates highly-detailed customer insights from Trustpilot reviews. Works best when dealing with a large number of reviews.

* Import Trustpilot reviews and vectorise in Qdrant vectorstore.
* Identify clusters of popular...

- **Noduri:** 37
- **Conexiuni:** 22
- **Declanșare:** 👆 Manual
- **Integrări:** Document Loader, Extractor Informații, Google Sheets, HTML, HTTP API, OpenAI Chat, OpenAI Embeddings, Qdrant, Sub-workflow, Text Splitter

### Deduplicate Scraping AI Grants for Eligibility using AI

> Rulează zilnic la ora 8:00. folosește HTTP API, folosește OpenAI Chat, folosește Extractor Informații, creează înregistrări în Airtable (+3 altele). Detalii: Try It Out!

 This n8n templates demonstrates how to automatically ingest a source of leads at regular intervals and take advantage of n8n's remove duplicates node to simplify duplicate detection.
Additionally after the leads are captured, a simple...

- **Noduri:** 24
- **Conexiuni:** 15
- **Declanșare:** ⏰ Programat
- **Integrări:** Airtable, Extractor Informații, Gmail, HTML, HTTP API, OpenAI Chat

### Enrich Property Inventory Survey with Image Recognition and AI Agent

> Se declanșează manual. folosește OpenAI Chat, caută în Airtable, folosește HTTP API, folosește Sub-workflow Tool (+4 altele). Detalii: 3. Build an AI Agent who Searches the Internet
[Read more about OpenAI Agents](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai)

This AI Agent has the ability to perform reverse image searches using our captured photos...

- **Noduri:** 29
- **Conexiuni:** 14
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, Airtable, HTTP API, OpenAI, OpenAI Chat, Parser Structurat, Sub-workflow Tool

### Extract insights & analyse YouTube comments via AI Agent chat

> Se declanșează prin mesaj de chat. folosește OpenAI Chat, folosește Sub-workflow Tool, folosește PostgreSQL Memory, folosește AI Agent (+2 altele). Detalii: Set up steps

1. **API Setup**:
 - Create a [Google Cloud](https://console.cloud.google.com/apis/dashboard) project and enable the YouTube Data API.
 - Generate an API key for [Apify](https://www.apify.com?fpr=ujogj).
 - Generate API key for...

- **Noduri:** 29
- **Conexiuni:** 20
- **Integrări:** AI Agent, HTTP API, OpenAI, OpenAI Chat, PostgreSQL Memory, Sub-workflow Tool

### Generate SEO Seed Keywords Using AI

> Se declanșează manual. folosește Anthropic Claude, folosește AI Agent. Detalii: Generate SEO Seed Keywords Using AI

This flow uses an AI node to generate Seed Keywords to focus SEO efforts on based on your ideal customer profile

**Outputs:** 
- List of 20 Seed Keywords


**Pre-requisites / Dependencies:**
- You know your...

- **Noduri:** 15
- **Conexiuni:** 6
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, Anthropic Claude

### Google Analytics: Weekly Report

> Rulează zilnic la ora 7:00. folosește Google Analytics, folosește Email SMTP, folosește Telegram, folosește OpenAI (+1 altele). Detalii: Welcome to my Google Analytics Weekly Report Workflow!

This workflow has the following sequence:

1. time trigger (e.g. every Monday at 7 a.m.)
2. retrieval of Google Analytics data from the last 7 days
3. assignment and summary of the data
4....

- **Noduri:** 14
- **Conexiuni:** 12
- **Declanșare:** ⏰ Programat
- **Integrări:** Calculator, Email SMTP, Google Analytics, OpenAI, Telegram

### Google analytics template

> Rulează programat (schedule). folosește Google Analytics, folosește HTTP API, creează înregistrări în Baserow. Detalii: Send Google analytics to A.I. and save results to baserow

This workflow will check for country views, page engagement and google search console results. It will take this week's data and compare it to last week's data.

[You can read more about...

- **Noduri:** 22
- **Conexiuni:** 17
- **Declanșare:** ⏰ Programat, 👆 Manual
- **Integrări:** Baserow, Google Analytics, HTTP API

### Google analytics template

> Rulează programat (schedule). folosește Google Analytics, folosește HTTP API, creează înregistrări în Baserow. Detalii: Send Google analytics to A.I. and save results to baserow

This workflow will check for country views, page engagement and google search console results. It will take this week's data and compare it to last week's data.

[You can read more about...

- **Noduri:** 22
- **Conexiuni:** 17
- **Declanșare:** ⏰ Programat, 👆 Manual
- **Integrări:** Baserow, Google Analytics, HTTP API

### HN Who is Hiring Scrape

> Se declanșează manual. folosește OpenAI Chat, folosește Parser Structurat, folosește HTTP API, folosește LangChain LLM (+1 altele). Detalii: Hacker News - Who is Hiring Scrape

In this template we setup a scraper for the monthly HN Who is Hiring post. This way we can scrape the data and transform it to a common data strcutre.

First we use the [Algolia Search](https://hn.algolia.com/)...

- **Noduri:** 20
- **Conexiuni:** 14
- **Declanșare:** 👆 Manual
- **Integrări:** Airtable, HTTP API, LangChain LLM, OpenAI Chat, Parser Structurat

### Hacker News to Video Template - AlexK1919

> Se declanșează manual. folosește hackerNews, folosește OpenAI Chat, folosește HTTP Tool, folosește Parser Structurat (+11 altele). Detalii: AlexK1919 
![Alex Kim](https://media.licdn.com/dms/image/v2/D5603AQFOYMkqCPl6Sw/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1718309808352?e=1736985600&v=beta&t=pQKm7lQfUU1ytuC2Gq1PRxNY-XmROFWbo-BjzUPxWOs)

 I’m Alex...

- **Noduri:** 48
- **Conexiuni:** 36
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, Dropbox, Google Drive, HTTP API, HTTP Tool, LinkedIn, OpenAI, OpenAI Chat, Parser Structurat, Twitter/X (+4 altele)
- **Tag-uri:** RunwayML, Video, OpenAI, Creatomate, Leonardo

### Host Your Own AI Deep Research Agent with n8n, Apify and OpenAI o3

> Se declanșează la trimiterea unui formular n8n. folosește Parser Structurat, folosește OpenAI Chat, folosește LangChain LLM, folosește HTTP API (+9 altele). Detalii: n8n DeepResearcher
 This template attempts to replicate OpenAI's DeepResearch feature which, at time of writing, is only available to their pro subscribers.

Though the inner workings of DeepResearch have not been made public, it is presumed the...

- **Noduri:** 87
- **Conexiuni:** 62
- **Integrări:** Google Gemini, HTTP API, LangChain LLM, Markdown, Notion, OpenAI Chat, Parser Structurat, Sub-workflow, executionData, form

### Intelligent Web Query and Semantic Re-Ranking Flow

> Se declanșează prin webhook HTTP. folosește Date/Time, folosește Webhook, folosește Parser Autofix, folosește Parser Structurat (+6 altele). Detalii: Step 2. Setup the Webhook Call Node

**Instructions for Setting Up the Webhook Call and Using It in Your Workflow**

This node is designed to send a **web search query** to the workflow (partly built in this chart) and return the results. Follow...

- **Noduri:** 20
- **Conexiuni:** 14
- **Declanșare:** 🌐 Webhook
- **Integrări:** Anthropic Claude, Date/Time, Google Gemini, HTTP API, LangChain LLM, OpenAI Chat, Parser Autofix, Parser Structurat, Răspuns Webhook, Webhook

### Learn Anything from HN - Get Top Resource Recommendations from Hacker News

> Se declanșează la trimiterea unui formular n8n. folosește Google Gemini, folosește LangChain LLM, folosește hackerNews, folosește HTTP API (+2 altele).

- **Noduri:** 10
- **Conexiuni:** 9
- **Integrări:** Email SMTP, Google Gemini, HTTP API, LangChain LLM, Markdown, hackerNews

### Make OpenAI Citation for File Retrieval RAG

> Se declanșează prin mesaj de chat. folosește Buffer Memory, folosește OpenAI, folosește HTTP API, folosește Markdown. Detalii: Make OpenAI Citation for File Retrieval RAG

 Use case

In this example, we will ensure that all texts from the OpenAI assistant search for citations and sources in the vector store files. We can also format the output for Markdown or HTML...

- **Noduri:** 19
- **Conexiuni:** 11
- **Integrări:** Buffer Memory, HTTP API, Markdown, OpenAI
- **Tag-uri:** sample, assist

### News Extraction

> Rulează zilnic la ora 4:00. folosește HTML, folosește OpenAI, folosește HTTP API, creează înregistrări în nocoDb. Detalii: Scraping posts of a news site without RSS feed


The [News Site](https://www.colt.net/resources/type/news/) from Colt, a telecom company, does not offer an RSS feed, therefore web scraping is the 
choice to extract and process the news.

The goal is...

- **Noduri:** 36
- **Conexiuni:** 17
- **Declanșare:** ⏰ Programat
- **Integrări:** HTML, HTTP API, OpenAI, nocoDb

### Open Deep Research - AI-Powered Autonomous Research Workflow

> Se declanșează prin mesaj de chat. folosește LangChain LLM, folosește lmChatOpenRouter, folosește HTTP API, folosește AI Agent (+2 altele). Detalii: Jina AI Setup Instructions
1. Obtain your API key from https://jina.ai/api-dashboard/key-manager.
2. Configure your Jina AI credential in n8n to ensure secure API access.

- **Noduri:** 17
- **Conexiuni:** 13
- **Integrări:** AI Agent, Buffer Memory, HTTP API, LangChain LLM, Wikipedia Tool, lmChatOpenRouter

### Query Perplexity AI from your n8n workflows

> Se declanșează manual. folosește HTTP API. Detalii: Credentials Setup

1/ Go to the perplexity dashboard, purchase some credits and create an API Key

https://www.perplexity.ai/settings/api

2/ In the perplexity Request node, use Generic Credentials, Header Auth. 

For the name, use the value...

- **Noduri:** 6
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** HTTP API

### Recipe Recommendations with Qdrant and Mistral

> Se declanșează manual. folosește HTTP API, folosește HTML, folosește Mistral Embeddings, folosește Document Loader (+5 altele). Detalii: Try it out!
 This workflow does the following:
* Fetches and stores this week's HelloFresh's menu
* Builds the foundation of a recommendation engine by storing the recipes in a Qdrant Vectorstore and SQLite database.
* Builds an AI Agent that allows...

- **Noduri:** 33
- **Conexiuni:** 20
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, Document Loader, HTML, HTTP API, Mistral AI, Mistral Embeddings, Qdrant, Sub-workflow Tool, Text Splitter

### Reconcile Rent Payments with Local Excel Spreadsheet and OpenAI

> Se declanșează de Monitor Fișiere Locale. folosește Cod Personalizat, folosește Parser Structurat, folosește Fișier Local, folosește Extracție Fișier (+2 altele). Detalii: Try It Out!
 This workflow ingests bank statements to analyses them against a list of tenants using an AI Agent. The agent then flags any issues such as missing payments or incorrect amounts which are exported to a XLSX spreadsheet.

 Note: This...

- **Noduri:** 17
- **Conexiuni:** 10
- **Integrări:** AI Agent, Cod Personalizat, Extracție Fișier, Fișier Local, OpenAI Chat, Parser Structurat

### SERPBear analytics template

> Se declanșează manual. folosește HTTP API, creează înregistrări în Baserow. Detalii: Send Matomo analytics to A.I. and save results to baserow

This workflow will check the Google keywords for your site and it's rank.

[💡 You can read more about this workflow...

- **Noduri:** 10
- **Conexiuni:** 5
- **Declanșare:** ⏰ Programat, 👆 Manual
- **Integrări:** Baserow, HTTP API

### Scrape Trustpilot Reviews with DeepSeek, Analyze Sentiment with OpenAI

> Se declanșează manual. folosește Extractor Informații, folosește HTTP API, folosește HTML, folosește Google Sheets (+3 altele). Detalii: Change to the name of the company registered on Trustpilot and the maximum number of pages to scrape

- **Noduri:** 20
- **Conexiuni:** 15
- **Declanșare:** 👆 Manual
- **Integrări:** Analiză Sentiment, Extractor Informații, Google Sheets, HTML, HTTP API, OpenAI Chat
- **Tag-uri:** Google Drive, OpenAI

### Scrape and summarize webpages with AI

> Se declanșează manual. folosește HTTP API, folosește HTML, folosește Document Loader, folosește Text Splitter (+2 altele). Detalii: Scrape latest Paul Graham essays

- **Noduri:** 15
- **Conexiuni:** 12
- **Declanșare:** 👆 Manual
- **Integrări:** Document Loader, HTML, HTTP API, LangChain Sumarizare, OpenAI Chat, Text Splitter

### Selenium Ultimate Scraper Workflow

> Se declanșează prin webhook HTTP. folosește HTML, folosește OpenAI Chat, folosește HTTP API, folosește Răspuns Webhook (+4 altele). Detalii: N8N Ultimate Scraper - Workflow

This workflow's objective is to collect data from any website page, whether it requires login or not.

For example, you can collect the number of stars of the n8n-ultimate-scraper project on GitHub.

...

- **Noduri:** 63
- **Conexiuni:** 45
- **Declanșare:** 🌐 Webhook
- **Integrări:** Conversie Fișier, Extractor Informații, HTML, HTTP API, OpenAI, OpenAI Chat, Răspuns Webhook, Webhook

### Spot Workplace Discrimination Patterns with AI

> Se declanșează manual. folosește OpenAI Chat, folosește HTTP API, folosește HTML, folosește Extractor Informații (+2 altele). Detalii: ![image](https://quickchart.io/chart?c=%7B%0A%20%20%22type%22%3A%20%22scatter%22%2C%0A%20%20%22data%22%3A%20%7B%0A%20%20%20%20%22datasets%22%3A%20%5B%0A%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%22label%22%3A%20%22Demographics%20Data%22%2C%0A%2...

- **Noduri:** 38
- **Conexiuni:** 23
- **Declanșare:** 👆 Manual
- **Integrări:** Extractor Informații, HTML, HTTP API, LangChain LLM, OpenAI Chat, quickChart
- **Tag-uri:** human_resources, openai

### Survey Insights with Qdrant, Python and Information Extractor

> Se declanșează de Execute Workflow Trigger. folosește OpenAI Embeddings, folosește Document Loader, folosește Text Splitter, folosește Google Sheets (+7 altele). Detalii: Try It Out!

 This workflow generates highly-detailed insights from survey responses. Works best when dealing with a large number of participants.

* Import survey responses and vectorise in Qdrant vectorstore.
* Identify clusters of popular...

- **Noduri:** 42
- **Conexiuni:** 29
- **Declanșare:** 👆 Manual
- **Integrări:** Document Loader, Extractor Informații, Google Sheets, HTTP API, OpenAI Chat, OpenAI Embeddings, Qdrant, Sub-workflow, Text Splitter

### Umami analytics template

> Se declanșează manual. folosește HTTP API, creează înregistrări în Baserow. Detalii: Send data from Umami to A.I. and then save to Baserow

You can find out more about the stats available in the [Umami API](https://umami.is/docs/api/website-stats-api)

Read the [case study...

- **Noduri:** 17
- **Conexiuni:** 10
- **Declanșare:** ⏰ Programat, 👆 Manual
- **Integrări:** Baserow, HTTP API

### Visual Regression Testing with Apify and AI Vision Model

> Rulează zilnic la ora 6:00. descarcă din Google Drive, folosește Google Gemini, folosește Parser Structurat, folosește HTTP API (+5 altele). Detalii: Try It Out!

 This workflow implements an approach to Visual Regression Testing - a means to test websites for defects - using AI Vision Models.

This workflow uses a Google Sheet to track a list of webpages to test and is split into 2 parts; Part A...

- **Noduri:** 34
- **Conexiuni:** 22
- **Declanșare:** ⏰ Programat, 👆 Manual
- **Integrări:** Google Drive, Google Gemini, Google Sheets, HTTP API, LangChain LLM, Parser Structurat, linear

### [1/3 - anomaly detection] [1/2 - KNN classification] Batch upload dataset to Qdrant (crops dataset)

> Se declanșează manual. folosește googleCloudStorage, folosește HTTP API. Detalii: Batch Uploading Dataset to Qdrant 
 This template imports dataset images from storage, creates embeddings for them in batches, and uploads them to Qdrant in batches. In this particular template, we work with [crops...

- **Noduri:** 25
- **Conexiuni:** 13
- **Declanșare:** 👆 Manual
- **Integrări:** HTTP API, googleCloudStorage
- **Tag-uri:** qdrant

### [2/2] KNN classifier (lands dataset)

> Se declanșează de Execute Workflow Trigger. folosește HTTP API. Detalii: KNN classification workflow-tool
 This n8n template takes an image URL (as anomaly detection tool does), and as output, it returns a class of the object on the image (out of land types list)

* An image URL is received via the Execute Workflow...

- **Noduri:** 18
- **Conexiuni:** 9
- **Integrări:** HTTP API
- **Tag-uri:** classifier

### [2/2] KNN classifier (lands dataset)

> Se declanșează de Execute Workflow Trigger. folosește HTTP API. Detalii: KNN classification workflow-tool
 This n8n template takes an image URL (as anomaly detection tool does), and as output, it returns a class of the object on the image (out of land types list)

* An image URL is received via the Execute Workflow...

- **Noduri:** 18
- **Conexiuni:** 9
- **Integrări:** HTTP API
- **Tag-uri:** classifier

### [2/3] Set up medoids (2 types) for anomaly detection (crops dataset)

> Se declanșează manual. folosește HTTP API. Detalii: For anomaly detection
1. The first pipeline is uploading (crops) dataset to Qdrant's collection.
2. **This is the second pipeline, to set up cluster (class) centres in this Qdrant collection & cluster (class) threshold scores.**
3. The third one is...

- **Noduri:** 48
- **Conexiuni:** 23
- **Declanșare:** 👆 Manual
- **Integrări:** HTTP API
- **Tag-uri:** anomaly-detection

### [3/3] Anomaly detection tool (crops dataset)

> Se declanșează de Execute Workflow Trigger. folosește HTTP API. Detalii: For anomaly detection
1. The first pipeline is uploading (crops) dataset to Qdrant's collection.
2. The second pipeline sets up cluster (class) centres in this Qdrant collection & cluster (class) threshold scores.
3. **This is the anomaly detection...

- **Noduri:** 17
- **Conexiuni:** 8
- **Integrări:** HTTP API
- **Tag-uri:** anomaly-detection

### [3/3] Anomaly detection tool (crops dataset)

> Se declanșează de Execute Workflow Trigger. folosește HTTP API. Detalii: For anomaly detection
1. The first pipeline is uploading (crops) dataset to Qdrant's collection.
2. The second pipeline sets up cluster (class) centres in this Qdrant collection & cluster (class) threshold scores.
3. **This is the anomaly detection...

- **Noduri:** 17
- **Conexiuni:** 8
- **Integrări:** HTTP API
- **Tag-uri:** anomaly-detection

### chrome extension backend with AI

> Se declanșează prin webhook HTTP. folosește Webhook, folosește OpenAI, folosește Răspuns Webhook. Detalii: AI prompt
You are an expert financial analyst tasked with providing an advanced technical analyses of a stock or crypto currency chart provided. Your analysis will be based on various technical indicators and will provide simple insights for novice...

- **Noduri:** 5
- **Conexiuni:** 2
- **Declanșare:** 🌐 Webhook
- **Integrări:** OpenAI, Răspuns Webhook, Webhook

### 🔍🛠️Perplexity Researcher to HTML Web Page

> Se declanșează prin webhook HTTP. folosește OpenAI Chat, folosește Parser Structurat, folosește Webhook, folosește Răspuns Webhook (+5 altele). Detalii: Create HTML Page with TailwindCSS Styling

- **Noduri:** 47
- **Conexiuni:** 29
- **Declanșare:** 🌐 Webhook
- **Integrări:** AI Agent, HTTP API, LangChain LLM, OpenAI Chat, Parser Structurat, Răspuns Webhook, Sub-workflow Tool, Telegram, Webhook

---

## Airtable

### AI Agent for project management and meetings with Airtable and Fireflies

> Se declanșează de Execute Workflow Trigger. folosește AI Agent, folosește OpenAI Chat, folosește Sub-workflow Tool, folosește gmailTool (+4 altele). Detalii: Set up steps

 Preparation
1. **Create Accounts**:
 - [N8N](https://n8n.partnerlinks.io/2hr10zpkki6a): For workflow automation.
 - [Airtable](https://airtable.com/): For database hosting and management.
 - [Fireflies](https://fireflies.ai/): For...

- **Noduri:** 18
- **Conexiuni:** 9
- **Declanșare:** 🌐 Webhook
- **Integrări:** AI Agent, Airtable, HTTP API, OpenAI Chat, Sub-workflow Tool, Webhook, gmailTool, googleCalendarTool

### AI Agent to chat with Airtable and analyze data

> Se declanșează prin mesaj de chat. folosește OpenAI Chat, folosește AI Agent, folosește Buffer Memory, folosește Sub-workflow Tool (+4 altele). Detalii: ![5min Logo](https://cflobdhpqwnoisuctsoc.supabase.co/storage/v1/object/public/my_storage/banner.png)
 AI Agent to chat with Airtable and analyze data
**Made by [Mark Shcherbakov](https://www.linkedin.com/in/marklowcoding/) from community...

- **Noduri:** 41
- **Conexiuni:** 27
- **Integrări:** AI Agent, Airtable, Buffer Memory, Cod Personalizat, HTTP API, OpenAI Chat, Sub-workflow Tool

### Get Airtable data in Obsidian Notes

> Se declanșează prin webhook HTTP. caută în airtableTool, folosește OpenAI Chat, folosește AI Agent, folosește Răspuns Webhook (+1 altele). Detalii: Get Airtable Data in Obsidian with AI Agent
<-- Watch the video to see it in action!

**How to Set Up:**
- Install the [Post Webhook Plugin](https://github.com/Masterb1234/obsidian-post-webhook/) in Obsidian.
- Insert the n8n Webhook URL into the...

- **Noduri:** 7
- **Conexiuni:** 4
- **Declanșare:** 🌐 Webhook
- **Integrări:** AI Agent, OpenAI Chat, Răspuns Webhook, Webhook, airtableTool
- **Tag-uri:** Obsidian

### Handling Job Application Submissions with AI and n8n Forms

> Se declanșează la trimiterea unui formular n8n. folosește Extracție Fișier, folosește OpenAI Chat, folosește Parser Structurat, creează înregistrări în Airtable (+6 altele). Detalii: Try It Out!

 This n8n template combines form file uploads with AI components to create a simple but effective job application submission flow.
It's a perfect low-cost solution without the bells and whistles of the surface yet is highly advanced...

- **Noduri:** 23
- **Conexiuni:** 13
- **Integrări:** Airtable, Clasificator Text, Extracție Fișier, HTTP API, LangChain LLM, OpenAI Chat, Parser Structurat, form

### OpenAI Assistant for Hubspot Chat

> Se declanșează prin webhook HTTP. folosește HTTP API, caută în Airtable, creează înregistrări în Airtable, folosește OpenAI (+1 altele). Detalii: Run required actions based on Assistant answer and respond to Assistant with the function answer. 

Each route is a function that you need to define inside your assistant configuration.

- **Noduri:** 34
- **Conexiuni:** 25
- **Declanșare:** 🌐 Webhook
- **Integrări:** Airtable, HTTP API, OpenAI, Webhook

---

## Database and Storage

### Chat with Postgresql Database

> Se declanșează prin mesaj de chat. folosește AI Agent, folosește OpenAI Chat, folosește postgresTool, folosește Buffer Memory. Detalii: 🛠️ Tools Used:
1. Execute SQL Query: Used to execute any query generated by the agent.
2. Get DB Schema and Tables List: It returns the list of all the tables with its schema name.
3. Get Table Definition: It returns table details like column names,...

- **Noduri:** 11
- **Conexiuni:** 6
- **Integrări:** AI Agent, Buffer Memory, OpenAI Chat, postgresTool

### Generate SQL queries from schema only - AI-powered

> Se declanșează prin mesaj de chat. folosește OpenAI Chat, folosește Buffer Memory, folosește mySql, folosește Conversie Fișier (+4 altele). Detalii: LangChain AI Agent's system prompt is modified.
It uses only the database schema to generate SQL queries. The agent creates these queries but does not execute them. Instead, it passes them to subsequent nodes.

**Example:**
"Can you show me the list...

- **Noduri:** 29
- **Conexiuni:** 17
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, Buffer Memory, Conversie Fișier, Extracție Fișier, Fișier Local, OpenAI Chat, mySql

### MongoDB Agent

> Se declanșează prin mesaj de chat. folosește OpenAI Chat, folosește mongoDbTool, folosește Buffer Memory, folosește Sub-workflow Tool (+1 altele). Detalii: AI Agent powered by OpenAI and MongoDB 

This flow is designed to work as an AI autonomous agent that can get chat messages, query data from MongoDB using the aggregation framework.

Following by augmenting the results from the sample movies...

- **Noduri:** 8
- **Conexiuni:** 5
- **Integrări:** AI Agent, Buffer Memory, OpenAI Chat, Sub-workflow Tool, mongoDbTool

### SQL agent with memory

> Se declanșează manual. folosește Buffer Memory, folosește OpenAI Chat, folosește HTTP API, folosește Compresie (+3 altele). Detalii: LangChain SQL Agent can make several queries before producing the final answer.
Try these examples:
1. "Please describe the database". This input usually requires just 1 query + an extra observation to produce a final answer.
2. "What are the...

- **Noduri:** 13
- **Conexiuni:** 8
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, Buffer Memory, Compresie, Fișier Local, HTTP API, OpenAI Chat

### Supabase Insertion & Upsertion & Retrieval

> Se declanșează prin mesaj de chat. descarcă din Google Drive, folosește Document Loader, folosește LangChain Retrieval QA, folosește OpenAI Chat (+5 altele). Detalii: PREPARATION (in Supabase)

- your database needs the extension 'pgvector' enabled -> select Database > Extension > Search for 'vector'
- make sure you have a table that has the following columns (if not, use the query below in the Supabase SQL...

- **Noduri:** 21
- **Conexiuni:** 12
- **Integrări:** Document Loader, Google Drive, LangChain Retrieval QA, OpenAI Chat, OpenAI Embeddings, Supabase, Supabase Vector, Text Splitter, Vector Retriever

---

## Discord

### Discord AI bot

> Se declanșează manual. folosește Webhook, folosește OpenAI, folosește Discord.

- **Noduri:** 9
- **Conexiuni:** 5
- **Declanșare:** 🌐 Webhook, 👆 Manual
- **Integrări:** Discord, OpenAI, Webhook

### Send daily translated Calvin and Hobbes Comics to Discord

> Rulează zilnic la ora 9:00. folosește OpenAI, folosește Discord, folosește OpenAI Chat, folosește Extractor Informații (+1 altele). Detalii: ![](https://raw.githubusercontent.com/2innnnn0/30-Days-of-ChatGPT/refs/heads/main/datapopcorn_logo_50px.png)
 Daily Cartoon (w/ AI Translate)

 How it works
- Automates the retrieval of Calvin and Hobbes daily comics.
- Extracts the comic image URL...

- **Noduri:** 8
- **Conexiuni:** 6
- **Declanșare:** ⏰ Programat
- **Integrări:** Discord, Extractor Informații, HTTP API, OpenAI, OpenAI Chat

### YouTube Videos with AI Summaries on Discord

> Se declanșează de rssFeedReadTrigger. folosește HTTP API, folosește Extracție Fișier, folosește OpenAI, folosește Discord. Detalii: Summarise Your YouTube Videos with AI for Discord

📽️ [Watch the Video Tutorial](https://mrc.fm/ai2d)

* Add your [YouTube channel ID](https://www.youtube.com/account_advanced) to the URL in the first node:...

- **Noduri:** 8
- **Conexiuni:** 6
- **Integrări:** Discord, Extracție Fișier, HTTP API, OpenAI

---

## Forms and Surveys

### Conversational Interviews with AI Agents and n8n Forms

> Se declanșează la trimiterea unui formular n8n. folosește Chat Memory, folosește form, folosește Crypto, folosește Redis (+10 altele). Detalii: Try it out! 

 Conducting user interviews have been traditionally difficult due to preparation, timing and execution costs. What if we let an AI/LLM do it instead?

This template enables automated AI/LLM powered user interviews using n8n forms and...

- **Noduri:** 40
- **Conexiuni:** 28
- **Declanșare:** 🌐 Webhook
- **Integrări:** AI Agent, Buffer Memory, Chat Memory, Crypto, Google Sheets, Groq, HTML, Redis, Răspuns Webhook, Webhook (+1 altele)

### Email Subscription Service with n8n Forms, Airtable and AI

> Rulează zilnic la ora 9:00. caută în Airtable, folosește Gmail, folosește Sub-workflow, actualizează date în Airtable (+8 altele). Detalii: Try It Out!

 This n8n templates demonstrates how to build a simple subscriber service entirely in n8n using n8n forms as a frontend, n8n generally as the backend and Airtable as the storage layer.

This template in particular shows a fully...

- **Noduri:** 32
- **Conexiuni:** 20
- **Declanșare:** ⏰ Programat
- **Integrări:** AI Agent, Airtable, Buffer Memory, Editor Imagine, Gmail, Groq, OpenAI, Sub-workflow, Wikipedia Tool, executionData

### Email Subscription Service with n8n Forms, Airtable and AI (1)

> Rulează zilnic la ora 9:00. caută în Airtable, folosește Gmail, folosește Sub-workflow, actualizează date în Airtable (+8 altele). Detalii: Try It Out!

 This n8n templates demonstrates how to build a simple subscriber service entirely in n8n using n8n forms as a frontend, n8n generally as the backend and Airtable as the storage layer.

This template in particular shows a fully...

- **Noduri:** 32
- **Conexiuni:** 20
- **Declanșare:** ⏰ Programat
- **Integrări:** AI Agent, Airtable, Buffer Memory, Editor Imagine, Gmail, Groq, OpenAI, Sub-workflow, Wikipedia Tool, executionData

### Qualifying Appointment Requests with AI & n8n Forms

> Se declanșează la trimiterea unui formular n8n. folosește form, folosește form, folosește OpenAI Chat, folosește Gmail (+5 altele). Detalii: Try it out!

 This n8n template is a simple appointment scheduling workflow using n8n forms with AI thrown in the mix for good measure. It also uses n8n's wait for approval feature which allows the ability to confirm appointment requests and create...

- **Noduri:** 25
- **Conexiuni:** 14
- **Integrări:** Clasificator Text, Gmail, Google Calendar, LangChain LLM, OpenAI Chat, Sub-workflow, form

---

## Gmail and Email Automation

### AI Email processing autoresponder with approval (Yes/No)

> Se declanșează la primirea unui email. folosește Email IMAP, folosește Markdown, folosește OpenAI Chat, folosește Email SMTP (+5 altele). Detalii: Main Flow

 Preliminary step:
Create a vector database on Qdrant and tokenize the documents useful for generating a response


 How it works
This workflow is designed to automate the process of handling incoming emails, summarizing their content,...

- **Noduri:** 17
- **Conexiuni:** 11
- **Integrări:** AI Agent, Email IMAP, Email SMTP, Gmail, LangChain Sumarizare, Markdown, OpenAI Chat, OpenAI Embeddings, Qdrant

### Analyze & Sort Suspicious Email Contents with ChatGPT

> Se declanșează de Gmail Trigger. folosește HTTP API, folosește OpenAI, folosește Jira, folosește Conversie Fișier. Detalii: ![hctiapi](https://uploads.n8n.io/templates/jira.png)
 Automated Jira Ticket Creation and Email Attachment

This section streamlines the process of logging phishing email reports in Jira, complete with detailed analysis and attachments. The workflow...

- **Noduri:** 25
- **Conexiuni:** 18
- **Integrări:** Conversie Fișier, HTTP API, Jira, OpenAI

### Analyze Suspicious Email Contents with ChatGPT Vision

> Se declanșează de Gmail Trigger. folosește HTTP API, folosește OpenAI, folosește Jira. Detalii: ![hctiapi](https://uploads.n8n.io/templates/hctiapi.png)
 HTML Screenshot Generation and Email Visualization

This section processes an email’s HTML content to create a visual representation, useful for documentation or phishing detection workflows....

- **Noduri:** 18
- **Conexiuni:** 12
- **Integrări:** HTTP API, Jira, OpenAI

### Auto Categorise Outlook Emails with AI

> Se declanșează manual. folosește Ollama, folosește Microsoft Outlook, actualizează date în Microsoft Outlook, folosește Markdown (+2 altele). Detalii: Watch Set Up Video 👇
[![Auto Categorise Outlook Emails with...

- **Noduri:** 36
- **Conexiuni:** 26
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, Markdown, Microsoft Outlook, Ollama

### Auto-label incoming Gmail messages with AI nodes

> Se declanșează de Gmail Trigger. obține date din Gmail, folosește Gmail, folosește Gmail, folosește LangChain LLM (+2 altele). Detalii: ⚠️ Note

1. Complete video guide for this workflow is available [on my YouTube](https://youtu.be/a8Dhj3Zh9vQ). 
2. Remember to add your credentials and configure nodes (covered in the video guide).
3. If you like this workflow, please subscribe to...

- **Noduri:** 19
- **Conexiuni:** 10
- **Integrări:** Gmail, LangChain LLM, OpenAI Chat, Parser Structurat

### Basic Automatic Gmail Email Labelling with OpenAI and Gmail API

> Se declanșează de Gmail Trigger. folosește OpenAI Chat, folosește gmailTool, obține date din gmailTool, folosește gmailTool (+3 altele). Detalii: Gmail labelling agent
- Read the message
- Read existing labels
- Create a new label if needed
- Assign label to message

----

Objective:
Automatically categorize incoming emails based on existing Gmail labels or create a new label if none...

- **Noduri:** 13
- **Conexiuni:** 8
- **Integrări:** AI Agent, Buffer Memory, OpenAI Chat, gmailTool

### Classify lemlist replies using OpenAI and automate reply handling

> Se declanșează de lemlistTrigger. folosește Markdown, folosește OpenAI Chat, folosește Parser Structurat, folosește Slack (+3 altele). Detalii: Get your lemlist API key

1. Go to your lemlist account or create one [HERE](https://app.lemlist.com/create-account)

2. Go to Settings -> Integrations

3. Generate your API Key and copy it

4. On this node, click on create new credential and paste...

- **Noduri:** 18
- **Conexiuni:** 7
- **Integrări:** HTTP API, LangChain LLM, Lemlist, Markdown, OpenAI Chat, Parser Structurat, Slack

### Compose reply draft in Gmail with OpenAI Assistant

> Rulează programat (schedule). folosește HTTP API, folosește Gmail, folosește Markdown, folosește Gmail (+2 altele). Detalii: ⚠️ Note

1. Complete video guide for this workflow is available [on my YouTube](https://youtu.be/a8Dhj3Zh9vQ). 
2. Remember to add your credentials and configure nodes (covered in the video guide).
3. If you like this workflow, please subscribe to...

- **Noduri:** 23
- **Conexiuni:** 12
- **Declanșare:** ⏰ Programat
- **Integrări:** Gmail, HTTP API, Markdown, OpenAI

### Contact Form Text Classifier for eCommerce

> Se declanșează la trimiterea unui formular n8n. folosește Clasificator Text, folosește OpenAI Chat, folosește Email SMTP, adaugă date în Google Sheets. Detalii: Important notes

This very simple workflow is ideal for eCommerce businesses or customer support teams looking to automate and streamline the handling of contact form submissions.

- It is possible to hook any external form such as CF7 for Wordpress...

- **Noduri:** 14
- **Conexiuni:** 8
- **Integrări:** Clasificator Text, Email SMTP, Google Sheets, OpenAI Chat

### Effortless Email Management with AI

> Se declanșează la primirea unui email. folosește Email IMAP, folosește Markdown, folosește Email SMTP, folosește Qdrant (+12 altele). Detalii: STEP 3 - MAIN FLOW


 How it works
This workflow automates the handling of incoming emails, summarizes their content, generates appropriate responses using a retrieval-augmented generation (RAG) approach, and obtains approval or suggestions before...

- **Noduri:** 31
- **Conexiuni:** 19
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, Clasificator Text, Document Loader, Email IMAP, Email SMTP, Gmail, Google Drive, HTTP API, LangChain Sumarizare, Markdown (+5 altele)

### Email Summary Agent

> Rulează zilnic la ora 7:00. citește date din Gmail, folosește OpenAI, folosește Gmail. Detalii: - Sends the summarized email report to recipients with a styled HTML layout.
- Update the "sendTo" and "ccList" fields with the email addresses of your recipients.

- **Noduri:** 9
- **Conexiuni:** 4
- **Declanșare:** ⏰ Programat
- **Integrări:** Gmail, OpenAI
- **Tag-uri:** Product, AI, Building blocks, Finance, IT Ops, OpenAI, Marketing, Support, HR, Project Management, DevOps

### Extract spend details (template)

> Se declanșează de Gmail Trigger. folosește Extracție Fișier, folosește HTML, folosește Parser Structurat, folosește Google Gemini (+3 altele). Detalii: B. Deal with the data
1. Multiple payment info in one mail: input the "sender" of the emails that contain more than one payment info. e.g. credit card daily spend notification
2. One payment info in one mail: input the "sender" of the emails that...

- **Noduri:** 24
- **Conexiuni:** 19
- **Integrări:** Extracție Fișier, Google Gemini, Google Sheets, Groq, HTML, LangChain LLM, Parser Structurat
- **Tag-uri:** Finance

### Gmail AI auto-responder: create draft replies to incoming emails

> Se declanșează de Gmail Trigger. folosește Parser Structurat, folosește OpenAI Chat, folosește Gmail, folosește LangChain LLM. Detalii: ...as a Draft in the conversation

- **Noduri:** 12
- **Conexiuni:** 7
- **Integrări:** Gmail, LangChain LLM, OpenAI Chat, Parser Structurat

### Microsoft Outlook AI Email Assistant

> Se declanșează manual. citește date din Microsoft Outlook, folosește OpenAI Chat, actualizează date în Microsoft Outlook, folosește Parser Structurat (+5 altele). Detalii: CRM Contact List Integration 
For this workflow I am retrieving supplier & client contacts from Monday.com the email assistant has better context to categorise, prioritise and reply to emails.
The list is updated daily or you can change the...

- **Noduri:** 28
- **Conexiuni:** 19
- **Declanșare:** ⏰ Programat, 👆 Manual
- **Integrări:** AI Agent, Airtable, Markdown, Microsoft Outlook, Monday.com, OpenAI Chat, Parser Structurat

### Send a ChatGPT email reply and save responses to Google Sheets

> Se declanșează de Gmail Trigger. folosește OpenAI, folosește Gmail, folosește Crypto, folosește HTML (+6 altele). Detalii: Send a ChatGPT email reply when email received and save responses to Google Sheets
This workflow sends a OpenAI GPT reply when an email is received from specific email recipients. It then saves the initial email and the GPT response to an...

- **Noduri:** 49
- **Conexiuni:** 32
- **Declanșare:** 🌐 Webhook
- **Integrări:** Crypto, Gmail, Google Sheets, HTML, OpenAI, Răspuns Webhook, Webhook

### Send specific PDF attachments from Gmail to Google Drive using OpenAI

> Se declanșează de Gmail Trigger. folosește readPDF, folosește OpenAI, folosește Google Drive. Detalii: Send specific PDF attachments from Gmail to Google Drive using OpenAI

_**DISCLAIMER**: You may have varying success when using this workflow so be prepared to validate the correctness of OpenAI's results._

This workflow reads PDF textual content...

- **Noduri:** 18
- **Conexiuni:** 11
- **Integrări:** Google Drive, OpenAI, readPDF

### Summarize emails with A.I. then send to messenger

> Se declanșează la primirea unui email. folosește Email IMAP, folosește HTTP API. Detalii: Don't use the official Line node. It's outdated.
 Credentials
- Use header auth
- Username: Authorization
- Password: Bearer {channel access token}

You can find your channel access token at the [Line API...

- **Noduri:** 7
- **Conexiuni:** 2
- **Integrări:** Email IMAP, HTTP API

### Summarize emails with A.I. then send to messenger

> Se declanșează la primirea unui email. folosește Email IMAP, folosește HTTP API. Detalii: Don't use the official Line node. It's outdated.
 Credentials
- Use header auth
- Username: Authorization
- Password: Bearer {channel access token}

You can find your channel access token at the [Line API...

- **Noduri:** 7
- **Conexiuni:** 2
- **Integrări:** Email IMAP, HTTP API

### Very simple Human in the loop system email with AI e IMAP

> Se declanșează la primirea unui email. folosește Email IMAP, folosește Markdown, folosește Email SMTP, folosește LangChain Sumarizare (+3 altele). Detalii: How it works
This workflow automates the handling of incoming emails, summarizes their content, generates appropriate responses and validate it through send IMAP email with "Human in the loop" system. 

You can quickly integrate Gmail and Outlook...

- **Noduri:** 16
- **Conexiuni:** 9
- **Integrări:** AI Agent, Email IMAP, Email SMTP, LangChain Sumarizare, Markdown, OpenAI Chat

### create e-mail responses with fastmail and OpenAI

> Se declanșează la primirea unui email. folosește HTTP API, folosește Email IMAP, folosește OpenAI. Detalii: Workflow Description:
This n8n workflow automates the drafting of email replies for Fastmail using OpenAI's GPT-4 model. Here’s the overall process:

1. **Email Monitoring**: The workflow continuously monitors a specified IMAP inbox for new, unread...

- **Noduri:** 11
- **Conexiuni:** 8
- **Integrări:** Email IMAP, HTTP API, OpenAI

### 📈 Receive Daily Market News from FT.com to your Microsoft outlook inbox

> Rulează zilnic la ora 7:00. folosește HTML, folosește HTTP API, folosește Google Gemini, folosește AI Agent (+1 altele). Detalii: Financial News Recap Workflow

This workflow automates the daily email delivery of curated financial news to a designated recipient at 7:00 AM. It extracts relevant financial news articles, structures the content, and sends it in a concise summary...

- **Noduri:** 8
- **Conexiuni:** 6
- **Declanșare:** ⏰ Programat
- **Integrări:** AI Agent, Google Gemini, HTML, HTTP API, Microsoft Outlook

---

## Google Drive and Google Sheets

### AI CV Screening Workflow

> Se declanșează la trimiterea unui formular n8n. folosește Google Gemini, folosește Gmail, folosește LangChain LLM, folosește Extracție Fișier (+1 altele).

- **Noduri:** 7
- **Conexiuni:** 6
- **Integrări:** Extracție Fișier, Gmail, Google Gemini, Google Sheets, LangChain LLM

### AI Logo Sheet Extractor to Airtable

> Se declanșează la trimiterea unui formular n8n. folosește AI Agent, folosește Parser Structurat, actualizează/creează în Airtable, folosește Crypto (+3 altele). Detalii: Instructions

This automation enables you to just upload any Image (via Form) of a Logo Sheet, containing multiple Images of Products, most likely and bringing them in some context to one another. 

After submitting an AI-Agent eats **that Logo...

- **Noduri:** 44
- **Conexiuni:** 31
- **Integrări:** AI Agent, Airtable, Crypto, HTML, OpenAI Chat, Parser Structurat

### AI agent: expense tracker in Google Sheets and n8n chat

> Se declanșează prin mesaj de chat. folosește AI Agent, folosește OpenAI Chat, folosește Buffer Memory, folosește Extractor Informații (+2 altele). Detalii: Save your expenses via chat message. 

LLM will parse your message to structured JSON and save as a new row into Google Sheet.

 Installation
 1. Set up Google Sheets:
Clone this...

- **Noduri:** 10
- **Conexiuni:** 7
- **Integrări:** AI Agent, Buffer Memory, Extractor Informații, Google Sheets, OpenAI Chat, Sub-workflow Tool

### Blog Automation TEMPLATE

> Rulează programat (schedule). folosește Google Sheets, folosește OpenAI Chat, actualizează date în Google Sheets, folosește LangChain LLM (+2 altele). Detalii: Publish Blog-Post
Use a generic XMLHttpRequest with subsequent response handling, since the Wordpress node did not work at all.

- **Noduri:** 35
- **Conexiuni:** 22
- **Declanșare:** ⏰ Programat, 👆 Manual
- **Integrări:** Google Sheets, HTTP API, LangChain LLM, OpenAI Chat
- **Tag-uri:** Published Template

### Build an OpenAI Assistant with Google Drive Integration

> Se declanșează manual. descarcă din Google Drive, folosește Buffer Memory, creează înregistrări în OpenAI, folosește OpenAI (+1 altele). Detalii: Step 3
Update the assistant information with the newly uploaded file

- **Noduri:** 12
- **Conexiuni:** 5
- **Declanșare:** 👆 Manual
- **Integrări:** Buffer Memory, Google Drive, OpenAI
- **Tag-uri:** Google Drive, OpenAI

### Chat with Google Sheet

> Se declanșează de Execute Workflow Trigger. folosește Google Sheets, folosește Sub-workflow Tool, folosește OpenAI Chat, folosește AI Agent. Detalii: Sub-workflow: Custom tool
This can be called by the agent above. It returns three different types of data from the Google Sheet, which can be used together for more complex queries without returning the whole sheet (which might be too big for GPT to...

- **Noduri:** 19
- **Conexiuni:** 12
- **Integrări:** AI Agent, Google Sheets, OpenAI Chat, Sub-workflow Tool

### Fine-tuning with OpenAI models

> Se declanșează manual. descarcă din Google Drive, folosește AI Agent, folosește OpenAI Chat, folosește OpenAI (+1 altele). Detalii: Step 1

Create the training file .jsonl with the following syntax and upload it to Drive.

{"messages": [{"role": "system", "content": "You are an experienced and helpful travel assistant."}, {"role": "user", "content": "What documents are needed to...

- **Noduri:** 9
- **Conexiuni:** 5
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, Google Drive, HTTP API, OpenAI, OpenAI Chat
- **Tag-uri:** Google Drive, OpenAI

### Flux Dev Image Generation Fal.ai

> Se declanșează manual. folosește HTTP API, folosește Google Drive. Detalii: Generic Credential Type
 Header : Authorization
Key $FAL_KEY"

for example:
Key 6f2960baxxxxxxxxx

- **Noduri:** 12
- **Conexiuni:** 8
- **Declanșare:** 👆 Manual
- **Integrări:** Google Drive, HTTP API

### Google Doc Summarizer to Google Sheets

> Se declanșează de googleDriveTrigger. obține date din Google Docs, folosește Wikipedia Tool, folosește Calculator, adaugă date în Google Sheets (+1 altele). Detalii: Description
This workflow is created by WeblineIndia, it streamlines and automates the end-to-end process of managing recently added document files in Google Drive. It begins by identifying the most recently uploaded .doc file in a designated folder...

- **Noduri:** 12
- **Conexiuni:** 5
- **Integrări:** Calculator, Google Docs, Google Sheets, OpenAI, Wikipedia Tool

### Qualify new leads in Google Sheets via OpenAI's GPT-4

> Se declanșează de googleSheetsTrigger. actualizează date în Google Sheets, folosește OpenAI. Detalii: 1. Create a Google Sheet document
* This template uses Google Sheet document connected to Google Forms, but a standalone Sheet document will work too
* Adapt initial trigger to your needs: check for new entries periodically or add a manual...

- **Noduri:** 9
- **Conexiuni:** 4
- **Integrări:** Google Sheets, OpenAI
- **Tag-uri:** Ted's Tech Talks

### RAG Workflow For Company Documents stored in Google Drive

> Se declanșează de googleDriveTrigger. folosește Pinecone, folosește Google Embeddings, folosește Document Loader, folosește Text Splitter (+5 altele). Detalii: Set up steps

1. Google Cloud Project and Vertex AI API:
* Create a Google Cloud project.
* Enable the Vertex AI API for your project.
2. Google AI API Key:
* Obtain a Google AI API key from Google AI Studio.
3. Pinecone Account:
* Create a free...

- **Noduri:** 18
- **Conexiuni:** 15
- **Integrări:** AI Agent, Buffer Memory, Document Loader, Google Drive, Google Embeddings, Google Gemini, Pinecone, Text Splitter, Vector Store Tool

### RAG:Context-Aware Chunking | Google Drive to Pinecone via OpenRouter & Gemini

> Se declanșează manual. folosește lmChatOpenRouter, folosește Pinecone, folosește Google Embeddings, folosește Document Loader (+4 altele). Detalii: Prepare context
In this section, the 
agent node will prepare 
context for a section 
(chunk of text), which 
will then be passed for 
conversion into a vectors 
along with the section itself.

- **Noduri:** 17
- **Conexiuni:** 13
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, Document Loader, Extracție Fișier, Google Drive, Google Embeddings, Pinecone, Text Splitter, lmChatOpenRouter
- **Tag-uri:** Sell

### Remove Advanced Background from Google Drive Images

> Se declanșează de googleDriveTrigger. folosește HTTP API, folosește Google Drive, descarcă din Google Drive, folosește Editor Imagine. Detalii: About this worfklow 

 How it works
This workflow does watch out for new images uploaded within Google Drive. 
Once there are new images it will download the image. And then run some logic, remove the background and add some padding to the output...

- **Noduri:** 16
- **Conexiuni:** 12
- **Integrări:** Editor Imagine, Google Drive, HTTP API

### Summarize Google Sheets form feedback via OpenAI's GPT-4

> Se declanșează manual. folosește Google Sheets, folosește OpenAI, folosește Markdown, folosește Gmail. Detalii: 1. Create a Google Sheet document
* This tutorial uses Google Sheet document connected to Google Forms, but a standalone Sheet document will work too
* Adapt initial trigger to your needs: run manually or at some time intervals

[Link to the Google...

- **Noduri:** 10
- **Conexiuni:** 5
- **Declanșare:** 👆 Manual
- **Integrări:** Gmail, Google Sheets, Markdown, OpenAI
- **Tag-uri:** Ted's Tech Talks

### Telegram-bot AI Da Nang

> Se declanșează la primirea unui mesaj Telegram. folosește Telegram, folosește Google Sheets, folosește AI Agent, folosește Telegram (+2 altele). Detalii: Retrieve Data
Get schedule from Google Spreadsheet and convert it to a Markdown-Table as context for the LLM

- **Noduri:** 23
- **Conexiuni:** 14
- **Integrări:** AI Agent, Buffer Memory, Google Sheets, Telegram, lmChatOpenRouter

### Vision-Based AI Agent Scraper - with Google Sheets, ScrapingBee, and Gemini

> Se declanșează manual. folosește HTTP API, folosește Parser Structurat, folosește Google Gemini, folosește Google Sheets (+4 altele). Detalii: ✨ Vision-Based AI Agent Scraper - with Google Sheets, ScrapingBee, and Gemini

 Important notes :
 Check legal regulations: 
This workflow involves scraping, so make sure to check the legal regulations around scraping in your country before getting...

- **Noduri:** 29
- **Conexiuni:** 12
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, Google Gemini, Google Sheets, HTTP API, Markdown, Parser Structurat, Sub-workflow Tool

### template in store

> Se declanșează de googleDriveTrigger. descarcă din Google Drive, folosește Telegram, folosește OpenAI, folosește writeBinaryFile (+3 altele). Detalii: Description
This automation allows you to upload a video to a configured Google Drive folder, and it will automatically create descriptions and upload it to Instagram and TikTok.

 How to Use
1. Generate an API token at upload-post.com and add to...

- **Noduri:** 13
- **Conexiuni:** 9
- **Integrări:** Google Drive, HTTP API, OpenAI, Telegram, readBinaryFile, writeBinaryFile

---

## HR and Recruitment

### BambooHR AI-Powered Company Policies and Benefits Chatbot

> Se declanșează manual. folosește Document Loader, folosește OpenAI Embeddings, folosește Text Splitter, folosește Buffer Memory (+12 altele). Detalii: AI Chatbot Operating Guidelines 
- When an employee asks for a contact person, first attempt to find the relevant contact in company_files. 
- If a contact person is found but their details (e.g., email or phone number) are missing, use the...

- **Noduri:** 50
- **Conexiuni:** 35
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, BambooHR, Buffer Memory, Clasificator Text, Document Loader, Extractor Informații, LangChain LLM, OpenAI Chat, OpenAI Embeddings, Parser Autofix (+5 altele)

### CV Screening with OpenAI

> Se declanșează manual. folosește Extracție Fișier, folosește HTTP API. Detalii: ![5min Logo](https://cflobdhpqwnoisuctsoc.supabase.co/storage/v1/object/public/my_storage/Untitled%20(1500%20x%20300%20px).png)
 CV Screening with OpenAI
**Made by [Mark Shcherbakov](https://www.linkedin.com/in/marklowcoding/) from community...

- **Noduri:** 11
- **Conexiuni:** 5
- **Declanșare:** 👆 Manual
- **Integrări:** Extracție Fișier, HTTP API

### HR & IT Helpdesk Chatbot with Audio Transcription

> Se declanșează manual. folosește HTTP API, folosește Extracție Fișier, folosește vectorStorePGVector, folosește OpenAI Embeddings (+8 altele). Detalii: 4. HR & IT AI Agent Provides Helpdesk Support 
n8n's AI agents allow you to create intelligent and interactive workflows that can access and retrieve data from internal knowledgebases. In this workflow, the AI agent is configured to provide answers...

- **Noduri:** 27
- **Conexiuni:** 18
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, Document Loader, Extracție Fișier, HTTP API, OpenAI, OpenAI Chat, OpenAI Embeddings, PostgreSQL Memory, Telegram, Text Splitter (+2 altele)

### HR Job Posting and Evaluation with AI

> Se declanșează la trimiterea unui formular n8n. creează înregistrări în Airtable, folosește Google Drive, descarcă din Google Drive, folosește Extracție Fișier (+10 altele). Detalii: Actions
-  Change the `Form Description` with the job description you are hiring for.
-  Make sure to check and change the prompts if need be to suit your use case.
-  Use the Simple Applicant Tracker template on Airtable to set up the tables...

- **Noduri:** 36
- **Conexiuni:** 28
- **Integrări:** AI Agent, Airtable, Email SMTP, Extracție Fișier, Google Drive, OpenAI, OpenAI Chat, Parser Structurat, airtableTool, form (+1 altele)
- **Tag-uri:** HR

---

## Instagram Twitter Social Media

### Create dynamic Twitter profile banner

> Se declanșează manual. folosește HTTP API, folosește Editor Imagine, folosește Editor Imagine.

- **Noduri:** 12
- **Conexiuni:** 11
- **Declanșare:** 👆 Manual
- **Integrări:** Editor Imagine, HTTP API

### Generate Instagram Content from Top Trends with AI Image Generation

> Rulează programat (schedule). folosește Telegram, folosește HTTP API, folosește PostgreSQL, folosește PostgreSQL (+3 altele). Detalii: Automated Instagram Content Creation from Trending Posts

This workflow automates the process of discovering and recreating trending content on Instagram:

1. Content Discovery:
 - Scrapes top trending posts from specific hashtags (blender3d,...

- **Noduri:** 44
- **Conexiuni:** 24
- **Declanșare:** ⏰ Programat
- **Integrări:** HTTP API, OpenAI, PostgreSQL, Telegram, facebookGraphApi

### InstaTest

> Se declanșează prin webhook HTTP. folosește Buffer Memory, folosește OpenAI Chat, folosește Răspuns Webhook, folosește Webhook (+1 altele). Detalii: Easy Instagram(via ManyChat) bot
---
 Description:
This template is a main part of Entire solution. It's getting new message from Instagram via ManyChat(Extra No-Code tool for getting and sending message in Instagram). Generating message using...

- **Noduri:** 11
- **Conexiuni:** 5
- **Declanșare:** 🌐 Webhook
- **Integrări:** AI Agent, Buffer Memory, OpenAI Chat, Răspuns Webhook, Webhook
- **Tag-uri:** AI

### OpenAI-powered tweet generator

> Se declanșează manual. folosește HTTP API, adaugă date în Airtable.

- **Noduri:** 5
- **Conexiuni:** 4
- **Declanșare:** 👆 Manual
- **Integrări:** Airtable, HTTP API

### Post New YouTube Videos to X

> Rulează programat (schedule). folosește Twitter/X, folosește OpenAI, folosește youTube. Detalii: 🆔 Ensure you enter your YouTube Channel ID in the "Channel ID" field of this node. You can find your [Channel ID here](https://youtube.com/account_advanced).

- **Noduri:** 6
- **Conexiuni:** 3
- **Declanșare:** ⏰ Programat
- **Integrări:** OpenAI, Twitter/X, youTube

### Reddit AI digest

> Se declanșează manual. caută în reddit, folosește OpenAI, folosește OpenAI. Detalii: What we learned
- 🪶 **Writing prompts**: small changes in the type of prompt result in very different results. e.g. for Summarising OpenAI would use multiple sentences even if we asked it to use only 1. We got better results by following OpenAI's...

- **Noduri:** 15
- **Conexiuni:** 9
- **Declanșare:** 👆 Manual
- **Integrări:** OpenAI, reddit

### Social Media Analysis and Automated Email Generation

> Se declanșează de googleSheetsTrigger. folosește HTTP API, folosește OpenAI Chat, folosește Parser Structurat, folosește LangChain LLM (+2 altele). Detalii: Social Media Analysis and Automated Email Generation

> by Thomas Vie [Thomas@pollup.net](mailto:thomas@pollup.net)

 **Who is this for?**
This template is ideal for marketers, lead generation specialists, and business professionals seeking to...

- **Noduri:** 19
- **Conexiuni:** 13
- **Integrări:** Email SMTP, Google Sheets, HTTP API, LangChain LLM, OpenAI Chat, Parser Structurat

### Speed Up Social Media Banners With BannerBear.com

> Se declanșează la trimiterea unui formular n8n. folosește HTTP API, folosește bannerbear, folosește Discord, folosește OpenAI. Detalii: Try It Out!
 This workflow does the following:
* Uses an n8n form to capture an event to be announced.
* Form includes imagery required for the event and this is sent to OpenAI Dalle-3 service to generate.
* Event details as well as the ai-generated...

- **Noduri:** 16
- **Conexiuni:** 6
- **Integrări:** Discord, HTTP API, OpenAI, bannerbear

### Twitter Virtual AI Influencer

> Rulează programat (schedule). folosește Twitter/X, folosește OpenAI. Detalii: Scheduled posting 
Write a tweet every 6 hours and randomize the minutes that it's posted at to make it seem natural.

- **Noduri:** 12
- **Conexiuni:** 5
- **Declanșare:** ⏰ Programat, 👆 Manual
- **Integrări:** OpenAI, Twitter/X

### Update Twitter banner using HTTP request

> Se declanșează manual. folosește HTTP API.

- **Noduri:** 4
- **Conexiuni:** 2
- **Declanșare:** 👆 Manual
- **Integrări:** HTTP API

---

## Notion

### Add positive feedback messages to a table in Notion

> Se declanșează la trimiterea unui formular n8n. folosește googleCloudNaturalLanguage, folosește Notion, folosește Slack, folosește Trello.

- **Noduri:** 6
- **Conexiuni:** 4
- **Integrări:** Notion, Slack, Trello, googleCloudNaturalLanguage

### Automate Competitor Research with Exa.ai, Notion and AI Agents

> Se declanșează manual. folosește OpenAI Chat, folosește HTTP Tool, folosește Parser Structurat, folosește Notion (+2 altele). Detalii: Try It Out!

 This workflow builds a competitor research agent using Exa.ai as a starting point. The HTTP Request tool is used to demonstrate how you can build powerful agents with minimal effort.

* Using Exa's findSimilar search, we ask it to look...

- **Noduri:** 39
- **Conexiuni:** 30
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, HTTP API, HTTP Tool, Notion, OpenAI Chat, Parser Structurat

### Automate LinkedIn Posts with AI

> Rulează zilnic la ora 15:00. actualizează date în Notion, folosește LinkedIn, folosește HTTP API, folosește OpenAI (+1 altele). Detalii: Fetch the day's post from my Notion database
A Notion _"database"_ is just a table on a Notion Page.
This table will have various rows, for which a minimum of three columns are required:
- Name
- Status
- Date

The Date column is the most important,...

- **Noduri:** 11
- **Conexiuni:** 8
- **Declanșare:** ⏰ Programat
- **Integrări:** HTTP API, LinkedIn, Notion, OpenAI

### Hugging Face to Notion

> Rulează zilnic la ora 8:00. folosește HTTP API, folosește HTML, citește date din Notion, folosește OpenAI (+1 altele).

- **Noduri:** 11
- **Conexiuni:** 11
- **Declanșare:** ⏰ Programat
- **Integrări:** HTML, HTTP API, Notion, OpenAI

### Notion AI Assistant Generator

> Se declanșează prin mesaj de chat. folosește Notion, folosește Parser Autofix, folosește Anthropic Claude, folosește Parser Structurat (+2 altele). Detalii: Generate new workflow version for specific notion db schema
Input a Notion database URL and get an AI Assistant chatbot workflow for it based on this template: https://n8n.io/workflows/2413-notion-knowledge-base-ai-assistant/

Project in notion:...

- **Noduri:** 24
- **Conexiuni:** 16
- **Integrări:** AI Agent, Anthropic Claude, Clasificator Text, Notion, Parser Autofix, Parser Structurat

### Notion knowledge base AI assistant

> Se declanșează prin mesaj de chat. folosește OpenAI Chat, folosește HTTP Tool, folosește Notion, folosește Buffer Memory (+1 altele). Detalii: Written set up steps
1. Add a Notion credential to your n8n workspace (follow [this Notion guide](https://developers.notion.com/docs/create-a-notion-integration))
2. [Duplicate Company knowledge base Notion...

- **Noduri:** 12
- **Conexiuni:** 7
- **Integrări:** AI Agent, Buffer Memory, HTTP Tool, Notion, OpenAI Chat

### Prod: Notion to Vector Store - Dimension 768

> Se declanșează de notionTrigger. folosește textSplitterTokenSplitter, citește date din Notion, folosește Document Loader, folosește Google Embeddings (+1 altele).

- **Noduri:** 8
- **Conexiuni:** 7
- **Integrări:** Document Loader, Google Embeddings, Notion, Pinecone, textSplitterTokenSplitter
- **Tag-uri:** Production

### RAG on living data

> Se declanșează prin mesaj de chat. folosește OpenAI Embeddings, folosește textSplitterTokenSplitter, folosește LangChain Retrieval QA, folosește Vector Retriever (+5 altele). Detalii: Store additional meta data with each embed, especially the Notion ID, which can be later used to find all belonging entries of one page, even if they got split into multiple embeds.

- **Noduri:** 34
- **Conexiuni:** 18
- **Declanșare:** ⏰ Programat
- **Integrări:** Document Loader, LangChain Retrieval QA, Notion, OpenAI Chat, OpenAI Embeddings, Supabase, Supabase Vector, Vector Retriever, textSplitterTokenSplitter

### Store Notion's Pages as Vector Documents into Supabase with OpenAI

> Se declanșează de notionTrigger. folosește OpenAI Embeddings, folosește textSplitterTokenSplitter, citește date din Notion, folosește Document Loader (+1 altele). Detalii: Store Notion's Pages as Vector Documents into Supabase

**This workflow assumes you have a Supabase project with a table that has a vector column. If you don't have it, follow the instructions here:** [Supabase Vector Columns...

- **Noduri:** 9
- **Conexiuni:** 7
- **Integrări:** Document Loader, Notion, OpenAI Embeddings, Supabase Vector, textSplitterTokenSplitter

### mails2notion V2

> Se declanșează de Gmail Trigger. folosește OpenAI Chat, folosește Calculator, folosește Parser Structurat, folosește Gmail (+5 altele). Detalii: The Email is processed in multiple ways:
- An actionable task is being generated based on the content, consisting of a short title, a short description and optionally a few details as bullet points
- A detailed Email summary is being generated
-...

- **Noduri:** 38
- **Conexiuni:** 22
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, Airtable, Calculator, Gmail, HTTP API, OpenAI Chat, Parser Structurat

---

## OpenAI and LLMs

### AI Agent : Google calendar assistant using OpenAI

> Se declanșează prin mesaj de chat. folosește OpenAI Chat, folosește Buffer Memory, citește date din googleCalendarTool, folosește googleCalendarTool (+1 altele). Detalii: Tools Agent - Calendar AI Agent

This **node** configures the **AI agent** for interaction with Google Calendar. 
It includes the following features:

- A **prompt source**: This is the user message derived from the chat input of the preceding node...

- **Noduri:** 13
- **Conexiuni:** 6
- **Integrări:** AI Agent, Buffer Memory, OpenAI Chat, googleCalendarTool

### AI Agent To Chat With Files In Supabase Storage

> Se declanșează manual. folosește HTTP API, folosește Document Loader, folosește Text Splitter, folosește Extracție Fișier (+7 altele). Detalii: Set up steps

1. **Fetch File List from Supabase**:
 - Use Supabase to retrieve the stored file list from a specified bucket.
 - Add logic to manage empty folder placeholders returned by Supabase, avoiding incorrect processing.

2. **Compare and...

- **Noduri:** 33
- **Conexiuni:** 21
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, Document Loader, Extracție Fișier, HTTP API, OpenAI Chat, OpenAI Embeddings, Supabase, Supabase Vector, Text Splitter, Vector Store Tool

### AI Agent for realtime insights on meetings

> Se declanșează prin webhook HTTP. folosește OpenAI, folosește PostgreSQL, folosește postgresTool, folosește HTTP API (+2 altele). Detalii: ![5min Logo](https://res.cloudinary.com/de9jgixzm/image/upload/v1739773200/Skool%20Assets/ejm3hqnvhgwpnu2fv92s.png)
 AI Agent for realtime insights on meetings
**Made by [Mark Shcherbakov](https://www.linkedin.com/in/marklowcoding/) from community...

- **Noduri:** 19
- **Conexiuni:** 9
- **Declanșare:** 🌐 Webhook
- **Integrări:** HTTP API, OpenAI, PostgreSQL, Supabase, Webhook, postgresTool

### AI Agent to chat with Supabase_PostgreSQL DB

> Se declanșează prin mesaj de chat. folosește OpenAI Chat, folosește postgresTool, folosește AI Agent. Detalii: ![5min Logo](https://res.cloudinary.com/de9jgixzm/image/upload/v1739773200/Skool%20Assets/ejm3hqnvhgwpnu2fv92s.png)
 AI Agent to chat with Supabase/PostgreSQL DB
**Made by [Mark Shcherbakov](https://www.linkedin.com/in/marklowcoding/) from community...

- **Noduri:** 11
- **Conexiuni:** 5
- **Integrări:** AI Agent, OpenAI Chat, postgresTool

### AI Agent to chat with you Search Console Data, using OpenAI and Postgres

> Se declanșează prin webhook HTTP. folosește PostgreSQL Memory, folosește OpenAI Chat, folosește Webhook, folosește Răspuns Webhook (+3 altele). Detalii: AI Agent to Chat with Your Search Console Data

This **AI Agent enables you to interact with your Search Console data** through a **chat interface**. Each node is **documented within the template**, providing sufficient information for setup and...

- **Noduri:** 30
- **Conexiuni:** 13
- **Declanșare:** 🌐 Webhook
- **Integrări:** AI Agent, HTTP API, OpenAI Chat, PostgreSQL Memory, Răspuns Webhook, Sub-workflow Tool, Webhook

### AI Agent with Ollama for current weather and wiki

> Se declanșează prin mesaj de chat. folosește Wikipedia Tool, folosește Buffer Memory, folosește AI Agent, folosește HTTP Tool (+1 altele). Detalii: In System Message, add the following.

"You are a helpful assistant, with weather tool and wiki tool. find out the latitude and longitude information of a location then use the weather tool for current weather and weather forecast. For general info,...

- **Noduri:** 10
- **Conexiuni:** 5
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, Buffer Memory, HTTP Tool, Ollama, Wikipedia Tool

### AI Customer feedback sentiment analysis

> Se declanșează la trimiterea unui formular n8n. adaugă date în Google Sheets, folosește OpenAI. Detalii: Instructions
1. Connect Google sheets
2. Connect your OpenAi account (api key + org Id)
3. Create a customer feedback form, use an existing one or use the one below as example. 
All set!


- Here is the example google sheet being used in this...

- **Noduri:** 9
- **Conexiuni:** 3
- **Integrări:** Google Sheets, OpenAI

### AI Data Extraction with Dynamic Prompts and Airtable

> Se declanșează prin webhook HTTP. folosește HTTP API, folosește Extracție Fișier, folosește LangChain LLM, folosește OpenAI Chat (+5 altele). Detalii: Try It Out!
 This n8n template powers a "dynamic" or "user-defined" prompts with PDF workflow pattern for a [Airtable](https://airtable.com/invite/r/cKzxFYVc) table. Simply put, it allows users to populate a spreadsheet using prompts without...

- **Noduri:** 51
- **Conexiuni:** 36
- **Declanșare:** 🌐 Webhook, 👆 Manual
- **Integrări:** Airtable, Extracție Fișier, HTTP API, LangChain LLM, OpenAI Chat, Webhook

### AI Data Extraction with Dynamic Prompts and Baserow

> Se declanșează prin webhook HTTP. folosește Webhook, folosește HTTP API, folosește Extracție Fișier, folosește LangChain LLM (+1 altele). Detalii: Try It Out!
 This n8n template powers a "dynamic" or "user-defined" prompts with PDF workflow pattern for a [Baserow](https://baserow.io) table. Simply put, it allows users to populate a spreadsheet using prompts without touching the underlying...

- **Noduri:** 45
- **Conexiuni:** 30
- **Declanșare:** 🌐 Webhook
- **Integrări:** Extracție Fișier, HTTP API, LangChain LLM, OpenAI Chat, Webhook

### AI Fitness Coach Strava Data Analysis and Personalized Training Insights

> Se declanșează de stravaTrigger. folosește Google Gemini, folosește Gmail, folosește AI Agent, folosește Email SMTP (+1 altele). Detalii: Developed by Amjid Ali

Thank you for using this workflow template. It has taken me countless hours of hard work, research, and dedication to develop, and I sincerely hope it adds value to your work.

If you find this template helpful, I kindly ask...

- **Noduri:** 15
- **Conexiuni:** 8
- **Integrări:** AI Agent, Email SMTP, Gmail, Google Gemini, WhatsApp

### AI Powered Web Scraping with Jina, Google Sheets and OpenAI _ the EASY way

> Se declanșează manual. adaugă date în Google Sheets, folosește OpenAI Chat, folosește Extractor Informații, folosește HTTP API. Detalii: Start here: Step-by Step Youtube Tutorial :star:

[![AI Powered Web Scraping : the EASY way with n8n and Jina.ai (no-code!)](https://img.youtube.com/vi/f3AJYXHirr8/sddefault.jpg)](https://youtu.be/f3AJYXHirr8)

[Google Sheet...

- **Noduri:** 7
- **Conexiuni:** 5
- **Declanșare:** 👆 Manual
- **Integrări:** Extractor Informații, Google Sheets, HTTP API, OpenAI Chat

### AI Social Media Caption Creator

> Se declanșează de airtableTrigger. folosește AI Agent, folosește OpenAI Chat, folosește Buffer Memory, folosește Airtable (+2 altele). Detalii: Welcome to my AI Social Media Caption Creator Workflow!

This workflow automatically creates a social media post caption in an editorial plan in Airtable. It also uses background information on the target group, tonality, etc. stored in Airtable.

...

- **Noduri:** 10
- **Conexiuni:** 8
- **Integrări:** AI Agent, Airtable, Buffer Memory, OpenAI Chat, airtableTool

### AI Voice Chat using Webhook, Memory Manager, OpenAI, Google Gemini & ElevenLabs

> Se declanșează prin webhook HTTP. folosește Chat Memory, folosește Buffer Memory, folosește Google Gemini, folosește Răspuns Webhook (+4 altele). Detalii: *  For the Text-to-Speech part, we'll use ElevenLabs.io, which is free and offers a variety of voices to choose from. However, you can also use the OpenAI `"Generate audio"` node instead.

















*  Since there is no pre-built node for...

- **Noduri:** 15
- **Conexiuni:** 10
- **Declanșare:** 🌐 Webhook
- **Integrări:** Buffer Memory, Chat Memory, Google Gemini, HTTP API, LangChain LLM, OpenAI, Răspuns Webhook, Webhook
- **Tag-uri:** Workflows

### AI agent chat

> Se declanșează prin mesaj de chat. folosește OpenAI Chat, folosește Buffer Memory, folosește SerpAPI Tool, folosește AI Agent.

- **Noduri:** 5
- **Conexiuni:** 4
- **Integrări:** AI Agent, Buffer Memory, OpenAI Chat, SerpAPI Tool

### AI chat with any data source (using the n8n workflow tool)

> Se declanșează prin mesaj de chat. folosește hackerNews, folosește AI Agent, folosește OpenAI Chat, folosește Sub-workflow Tool. Detalii: Main workflow: AI agent using custom tool
Try it out by clicking 'Chat' and entering 'What is the 5th most popular post ever on Hacker News?'

- **Noduri:** 12
- **Conexiuni:** 6
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, OpenAI Chat, Sub-workflow Tool, hackerNews

### AI chatbot that can search the web

> Se declanșează prin mesaj de chat. folosește OpenAI Chat, folosește Wikipedia Tool, folosește Buffer Memory, folosește SerpAPI Tool (+1 altele). Detalii: The conversation history(last 20 messages) is stored in a buffer memory

- **Noduri:** 9
- **Conexiuni:** 5
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, Buffer Memory, OpenAI Chat, SerpAPI Tool, Wikipedia Tool

### AI web researcher for sales

> Se declanșează manual. folosește OpenAI Chat, folosește Sub-workflow Tool, folosește SerpAPI Tool, folosește Parser Structurat (+3 altele). Detalii: Read Me

This workflow allows you to do account research with the web using AI.

The advanced AI module has 2 capabilities: 
- Research Google using SerpAPI
- Visit and get website content using a sub-workflow


From an unstructured input like a...

- **Noduri:** 22
- **Conexiuni:** 13
- **Declanșare:** ⏰ Programat, 👆 Manual
- **Integrări:** AI Agent, Google Sheets, OpenAI Chat, Parser Structurat, SerpAPI Tool, Sub-workflow Tool

### AI-Driven Lead Management and Inquiry Automation with ERPNext & n8n

> Se declanșează prin webhook HTTP. folosește AI Agent, folosește OpenAI Chat, folosește googleSheetsTool, folosește Microsoft Outlook (+3 altele). Detalii: Developed by Amjid Ali

Thank you for using this workflow template. It has taken me countless hours of hard work, research, and dedication to develop, and I sincerely hope it adds value to your work.

If you find this template helpful, I kindly ask...

- **Noduri:** 27
- **Conexiuni:** 15
- **Declanșare:** 🌐 Webhook
- **Integrări:** AI Agent, HTTP API, Microsoft Outlook, OpenAI Chat, Webhook, googleDocsTool, googleSheetsTool

### AI-Generated Summary Block for WordPress Posts - with OpenAI, WordPress, Google Sheets & Slack

> Se declanșează manual. folosește Clasificator Text, folosește OpenAI Chat, folosește Webhook, folosește HTTP API (+8 altele). Detalii: Trigger - Two Options
To use this workflow, you have two trigger options.

The default trigger is **"When clicking 'Test workflow'"**, allowing you to manually test the scenario.

If you want to use this workflow in production, you can choose one of...

- **Noduri:** 32
- **Conexiuni:** 20
- **Declanșare:** 🌐 Webhook, ⏰ Programat, 👆 Manual
- **Integrări:** Clasificator Text, Date/Time, Google Sheets, HTTP API, Markdown, OpenAI, OpenAI Chat, Slack, Webhook, WordPress

### AI-Powered Candidate Shortlisting Automation for ERPNext

> Se declanșează prin webhook HTTP. actualizează date în erpNext, obține date din erpNext, folosește Google Gemini, folosește HTTP API (+6 altele). Detalii: Developed by Amjid Ali

Thank you for using this workflow template. It has taken me countless hours of hard work, research, and dedication to develop, and I sincerely hope it adds value to your work.

If you find this template helpful, I kindly ask...

- **Noduri:** 39
- **Conexiuni:** 19
- **Declanșare:** 🌐 Webhook
- **Integrări:** AI Agent, Extracție Fișier, Google Gemini, HTTP API, Microsoft Outlook, Webhook, WhatsApp, erpNext

### AI-powered WooCommerce Support-Agent

> Se declanșează de Execute Workflow Trigger. folosește Buffer Memory, citește date din WooCommerce, folosește HTTP API, folosește dhl (+5 altele). Detalii: How to supply user email
As we want to ensure that customers can only query information about their own orders, the email address gets encrypted in the backend, and then decrypt again in this workflow. If the email was allowed to be set unencrypted,...

- **Noduri:** 40
- **Conexiuni:** 23
- **Declanșare:** 🌐 Webhook
- **Integrări:** AI Agent, Buffer Memory, HTTP API, OpenAI Chat, Răspuns Webhook, Sub-workflow Tool, Webhook, WooCommerce, dhl

### Actioning Your Meeting Next Steps using Transcripts and AI

> Se declanșează manual. folosește OpenAI Chat, folosește HTTP API, descarcă din Google Drive, folosește Extracție Fișier (+6 altele). Detalii: 3: Using the Custom Workflow Tool
[Read more about Workflow Triggers](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflowtrigger)

One common implementation of tool use is to set them up as workflows which are intended...

- **Noduri:** 28
- **Conexiuni:** 16
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, Extracție Fișier, Google Calendar, Google Drive, HTTP API, OpenAI Chat, Parser Structurat, Sub-workflow Tool

### Advanced AI Demo (Presented at AI Developers #14 meetup)

> Se declanșează prin mesaj de chat. folosește Slack, folosește Text Splitter, folosește OpenAI Embeddings, folosește Document Loader (+12 altele). Detalii: ![h](https://i.imghippo.com/files/d9Bgv1721858679.pngfull-width)
[Open Calendar](https://calendar.google.com/calendar/u/0/r/day/2024/7/26)

- **Noduri:** 39
- **Conexiuni:** 19
- **Declanșare:** 🌐 Webhook
- **Integrări:** AI Agent, Anthropic Claude, Buffer Memory, Clasificator Text, Document Loader, Gmail, HTTP API, HTTP Tool, LangChain Retrieval QA, OpenAI Chat (+6 altele)

### Agent with custom HTTP Request

> Se declanșează prin mesaj de chat. folosește OpenAI Chat, folosește HTTP API, folosește AI Agent, folosește Markdown (+1 altele). Detalii: Post-processing of the HTML page:
1. Keep only <BODY> content
2. Remove inline <SCRIPT> tag entirely, as well as: NOSCRIPT, IFRAME, OBJECT, EMBED, VIDEO, AUDIO, SVG, and HTML comments.
3. In case query parameter method=simplified, replace all page...

- **Noduri:** 20
- **Conexiuni:** 13
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, HTTP API, Markdown, OpenAI Chat, Sub-workflow Tool

### Ask a human

> Se declanșează de Execute Workflow Trigger. folosește Buffer Memory, folosește Sub-workflow Tool, folosește AI Agent, folosește Slack (+1 altele). Detalii: Sub-workflow: Custom tool
The agent above can call this workflow. It checks if the user has supplied an email address. If they haven't it prompts them to provide one. If they have, it messages a customer support channel for help.

- **Noduri:** 17
- **Conexiuni:** 7
- **Integrări:** AI Agent, Buffer Memory, OpenAI Chat, Slack, Sub-workflow Tool

### Automate Customer Support Issue Resolution using AI Text Classifier

> Rulează programat (schedule). folosește OpenAI Chat, citește date din Jira, actualizează date în Jira, folosește Jira (+9 altele). Detalii: Try It Out!

 This n8n template is designed to assist and improve customer support team member capacity by automating the resolution of long-lived and forgotten JIRA issues.

* Schedule Trigger runs daily to check for long-lived unresolved issues...

- **Noduri:** 36
- **Conexiuni:** 24
- **Declanșare:** ⏰ Programat
- **Integrări:** AI Agent, Analiză Sentiment, Clasificator Text, Jira, LangChain LLM, OpenAI Chat, Parser Structurat, Slack, Sub-workflow, jiraTool (+1 altele)

### Automate Image Validation Tasks using AI Vision

> Se declanșează manual. folosește Parser Structurat, descarcă din Google Drive, folosește Editor Imagine, folosește LangChain LLM (+1 altele). Detalii: 2. Verify Passport Photo Validity Using AI Vision Model
[Learn more about Basic LLM Chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm)

Verifying if a photo is suitable for a passport photo is a...

- **Noduri:** 11
- **Conexiuni:** 7
- **Declanșare:** 👆 Manual
- **Integrări:** Editor Imagine, Google Drive, Google Gemini, LangChain LLM, Parser Structurat

### Automate Your RFP Process with OpenAI Assistants

> Se declanșează prin webhook HTTP. folosește Extracție Fișier, folosește outputParserItemList, folosește Google Docs, folosește OpenAI Chat (+6 altele). Detalii: Try It Out!

**This workflow does the following:**
* Receives a RFP document via webhook
* Creates a new RFP response document via Google Docs
* Uses LLMs to extract the questions from the RFP document into a questions list
* Loops through each...

- **Noduri:** 23
- **Conexiuni:** 12
- **Declanșare:** 🌐 Webhook
- **Integrări:** Extracție Fișier, Gmail, Google Docs, LangChain LLM, OpenAI, OpenAI Chat, Slack, Webhook, outputParserItemList

### Calendar_scheduling

> Se declanșează de Gmail Trigger. folosește OpenAI Chat, folosește Sub-workflow Tool, citește date din Google Calendar, folosește LangChain LLM (+4 altele). Detalii: Check if incoming email is about appointment
We use LLM to check subject and body of the email and determine if it's an appointment request.

- **Noduri:** 21
- **Conexiuni:** 14
- **Integrări:** AI Agent, Gmail, Google Calendar, LangChain LLM, OpenAI Chat, Parser Structurat, Sub-workflow Tool

### Chat with OpenAI Assistant (by adding a memory)

> Se declanșează prin mesaj de chat. folosește OpenAI Assistant, folosește Calculator, folosește Chat Memory, folosește Buffer Memory. Detalii: Try me out
1. In the OpenAI Assistant node, make sure your OpenAI credentials are set and choose an assistant to use (you'll need to create one if you don't have one already)
2. Click the 'Chat' button below

 - In the first message, tell the AI...

- **Noduri:** 14
- **Conexiuni:** 8
- **Integrări:** Buffer Memory, Calculator, Chat Memory, OpenAI Assistant

### Chat with local LLMs using n8n and Ollama

> Se declanșează prin mesaj de chat. folosește Ollama, folosește LangChain LLM. Detalii: Chat with local LLMs using n8n and Ollama
This n8n workflow allows you to seamlessly interact with your self-hosted Large Language Models (LLMs) through a user-friendly chat interface. By connecting to Ollama, a powerful tool for managing local...

- **Noduri:** 5
- **Conexiuni:** 2
- **Integrări:** LangChain LLM, Ollama

### Complete Youtube

> Se declanșează prin mesaj de chat. folosește AI Agent, folosește Sub-workflow Tool, folosește OpenAI Chat, folosește Buffer Memory (+2 altele). Detalii: This part should be abstracted to another workflow and called inside the "youtube_search" tool of the main AI Agent.

- **Noduri:** 15
- **Conexiuni:** 11
- **Integrări:** AI Agent, Buffer Memory, HTTP API, OpenAI Chat, Sub-workflow Tool, youTube

### Content to 9:16 Aspect Image Generator v1

> Se declanșează manual. caută în Airtable, folosește Airtable, folosește OpenAI, folosește HTTP API (+2 altele). Detalii: AlexK1919 
![Alex Kim](https://media.licdn.com/dms/image/v2/D5603AQFOYMkqCPl6Sw/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1718309808352?e=1736985600&v=beta&t=pQKm7lQfUU1ytuC2Gq1PRxNY-XmROFWbo-BjzUPxWOs)

 I’m Alex, an...

- **Noduri:** 39
- **Conexiuni:** 26
- **Declanșare:** 👆 Manual
- **Integrări:** Airtable, HTTP API, OpenAI, Wikipedia Tool
- **Tag-uri:** OpenAI, RunwayML, Video, Creatomate, Leonardo, App 2

### Create a Branded AI-Powered Website Chatbot

> Se declanșează de Execute Workflow Trigger. folosește Buffer Memory, folosește Răspuns Webhook, folosește OpenAI Chat, folosește HTTP Tool (+4 altele). Detalii: Read to blog post to get started 📝
**Follow along to add a custom branded chat widget to your webiste**

[![Custom Branded n8n...

- **Noduri:** 24
- **Conexiuni:** 13
- **Declanșare:** 🌐 Webhook
- **Integrări:** AI Agent, Buffer Memory, HTTP API, HTTP Tool, Microsoft Outlook, OpenAI Chat, Răspuns Webhook, Sub-workflow Tool

### Daily Podcast Summary

> Rulează zilnic la ora 8:00. folosește Gmail, folosește HTTP API, folosește HTML, folosește OpenAI. Detalii: Daily Podcast Summary
 This workflow will summarize the content in the day's top podcasts for a certain genre, then send you the podcasts with summaries by email

 Setup:
 1. Create a free API key on Taddy here: https://taddy.org/signup/developers
...

- **Noduri:** 21
- **Conexiuni:** 15
- **Declanșare:** ⏰ Programat
- **Integrări:** Gmail, HTML, HTTP API, OpenAI

### Daily meetings summarization with Gemini AI

> Rulează zilnic la ora 9:00. folosește Slack, citește date din googleCalendarTool, folosește AI Agent, folosește Google Gemini. Detalii: Trigger the task daily, receive the meetings data, process the data and return response for sending











No memory assigned to the model since the model is running one task and doesn't need a followup, then send the data to the user.

- **Noduri:** 9
- **Conexiuni:** 4
- **Declanșare:** ⏰ Programat
- **Integrări:** AI Agent, Google Gemini, Slack, googleCalendarTool

### Detect hallucinations using specialised Ollama model bespoke-minicheck

> Se declanșează manual. folosește LangChain LLM, folosește Ollama, folosește lmOllama. Detalii: Fact checking

This use a small ollama model that is specialized on that task: https://ollama.com/library/bespoke-minicheck

You have to install it before use with `ollama pull bespoke-minicheck`.

- **Noduri:** 18
- **Conexiuni:** 12
- **Declanșare:** 👆 Manual
- **Integrări:** LangChain LLM, Ollama, lmOllama

### Docsify example

> Se declanșează prin webhook HTTP. folosește Conversie Fișier, folosește Extracție Fișier, folosește HTML, folosește Fișier Local (+10 altele). Detalii: Serve main Markdown table with the workflow overview
*NOTE! Here we don't reply with HTML content. Only Markdown elements are sent back and processed by the JS library*
* Create an overall table when `README.md` (the home page) is requested
* Create...

- **Noduri:** 60
- **Conexiuni:** 44
- **Declanșare:** 🌐 Webhook
- **Integrări:** Comandă Shell, Conversie Fișier, Extracție Fișier, Fișier Local, HTML, LangChain LLM, OpenAI Chat, Parser Autofix, Parser Structurat, Răspuns Webhook (+2 altele)

### Dynamically generate HTML page from user request using OpenAI Structured Output

> Se declanșează prin webhook HTTP. folosește Răspuns Webhook, folosește HTTP API, folosește OpenAI, folosește HTML (+1 altele). Detalii: Workflow: Dynamically generate an HTML page from a user request using OpenAI Structured Output

**Overview**
- This workflow is a experiment to build HTML pages from a user input using the new Structured Output from OpenAI.
- The Structured Output...

- **Noduri:** 7
- **Conexiuni:** 4
- **Declanșare:** 🌐 Webhook
- **Integrări:** HTML, HTTP API, OpenAI, Răspuns Webhook, Webhook

### Dynamically generate HTML page from user request using OpenAI Structured Output

> Se declanșează prin webhook HTTP. folosește Răspuns Webhook, folosește HTTP API, folosește OpenAI, folosește HTML (+1 altele). Detalii: Workflow: Dynamically generate an HTML page from a user request using OpenAI Structured Output

**Overview**
- This workflow is a experiment to build HTML pages from a user input using the new Structured Output from OpenAI.
- The Structured Output...

- **Noduri:** 7
- **Conexiuni:** 4
- **Declanșare:** 🌐 Webhook
- **Integrări:** HTML, HTTP API, OpenAI, Răspuns Webhook, Webhook

### Easy Image Captioning with Gemini 1.5 Pro

> Se declanșează manual. folosește Google Gemini, folosește Parser Structurat, folosește Editor Imagine, folosește Editor Imagine (+3 altele). Detalii: 2. Using Vision Model to Generate Caption
[Learn more about the Basic LLM Chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm)

n8n's basic LLM node supports multimodal input by allowing you to...

- **Noduri:** 16
- **Conexiuni:** 10
- **Declanșare:** 👆 Manual
- **Integrări:** Editor Imagine, Google Gemini, HTTP API, LangChain LLM, Parser Structurat

### Email AI Auto-responder. Summerize and send email

> Se declanșează la primirea unui email. folosește Email IMAP, folosește Markdown, folosește OpenAI Chat, folosește Email SMTP (+11 altele). Detalii: STEP 3 - MAIN FLOW

- Transform the email into Markdown format for optimal reading by the LLM model
- Email Summarization through DeepSeek R1 (any model can be used)
- I classify the email in such a way as to continue only with emails regarding...

- **Noduri:** 26
- **Conexiuni:** 19
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, Clasificator Text, Document Loader, Email IMAP, Email SMTP, Google Drive, HTTP API, LangChain LLM, LangChain Sumarizare, Markdown (+4 altele)

### Enrich FAQ sections on your website pages at scale with AI

> Se declanșează manual. folosește OpenAI Chat, folosește Google Drive, folosește Google Sheets, folosește Sub-workflow (+6 altele). Detalii: Generate JSON schemas and upload to Google Drive
* The generated files are saved to specific folders in Google Drive, organized by the type of integration (native, credential-only, non-native) or category.
* After processing each service or...

- **Noduri:** 36
- **Conexiuni:** 25
- **Declanșare:** 👆 Manual
- **Integrări:** Google Drive, Google Sheets, HTTP API, LangChain LLM, OpenAI Chat, Strapi, Sub-workflow, Webflow, WordPress

### Extract personal data with a self-hosted LLM Mistral NeMo

> Se declanșează prin mesaj de chat. folosește Ollama, folosește Parser Autofix, folosește Parser Structurat, folosește LangChain LLM. Detalii: If the LLM response does not pass 
the **Structured Output Parser** checks,
**Auto-Fixer** will call the model again with a different 
prompt to correct the original response.

- **Noduri:** 13
- **Conexiuni:** 5
- **Integrări:** LangChain LLM, Ollama, Parser Autofix, Parser Structurat

### FLUX-fill standalone

> Se declanșează prin webhook HTTP. folosește Răspuns Webhook, folosește HTTP API, folosește Webhook, folosește HTML. Detalii: HTML code of the editor
* Konva.js
* img-comparison-slider to compare edits vs original file
* Additional css + js files for the editor logic

- **Noduri:** 18
- **Conexiuni:** 10
- **Declanșare:** 🌐 Webhook
- **Integrări:** HTML, HTTP API, Răspuns Webhook, Webhook

### Flux AI Image Generator

> Se declanșează la trimiterea unui formular n8n. folosește Răspuns Webhook, încarcă fișiere în s3, folosește HTTP API. Detalii: Run flux model
In `Call huggingface inference api` You can change `black-forest-labs/FLUX.1-schnell` in URL parameter to other models:
- `black-forest-labs/FLUX.1-dev`
- `Shakker-Labs/FLUX.1-dev-LoRA-AntiBlur`
- `XLabs-AI/flux-RealismLora`
-...

- **Noduri:** 19
- **Conexiuni:** 10
- **Declanșare:** 🌐 Webhook
- **Integrări:** HTTP API, Răspuns Webhook, s3

### Generate Text-to-Speech Using Elevenlabs via API

> Se declanșează prin webhook HTTP. folosește Răspuns Webhook, folosește Webhook, folosește HTTP API. Detalii: Generate Text-to-Speech Using Elevenlabs via API
This workflow provides an API endpoint to generate speech from text using [Elevenlabs.io](https://elevenlabs.io/), a popular text-to-speech service.

 Step 1: Configure Custom Credentials in n8n
To...

- **Noduri:** 6
- **Conexiuni:** 3
- **Declanșare:** 🌐 Webhook
- **Integrări:** HTTP API, Răspuns Webhook, Webhook

### Generate audio from text using OpenAI - text-to-speech Workflow

> Se declanșează prin webhook HTTP. folosește Răspuns Webhook, folosește Webhook, folosește OpenAI. Detalii: This `Webhook` node triggers the workflow when it receives a POST request.

 1. Test Mode:
* Use the test webhook URL
* Click the `Test workflow` button on the canvas. (In test mode, the webhook only works for one call after you click this button)

...

- **Noduri:** 5
- **Conexiuni:** 2
- **Declanșare:** 🌐 Webhook
- **Integrări:** OpenAI, Răspuns Webhook, Webhook

### Generating Image Embeddings via Textual Summarisation

> Se declanșează manual. descarcă din Google Drive, folosește Editor Imagine, folosește Editor Imagine, folosește Document Loader (+4 altele). Detalii: 2. Image Embedding Methods
[Read more about working with images in n8n](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.editimage)

There are a [myriad of image embedding...

- **Noduri:** 22
- **Conexiuni:** 11
- **Declanșare:** 👆 Manual
- **Integrări:** Document Loader, Editor Imagine, Google Drive, OpenAI, OpenAI Embeddings, Text Splitter, Vector Store

### HR-focused automation pipeline with AI

> Se declanșează la trimiterea unui formular n8n. folosește Extracție Fișier, folosește Extractor Informații, folosește LangChain Sumarizare, adaugă date în Google Sheets (+4 altele). Detalii: HR Expert 
This workflow automates the process of handling job applications by extracting relevant information from submitted CVs, analyzing the candidate's qualifications against a predefined profile, and storing the results in a Google Sheet

- **Noduri:** 18
- **Conexiuni:** 11
- **Integrări:** Extractor Informații, Extracție Fișier, Google Drive, Google Sheets, LangChain LLM, LangChain Sumarizare, OpenAI Chat, Parser Structurat

### Image Generation API

> Se declanșează prin webhook HTTP. folosește Webhook, folosește Răspuns Webhook, folosește OpenAI. Detalii: Creating your Prompt-URL 
**To use this Workflow you need to append your prompt to your Webhook URL in the following way**

1. Take your Webhook URL
2. Ideate a Prompt and Replace every Space (" ") by %20 (Url Encoding)
3. Append "?input=" and right...

- **Noduri:** 7
- **Conexiuni:** 2
- **Declanșare:** 🌐 Webhook
- **Integrări:** OpenAI, Răspuns Webhook, Webhook

### LangChain - Example - Code Node Example

> Se declanșează manual. folosește lmOpenAi, folosește OpenAI Chat, folosește AI Agent. Detalii: Self-coded LLM Chain Node

- **Noduri:** 10
- **Conexiuni:** 6
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, OpenAI Chat, lmOpenAi
- **Tag-uri:** LangChain - Example

### LangChain - Example - Workflow Retriever

> Se declanșează manual. folosește retrieverWorkflow, folosește LangChain Retrieval QA, folosește OpenAI Chat. Detalii: Replace "Workflow ID" with the ID the Subworkflow got saved as

- **Noduri:** 7
- **Conexiuni:** 4
- **Declanșare:** 👆 Manual
- **Integrări:** LangChain Retrieval QA, OpenAI Chat, retrieverWorkflow
- **Tag-uri:** LangChain - Example

### Load Prompts from Github Repo and auto populate n8n expressions

> Se declanșează manual. obține date din GitHub, folosește Extracție Fișier, folosește AI Agent, folosește Ollama. Detalii: Replaces the values in the prompt with the variables in the 
 'setVars' Node

- **Noduri:** 17
- **Conexiuni:** 11
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, Extracție Fișier, GitHub, Ollama

### Narrating over a Video using Multimodal AI

> Se declanșează manual. folosește OpenAI Chat, folosește HTTP API, folosește Conversie Fișier, folosește Google Drive (+3 altele). Detalii: Try It Out!

 This n8n template takes a video and extracts frames from it which are used with a multimodal LLM to generate a script. The script is then passed to the same multimodal LLM to generate a voiceover clip.

This template was inspired by...

- **Noduri:** 21
- **Conexiuni:** 13
- **Declanșare:** 👆 Manual
- **Integrări:** Conversie Fișier, Editor Imagine, Google Drive, HTTP API, LangChain LLM, OpenAI, OpenAI Chat

### OpenAI Assistant with custom n8n tools

> Se declanșează prin mesaj de chat. folosește OpenAI Assistant, folosește Sub-workflow Tool, folosește Cod Personalizat. Detalii: Sub-workflow: Return the capitals of fictional countries
It can either list the countries it knows about or return the capital of a specific country

- **Noduri:** 14
- **Conexiuni:** 9
- **Declanșare:** 👆 Manual
- **Integrări:** Cod Personalizat, OpenAI Assistant, Sub-workflow Tool

### OpenAI Assistant workflow: uploa file, create an Assistant, chat with it!

> Se declanșează manual. descarcă din Google Drive, folosește OpenAI, creează înregistrări în OpenAI. Detalii: STEP 4. Expand the Assistant. Check the tutorials:

[Create a WhatsApp bot](https://blog.n8n.io/whatsapp-bot/)
[Create simple Telegram bot](https://blog.n8n.io/telegram-bots/)
[![Create a Telegram AI...

- **Noduri:** 10
- **Conexiuni:** 2
- **Declanșare:** 👆 Manual
- **Integrări:** Google Drive, OpenAI

### OpenAI Personal Shopper with RAG and WooCommerce

> Se declanșează prin mesaj de chat. folosește Buffer Memory, folosește Calculator, folosește OpenAI Chat, folosește Vector Store Tool (+10 altele). Detalii: Step 2 
The Information Extractor tries to understand if the request is related to products and if so, it extracts the useful information to filter the products available on WooCommerce by calling the "personal_shopper". If it is a general question,...

- **Noduri:** 25
- **Conexiuni:** 19
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, Buffer Memory, Calculator, Document Loader, Extractor Informații, Google Drive, HTTP API, OpenAI Chat, OpenAI Embeddings, Qdrant (+3 altele)

### OpenAI-model-examples

> Se declanșează manual. folosește OpenAI, folosește OpenAI, folosește HTTP API, folosește HTML (+1 altele). Detalii: ChatGPT example 3.1
 When using ChatGPT programmatically, create an array of system / user / assistant contents and append them one after another
 Call ChatGPT API via HTTP Request node to provide all messages at once

- **Noduri:** 27
- **Conexiuni:** 11
- **Declanșare:** 👆 Manual
- **Integrări:** HTML, HTTP API, OpenAI, readBinaryFiles

### Organise Your Local File Directories With AI

> Se declanșează de Monitor Fișiere Locale. folosește Comandă Shell, folosește Mistral AI, folosește Parser Structurat, folosește LangChain LLM. Detalii: Try It Out!
 This workflow does the following:
* Monitors a target folder for changes using the local file trigger
* identifies all files and subdirectories in the target folder and passes this to Mistral AI
* Mistral AI suggests where to move top...

- **Noduri:** 16
- **Conexiuni:** 9
- **Integrări:** Comandă Shell, LangChain LLM, Mistral AI, Parser Structurat

### Podcast Digest

> Se declanșează manual. folosește documentJsonInputLoader, folosește Text Splitter, folosește LangChain Sumarizare, folosește OpenAI Chat (+5 altele). Detalii: Generate Questions and Topics from the summary and make sure the response follows required schema.

- **Noduri:** 19
- **Conexiuni:** 14
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, Gmail, LangChain LLM, LangChain Sumarizare, OpenAI Chat, Parser Structurat, Text Splitter, Wikipedia Tool, documentJsonInputLoader

### Prompt-based Object Detection with Gemini 2.0

> Se declanșează manual. folosește HTTP API, folosește Editor Imagine, folosește Editor Imagine. Detalii: Try it out!
 This n8n template demonstrates how to use Gemini 2.0's new Bounding Box detection capabilities your workflows.

The key difference being this enables prompt-based object detection for images which is pretty powerful for things like...

- **Noduri:** 14
- **Conexiuni:** 7
- **Declanșare:** 👆 Manual
- **Integrări:** Editor Imagine, HTTP API

### Proxmox AI Agent with n8n and Generative AI Integration

> Se declanșează prin mesaj de chat. folosește HTTP API, folosește HTTP Tool, folosește Parser Autofix, folosește Google Gemini (+3 altele). Detalii: Developed by Amjid Ali

Thank you for using this workflow template. It has taken me countless hours of hard work, research, and dedication to develop, and I sincerely hope it adds value to your work.

If you find this template helpful, I kindly ask...

- **Noduri:** 35
- **Conexiuni:** 22
- **Declanșare:** 🌐 Webhook
- **Integrări:** AI Agent, Google Gemini, HTTP API, HTTP Tool, Parser Autofix, Parser Structurat, Webhook

### Query n8n Credentials with AI SQL Agent

> Se declanșează manual. folosește Cod Personalizat, folosește OpenAI Chat, folosește Buffer Memory, folosește AI Agent (+1 altele). Detalii: Step 1. Store Workflows Credential Mappings to Database

We'll achieve this by querying n8n's built-in API to query all workflows, extract the credentials list from the nodes within and then store them in a SQLite database. Don't worry, the actual...

- **Noduri:** 13
- **Conexiuni:** 7
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, Buffer Memory, Cod Personalizat, OpenAI Chat, n8n Sub-workflow

### RAG Workflow For Stock Earnings Report Analysis

> Se declanșează manual. folosește Pinecone, folosește Google Embeddings, folosește Document Loader, folosește Text Splitter (+7 altele). Detalii: Set up steps
1. Google Cloud Project & Vertex AI API:
	* Create a Google Cloud project.
	* Enable the Vertex AI API for your project.
2. Google AI API key:
	* Obtain a Google AI API key from Google AI Studio.
3. Pinecone account and API key:
	*...

- **Noduri:** 18
- **Conexiuni:** 14
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, Document Loader, Google Docs, Google Drive, Google Embeddings, Google Gemini, Google Sheets, OpenAI Chat, Pinecone, Text Splitter (+1 altele)

### Social Media AI Agent - Telegram

> Rulează programat (schedule). folosește HTTP API, folosește Markdown, actualizează date în Airtable, folosește LinkedIn (+5 altele). Detalii: Automate the curation and sharing of trending GitHub discussions from Hacker News to Twitter and LinkedIn. This workflow leverages AI to generate engaging posts, streamlining your social media content creation and distribution.

- **Noduri:** 26
- **Conexiuni:** 18
- **Declanșare:** ⏰ Programat
- **Integrări:** Airtable, HTTP API, LinkedIn, Markdown, OpenAI, Telegram, Twitter/X

### Stock Q&A Workflow

> Se declanșează prin mesaj de chat. folosește OpenAI Embeddings, folosește LangChain Retrieval QA, folosește Răspuns Webhook, folosește Vector Retriever (+6 altele). Detalii: Start here: Step-by Step Youtube Tutorial :star:

[![Building an AI Crew to Analyze Financial Data with CrewAI and n8n](https://img.youtube.com/vi/pMvizUx5n1g/sddefault.jpg)](https://www.youtube.com/watch?v=pMvizUx5n1g)

- **Noduri:** 17
- **Conexiuni:** 12
- **Declanșare:** 🌐 Webhook, 👆 Manual
- **Integrări:** Google Drive, LangChain Retrieval QA, OpenAI Chat, OpenAI Embeddings, Qdrant, Răspuns Webhook, Text Splitter, Vector Retriever, Webhook, documentBinaryInputLoader

### Summarize YouTube Videos from Transcript

> Se declanșează la trimiterea unui formular n8n. folosește HTTP API, folosește LangChain Sumarizare, folosește OpenAI Chat. Detalii: **Summarize YouTube videos**

This project automates the summarization of YouTube videos, transforming lengthy content into concise, actionable insights. By leveraging AI and workflow automation, it extracts video transcripts, analyzes key points,...

- **Noduri:** 10
- **Conexiuni:** 4
- **Integrări:** HTTP API, LangChain Sumarizare, OpenAI Chat

### Testing Mulitple Local LLM with LM Studio

> Se declanșează prin mesaj de chat. folosește HTTP API, folosește Date/Time, folosește OpenAI Chat, adaugă date în Google Sheets (+2 altele). Detalii: 3. 💡Update the LM Settings

From here, you can modify the following
 parameters to fine-tune model behavior:

- **Temperature**: Controls randomness. Higher values (e.g., 1.0) produce more diverse results, while lower values (e.g., 0.2) make...

- **Noduri:** 21
- **Conexiuni:** 11
- **Integrări:** Date/Time, Google Sheets, HTTP API, LangChain LLM, OpenAI Chat
- **Tag-uri:** Training, Template

### Text to Speech (OpenAI)

> Se declanșează manual. folosește HTTP API. Detalii: Configuration Options
- "input_text" is the text you would like to be turned into speech, and can be replaced with a programmatic value for your use case. Bear in mind that the maximum number of tokens per API call is 4,000.

- "voice" is the voice...

- **Noduri:** 8
- **Conexiuni:** 2
- **Declanșare:** 👆 Manual
- **Integrări:** HTTP API

### Transform Image to Lego Style Using Line and Dall-E

> Se declanșează prin webhook HTTP. folosește Webhook, folosește HTTP API, folosește OpenAI, folosește OpenAI.

- **Noduri:** 5
- **Conexiuni:** 4
- **Declanșare:** 🌐 Webhook
- **Integrări:** HTTP API, OpenAI, Webhook

### Translate audio using AI

> Se declanșează manual. folosește OpenAI Chat, folosește HTTP API, folosește LangChain LLM. Detalii: 2] Get your ElevenLabs API key (click your name in the bottom-left of [ElevenLabs](https://elevenlabs.io/voice-lab) and choose ‘profile’)

In this node, create a new header auth cred. Set the name to `xi-api-key` and the value to your API key

- **Noduri:** 12
- **Conexiuni:** 6
- **Declanșare:** 👆 Manual
- **Integrări:** HTTP API, LangChain LLM, OpenAI Chat

### Use any LLM-Model via OpenRouter

> Se declanșează prin mesaj de chat. folosește AI Agent, folosește Buffer Memory, folosește OpenAI Chat. Detalii: Model examples

* openai/o3-mini
* google/gemini-2.0-flash-001
* deepseek/deepseek-r1-distill-llama-8b
* mistralai/mistral-small-24b-instruct-2501:free
* qwen/qwen-turbo

For more see https://openrouter.ai/models

- **Noduri:** 8
- **Conexiuni:** 4
- **Integrări:** AI Agent, Buffer Memory, OpenAI Chat
- **Tag-uri:** Published Template

### Voice RAG Chatbot with ElevenLabs and OpenAI

> Se declanșează manual. folosește AI Agent, folosește Vector Store Tool, folosește Qdrant, folosește OpenAI Embeddings (+9 altele). Detalii: STEP 1

 Create an Agent on ElevenLabs 
- Create an agent on ElevenLabs (eg. test_n8n)
- Add "First message" (eg. Hi, Can I help you?)
- Add the "System Prompt" message... eg:
'You are the waiter of "Pizzeria da Michele" in Verona. If you are asked...

- **Noduri:** 23
- **Conexiuni:** 15
- **Declanșare:** 🌐 Webhook, 👆 Manual
- **Integrări:** AI Agent, Buffer Memory, Document Loader, Google Drive, HTTP API, OpenAI Chat, OpenAI Embeddings, Qdrant, Răspuns Webhook, Vector Store Tool (+2 altele)

### [AI/LangChain] Output Parser 4

> Se declanșează manual. folosește LangChain LLM, folosește Parser Structurat, folosește Parser Autofix, folosește OpenAI Chat. Detalii: Parser which defines the output format and which gets used to validate the output

- **Noduri:** 11
- **Conexiuni:** 6
- **Declanșare:** 👆 Manual
- **Integrări:** LangChain LLM, OpenAI Chat, Parser Autofix, Parser Structurat

### lemlist __ GPT-3_ Supercharge your sales workflows

> Se declanșează de lemlistTrigger. folosește Lemlist, folosește HubSpot, folosește HTTP API, folosește Slack (+1 altele).

- **Noduri:** 12
- **Conexiuni:** 7
- **Integrări:** HTTP API, HubSpot, Lemlist, OpenAI, Slack

### modelo do chatbot

> Se declanșează prin mesaj de chat. folosește OpenAI, folosește PostgreSQL Memory, folosește mySqlTool, folosește HTTP Tool.

- **Noduri:** 12
- **Conexiuni:** 10
- **Integrări:** HTTP Tool, OpenAI, PostgreSQL Memory, mySqlTool

### ⚡AI-Powered YouTube Video Summarization & Analysis

> Se declanșează prin webhook HTTP. folosește Webhook, folosește Răspuns Webhook, folosește Telegram, obține date din youTube (+2 altele).

- **Noduri:** 12
- **Conexiuni:** 8
- **Declanșare:** 🌐 Webhook
- **Integrări:** LangChain LLM, OpenAI Chat, Răspuns Webhook, Telegram, Webhook, youTube

### 🐋DeepSeek V3 Chat & R1 Reasoning Quick Start

> Se declanșează prin mesaj de chat. folosește AI Agent, folosește OpenAI Chat, folosește Buffer Memory, folosește LangChain LLM (+2 altele). Detalii: Your First DeepSeek API Call

The DeepSeek API uses an API format compatible with OpenAI. By modifying the configuration, you can use the OpenAI SDK or softwares compatible with the OpenAI API to access the DeepSeek...

- **Noduri:** 15
- **Conexiuni:** 5
- **Integrări:** AI Agent, Buffer Memory, HTTP API, LangChain LLM, Ollama, OpenAI Chat

### 🔥📈🤖 AI Agent for n8n Creators Leaderboard - Find Popular Workflows

> Se declanșează de When Executed by Another Workflow. folosește HTTP API, folosește OpenAI Chat, folosește Sub-workflow Tool, folosește Conversie Fișier (+4 altele). Detalii: n8n Creators Leaderboard Stats Workflow

 Overview
This workflow aggregates and processes data from the n8n community to generate detailed statistics about creators and their workflows. It fetches information from JSON files stored on GitHub, merges...

- **Noduri:** 43
- **Conexiuni:** 24
- **Integrări:** AI Agent, Buffer Memory, Conversie Fișier, Fișier Local, HTTP API, Ollama, OpenAI Chat, Sub-workflow Tool

### 🗨️Ollama Chat

> Se declanșează prin mesaj de chat. folosește LangChain LLM, folosește lmOllama. Detalii: 🦙 Ollama Chat Workflow

A simple N8N workflow that integrates Ollama LLM for chat message processing and returns a structured JSON object.

 Overview
This workflow creates a chat interface that processes messages using the Llama 3.2 model through...

- **Noduri:** 14
- **Conexiuni:** 4
- **Integrări:** LangChain LLM, lmOllama

### 🤖🧑‍💻 AI Agent for Top n8n Creators Leaderboard Reporting

> Se declanșează de When Executed by Another Workflow. folosește HTTP API, folosește OpenAI Chat, folosește Sub-workflow Tool, folosește Conversie Fișier (+8 altele). Detalii: n8n Top Creators Leaderboard Reporting Workflow

 Why This Workflow is Important
This workflow is a powerful tool for reporting on the n8n community's creators and workflows. It provides valuable insights into the most popular workflows, top...

- **Noduri:** 49
- **Conexiuni:** 25
- **Declanșare:** ⏰ Programat
- **Integrări:** AI Agent, Conversie Fișier, Fișier Local, Gmail, Google Drive, Google Gemini, HTTP API, LangChain LLM, Markdown, OpenAI Chat (+2 altele)

---

## Other Integrations and Use Cases

### API Schema Extractor

> Se declanșează manual. folosește HTTP API, folosește Text Splitter, folosește Document Loader, folosește executionData (+10 altele). Detalii: Stage 2 - Extract API Operations From Documentation
- Fetch a list of services pending extraction from Database (Google Sheet)
- Query Vector store (Qdrant) to figure out service's products, solutions and offerings
- Query Vector store (Qdrant)...

- **Noduri:** 88
- **Conexiuni:** 75
- **Declanșare:** 👆 Manual
- **Integrări:** Clasificator Text, Document Loader, Extractor Informații, Google Drive, Google Embeddings, Google Gemini, Google Sheets, HTTP API, Qdrant, Sub-workflow (+2 altele)

### Analyze Screenshots with AI

> Se declanșează manual. folosește HTTP API, folosește OpenAI. Detalii: Analyze the Screenshot 
Analyze the screenshot using OpenAI.

Add your OpenAI Credentials on the top of the node.

The prompt is an example. Change it based on what you want to extract from the screenshot.

- **Noduri:** 9
- **Conexiuni:** 4
- **Declanșare:** 👆 Manual
- **Integrări:** HTTP API, OpenAI

### Analyze feedback using AWS Comprehend and send it to a Mattermost channel

> Se declanșează la trimiterea unui formular n8n. folosește Mattermost, folosește awsComprehend.

- **Noduri:** 5
- **Conexiuni:** 3
- **Integrări:** Mattermost, awsComprehend

### Analyze the sentiment of feedback and send a message on Mattermost

> Se declanșează la trimiterea unui formular n8n. folosește googleCloudNaturalLanguage, folosește Mattermost.

- **Noduri:** 5
- **Conexiuni:** 3
- **Integrări:** Mattermost, googleCloudNaturalLanguage

### Automate Pinterest Analysis & AI-Powered Content Suggestions With Pinterest API

> Rulează zilnic la ora 8:00. folosește OpenAI Chat, folosește airtableTool, folosește HTTP API, actualizează/creează în Airtable (+3 altele). Detalii: Scheduled trigger begin process to gather Pinterest Pin data and store them within Airtable. This data can be referenced or analyzed accordingly. 

*If you would like to bring in Pinterest Ads data, the data is already labeled as Organic.

This is...

- **Noduri:** 13
- **Conexiuni:** 8
- **Declanșare:** ⏰ Programat
- **Integrări:** AI Agent, Airtable, Gmail, HTTP API, LangChain Sumarizare, OpenAI Chat, airtableTool

### Automate SIEM Alert Enrichment with MITRE ATT&CK, Qdrant & Zendesk in n8n

> Se declanșează prin mesaj de chat. folosește AI Agent, folosește OpenAI Chat, folosește OpenAI Embeddings, folosește Document Loader (+8 altele). Detalii: ![n8n](https://uploads.n8n.io/templates/qdrantlogo.png)
 Embed your Vector Store
To provide data for your Vector store, you need to pass it in as JSON, and ensure it's setup correctly. This flow pulls the JSON file from Google Drive and extracts the...

- **Noduri:** 26
- **Conexiuni:** 22
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, Buffer Memory, Document Loader, Extracție Fișier, Google Drive, OpenAI Chat, OpenAI Embeddings, Parser Structurat, Qdrant, Zendesk (+1 altele)

### Automate testimonials in Strapi with n8n

> Se declanșează prin webhook HTTP. creează înregistrări în Strapi, folosește interval, caută în Twitter/X, folosește Webhook (+1 altele).

- **Noduri:** 14
- **Conexiuni:** 12
- **Declanșare:** 🌐 Webhook
- **Integrări:** Strapi, Twitter/X, Webhook, googleCloudNaturalLanguage, interval

### Bitrix24 Chatbot Application Workflow example with Webhook Integration

> Se declanșează prin webhook HTTP. folosește Webhook, folosește HTTP API, folosește Răspuns Webhook.

- **Noduri:** 13
- **Conexiuni:** 11
- **Declanșare:** 🌐 Webhook
- **Integrări:** HTTP API, Răspuns Webhook, Webhook
- **Tag-uri:** Tech demo, Bitrix24, Chatbot

### ChatGPT Automatic Code Review in Gitlab MR

> Se declanșează prin webhook HTTP. folosește Webhook, folosește OpenAI Chat, folosește HTTP API, folosește LangChain LLM. Detalii: Filter comments and customize your trigger words ⬇️

- **Noduri:** 14
- **Conexiuni:** 9
- **Declanșare:** 🌐 Webhook
- **Integrări:** HTTP API, LangChain LLM, OpenAI Chat, Webhook

### Classify new bugs in Linear with OpenAI_s GPT-4 and move them to the right team

> Se declanșează de linearTrigger. actualizează date în linear, folosește HTTP API, folosește Slack, folosește OpenAI. Detalii: Setup
1. Add your Linear and OpenAi credentials
2. Change the team in the `Linear Trigger` to match your needs
3. Customize your teams and their areas of responsibility in the `Set me up` node. Please use the format `[Teamname][Description/Areas of...

- **Noduri:** 12
- **Conexiuni:** 8
- **Integrări:** HTTP API, OpenAI, Slack, linear

### Create, update, and get a profile in Humantic AI

> Se declanșează manual. folosește humanticAi, folosește HTTP API, actualizează date în humanticAi, obține date din humanticAi.

- **Noduri:** 5
- **Conexiuni:** 4
- **Declanșare:** 👆 Manual
- **Integrări:** HTTP API, humanticAi

### Enhance Customer Chat by Buffering Messages with Twilio and Redis

> Se declanșează de twilioTrigger. folosește OpenAI Chat, folosește Redis, folosește Buffer Memory, obține date din Redis (+3 altele). Detalii: Try It Out!
 This workflow demonstrates a simple approach to stagger an AI Agent's reply if users often send in a sequence of partial messages and in short bursts.

* Twilio webhook receives user's messages which are recorded in a message stack...

- **Noduri:** 18
- **Conexiuni:** 10
- **Integrări:** AI Agent, Buffer Memory, Chat Memory, OpenAI Chat, Redis, Twilio

### Hacker News Throwback Machine - See What Was Hot on This Day, Every Year!

> Rulează zilnic la ora 21:00. folosește LangChain LLM, folosește Google Gemini, folosește HTTP API, folosește HTML (+1 altele).

- **Noduri:** 13
- **Conexiuni:** 12
- **Declanșare:** ⏰ Programat
- **Integrări:** Google Gemini, HTML, HTTP API, LangChain LLM, Telegram

### Handling Appointment Leads and Follow-up With Twilio, Cal.com and AI

> Se declanșează de twilioTrigger. folosește OpenAI Chat, caută în Airtable, folosește Twilio, actualizează date în Airtable (+5 altele). Detalii: Try It Out!

 This workflow implements an appointment scheduling chatbot which is powered by an AI tools agent.
* Workflow is triggered by Customer enquires sent via SMS
* Customer session management and chat history are captured in Airtable to...

- **Noduri:** 36
- **Conexiuni:** 21
- **Declanșare:** ⏰ Programat
- **Integrări:** AI Agent, Airtable, HTTP Tool, LangChain LLM, OpenAI Chat, Parser Autofix, Parser Structurat, Twilio

### Integrating AI with Open-Meteo API for Enhanced Weather Forecasting

> Se declanșează prin mesaj de chat. folosește OpenAI Chat, folosește AI Agent, folosește Buffer Memory, folosește HTTP Tool. Detalii: Integrating AI with Open-Meteo API for Enhanced Weather Forecasting

 Use case

 Workshop

We are using this workflow in our workshops to teach how to use Tools a.k.a functions with artificial intelligence. In this specific case, we will use a...

- **Noduri:** 12
- **Conexiuni:** 5
- **Integrări:** AI Agent, Buffer Memory, HTTP Tool, OpenAI Chat

### Introduction to the HTTP Tool

> Se declanșează manual. folosește OpenAI Chat, folosește HTTP Tool, folosește AI Agent. Detalii: Try It Out!

 The HTTP tool is drastically simplifies API-enabled AI agents cutting down the number of workflow nodes by as much as 10!

* Available since v1.47.0
* Recommended for single purpose APIs which don't require much post-fetch...

- **Noduri:** 12
- **Conexiuni:** 7
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, HTTP Tool, OpenAI Chat

### KB Tool - Confluence Knowledge Base

> Se declanșează de Execute Workflow Trigger. folosește HTTP API. Detalii: ![n8n](https://i.imgur.com/qXWqiOd.png)
 Enhance Query Resolution with the Knowledge Base Tool!

Our **Knowledge Base Tool** is crafted to seamlessly integrate into the IT Department Q&A Workflow, enhancing the IT support process by enabling...

- **Noduri:** 7
- **Conexiuni:** 2
- **Integrări:** HTTP API

### LINE Assistant with Google Calendar and Gmail Integration

> Se declanșează prin webhook HTTP. folosește AI Agent, folosește Buffer Memory, folosește OpenAI Chat, folosește Wikipedia Tool (+6 altele).

- **Noduri:** 14
- **Conexiuni:** 12
- **Declanșare:** 🌐 Webhook
- **Integrări:** AI Agent, Buffer Memory, HTTP API, OpenAI, OpenAI Chat, Webhook, Wikipedia Tool, gmailTool, googleCalendarTool

### Monthly Spotify Track Archiving and Playlist Classification

> Rulează programat (schedule). folosește HTTP API, folosește Anthropic Claude, folosește spotify, folosește spotify (+4 altele). Detalii: Playlists' Description Examples


| Playlist Name | Playlist Description...

- **Noduri:** 37
- **Conexiuni:** 26
- **Declanșare:** ⏰ Programat
- **Integrări:** Anthropic Claude, Google Sheets, HTTP API, LangChain LLM, Parser Structurat, spotify

### Obsidian Notes Read Aloud: Available as a Podcast Feed

> Se declanșează prin webhook HTTP. folosește OpenAI, folosește Webhook, folosește HTTP API, folosește Răspuns Webhook (+2 altele). Detalii: Send Notes to Webhook
**Setup:**
- Install [Post Webhook Plugin](https://github.com/Masterb1234/obsidian-post-webhook/) in Obsidian
- Enter n8n Webhook URL and name in plugin settings

**Usage:**
- Select text or use full note
- Open Command Palette...

- **Noduri:** 23
- **Conexiuni:** 13
- **Declanșare:** 🌐 Webhook
- **Integrări:** Google Sheets, HTTP API, OpenAI, Răspuns Webhook, Webhook

### Printify Automation - Update Title and Description - AlexK1919

> Se declanșează manual. folosește HTTP API, folosește Calculator, folosește Wikipedia Tool, adaugă date în Google Sheets (+2 altele). Detalii: AlexK1919 
![Alex Kim](https://media.licdn.com/dms/image/v2/D5603AQFOYMkqCPl6Sw/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1718309808352?e=1736985600&v=beta&t=pQKm7lQfUU1ytuC2Gq1PRxNY-XmROFWbo-BjzUPxWOs)

 I’m Alex...

- **Noduri:** 26
- **Conexiuni:** 19
- **Declanșare:** 👆 Manual
- **Integrări:** Calculator, Google Sheets, HTTP API, OpenAI, Wikipedia Tool
- **Tag-uri:** Printify, OpenAI

### Qualify replies from Pipedrive persons with AI

> Se declanșează de Gmail Trigger. caută în Pipedrive, obține date din Pipedrive, folosește OpenAI, folosește Pipedrive. Detalii: About the workflow
The workflow reads every reply that is received from a cold email campaign and qualifies if the lead is interested in a meeting. If the lead is interested, a deal is made in pipedrive. You can add as many email inboxes as you...

- **Noduri:** 11
- **Conexiuni:** 9
- **Integrări:** OpenAI, Pipedrive

### Siri AI Agent_ Apple Shortcuts powered voice template

> Se declanșează prin webhook HTTP. folosește OpenAI Chat, folosește Răspuns Webhook, folosește AI Agent, folosește Webhook. Detalii: ![Siri Template Thumbnail](https://uploads.n8n.io/devrel/wf-siri-header.pngfull-width)
 "Hey Siri, Ask Agent" workflow
**Made by [Max Tkacz](https://www.linkedin.com/in/maxtkacz) during the [30 Day AI...

- **Noduri:** 7
- **Conexiuni:** 3
- **Declanșare:** 🌐 Webhook
- **Integrări:** AI Agent, OpenAI Chat, Răspuns Webhook, Webhook

### Text automations using Apple Shortcuts

> Se declanșează prin webhook HTTP. folosește Răspuns Webhook, folosește Webhook, folosește OpenAI. Detalii: Workflow: Text automations using Apple Shortcuts

**Overview**
- This workflow answers user requests sent via Apple Shortcuts
- Several Shortcuts call the same webhook, with a query and a type of query
- Types of query are:
 - translate to english
...

- **Noduri:** 10
- **Conexiuni:** 7
- **Declanșare:** 🌐 Webhook
- **Integrări:** OpenAI, Răspuns Webhook, Webhook

### Text automations using Apple Shortcuts (1)

> Se declanșează prin webhook HTTP. folosește Răspuns Webhook, folosește Webhook, folosește OpenAI. Detalii: Workflow: Text automations using Apple Shortcuts

**Overview**
- This workflow answers user requests sent via Apple Shortcuts
- Several Shortcuts call the same webhook, with a query and a type of query
- Types of query are:
 - translate to english
...

- **Noduri:** 10
- **Conexiuni:** 7
- **Declanșare:** 🌐 Webhook
- **Integrări:** OpenAI, Răspuns Webhook, Webhook

### UTM Link Creator & QR Code Generator with Scheduled Google Analytics Reports

> Se declanșează manual. folosește OpenAI Chat, folosește Buffer Memory, folosește googleAnalyticsTool, actualizează/creează în Airtable (+3 altele). Detalii: Schedule a Google Analytics Reports with Medium/Source to track UTM link performance. Update the reporting fields to fit your business needs. You can track traffic, conversions and other engagement metrics.

*Sample Google Report Metrics: Sessions....

- **Noduri:** 14
- **Conexiuni:** 10
- **Declanșare:** ⏰ Programat, 👆 Manual
- **Integrări:** AI Agent, Airtable, Buffer Memory, Gmail, HTTP API, OpenAI Chat, googleAnalyticsTool

### Use AI to organize your Todoist Inbox

> Rulează programat (schedule). actualizează date în Todoist, citește date din Todoist, folosește OpenAI. Detalii: 💫 To setup this template

1. Add your Todoist credentials
2. Add your OpenAI credentials
3. Set your project names and add priority

- **Noduri:** 12
- **Conexiuni:** 6
- **Declanșare:** ⏰ Programat
- **Integrări:** OpenAI, Todoist

### Visualize your SQL Agent queries with OpenAI and Quickchart.io

> Se declanșează de Execute "Generate a chart" tool. folosește OpenAI Chat, folosește Sub-workflow, folosește HTTP API, folosește AI Agent (+3 altele). Detalii: Overview 
- This workflow aims to provide data visualization capabilities to a native SQL Agent. 
- Together, they can help foster data analysis and data visualization within a team. 
- It uses the native SQL Agent that works well and adds...

- **Noduri:** 19
- **Conexiuni:** 11
- **Integrări:** AI Agent, Buffer Memory, Clasificator Text, Extractor Informații, HTTP API, OpenAI Chat, Sub-workflow

### Zoom AI Meeting Assistant

> Se declanșează manual. folosește OpenAI Chat, citește date din Zoom, folosește HTTP API, folosește Extracție Fișier (+6 altele). Detalii: Welcome to my Zoom AI Meeting Assistant Workflow!

 This workflow has the following sequence:

1. manual trigger (Can be replaced by a scheduled trigger or a webhook)
2. retrieval of of Zoom meeting data
3. filter the events of the last 24 hours
4....

- **Noduri:** 24
- **Conexiuni:** 20
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, ClickUp, Email SMTP, Extracție Fișier, HTTP API, OpenAI, OpenAI Chat, Sub-workflow Tool, Zoom, microsoftOutlookTool

### get_a_web_page

> Se declanșează de Execute Workflow Trigger. folosește HTTP API. Detalii: Send URL got Crawl
This can be reused by Ai Agents and any Workspace to crawl a site. All that Workspace has to do is send a request:

```json
 {
 "url": "Some URL to Get"
 }
```

- **Noduri:** 4
- **Conexiuni:** 2
- **Integrări:** HTTP API
- **Tag-uri:** tools

---

## PDF and Document Processing

### Ask questions about a PDF using AI

> Se declanșează prin mesaj de chat. descarcă din Google Drive, folosește Text Splitter, folosește OpenAI Embeddings, folosește Document Loader (+4 altele). Detalii: Try me out
1. In Pinecone, create an index with 1536 dimensions and select it in *both* Pinecone nodes
2. Click 'test workflow' at the bottom of the canvas to load data into the vector store
3. Click 'chat' at the bottom of the canvas to ask...

- **Noduri:** 16
- **Conexiuni:** 11
- **Declanșare:** 👆 Manual
- **Integrări:** Document Loader, Google Drive, LangChain Retrieval QA, OpenAI Chat, OpenAI Embeddings, Pinecone, Text Splitter, Vector Retriever

### Breakdown Documents into Study Notes using Templating MistralAI and Qdrant

> Se declanșează de Monitor Fișiere Locale. folosește Document Loader, folosește Text Splitter, folosește Mistral Embeddings, folosește Mistral AI (+12 altele). Detalii: Try It Out! 

 This workflow automates generating notes from a source document.
* It watches a target folder to pick up new files.
* When a new file is detected, it saves the contents of the file in a vectorstore.
* multiple AI agents guided by a...

- **Noduri:** 42
- **Conexiuni:** 34
- **Integrări:** Conversie Fișier, Document Loader, Extracție Fișier, Fișier Local, LangChain LLM, LangChain Retrieval QA, LangChain Sumarizare, Mistral AI, Mistral Embeddings, Qdrant (+3 altele)

### CV Resume PDF Parsing with Multimodal Vision AI

> Se declanșează manual. folosește Parser Structurat, descarcă din Google Drive, folosește HTTP API, folosește Editor Imagine (+2 altele). Detalii: 3. Parse Resume with Multimodal LLM
[Read more about using Basic LLM Chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm/)

Multimodal LLMs are LLMs which can accept binary inputs such as images,...

- **Noduri:** 13
- **Conexiuni:** 7
- **Declanșare:** 👆 Manual
- **Integrări:** Editor Imagine, Google Drive, Google Gemini, HTTP API, LangChain LLM, Parser Structurat

### Chat with PDF docs using AI (quoting sources)

> Se declanșează manual. folosește OpenAI Embeddings, folosește Document Loader, descarcă din Google Drive, folosește OpenAI Chat (+4 altele). Detalii: Try me out
1. In Pinecone, create an index with 1536 dimensions and select it in the two vector store nodes
2. Populate Pinecone by clicking the 'test workflow' button below
3. Click the 'chat' button below and enter the following:

_Which email...

- **Noduri:** 22
- **Conexiuni:** 16
- **Declanșare:** 👆 Manual
- **Integrări:** Document Loader, Google Drive, LangChain LLM, OpenAI Chat, OpenAI Embeddings, Parser Structurat, Pinecone, Text Splitter

### Convert URL HTML to Markdown Format and Get Page Links

> Se declanșează manual. folosește HTTP API. Detalii: Convert URL HTML to Markdown and Get Page Links

 Use Case
Transform web pages into AI-friendly markdown format:
- You need to process webpage content for LLM analysis
- You want to extract both content and links from web pages
- You need clean,...

- **Noduri:** 17
- **Conexiuni:** 10
- **Declanșare:** 👆 Manual
- **Integrări:** HTTP API

### ETL pipeline

> Rulează programat (cron). caută în Twitter/X, folosește PostgreSQL, folosește mongoDb, folosește Slack (+1 altele).

- **Noduri:** 9
- **Conexiuni:** 7
- **Declanșare:** ⏰ Programat
- **Integrări:** PostgreSQL, Slack, Twitter/X, googleCloudNaturalLanguage, mongoDb

### Extract and process information directly from PDF using Claude and Gemini

> Se declanșează manual. folosește Extracție Fișier, descarcă din Google Drive, folosește HTTP API. Detalii: Workflow: Extract data from PDF with Claude 3.5 Sonnet or Gemini 2.0 Flash

**Overview**
- This workflow helps you compare Claude 3.5 Sonnet and Gemini 2.0 Flash when extracting data from a PDF
- This workflow extracts and processes the data within...

- **Noduri:** 11
- **Conexiuni:** 4
- **Declanșare:** 👆 Manual
- **Integrări:** Extracție Fișier, Google Drive, HTTP API

### Extract data from resume and create PDF with Gotenberg

> Se declanșează la primirea unui mesaj Telegram. folosește OpenAI Chat, folosește Parser Autofix, folosește Parser Structurat, folosește Telegram (+5 altele). Detalii: ⚠️ Note

This is *resume extractor* workflow that I had a pleasure to present during [n8n community hangout](https://youtu.be/eZacuxrhCuo?si=KkJQrgQuvLxj-6FM&t=1701
) on March 7, 2024.

1. Remember to add your credentials and configure nodes.
2....

- **Noduri:** 43
- **Conexiuni:** 30
- **Integrări:** Conversie Fișier, Extracție Fișier, HTTP API, LangChain LLM, OpenAI Chat, Parser Autofix, Parser Structurat, Telegram

### Extract text from PDF and image using Vertex AI (Gemini) into CSV

> Se declanșează de googleDriveTrigger. folosește Google Gemini, descarcă din Google Drive, folosește Extracție Fișier, folosește HTTP API (+3 altele). Detalii: How to extract PDF and image text into CSV using n8n (without manual data entry)

This workflow will extract text data from PDF and images, then store it as CSV.

[💡 You can read more about this workflow...

- **Noduri:** 16
- **Conexiuni:** 10
- **Integrări:** Conversie Fișier, Extracție Fișier, Google Drive, Google Gemini, HTTP API, LangChain LLM

### Image to license plate number

> Se declanșează la trimiterea unui formular n8n. folosește LangChain LLM, folosește form, folosește lmChatOpenRouter.

- **Noduri:** 5
- **Conexiuni:** 4
- **Integrări:** LangChain LLM, form, lmChatOpenRouter

### Invoice data extraction with LlamaParse and OpenAI

> Se declanșează de Gmail Trigger. folosește lmOpenAi, folosește Parser Structurat, folosește HTTP API, adaugă date în Google Sheets (+3 altele). Detalii: Try Me Out!

**This workflow does the following:**
* Waits for email invoices with PDF attachments.
* Uses the LlamaParse service to convert the invoice PDF into a markdown file.
* Uses a LLM to extract invoice data from the Markdown file.
* Exports...

- **Noduri:** 26
- **Conexiuni:** 16
- **Integrări:** Gmail, Google Sheets, HTTP API, LangChain LLM, Parser Structurat, lmOpenAi

### Invoice data extraction with LlamaParse and OpenAI (1)

> Se declanșează de Gmail Trigger. folosește lmOpenAi, folosește Parser Structurat, folosește HTTP API, adaugă date în Google Sheets (+3 altele). Detalii: Try Me Out!

**This workflow does the following:**
* Waits for email invoices with PDF attachments.
* Uses the LlamaParse service to convert the invoice PDF into a markdown file.
* Uses a LLM to extract invoice data from the Markdown file.
* Exports...

- **Noduri:** 26
- **Conexiuni:** 16
- **Integrări:** Gmail, Google Sheets, HTTP API, LangChain LLM, Parser Structurat, lmOpenAi

### Manipulate PDF with Adobe developer API

> Se declanșează manual. folosește HTTP API, descarcă din Dropbox. Detalii: Adobe API Wrapper

See Adobe documentation:
- https://developer.adobe.com/document-services/docs/overview/pdf-services-api/howtos/
- https://developer.adobe.com/document-services/docs/overview/pdf-extract-api/gettingstarted/

In short, this workflow...

- **Noduri:** 20
- **Conexiuni:** 13
- **Declanșare:** 👆 Manual
- **Integrări:** Dropbox, HTTP API

### Parse PDF with LlamaParse and save to Airtable

> Se declanșează de googleDriveTrigger. descarcă din Google Drive, folosește HTTP API, creează înregistrări în Airtable, folosește Webhook. Detalii: ![5min Logo](https://cflobdhpqwnoisuctsoc.supabase.co/storage/v1/object/public/my_storage/banner.png)
 AI Agent for realtime insights on meetings
**Made by [Mark Shcherbakov](https://www.linkedin.com/in/marklowcoding/) from community...

- **Noduri:** 18
- **Conexiuni:** 7
- **Declanșare:** 🌐 Webhook
- **Integrări:** Airtable, Google Drive, HTTP API, Webhook

### Prepare CSV files with GPT-4

> Se declanșează manual. folosește OpenAI, folosește Fișier Spreadsheet, folosește writeBinaryFile, folosește moveBinaryData. Detalii: This is a helper workflow to create 3 CSV files
 Feel free to adapt as needed
 Some mock data from GPT is pinned for convenience

- **Noduri:** 11
- **Conexiuni:** 9
- **Declanșare:** 👆 Manual
- **Integrări:** Fișier Spreadsheet, OpenAI, moveBinaryData, writeBinaryFile

### Remove Personally Identifiable Information (PII) from CSV Files with OpenAI

> Se declanșează de googleDriveTrigger. descarcă din Google Drive, folosește Extracție Fișier, folosește OpenAI, folosește Google Drive. Detalii: Remove PII from CSV Files
This workflow monitors a Google Drive folder for new CSV files, identifies and removes PII columns using OpenAI, and uploads the sanitized file back to the drive. It requires Google Drive and OpenAI integrations with API...

- **Noduri:** 10
- **Conexiuni:** 9
- **Integrări:** Extracție Fișier, Google Drive, OpenAI

### Transcribing Bank Statements To Markdown Using Gemini Vision AI

> Se declanșează manual. folosește Google Gemini, descarcă din Google Drive, folosește HTTP API, folosește Compresie (+3 altele). Detalii: 3. Convert PDF Pages to Markdown Using Vision Model
[Learn more about using the Basic LLM node](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm)

Unlike traditional OCR, vision models ("VLMs")...

- **Noduri:** 20
- **Conexiuni:** 11
- **Declanșare:** 👆 Manual
- **Integrări:** Compresie, Editor Imagine, Extractor Informații, Google Drive, Google Gemini, HTTP API, LangChain LLM

### Whisper Transkription copy

> Se declanșează de googleDriveTrigger. descarcă din Google Drive, folosește Notion, folosește OpenAI, folosește OpenAI. Detalii: Send to OpenAI for Transcription and Summary

After we have the file, we send it to OpenAI for transciption and sending that transcipt to OpenAI to get a summary and some additional information

- **Noduri:** 8
- **Conexiuni:** 4
- **Integrări:** Google Drive, Notion, OpenAI

---

## Slack

### AI-Powered Information Monitoring with OpenAI, Google Sheets, Jina AI and Slack

> Rulează programat (schedule). folosește OpenAI Chat, folosește LangChain LLM, folosește rssFeedRead, folosește Clasificator Text (+4 altele). Detalii: Workflow Overview

 Check Legal Regulations:
This workflow involves scraping, so ensure you comply with the legal regulations in your country before getting started. Better safe than sorry!

 📌 Purpose 
This workflow enables **automated and...

- **Noduri:** 31
- **Conexiuni:** 15
- **Declanșare:** ⏰ Programat
- **Integrări:** Clasificator Text, Google Sheets, HTTP API, LangChain LLM, OpenAI Chat, Slack, rssFeedRead

### Creating a AI Slack Bot with Google Gemini

> Se declanșează prin webhook HTTP. folosește Google Gemini, folosește Buffer Memory, folosește Slack, folosește Webhook (+1 altele). Detalii: This is a POST Webhook endpoint

Make sure to configure this webhook using a https:// wraper and dont use the default http://localhost:5678 as that will not be recognized by your slack webhook


Once the data has been sent to your webhook, the next...

- **Noduri:** 10
- **Conexiuni:** 4
- **Declanșare:** 🌐 Webhook
- **Integrări:** AI Agent, Buffer Memory, Google Gemini, Slack, Webhook

### Customer Support Channel and Ticketing System with Slack and Linear

> Rulează programat (schedule). caută în Slack, folosește OpenAI Chat, folosește Parser Structurat, citește date din linear (+2 altele). Detalii: Try It Out!
 This workflow does the following:
* Monitors a Slack channel for new user messages asking for assistance
* Only user messages which are tagged with the ticket(🎫) emoji are processed.
* Linear is first checked to see if a ticket was...

- **Noduri:** 19
- **Conexiuni:** 11
- **Declanșare:** ⏰ Programat
- **Integrări:** LangChain LLM, OpenAI Chat, Parser Structurat, Slack, linear

### Enhance Security Operations with the Qualys Slack Shortcut Bot!

> Se declanșează prin webhook HTTP. folosește Sub-workflow, folosește HTTP API, folosește Răspuns Webhook, folosește Webhook. Detalii: ![n8n](https://uploads.n8n.io/templates/n8n.png)
 Enhance Security Operations with the Qualys Slack Shortcut Bot!

Our **Qualys Slack Shortcut Bot** is strategically designed to facilitate immediate security operations directly from Slack. This...

- **Noduri:** 23
- **Conexiuni:** 9
- **Declanșare:** 🌐 Webhook
- **Integrări:** HTTP API, Răspuns Webhook, Sub-workflow, Webhook

### Enhance Security Operations with the Qualys Slack Shortcut Bot! (1)

> Se declanșează prin webhook HTTP. folosește Sub-workflow, folosește HTTP API, folosește Răspuns Webhook, folosește Webhook. Detalii: ![n8n](https://uploads.n8n.io/templates/n8n.png)
 Enhance Security Operations with the Qualys Slack Shortcut Bot!

Our **Qualys Slack Shortcut Bot** is strategically designed to facilitate immediate security operations directly from Slack. This...

- **Noduri:** 23
- **Conexiuni:** 9
- **Declanșare:** 🌐 Webhook
- **Integrări:** HTTP API, Răspuns Webhook, Sub-workflow, Webhook

### IT Ops AI SlackBot Workflow - Chat with your knowledge base

> Se declanșează prin webhook HTTP. folosește Răspuns Webhook, folosește OpenAI Chat, folosește Buffer Memory, folosește Slack (+4 altele). Detalii: ![n8n](https://i.imgur.com/lKnBNnH.png)
 Streamline IT Inquiries with n8n & AI!

 Introducing the IT Ops AI SlackBot Workflow---a sophisticated solution designed to automate and optimize the management of IT-related inquiries via Slack.

When an...

- **Noduri:** 20
- **Conexiuni:** 9
- **Declanșare:** 🌐 Webhook
- **Integrări:** AI Agent, Buffer Memory, OpenAI Chat, Răspuns Webhook, Slack, Sub-workflow Tool, Webhook

### My workflow 6

> Se declanșează prin webhook HTTP. folosește Webhook, folosește LangChain LLM, folosește OpenAI Chat, folosește Slack. Detalii: Create an AI chatbot with Slack slash commands! 🤖

In this tutorial, we'll show you how to create an AI chatbot that works in Slack using n8n. We'll explain step by step how to implement a practical chatbot, from personal messages through slash...

- **Noduri:** 11
- **Conexiuni:** 4
- **Declanșare:** 🌐 Webhook
- **Integrări:** LangChain LLM, OpenAI Chat, Slack, Webhook

### Sentiment Analysis Tracking on Support Issues with Linear and Slack

> Se declanșează de airtableTrigger. folosește OpenAI Chat, folosește Extractor Informații, caută în Airtable, actualizează/creează în Airtable (+2 altele). Detalii: Try It Out!
 This n8n template performs continous monitoring on Linear Issue conversations performing sentiment analysis and alerting when the sentiment becomes negative.
This is helpful to quickly identify difficult customer support situations...

- **Noduri:** 19
- **Conexiuni:** 13
- **Declanșare:** ⏰ Programat
- **Integrări:** Airtable, Extractor Informații, GraphQL, OpenAI Chat, Slack

### Sentiment Analysis Tracking on Support Issues with Linear and Slack (1)

> Se declanșează de airtableTrigger. folosește OpenAI Chat, folosește Extractor Informații, caută în Airtable, actualizează/creează în Airtable (+2 altele). Detalii: Try It Out!
 This n8n template performs continous monitoring on Linear Issue conversations performing sentiment analysis and alerting when the sentiment becomes negative.
This is helpful to quickly identify difficult customer support situations...

- **Noduri:** 19
- **Conexiuni:** 13
- **Declanșare:** ⏰ Programat
- **Integrări:** Airtable, Extractor Informații, GraphQL, OpenAI Chat, Slack

### Venafi Cloud Slack Cert Bot

> Se declanșează prin webhook HTTP. folosește venafiTlsProtectCloud, folosește Răspuns Webhook, folosește HTTP API, folosește Sub-workflow (+3 altele). Detalii: ![n8n](https://i.imgur.com/lKnBNnH.png)
 Enhance Security Operations with the Venafi Slack CertBot!

Our **Venafi Slack CertBot** is strategically designed to facilitate immediate security operations directly from Slack. This tool allows end users...

- **Noduri:** 38
- **Conexiuni:** 22
- **Declanșare:** 🌐 Webhook
- **Integrări:** HTTP API, OpenAI, Răspuns Webhook, Slack, Sub-workflow, Webhook, venafiTlsProtectCloud

### piepdrive-test

> Se declanșează de pipedriveTrigger. folosește Pipedrive, folosește HTTP API, folosește Markdown, folosește Slack (+1 altele). Detalii: Enrich Pipedrive's Organization Data with GPT-4o When an Organization is Created in Pipedrive

This workflow **enriches a Pipedrive organization's data by adding a note to the organization object in Pipedrive**. It assumes there is a custom...

- **Noduri:** 8
- **Conexiuni:** 6
- **Integrări:** HTTP API, Markdown, OpenAI, Pipedrive, Slack

---

## Telegram

### AI-Powered Children_s Arabic Storytelling on Telegram

> Rulează programat (schedule). folosește OpenAI Chat, folosește Text Splitter, folosește LangChain Sumarizare, folosește OpenAI (+3 altele). Detalii: Template for Kids' Story in Arabic

The n8n template for creating kids' stories in Arabic provides a versatile platform for storytellers to captivate young audiences with educational and interactive tales. Along with its core functionalities, this...

- **Noduri:** 15
- **Conexiuni:** 10
- **Declanșare:** ⏰ Programat
- **Integrări:** LangChain Sumarizare, OpenAI, OpenAI Chat, Telegram, Text Splitter

### AI-Powered Children_s English Storytelling on Telegram with OpenAI

> Rulează programat (schedule). folosește OpenAI Chat, folosește LangChain Sumarizare, folosește Text Splitter, folosește OpenAI (+3 altele). Detalii: Setting Up a Workflow for "AI-Powered Children's English Storytelling on Telegram"

In this guide, we will walk you through the process of setting up a workflow to create and share captivating children's stories using the provided configuration....

- **Noduri:** 14
- **Conexiuni:** 9
- **Declanșare:** ⏰ Programat
- **Integrări:** LangChain Sumarizare, OpenAI, OpenAI Chat, Telegram, Text Splitter

### Agentic Telegram AI bot with LangChain nodes and new tools

> Se declanșează la primirea unui mesaj Telegram. folosește OpenAI Chat, folosește Buffer Memory, folosește Telegram, trimite documente prin telegramTool (+2 altele). Detalii: Generate an image with Dall-E-3 and send it via Telegram

- **Noduri:** 8
- **Conexiuni:** 6
- **Integrări:** AI Agent, Buffer Memory, HTTP Tool, OpenAI Chat, Telegram, telegramTool

### Angie, Personal AI Assistant with Telegram Voice and Text

> Se declanșează la primirea unui mesaj Telegram. citește date din googleCalendarTool, folosește Buffer Memory, citește date din gmailTool, folosește OpenAI Chat (+4 altele). Detalii: Start here: Step-by Step Youtube Tutorial :star:

[![Building an AI Personal Assistant](https://img.youtube.com/vi/pXjowPc6V2s/sddefault.jpg)](https://youtu.be/pXjowPc6V2s)

- **Noduri:** 15
- **Conexiuni:** 12
- **Integrări:** AI Agent, Buffer Memory, OpenAI, OpenAI Chat, Telegram, baserowTool, gmailTool, googleCalendarTool

### Automated AI image analysis and response via Telegram

> Se declanșează la primirea unui mesaj Telegram. folosește Telegram, folosește OpenAI. Detalii: Automated Image Analysis and Response via Telegram

 Example: @SubAlertMe_Bot

 Summary:
The automated image analysis and response workflow using n8n is a sophisticated solution designed to streamline the process of analyzing images sent via...

- **Noduri:** 8
- **Conexiuni:** 4
- **Integrări:** OpenAI, Telegram

### Chat with OpenAIs GPT via a simple Telegram Bot

> Se declanșează la primirea unui mesaj Telegram. folosește OpenAI Chat, folosește AI Agent, folosește Telegram.

- **Noduri:** 4
- **Conexiuni:** 3
- **Integrări:** AI Agent, OpenAI Chat, Telegram

### Detect toxic language in Telegram messages

> Se declanșează la primirea unui mesaj Telegram. folosește googlePerspective, folosește Telegram.

- **Noduri:** 5
- **Conexiuni:** 3
- **Integrări:** Telegram, googlePerspective

### Image Creation with OpenAI and Telegram

> Se declanșează la primirea unui mesaj Telegram. folosește OpenAI, trimite imagini prin Telegram. Detalii: N8N Workflow: AI-Enhanced Image Processing and Communication

 Description:
This n8n workflow integrates artificial intelligence to optimize image processing tasks and streamline communication via Telegram. Each node in the workflow provides...

- **Noduri:** 12
- **Conexiuni:** 4
- **Integrări:** OpenAI, Telegram

### NeurochainAI Basic API Integration

> Se declanșează la primirea unui mesaj Telegram. folosește HTTP API, folosește Telegram, trimite imagini prin Telegram, folosește Telegram (+1 altele). Detalii: Instructions for Using the Template
Follow these steps to set up and use this template:

**Create a Telegram Bot**:
- Open Telegram and search for BotFather.
- Use the ``/newbot`` command to create your bot.
- Follow the prompts and copy the Token...

- **Noduri:** 29
- **Conexiuni:** 14
- **Integrări:** HTTP API, Telegram

### Play with Spotify from Telegram

> Se declanșează la primirea unui mesaj Telegram. folosește OpenAI, caută în spotify, folosește spotify, folosește spotify (+3 altele). Detalii: Telegram to Spotify 
Ask AI about a track with artist and song name or if you can't remember describe it and AI does it's thing.

- **Noduri:** 14
- **Conexiuni:** 12
- **Integrări:** OpenAI, Telegram, spotify

### Send a random recipe once a day to Telegram

> Rulează programat (cron). listează date din Airtable, trimite imagini prin Telegram, folosește Telegram, adaugă date în Airtable (+1 altele).

- **Noduri:** 15
- **Conexiuni:** 12
- **Declanșare:** ⏰ Programat
- **Integrări:** Airtable, HTTP API, Telegram

### Telegram AI Langchain bot

> Se declanșează de Execute Workflow Trigger. folosește OpenAI Chat, folosește Buffer Memory, folosește Telegram, trimite imagini prin Telegram (+3 altele). Detalii: Generate an image with Dall-E 3 and send it via Telegram

- **Noduri:** 12
- **Conexiuni:** 9
- **Integrări:** AI Agent, Buffer Memory, HTTP API, OpenAI Chat, Sub-workflow Tool, Telegram

### Telegram AI multi-format chatbot

> Se declanșează la primirea unui mesaj Telegram. folosește OpenAI Chat, folosește Buffer Memory, folosește Telegram, folosește OpenAI (+2 altele). Detalii: 1. Send incoming message to the AI Agent
 2. Deliver agent reply to the user

- **Noduri:** 15
- **Conexiuni:** 9
- **Integrări:** AI Agent, Buffer Memory, OpenAI, OpenAI Chat, Telegram

### Telegram AI-bot

> Se declanșează la primirea unui mesaj Telegram. folosește OpenAI, folosește Telegram, folosește Telegram, trimite imagini prin Telegram. Detalii: Chatbot mode by default
 (when no command is provided)

- **Noduri:** 16
- **Conexiuni:** 9
- **Integrări:** OpenAI, Telegram
- **Tag-uri:** tutorial

### Telegram Bot with Supabase memory and OpenAI assistant integration

> Se declanșează la primirea unui mesaj Telegram. folosește HTTP API, folosește Supabase, folosește Telegram, citește date din Supabase. Detalii: Set up steps
1. **Create a Telegram Bot** using the [Botfather](https://t.me/botfather) and obtain the bot token.
2. **Set up Supabase:**
	1. Create a new project and generate a ```SUPABASE_URL``` and ```SUPABASE_KEY```.
	2. Create a new table named...

- **Noduri:** 17
- **Conexiuni:** 9
- **Integrări:** HTTP API, Supabase, Telegram

### Telegram RAG pdf

> Se declanșează la primirea unui mesaj Telegram. folosește OpenAI Embeddings, folosește Document Loader, folosește Text Splitter, folosește LangChain Retrieval QA (+4 altele). Detalii: Chat with Database

1. **Receive** the incoming chat message.
2. **Retrieve** relevant chunks from the _vector store_.
3. **Pass** these chunks to the model.

The model will use the retrieved information to **formulate a precise response**.

- **Noduri:** 20
- **Conexiuni:** 16
- **Integrări:** Document Loader, Groq, LangChain Retrieval QA, OpenAI Embeddings, Pinecone, Telegram, Text Splitter, Vector Retriever

### Translate Telegram audio messages with AI (55 supported languages) v1

> Se declanșează la primirea unui mesaj Telegram. folosește Telegram, folosește OpenAI Chat, folosește LangChain LLM, trimite audio prin Telegram (+2 altele). Detalii: Multi-lingual AI Powered Universal Translator with Speech ⭐

 Key capabilities
This flow enables a Telegram bot that can 
- accept speech in one of 55 languages 
- translates to another language and returns result in speech

 Use case:
- Learning a...

- **Noduri:** 13
- **Conexiuni:** 8
- **Integrări:** LangChain LLM, OpenAI, OpenAI Chat, Telegram

### 🐋🤖 DeepSeek AI Agent + Telegram + LONG TERM Memory 🧠

> Se declanșează prin webhook HTTP. folosește Telegram, folosește Webhook, folosește AI Agent, folosește Buffer Memory (+3 altele). Detalii: How to set up a Telegram Bot WebHook

 WebHook Setup Process

**Basic Concept**
A WebHook allows your Telegram bot to automatically receive updates instead of manually polling the Bot API.

**Setup Method**
To set a WebHook, make a GET request using...

- **Noduri:** 23
- **Conexiuni:** 11
- **Declanșare:** 🌐 Webhook
- **Integrări:** AI Agent, Buffer Memory, Google Docs, OpenAI Chat, Telegram, Webhook, googleDocsTool

### 🤖 Telegram Messaging Agent for Text/Audio/Images

> Se declanșează prin webhook HTTP. folosește Telegram, folosește Webhook, folosește HTTP API, folosește OpenAI Chat (+5 altele). Detalii: How to set up a Telegram Bot WebHook

 WebHook Setup Process

**Basic Concept**
A WebHook allows your Telegram bot to automatically receive updates instead of manually polling the Bot API.

**Setup Method**
To set a WebHook, make a GET request using...

- **Noduri:** 39
- **Conexiuni:** 21
- **Declanșare:** 🌐 Webhook
- **Integrări:** Clasificator Text, Conversie Fișier, Extracție Fișier, HTTP API, OpenAI, OpenAI Chat, Telegram, Webhook

### 🤖🧠 AI Agent Chatbot + LONG TERM Memory + Note Storage + Telegram

> Se declanșează prin mesaj de chat. folosește OpenAI Chat, folosește Buffer Memory, actualizează date în googleDocsTool, obține date din Google Docs (+2 altele). Detalii: AI AGENT with Long Term Memory & Note Storage

- **Noduri:** 21
- **Conexiuni:** 12
- **Integrări:** AI Agent, Buffer Memory, Google Docs, OpenAI Chat, Telegram, googleDocsTool

---

## WhatsApp

### Automate Sales Meeting Prep with AI & APIFY Sent To WhatsApp

> Se declanșează de Execute Workflow Trigger. obține date din Gmail, citește date din Google Calendar, folosește OpenAI Chat, folosește Extractor Informații (+6 altele). Detalii: 2. Extract Attendee Details From Invite
[Learn more about the Information Extractor node](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.information-extractor/)

Once we have our upcoming meeting, it'll be nice...

- **Noduri:** 61
- **Conexiuni:** 40
- **Declanșare:** ⏰ Programat
- **Integrări:** Extractor Informații, Gmail, Google Calendar, HTML, HTTP API, LangChain LLM, OpenAI Chat, Sub-workflow, WhatsApp

### Building Your First WhatsApp Chatbot

> Se declanșează de whatsAppTrigger. folosește OpenAI Chat, folosește Buffer Memory, folosește Vector Store Tool, folosește OpenAI Embeddings (+7 altele). Detalii: Try It Out!

 This n8n template builds a simple WhatsApp chabot acting as a Sales Agent. The Agent is backed by a product catalog vector store to better answer user's questions.

* This template is in 2 parts: creating the product catalog vector...

- **Noduri:** 28
- **Conexiuni:** 15
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, Buffer Memory, Document Loader, Extracție Fișier, HTTP API, OpenAI Chat, OpenAI Embeddings, Text Splitter, Vector Store, Vector Store Tool (+1 altele)

### Building Your First WhatsApp Chatbot (1)

> Se declanșează de whatsAppTrigger. folosește OpenAI Chat, folosește Buffer Memory, folosește Vector Store Tool, folosește OpenAI Embeddings (+7 altele). Detalii: Try It Out!

 This n8n template builds a simple WhatsApp chabot acting as a Sales Agent. The Agent is backed by a product catalog vector store to better answer user's questions.

* This template is in 2 parts: creating the product catalog vector...

- **Noduri:** 28
- **Conexiuni:** 15
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, Buffer Memory, Document Loader, Extracție Fișier, HTTP API, OpenAI Chat, OpenAI Embeddings, Text Splitter, Vector Store, Vector Store Tool (+1 altele)

### Business WhatsApp AI RAG Chatbot

> Se declanșează manual. folosește Răspuns Webhook, folosește AI Agent, folosește OpenAI Chat, folosește Qdrant (+9 altele). Detalii: STEP 4

 RAG System













* *Respond* webhook receives various POST Requests from Meta regarding WhatsApp messages (user messages + status notifications)
* Check if the incoming JSON contains user message
* Echo back the text message to the...

- **Noduri:** 24
- **Conexiuni:** 13
- **Declanșare:** 🌐 Webhook, 👆 Manual
- **Integrări:** AI Agent, Buffer Memory, Document Loader, Google Drive, HTTP API, OpenAI Chat, OpenAI Embeddings, Qdrant, Răspuns Webhook, Webhook (+2 altele)

### Respond to WhatsApp Messages with AI Like a Pro!

> Se declanșează de whatsAppTrigger. folosește WhatsApp, folosește HTTP API, folosește Buffer Memory, folosește Wikipedia Tool (+4 altele). Detalii: Try It Out!

 This n8n template demonstrates the beginnings of building your own n8n-powered WhatsApp chatbot! Under the hood, utilise n8n's powerful AI features to handle different message types and use an AI agent to respond to the user. A...

- **Noduri:** 35
- **Conexiuni:** 23
- **Integrări:** AI Agent, Buffer Memory, Google Gemini, HTTP API, LangChain LLM, WhatsApp, Wikipedia Tool

---

## WordPress

### Auto categorize wordpress template

> Se declanșează manual. actualizează date în WordPress, citește date din WordPress, folosește OpenAI Chat, folosește AI Agent. Detalii: How to Auto-Categorize 82 Blog Posts in 2 Minutes using A.I. (No Coding Required)

💡 Read the [case study here](https://rumjahn.com/how-to-use-a-i-to-categorize-wordpress-posts-and-streamline-your-content-organization-process/).

📺 Watch the...

- **Noduri:** 9
- **Conexiuni:** 4
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, OpenAI Chat, WordPress

### Auto-Tag Blog Posts in WordPress with AI

> Se declanșează de rssFeedReadTrigger. folosește OpenAI Chat, folosește Parser Autofix, folosește Parser Structurat, folosește HTTP API (+3 altele). Detalii: Handing off tagging and categorization fully to AI lets you **put your WordPress account on autopilot** without a human-in-the-loop.

In this example the application is use-case agnostic, but with this workflow you can:
1. Use AI to rewrite content...

- **Noduri:** 32
- **Conexiuni:** 21
- **Integrări:** HTTP API, LangChain LLM, OpenAI Chat, Parser Autofix, Parser Structurat, Sub-workflow, WordPress
- **Tag-uri:** marketing

### Automate Blog Creation in Brand Voice with AI

> Se declanșează manual. folosește OpenAI Chat, folosește Extractor Informații, folosește HTTP API, folosește HTML (+3 altele). Detalii: Try It Out!
 This n8n template demonstrates how to use AI to generate new on-brand written content by analysing previously published content.

With such an approach, it's possible to generate a steady stream of blog article drafts quickly with high...

- **Noduri:** 27
- **Conexiuni:** 17
- **Declanșare:** 👆 Manual
- **Integrări:** Extractor Informații, HTML, HTTP API, LangChain LLM, Markdown, OpenAI Chat, WordPress

### Automate Content Generator for WordPress with DeepSeek R1

> Se declanșează manual. folosește Google Sheets, folosește WordPress, folosește HTTP API, actualizează date în Google Sheets (+1 altele). Detalii: Target
This workflow is designed to automatically generate seo-friendly content for wordpress through DeepSeek R1 by giving input ideas on how to structure the article. A cover image is also generated and uploaded with OpenAI DALL-E 3. This flow is...

- **Noduri:** 17
- **Conexiuni:** 9
- **Declanșare:** 👆 Manual
- **Integrări:** Google Sheets, HTTP API, OpenAI, WordPress

### RAG & GenAI App With WordPress Content

> Se declanșează manual. folosește OpenAI Embeddings, folosește Document Loader, folosește textSplitterTokenSplitter, folosește OpenAI Chat (+10 altele). Detalii: Workflow 3 : Use this workflow to enable chat functionality with your website content. The chat can be embedded into your website to enhance user experience

- **Noduri:** 53
- **Conexiuni:** 41
- **Declanșare:** 🌐 Webhook, ⏰ Programat, 👆 Manual
- **Integrări:** AI Agent, Document Loader, HTTP API, Markdown, OpenAI Chat, OpenAI Embeddings, PostgreSQL, PostgreSQL Memory, Răspuns Webhook, Supabase (+3 altele)

### Write a WordPress post with AI (starting from a few keywords)

> Se declanșează la trimiterea unui formular n8n. folosește WordPress, folosește HTTP API, folosește Răspuns Webhook, folosește OpenAI (+1 altele). Detalii: The image is generated with Dall-E, uploaded to WordPress, and then connected to the post as its featured image

- **Noduri:** 37
- **Conexiuni:** 13
- **Declanșare:** 🌐 Webhook
- **Integrări:** HTTP API, OpenAI, Răspuns Webhook, Wikipedia Tool, WordPress

---

## analytics

### 1690-markdown-report-generation

> Se declanșează manual. folosește Markdown, folosește Email SMTP, folosește HTTP API, folosește moveBinaryData.

**Locație:** `1690-markdown-report-generation`

- **Noduri:** 10
- **Conexiuni:** 9
- **Declanșare:** 👆 Manual
- **Integrări:** Email SMTP, HTTP API, Markdown, moveBinaryData

### 1692-markdown-timesheet-report-generation

> Se declanșează manual. folosește Markdown, folosește Email SMTP, folosește HTTP API, folosește moveBinaryData.

**Locație:** `1692-markdown-timesheet-report-generation`

- **Noduri:** 10
- **Conexiuni:** 9
- **Declanșare:** 👆 Manual
- **Integrări:** Email SMTP, HTTP API, Markdown, moveBinaryData

### 1931-report-number-of-weekly-created-records-in-an-app

> Rulează programat (schedule). citește date din Notion, folosește Slack. Detalii: 2. Filter and transform your data

















We only want to count the UX ideas of the team. We use the `Filter` node to filter out all other items, and use the `Item Lists` node to summarize the data for us.

To edit the nodes, simply drag...

**Locație:** `1931-report-number-of-weekly-created-records-in-an-app`

- **Noduri:** 11
- **Conexiuni:** 5
- **Declanșare:** ⏰ Programat
- **Integrări:** Notion, Slack

### 1996-ai-customer-feedback-sentiment-analysis

> Se declanșează la trimiterea unui formular n8n. adaugă date în Google Sheets, folosește OpenAI. Detalii: Instructions
1. Connect Google sheets
2. Connect your OpenAi account (api key + org Id)
3. Create a customer feedback form, use an existing one or use the one below as example. 
All set!


- Here is the example google sheet being used in this...

**Locație:** `1996-ai-customer-feedback-sentiment-analysis`

- **Noduri:** 9
- **Conexiuni:** 3
- **Integrări:** Google Sheets, OpenAI

### 812-send-instagram-statistics-to-mattermost

> Rulează programat (cron). folosește Mattermost, folosește Date/Time, folosește Google Sheets.

**Locație:** `812-send-instagram-statistics-to-mattermost`

- **Noduri:** 5
- **Conexiuni:** 4
- **Declanșare:** ⏰ Programat
- **Integrări:** Date/Time, Google Sheets, Mattermost

### 815-create-a-short-url-and-get-the-statistics-of-the-url

> Se declanșează manual. folosește yourls, folosește yourls.

**Locație:** `815-create-a-short-url-and-get-the-statistics-of-the-url`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** 👆 Manual
- **Integrări:** yourls

---

## api-webhooks

### 119-webhook-returning-xml

> Se declanșează prin webhook HTTP. folosește XML, folosește Răspuns Webhook, folosește Webhook.

**Locație:** `119-webhook-returning-xml`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** 🌐 Webhook
- **Integrări:** Răspuns Webhook, Webhook, XML

### 1236-use-redis-to-rate-limit-your-low-code-api

> Se declanșează prin webhook HTTP. listează date din Airtable, folosește Redis, folosește Webhook.

**Locație:** `1236-use-redis-to-rate-limit-your-low-code-api`

- **Noduri:** 11
- **Conexiuni:** 8
- **Declanșare:** 🌐 Webhook
- **Integrări:** Airtable, Redis, Webhook

### 1440-handle-verification-for-twitter-webhook

> Se declanșează prin webhook HTTP. folosește Webhook, folosește Crypto.

**Locație:** `1440-handle-verification-for-twitter-webhook`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** 🌐 Webhook
- **Integrări:** Crypto, Webhook

### 1535-automate-testimonials-in-strapi-with-n8n

> Se declanșează prin webhook HTTP. creează înregistrări în Strapi, folosește interval, caută în Twitter/X, folosește Webhook (+1 altele).

**Locație:** `1535-automate-testimonials-in-strapi-with-n8n`

- **Noduri:** 14
- **Conexiuni:** 12
- **Declanșare:** 🌐 Webhook
- **Integrări:** Strapi, Twitter/X, Webhook, googleCloudNaturalLanguage, interval

### 1588-manage-adobe-acrobat-e-signatures-with-webhooks

> Se declanșează prin webhook HTTP. folosește Webhook, folosește Răspuns Webhook.

**Locație:** `1588-manage-adobe-acrobat-e-signatures-with-webhooks`

- **Noduri:** 5
- **Conexiuni:** 4
- **Declanșare:** 🌐 Webhook
- **Integrări:** Răspuns Webhook, Webhook

### 159-send-rss-feed-data-to-webhook

> Se declanșează manual. folosește rssFeedRead, folosește mongoDb, folosește mongoDb, folosește HTTP API.

**Locație:** `159-send-rss-feed-data-to-webhook`

- **Noduri:** 18
- **Conexiuni:** 17
- **Declanșare:** ⏰ Programat, 👆 Manual
- **Integrări:** HTTP API, mongoDb, rssFeedRead

### 1748-pulling-data-from-services-that-n8n-doesnt-have-a-pre-built-integration-for

> Se declanșează manual. folosește htmlExtract, folosește HTTP API. Detalii: 3. Handle Pagination
 Sometimes you need to make the same request multiple times to get all the data you need (pagination).

 The pagination process goes as follow:
 1. Loop through the pages of the input source (`HTTP Request` node named "Get my...

**Locație:** `1748-pulling-data-from-services-that-n8n-doesnt-have-a-pre-built-integration-for`

- **Noduri:** 14
- **Conexiuni:** 8
- **Declanșare:** 👆 Manual
- **Integrări:** HTTP API, htmlExtract

### 1750-creating-an-api-endpoint

> Se declanșează prin webhook HTTP. folosește Webhook, folosește Răspuns Webhook. Detalii: How to use it
1. Execute the workflow so that the webhook starts listening
2. Make a test request by pasting, **in a new browser tab**, the test URL from the `Webhook` node and appending the following test at the end...

**Locație:** `1750-creating-an-api-endpoint`

- **Noduri:** 5
- **Conexiuni:** 2
- **Declanșare:** 🌐 Webhook
- **Integrări:** Răspuns Webhook, Webhook

### 216-api-queries-data-from-graphql

> Se declanșează prin webhook HTTP. folosește GraphQL, folosește Webhook.

**Locație:** `216-api-queries-data-from-graphql`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** 🌐 Webhook
- **Integrări:** GraphQL, Webhook

### 2274-low-code-api-for-flutterflow-apps

> Se declanșează prin webhook HTTP. folosește n8nTrainingCustomerDatastore, folosește Webhook, folosește Răspuns Webhook. Detalii: Low-code API for Flutterflow apps
 Set up
1. Copy the Webhook URL from `On new flutterflow call` step. This is the URL you will make a GET request to in FlutterFlow.
2. Replace the "Customer Datastore" step with your own data source or any other...

**Locație:** `2274-low-code-api-for-flutterflow-apps`

- **Noduri:** 9
- **Conexiuni:** 4
- **Declanșare:** 🌐 Webhook
- **Integrări:** Răspuns Webhook, Webhook, n8nTrainingCustomerDatastore

### 2419-visual-regression-testing-with-apify-and-ai-vision-model

> Rulează zilnic la ora 6:00. descarcă din Google Drive, folosește Google Gemini, folosește Parser Structurat, folosește HTTP API (+5 altele). Detalii: Try It Out!

 This workflow implements an approach to Visual Regression Testing - a means to test websites for defects - using AI Vision Models.

This workflow uses a Google Sheet to track a list of webpages to test and is split into 2 parts; Part A...

**Locație:** `2419-visual-regression-testing-with-apify-and-ai-vision-model`

- **Noduri:** 34
- **Conexiuni:** 22
- **Declanșare:** ⏰ Programat, 👆 Manual
- **Integrări:** Google Drive, Google Gemini, Google Sheets, HTTP API, LangChain LLM, Parser Structurat, linear

### 2424-manipulate-pdf-with-adobe-developer-api

> Se declanșează manual. folosește HTTP API, descarcă din Dropbox. Detalii: Adobe API Wrapper

See Adobe documentation:
- https://developer.adobe.com/document-services/docs/overview/pdf-services-api/howtos/
- https://developer.adobe.com/document-services/docs/overview/pdf-extract-api/gettingstarted/

In short, this workflow...

**Locație:** `2424-manipulate-pdf-with-adobe-developer-api`

- **Noduri:** 20
- **Conexiuni:** 13
- **Declanșare:** 👆 Manual
- **Integrări:** Dropbox, HTTP API

### 2435-monitor-multiple-github-repos-via-webhook

> Se declanșează manual. folosește HTTP API, folosește Slack, folosește Telegram, folosește Webhook. Detalii: Setup
 1. Creating Credentials on Github
 Generate a personal access token on github by following these esteps;
- Right hand side of page -> Settings -> scroll to bottom -> Developer Settings > Personal Access Token > Tokens (classic) > Generate New...

**Locație:** `2435-monitor-multiple-github-repos-via-webhook`

- **Noduri:** 19
- **Conexiuni:** 9
- **Declanșare:** 🌐 Webhook, 👆 Manual
- **Integrări:** HTTP API, Slack, Telegram, Webhook

### 2658-api-schema-extractor

> Se declanșează manual. folosește HTTP API, folosește Text Splitter, folosește Document Loader, folosește executionData (+10 altele). Detalii: Stage 2 - Extract API Operations From Documentation
- Fetch a list of services pending extraction from Database (Google Sheet)
- Query Vector store (Qdrant) to figure out service's products, solutions and offerings
- Query Vector store (Qdrant)...

**Locație:** `2658-api-schema-extractor`

- **Noduri:** 88
- **Conexiuni:** 75
- **Declanșare:** 👆 Manual
- **Integrări:** Clasificator Text, Document Loader, Extractor Informații, Google Drive, Google Embeddings, Google Gemini, Google Sheets, HTTP API, Qdrant, Sub-workflow (+2 altele)

### 351-webhooks-with-mattermost

> Se declanșează prin webhook HTTP. folosește Webhook, folosește HTTP API, folosește Mattermost.

**Locație:** `351-webhooks-with-mattermost`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** 🌐 Webhook
- **Integrări:** HTTP API, Mattermost, Webhook

### 471-send-github-notifications-to-discord-webhook

> Rulează programat (cron). folosește HTTP API, folosește Discord.

**Locație:** `471-send-github-notifications-to-discord-webhook`

- **Noduri:** 6
- **Conexiuni:** 5
- **Declanșare:** ⏰ Programat
- **Integrări:** Discord, HTTP API

### 558-get-the-last-five-spacex-launches-from-the-spacex-land-api-using-graphql

> Se declanșează manual. folosește GraphQL.

**Locație:** `558-get-the-last-five-spacex-launches-from-the-spacex-land-api-using-graphql`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** GraphQL

### 652-store-data-received-from-webhook-in-json

> Se declanșează manual. folosește HTTP API, folosește moveBinaryData, folosește writeBinaryFile.

**Locație:** `652-store-data-received-from-webhook-in-json`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** HTTP API, moveBinaryData, writeBinaryFile

### 779-create-update-and-get-an-entry-in-strapi

> Se declanșează manual. creează înregistrări în Strapi, actualizează date în Strapi, folosește Strapi.

**Locație:** `779-create-update-and-get-an-entry-in-strapi`

- **Noduri:** 6
- **Conexiuni:** 5
- **Declanșare:** 👆 Manual
- **Integrări:** Strapi

### 968-create-an-event-in-posthog-when-a-request-is-made-to-a-webhook-url

> Se declanșează prin webhook HTTP. folosește postHog, folosește Webhook.

**Locație:** `968-create-an-event-in-posthog-when-a-request-is-made-to-a-webhook-url`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 🌐 Webhook
- **Integrări:** Webhook, postHog

---

## automation

### 100-using-the-merge-node-merge-by-key

> Declanșare manuală sau nedeterminată.

**Locație:** `100-using-the-merge-node-merge-by-key`

- **Noduri:** 5
- **Conexiuni:** 4

### 101-write-json-to-disk-binary

> Declanșare manuală sau nedeterminată. folosește writeBinaryFile.

**Locație:** `101-write-json-to-disk-binary`

- **Noduri:** 3
- **Conexiuni:** 2
- **Integrări:** writeBinaryFile

### 1041-create-update-and-get-an-object-from-bubble

> Declanșare manuală sau nedeterminată. creează înregistrări în Bubble, actualizează date în Bubble, folosește Bubble.

**Locație:** `1041-create-update-and-get-an-object-from-bubble`

- **Noduri:** 3
- **Conexiuni:** 2
- **Integrări:** Bubble

### 1047-send-location-updates-of-the-iss-every-minute-to-a-queue-in-aws-sqs

> Rulează programat (cron). folosește AWS SQS, folosește HTTP API.

**Locație:** `1047-send-location-updates-of-the-iss-every-minute-to-a-queue-in-aws-sqs`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** ⏰ Programat
- **Integrări:** AWS SQS, HTTP API

### 1048-create-update-and-get-an-item-from-webflow

> Se declanșează manual. creează înregistrări în Webflow, actualizează date în Webflow, folosește Webflow.

**Locație:** `1048-create-update-and-get-an-item-from-webflow`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** Webflow

### 1053-git-backup-of-workflows-and-credentials

> Se declanșează manual. folosește Comandă Shell.

**Locație:** `1053-git-backup-of-workflows-and-credentials`

- **Noduri:** 7
- **Conexiuni:** 6
- **Declanșare:** ⏰ Programat, 👆 Manual
- **Integrări:** Comandă Shell

### 1073-scrape-and-store-data-from-multiple-website-pages

> Se declanșează manual. folosește HTTP API, folosește htmlExtract, folosește mongoDb, folosește uproc (+4 altele).

**Locație:** `1073-scrape-and-store-data-from-multiple-website-pages`

- **Noduri:** 23
- **Conexiuni:** 23
- **Declanșare:** 👆 Manual
- **Integrări:** Comandă Shell, HTTP API, htmlExtract, mongoDb, readBinaryFile, uproc, writeBinaryFile

### 1074-add-liked-songs-to-a-spotify-monthly-playlist

> Rulează programat (schedule). folosește spotify, citește date din nocoDb, creează înregistrări în nocoDb, folosește spotify (+2 altele). Detalii: Check if the song is in the Spotify playlist. If not, add it.

**Locație:** `1074-add-liked-songs-to-a-spotify-monthly-playlist`

- **Noduri:** 30
- **Conexiuni:** 26
- **Declanșare:** ⏰ Programat
- **Integrări:** nocoDb, spotify

### 1093-build-a-self-hosted-url-shortener-with-a-dashboard

> Se declanșează prin webhook HTTP. folosește Webhook, folosește Crypto, adaugă date în Airtable, listează date din Airtable (+1 altele).

**Locație:** `1093-build-a-self-hosted-url-shortener-with-a-dashboard`

- **Noduri:** 26
- **Conexiuni:** 19
- **Declanșare:** 🌐 Webhook
- **Integrări:** Airtable, Crypto, Webhook

### 1110-add-articles-to-a-notion-list-by-accessing-a-discord-slash-command

> Se declanșează prin webhook HTTP. folosește Webhook, folosește HTTP API, folosește htmlExtract, folosește Notion.

**Locație:** `1110-add-articles-to-a-notion-list-by-accessing-a-discord-slash-command`

- **Noduri:** 7
- **Conexiuni:** 5
- **Declanșare:** 🌐 Webhook
- **Integrări:** HTTP API, Notion, Webhook, htmlExtract

### 1111-create-transcription-jobs-using-aws-transcribe

> Se declanșează manual. folosește awsTranscribe, citește date din awsS3.

**Locație:** `1111-create-transcription-jobs-using-aws-transcribe`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** 👆 Manual
- **Integrări:** awsS3, awsTranscribe

### 1114-create-update-and-get-a-task-in-microsoft-to-do

> Se declanșează manual. creează înregistrări în microsoftToDo, actualizează date în microsoftToDo, folosește microsoftToDo.

**Locație:** `1114-create-update-and-get-a-task-in-microsoft-to-do`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** microsoftToDo

### 1115-manage-changes-using-the-git-node

> Se declanșează manual. folosește git, folosește git, folosește git, folosește git.

**Locație:** `1115-manage-changes-using-the-git-node`

- **Noduri:** 5
- **Conexiuni:** 4
- **Declanșare:** 👆 Manual
- **Integrări:** git

### 1130-add-a-check-condition-for-a-loop-in-n8n

> Se declanșează manual. folosește Twitter/X.

**Locație:** `1130-add-a-check-condition-for-a-loop-in-n8n`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** Twitter/X

### 1132-trigger-a-build-in-travis-ci-when-code-changes-are-push-to-a-github-repo

> Se declanșează de githubTrigger. folosește travisCi.

**Locație:** `1132-trigger-a-build-in-travis-ci-when-code-changes-are-push-to-a-github-repo`

- **Noduri:** 4
- **Conexiuni:** 2
- **Integrări:** travisCi

### 1160-merge-data-for-multiple-executions

> Se declanșează manual. folosește rssFeedRead.

**Locație:** `1160-merge-data-for-multiple-executions`

- **Noduri:** 6
- **Conexiuni:** 5
- **Declanșare:** 👆 Manual
- **Integrări:** rssFeedRead

### 1222-backup-workflows-to-github

> Rulează programat (cron). folosește GitHub, obține date din GitHub, folosește GitHub, folosește HTTP API.

**Locație:** `1222-backup-workflows-to-github`

- **Noduri:** 11
- **Conexiuni:** 9
- **Declanșare:** ⏰ Programat
- **Integrări:** GitHub, HTTP API

### 1243-avoid-rate-limiting-by-batching-http-requests

> Se declanșează manual. folosește n8nTrainingCustomerDatastore, folosește HTTP API.

**Locație:** `1243-avoid-rate-limiting-by-batching-http-requests`

- **Noduri:** 6
- **Conexiuni:** 5
- **Declanșare:** 👆 Manual
- **Integrări:** HTTP API, n8nTrainingCustomerDatastore

### 1254-deploy-site-when-new-content-gets-added

> Se declanșează prin webhook HTTP. folosește Webhook, creează înregistrări în netlify.

**Locație:** `1254-deploy-site-when-new-content-gets-added`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 🌐 Webhook
- **Integrări:** Webhook, netlify

### 1274-assign-issues-to-interested-contributors

> Se declanșează de githubTrigger. folosește GitHub, folosește GitHub.

**Locație:** `1274-assign-issues-to-interested-contributors`

- **Noduri:** 11
- **Conexiuni:** 5
- **Integrări:** GitHub

### 1298-get-top-5-products-on-product-hunt-every-hour

> Rulează programat (cron). folosește GraphQL, folosește Discord.

**Locație:** `1298-get-top-5-products-on-product-hunt-every-hour`

- **Noduri:** 5
- **Conexiuni:** 4
- **Declanșare:** ⏰ Programat
- **Integrări:** Discord, GraphQL

### 1306-serve-a-static-html-page-when-a-link-is-accessed

> Se declanșează prin webhook HTTP. folosește Răspuns Webhook, folosește Webhook.

**Locație:** `1306-serve-a-static-html-page-when-a-link-is-accessed`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 🌐 Webhook
- **Integrări:** Răspuns Webhook, Webhook

### 1309-get-only-new-rss-with-photo

> Rulează programat (cron). folosește rssFeedRead, folosește htmlExtract.

**Locație:** `1309-get-only-new-rss-with-photo`

- **Noduri:** 5
- **Conexiuni:** 5
- **Declanșare:** ⏰ Programat
- **Integrări:** htmlExtract, rssFeedRead

### 1325-transf-meeting-booking-into-notion-s-task-with-verified-information

> Se declanșează de calendlyTrigger. folosește Notion, folosește dropcontact.

**Locație:** `1325-transf-meeting-booking-into-notion-s-task-with-verified-information`

- **Noduri:** 3
- **Conexiuni:** 2
- **Integrări:** Notion, dropcontact

### 1328-use-regex-to-select-date

> Se declanșează manual.

**Locație:** `1328-use-regex-to-select-date`

- **Noduri:** 6
- **Conexiuni:** 5
- **Declanșare:** 👆 Manual

### 1330-demonstrates-the-use-of-the-item-index-method

> Se declanșează manual. folosește n8nTrainingCustomerDatastore, folosește HTTP API.

**Locație:** `1330-demonstrates-the-use-of-the-item-index-method`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** HTTP API, n8nTrainingCustomerDatastore

### 1349-create-an-issue-on-gitlab-on-every-github-release

> Rulează programat (cron). citește date din GitHub, folosește GitLab.

**Locație:** `1349-create-an-issue-on-gitlab-on-every-github-release`

- **Noduri:** 6
- **Conexiuni:** 6
- **Declanșare:** ⏰ Programat
- **Integrări:** GitHub, GitLab

### 1363-join-data-from-postgres-and-mysql

> Se declanșează prin webhook HTTP. folosește Webhook, folosește mySql, folosește HTTP API, folosește PostgreSQL.

**Locație:** `1363-join-data-from-postgres-and-mysql`

- **Noduri:** 6
- **Conexiuni:** 5
- **Declanșare:** 🌐 Webhook
- **Integrări:** HTTP API, PostgreSQL, Webhook, mySql

### 1364-cron-routines-with-telegram

> Se declanșează manual. folosește Telegram, folosește Webhook, folosește mySql.

**Locație:** `1364-cron-routines-with-telegram`

- **Noduri:** 7
- **Conexiuni:** 5
- **Declanșare:** 🌐 Webhook, ⏰ Programat, 👆 Manual
- **Integrări:** Telegram, Webhook, mySql

### 1373-create-a-new-user-in-notion-based-on-the-signup-form-submission

> Se declanșează prin webhook HTTP. folosește Webhook, folosește Notion, citește date din Notion, actualizează date în Notion.

**Locație:** `1373-create-a-new-user-in-notion-based-on-the-signup-form-submission`

- **Noduri:** 12
- **Conexiuni:** 11
- **Declanșare:** 🌐 Webhook
- **Integrări:** Notion, Webhook

### 1374-create-a-new-team-for-a-project-in-notion

> Se declanșează prin webhook HTTP. citește date din Notion, folosește Notion, actualizează date în Notion, folosește Webhook.

**Locație:** `1374-create-a-new-team-for-a-project-in-notion`

- **Noduri:** 23
- **Conexiuni:** 21
- **Declanșare:** 🌐 Webhook
- **Integrări:** Notion, Webhook

### 1376-share-jokes-on-twitter-automatically

> Rulează programat (cron). folosește HTTP API, folosește Twitter/X.

**Locație:** `1376-share-jokes-on-twitter-automatically`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** ⏰ Programat
- **Integrări:** HTTP API, Twitter/X

### 1381-search-and-download-torrents-using-transmission-daemon

> Se declanșează prin webhook HTTP. folosește Webhook, folosește HTTP API, folosește Telegram.

**Locație:** `1381-search-and-download-torrents-using-transmission-daemon`

- **Noduri:** 8
- **Conexiuni:** 6
- **Declanșare:** 🌐 Webhook
- **Integrări:** HTTP API, Telegram, Webhook

### 1387-send-automated-daily-reminders-on-telegram

> Rulează programat (cron). folosește Telegram.

**Locație:** `1387-send-automated-daily-reminders-on-telegram`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** ⏰ Programat
- **Integrări:** Telegram

### 1393-extract-and-store-text-from-chat-images-using-aws-s3

> Se declanșează la primirea unui mesaj Telegram. folosește awsTextract, adaugă date în Airtable, încarcă fișiere în awsS3.

**Locație:** `1393-extract-and-store-text-from-chat-images-using-aws-s3`

- **Noduri:** 4
- **Conexiuni:** 2
- **Integrări:** Airtable, awsS3, awsTextract

### 1415-plex-automatic-qbittorent-throttler

> Se declanșează prin webhook HTTP. folosește Webhook, folosește HTTP API.

**Locație:** `1415-plex-automatic-qbittorent-throttler`

- **Noduri:** 21
- **Conexiuni:** 16
- **Declanșare:** 🌐 Webhook
- **Integrări:** HTTP API, Webhook

### 1418-create-an-rss-feed-based-on-a-website-s-content

> Se declanșează manual. folosește htmlExtract, folosește HTTP API, folosește Date/Time, folosește Webhook (+1 altele).

**Locație:** `1418-create-an-rss-feed-based-on-a-website-s-content`

- **Noduri:** 12
- **Conexiuni:** 11
- **Declanșare:** 🌐 Webhook, 👆 Manual
- **Integrări:** Date/Time, HTTP API, Răspuns Webhook, Webhook, htmlExtract

### 1423-tiny-tiny-rss-new-stared-article-saved-to-wallabag

> Se declanșează manual. folosește HTTP API.

**Locație:** `1423-tiny-tiny-rss-new-stared-article-saved-to-wallabag`

- **Noduri:** 10
- **Conexiuni:** 8
- **Declanșare:** ⏰ Programat, 👆 Manual
- **Integrări:** HTTP API

### 1425-send-a-random-recipe-once-a-day-to-telegram

> Rulează programat (cron). listează date din Airtable, trimite imagini prin Telegram, folosește Telegram, adaugă date în Airtable (+1 altele).

**Locație:** `1425-send-a-random-recipe-once-a-day-to-telegram`

- **Noduri:** 15
- **Conexiuni:** 12
- **Declanșare:** ⏰ Programat
- **Integrări:** Airtable, HTTP API, Telegram

### 1442-automate-assigning-github-issues

> Se declanșează de githubTrigger. folosește GitHub, folosește GitHub.

**Locație:** `1442-automate-assigning-github-issues`

- **Noduri:** 10
- **Conexiuni:** 5
- **Integrări:** GitHub

### 1469-post-rss-feed-items-from-yesterday-to-slack

> Rulează programat (cron). folosește Date/Time, folosește rssFeedRead, folosește Slack.

**Locație:** `1469-post-rss-feed-items-from-yesterday-to-slack`

- **Noduri:** 6
- **Conexiuni:** 5
- **Declanșare:** ⏰ Programat
- **Integrări:** Date/Time, Slack, rssFeedRead

### 1472-standup-bot-1-4-initialize

> Se declanșează manual. folosește writeBinaryFile, folosește moveBinaryData.

**Locație:** `1472-standup-bot-1-4-initialize`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** moveBinaryData, writeBinaryFile

### 1473-standup-bot-2-4-read-config

> Se declanșează manual. folosește readBinaryFile, folosește moveBinaryData.

**Locație:** `1473-standup-bot-2-4-read-config`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** 👆 Manual
- **Integrări:** moveBinaryData, readBinaryFile

### 1474-standup-bot-3-4-override-config

> Se declanșează manual. folosește writeBinaryFile, folosește moveBinaryData.

**Locație:** `1474-standup-bot-3-4-override-config`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** 👆 Manual
- **Integrări:** moveBinaryData, writeBinaryFile

### 1475-standup-bot-4-4-worker

> Se declanșează prin webhook HTTP. folosește Mattermost, folosește HTTP API, folosește Webhook, folosește Sub-workflow (+2 altele).

**Locație:** `1475-standup-bot-4-4-worker`

- **Noduri:** 29
- **Conexiuni:** 23
- **Declanșare:** 🌐 Webhook, ⏰ Programat
- **Integrări:** HTTP API, Mattermost, Sub-workflow, Webhook

### 1497-sum-or-aggregate-a-column-of-spreadsheet-or-table-data

> Se declanșează manual.

**Locație:** `1497-sum-or-aggregate-a-column-of-spreadsheet-or-table-data`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** 👆 Manual

### 1534-back-up-your-n8n-workflows-to-github

> Se declanșează manual. folosește n8n Sub-workflow, folosește HTTP API, folosește GitHub, folosește GitHub (+3 altele). Detalii: Backup to GitHub 
This workflow will backup all instance workflows to GitHub every 24 hours.

The files are saved into folders using `YYYY/MM/` for the directory path and `ID.json` for the filename.

The Repo Owner, Repo Name and Main folder are set...

**Locație:** `1534-back-up-your-n8n-workflows-to-github`

- **Noduri:** 26
- **Conexiuni:** 21
- **Declanșare:** ⏰ Programat, 👆 Manual
- **Integrări:** GitHub, HTTP API, Slack, Sub-workflow, n8n Sub-workflow

### 1554-get-data-from-multiple-rss-feeds-to-telegram

> Rulează programat (cron). folosește rssFeedRead, folosește Telegram.

**Locație:** `1554-get-data-from-multiple-rss-feeds-to-telegram`

- **Noduri:** 11
- **Conexiuni:** 7
- **Declanșare:** ⏰ Programat
- **Integrări:** Telegram, rssFeedRead

### 156-get-execute-command-data-and-transfer-to-json

> Declanșare manuală sau nedeterminată. folosește Comandă Shell.

**Locație:** `156-get-execute-command-data-and-transfer-to-json`

- **Noduri:** 3
- **Conexiuni:** 1
- **Integrări:** Comandă Shell

### 1576-push-your-public-ip-to-namecheaps-dynamic-dns

> Rulează programat (cron). folosește HTTP API.

**Locație:** `1576-push-your-public-ip-to-namecheaps-dynamic-dns`

- **Noduri:** 7
- **Conexiuni:** 6
- **Declanșare:** ⏰ Programat
- **Integrări:** HTTP API

### 1599-send-new-youtube-channel-videos-to-telegram

> Declanșare manuală sau nedeterminată. folosește interval, folosește youTube, folosește Telegram.

**Locație:** `1599-send-new-youtube-channel-videos-to-telegram`

- **Noduri:** 5
- **Conexiuni:** 4
- **Integrări:** Telegram, interval, youTube

### 1605-extend-n8n-with-additional-tools

> Se declanșează la primirea unui mesaj Telegram. folosește Telegram, trimite imagini prin Telegram, folosește HTTP API, folosește Fișier Spreadsheet (+3 altele).

**Locație:** `1605-extend-n8n-with-additional-tools`

- **Noduri:** 21
- **Conexiuni:** 16
- **Integrări:** Comandă Shell, Fișier Spreadsheet, HTTP API, Telegram, readBinaryFile, writeBinaryFile

### 1621-split-out-binary-data

> Se declanșează manual. folosește HTTP API, folosește Compresie. Detalii: Example Data
The first two nodes simply fetch some example data to work with.

In the real world, you'd probably process incoming emails, uploaded FTP files or something similar instead.

**Locație:** `1621-split-out-binary-data`

- **Noduri:** 6
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** Compresie, HTTP API

### 1700-very-quick-quickstart

> Se declanșează manual. folosește n8nTrainingCustomerDatastore. Detalii: About the very quick quickstart workflow

This is an incomplete workflow, used in the [very quick quickstart](https://docs.n8n.io//try-it-out/quickstart/) tutorial.

**Locație:** `1700-very-quick-quickstart`

- **Noduri:** 6
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** n8nTrainingCustomerDatastore

### 1739-move-data-between-json-and-spreadsheets

> Declanșare manuală sau nedeterminată. folosește HTTP API, adaugă date în Google Sheets, folosește Fișier Spreadsheet, folosește Fișier Spreadsheet (+3 altele). Detalii: JSON file > Google Sheets

**Locație:** `1739-move-data-between-json-and-spreadsheets`

- **Noduri:** 14
- **Conexiuni:** 8
- **Integrări:** Fișier Spreadsheet, Gmail, Google Sheets, HTTP API, moveBinaryData, writeBinaryFile

### 1744-working-with-dates-and-times

> Se declanșează manual. folosește Date/Time. Detalii: 2. Advanced way: Using Expressions
In this `Set` node, we set dates using [Luxon expressions](https://docs.n8n.io/code-examples/expressions/luxon/) for the following formats:

Now - `{{$now}}`
Current time with seconds -...

**Locație:** `1744-working-with-dates-and-times`

- **Noduri:** 9
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** Date/Time

### 1746-filtering-and-branching-data

> Se declanșează manual. folosește n8nTrainingCustomerDatastore. Detalii: 3. Multiple branches
We use the `Switch` when there more than 2 possible outcomes to the filtering. We do that by specifying the condition under **Routing rules** inside the node.

In this example we send all **US-based** customers data to route 0,...

**Locație:** `1746-filtering-and-branching-data`

- **Noduri:** 9
- **Conexiuni:** 2
- **Declanșare:** 👆 Manual
- **Integrări:** n8nTrainingCustomerDatastore

### 1747-joining-different-datasets

> Se declanșează manual. Detalii: Aggregating data with the Merge node

 The merge node is one of the most useful nodes in n8n. In this workflow we show how to merge data from two different sources (similar to SQL joins).

 The most-used operations of the merge node are presented...

**Locație:** `1747-joining-different-datasets`

- **Noduri:** 17
- **Conexiuni:** 7
- **Declanșare:** 👆 Manual

### 1749-rate-limiting-and-waiting-for-external-events

> Se declanșează manual. folosește n8nTrainingCustomerDatastore, folosește n8nTrainingCustomerMessenger. Detalii: 2. Wait for an external event
Use this operation when an external step is needed in order to continue with the rest of the workflow.
For example - a workflow sends a purchase approval link to the merchant (using Gmail, Slack etc..) and waits for the...

**Locație:** `1749-rate-limiting-and-waiting-for-external-events`

- **Noduri:** 13
- **Conexiuni:** 9
- **Declanșare:** 👆 Manual
- **Integrări:** n8nTrainingCustomerDatastore, n8nTrainingCustomerMessenger

### 1751-preparing-data-to-be-sent-to-a-service

> Se declanșează manual. actualizează/creează în Google Sheets, folosește n8nTrainingCustomerDatastore. Detalii: This is where we put the data in the format that Google Sheets expect. 
This means changing the field name from `name` to `Full name`, dropping all fields except `ID`, `Email` and adding a `Created time` field

**Locație:** `1751-preparing-data-to-be-sent-to-a-service`

- **Noduri:** 6
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** Google Sheets, n8nTrainingCustomerDatastore

### 1799-rss-feed-for-ard-audiothek-podcasts

> Se declanșează manual. folosește HTTP API, folosește htmlExtract, folosește Webhook, folosește Răspuns Webhook.

**Locație:** `1799-rss-feed-for-ard-audiothek-podcasts`

- **Noduri:** 11
- **Conexiuni:** 10
- **Declanșare:** 🌐 Webhook, 👆 Manual
- **Integrări:** HTTP API, Răspuns Webhook, Webhook, htmlExtract

### 18-n8n-nodemation-basic-getting-started-on-the-workflow-canvas-1-3

> Declanșare manuală sau nedeterminată. folosește interval.

**Locație:** `18-n8n-nodemation-basic-getting-started-on-the-workflow-canvas-1-3`

- **Noduri:** 3
- **Conexiuni:** 2
- **Integrări:** interval

### 1814-merge-multiple-runs-into-one

> Se declanșează manual. folosește n8nTrainingCustomerDatastore.

**Locație:** `1814-merge-multiple-runs-into-one`

- **Noduri:** 7
- **Conexiuni:** 6
- **Declanșare:** 👆 Manual
- **Integrări:** n8nTrainingCustomerDatastore

### 1839-import-csv-into-mysql

> Se declanșează manual. folosește readBinaryFile, folosește Fișier Spreadsheet, folosește mySql.

**Locație:** `1839-import-csv-into-mysql`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** Fișier Spreadsheet, mySql, readBinaryFile

### 1856-turn-on-a-light-to-a-specific-color-on-any-update-in-github-repository

> Se declanșează de githubTrigger. folosește homeAssistant. Detalii: Configure light here
It is likely the name of the light that you want to turn a specific colour is not called `light.lamp`. In which case, please head to your Home Assistant instance and find the light taking note of it's `entity_id`. See discussion...

**Locație:** `1856-turn-on-a-light-to-a-specific-color-on-any-update-in-github-repository`

- **Noduri:** 4
- **Conexiuni:** 1
- **Integrări:** homeAssistant

### 1892-get-workflows-affected-by-0-214-3-migration

> Se declanșează prin webhook HTTP. folosește n8n Sub-workflow, folosește Webhook, folosește HTML, folosește Răspuns Webhook. Detalii: ⚠️ When and how to use this workflow

If you previously upgraded to n8n version `0.214.3`, some of your workflows might have accidentally been re-wired in the wrong way. This affected nodes which have more than 1 output, such as `If`, `Switch`, and...

**Locație:** `1892-get-workflows-affected-by-0-214-3-migration`

- **Noduri:** 9
- **Conexiuni:** 4
- **Declanșare:** 🌐 Webhook
- **Integrări:** HTML, Răspuns Webhook, Webhook, n8n Sub-workflow

### 1895-reddit-ai-digest

> Se declanșează manual. caută în reddit, folosește OpenAI, folosește OpenAI. Detalii: What we learned
- 🪶 **Writing prompts**: small changes in the type of prompt result in very different results. e.g. for Summarising OpenAI would use multiple sentences even if we asked it to use only 1. We got better results by following OpenAI's...

**Locație:** `1895-reddit-ai-digest`

- **Noduri:** 15
- **Conexiuni:** 9
- **Declanșare:** 👆 Manual
- **Integrări:** OpenAI, reddit

### 19-n8n-nodemation-basic-creating-your-first-simple-workflow-2-3

> Se declanșează prin webhook HTTP. folosește Webhook, folosește HTTP API.

**Locație:** `19-n8n-nodemation-basic-creating-your-first-simple-workflow-2-3`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** 🌐 Webhook
- **Integrări:** HTTP API, Webhook

### 1900-openai-examples-chatgpt-dalle-2-whisper-1-5-in-1

> Se declanșează manual. folosește OpenAI, folosește OpenAI, folosește HTTP API, folosește HTML (+1 altele). Detalii: ChatGPT example 3.1
 When using ChatGPT programmatically, create an array of system / user / assistant contents and append them one after another
 Call ChatGPT API via HTTP Request node to provide all messages at once

**Locație:** `1900-openai-examples-chatgpt-dalle-2-whisper-1-5-in-1`

- **Noduri:** 27
- **Conexiuni:** 11
- **Declanșare:** 👆 Manual
- **Integrări:** HTML, HTTP API, OpenAI, readBinaryFiles

### 1913-count-the-items-returned-by-a-node

> Se declanșează manual. folosește n8nTrainingCustomerDatastore.

**Locație:** `1913-count-the-items-returned-by-a-node`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** 👆 Manual
- **Integrări:** n8nTrainingCustomerDatastore

### 1916-merge-binary-objects-on-multiple-items-into-a-single-item

> Se declanșează manual. folosește HTTP API. Detalii: Transformation
This is where the magic happens. Multiple items with one binary object each are being transformed into one item with multiple binary objects.

**Locație:** `1916-merge-binary-objects-on-multiple-items-into-a-single-item`

- **Noduri:** 6
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** HTTP API

### 1918-load-data-into-snowflake

> Se declanșează manual. folosește HTTP API, folosește Fișier Spreadsheet, folosește snowflake.

**Locație:** `1918-load-data-into-snowflake`

- **Noduri:** 5
- **Conexiuni:** 4
- **Declanșare:** 👆 Manual
- **Integrări:** Fișier Spreadsheet, HTTP API, snowflake

### 1943-comparing-data-with-the-compare-datasets-node

> Se declanșează manual. Detalii: Comparing data with the Compare Datasets node

The [Compare Datasets](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.comparedatasets/) node compares data streams before merging them. It outputs up to four different...

**Locație:** `1943-comparing-data-with-the-compare-datasets-node`

- **Noduri:** 6
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual

### 1944-compare-sql-datasets

> Se declanșează manual. folosește mySql.

**Locație:** `1944-compare-sql-datasets`

- **Noduri:** 5
- **Conexiuni:** 4
- **Declanșare:** 👆 Manual
- **Integrări:** mySql

### 1947-sql-to-xml-export-with-xsl-template-formatting

> Se declanșează prin webhook HTTP. folosește Webhook, folosește mySql, folosește XML, folosește HTML (+3 altele). Detalii: Set node can be used as well
 XML declaration and a link to the XSL template are added here
 Note that {{$env.WEBHOOK_URL}} variable is used, so that an URL of your n8n instance is automatically selected

**Locație:** `1947-sql-to-xml-export-with-xsl-template-formatting`

- **Noduri:** 15
- **Conexiuni:** 9
- **Declanșare:** 🌐 Webhook
- **Integrări:** HTML, HTTP API, Răspuns Webhook, Webhook, XML, moveBinaryData, mySql

### 1953-suggest-meeting-slots-using-ai

> Se declanșează de Gmail Trigger. folosește OpenAI Chat, folosește Sub-workflow Tool, citește date din Google Calendar, folosește LangChain LLM (+4 altele). Detalii: Check if incoming email is about appointment
We use LLM to check subject and body of the email and determine if it's an appointment request.

**Locație:** `1953-suggest-meeting-slots-using-ai`

- **Noduri:** 21
- **Conexiuni:** 14
- **Integrări:** AI Agent, Gmail, Google Calendar, LangChain LLM, OpenAI Chat, Parser Structurat, Sub-workflow Tool

### 1955-custom-langchain-agent-written-in-javascript

> Se declanșează manual. folosește lmOpenAi, folosește OpenAI Chat, folosește AI Agent. Detalii: Self-coded LLM Chain Node

**Locație:** `1955-custom-langchain-agent-written-in-javascript`

- **Noduri:** 10
- **Conexiuni:** 6
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, OpenAI Chat, lmOpenAi

### 1956-ai-summarize-podcast-episode-and-enhance-using-wikipedia

> Se declanșează manual. folosește documentJsonInputLoader, folosește Text Splitter, folosește LangChain Sumarizare, folosește OpenAI Chat (+5 altele). Detalii: Generate Questions and Topics from the summary and make sure the response follows required schema.

**Locație:** `1956-ai-summarize-podcast-episode-and-enhance-using-wikipedia`

- **Noduri:** 19
- **Conexiuni:** 14
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, Gmail, LangChain LLM, LangChain Sumarizare, OpenAI Chat, Parser Structurat, Text Splitter, Wikipedia Tool, documentJsonInputLoader

### 1957-force-ai-to-use-a-specific-output-format

> Se declanșează manual. folosește LangChain LLM, folosește Parser Structurat, folosește Parser Autofix, folosește OpenAI Chat. Detalii: Parser which defines the output format and which gets used to validate the output

**Locație:** `1957-force-ai-to-use-a-specific-output-format`

- **Noduri:** 11
- **Conexiuni:** 6
- **Declanșare:** 👆 Manual
- **Integrări:** LangChain LLM, OpenAI Chat, Parser Autofix, Parser Structurat

### 1961-slack-chatbot-powered-by-ai

> Se declanșează prin webhook HTTP. folosește Webhook, folosește Slack, folosește OpenAI Chat, folosește Buffer Memory (+3 altele). Detalii: Slack POSTs to Webhook on every message so we need to filter-out bot messages

**Locație:** `1961-slack-chatbot-powered-by-ai`

- **Noduri:** 14
- **Conexiuni:** 7
- **Declanșare:** 🌐 Webhook
- **Integrări:** AI Agent, Buffer Memory, OpenAI Chat, SerpAPI Tool, Slack, Webhook, Wikipedia Tool

### 1966-itemmatching-usage-example

> Se declanșează manual. folosește n8nTrainingCustomerDatastore. Detalii: About this workflow

This workflow provides a simple example of how to use `itemMatching(itemIndex: Number)` in the Code node to retrieve linked items from earlier in the workflow.

This example uses JavaScript. Refer to [Retrieve linked items from...

**Locație:** `1966-itemmatching-usage-example`

- **Noduri:** 8
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** n8nTrainingCustomerDatastore

### 1997-authenticate-a-user-in-a-workflow-with-openid-connect

> Se declanșează prin webhook HTTP. folosește Webhook, folosește HTTP API, folosește Răspuns Webhook, folosește HTML. Detalii: Quick setup with Keycloak
1. Open your Keycloak
2. Go to `Realm settings` and opn `OpenID Endpoint Configuration`
3. This will opene a new tab. Copy out the `authorization_endpoint`, `token_endpoint` and the `userinfo_endpoint` and add it to the...

**Locație:** `1997-authenticate-a-user-in-a-workflow-with-openid-connect`

- **Noduri:** 15
- **Conexiuni:** 10
- **Declanșare:** 🌐 Webhook
- **Integrări:** HTML, HTTP API, Răspuns Webhook, Webhook

### 1999-de-activate-n8n-workflows-using-telegram-commands

> Se declanșează la primirea unui mesaj Telegram. folosește n8n Sub-workflow, folosește n8n Sub-workflow. Detalii: Telegram N8N workflow (de)activator

 What does it do?
This workflow helps you to quickly activate or deactivate a workflow through Telegram. Sometimes we are not able to access a PC to resolve an issue if something goes wrong with a workflow. If...

**Locație:** `1999-de-activate-n8n-workflows-using-telegram-commands`

- **Noduri:** 12
- **Conexiuni:** 5
- **Integrări:** n8n Sub-workflow

### 2007-telegram-echo-bot

> Se declanșează la primirea unui mesaj Telegram. folosește Telegram. Detalii: This is a workflow for a Telegram-echo bot
1. Add your Telegram bot credentials for both nodes
2. Activate the workflow
3. Send something to the bot (i.e. a message, a forwarded message, sticker, emoji, voice, file, an image...)
4. Second node will...

**Locație:** `2007-telegram-echo-bot`

- **Noduri:** 3
- **Conexiuni:** 1
- **Integrări:** Telegram

### 2036-domain-extractor

> Se declanșează de Execute Workflow Trigger. Detalii: Read Me

This node is designed to cleanse URLs and extract their domain names efficiently. 

It effectively handles a wide range of URL formats, including those with unconventional or complex top-level domains (TLDs), such as 'co.uk'.

You can also...

**Locație:** `2036-domain-extractor`

- **Noduri:** 4
- **Conexiuni:** 2

### 2038-bookmarking-urls-in-your-browser-and-save-them-to-notion

> Se declanșează prin webhook HTTP. folosește Webhook, folosește Notion. Detalii: Adding data to notion
Go to your notion database and add a new database that shall be recording all your bookmarks. Make sure to add your application. (If you do not add this your bookmark wont be saved)

Test the webhook with to see how the urls...

**Locație:** `2038-bookmarking-urls-in-your-browser-and-save-them-to-notion`

- **Noduri:** 4
- **Conexiuni:** 1
- **Declanșare:** 🌐 Webhook
- **Integrări:** Notion, Webhook

### 2070-airtable-automate-recurring-tasks

> Se declanșează de airtableTrigger. obține date din Airtable, folosește HTTP API, folosește Slack. Detalii: Setup Checklist

1. Go to the Airtable Template and copy the latest version of the base
2. Go to the `Automate` table and open the view `First Task - Create Task`. From here, copy the BaseId, TableId and ViewId into the trigger. Make that the field...

**Locație:** `2070-airtable-automate-recurring-tasks`

- **Noduri:** 14
- **Conexiuni:** 9
- **Integrări:** Airtable, HTTP API, Slack

### 2071-upload-bulk-records-from-csv-airtable-interfaces

> Se declanșează de airtableTrigger. obține date din Airtable, folosește HTTP API, folosește Fișier Spreadsheet. Detalii: Setup Checklist

 1.Go to the Airtable Template and copy the latest version of the base
 
 2. From your new Airtable base URL, get and replace your base and tables id's into this workflow's trigger node.
 3. Input your Airtable Id's in the second...

**Locație:** `2071-upload-bulk-records-from-csv-airtable-interfaces`

- **Noduri:** 17
- **Conexiuni:** 10
- **Integrări:** Airtable, Fișier Spreadsheet, HTTP API

### 2073-monday-com-useful-utilities

> Se declanșează manual. obține date din Monday.com, folosește HTTP API, folosește Conversie Fișier.

**Locație:** `2073-monday-com-useful-utilities`

- **Noduri:** 14
- **Conexiuni:** 9
- **Declanșare:** 👆 Manual
- **Integrări:** Conversie Fișier, HTTP API, Monday.com

### 2074-send-n8n-automation-errors-to-a-monday-com-board

> Se declanșează de Error Trigger. folosește Monday.com, folosește Date/Time, folosește Monday.com.

**Locație:** `2074-send-n8n-automation-errors-to-a-monday-com-board`

- **Noduri:** 5
- **Conexiuni:** 4
- **Integrări:** Date/Time, Monday.com

### 2086-retrieve-a-monday-com-row-and-all-data-in-a-single-node

> Se declanșează de Execute Workflow Trigger. obține date din Monday.com, folosește Sub-workflow. Detalii: HOW TO USE
-Copy these nodes into another workflow, and update the workflow id in the execute workflow node
-Using the Edit Fields nodes, define the “pulse” variable which will tell the workflow which monday item to pull data from.

**Locație:** `2086-retrieve-a-monday-com-row-and-all-data-in-a-single-node`

- **Noduri:** 26
- **Conexiuni:** 19
- **Integrări:** Monday.com, Sub-workflow

### 2105-get-all-members-of-a-discord-server-with-a-specific-role

> Se declanșează manual. șterge date din Google Sheets, adaugă date în Google Sheets, folosește Google Sheets, folosește Discord (+2 altele). Detalii: Setup
1. Add your Google Sheets and Discord credentials.
2. Create a Google Sheets document that contains `ID` as a column. We're using this to remember which member we received last.
3. Edit the fields in the setup node `Setup: Edit this to get...

**Locație:** `2105-get-all-members-of-a-discord-server-with-a-specific-role`

- **Noduri:** 16
- **Conexiuni:** 12
- **Declanșare:** 🌐 Webhook, 👆 Manual
- **Integrări:** Discord, Google Sheets, Răspuns Webhook, Webhook

### 2138-create-linear-tickets-from-notion-content

> Se declanșează la trimiterea unui formular n8n. folosește GraphQL, citește date din Notion, folosește linear, folosește HTTP API (+2 altele). Detalii: Try me out
1. In the form trigger node, enter the names of your Linear team(s) to display on the form 
2. Make sure your Notion page is formatted according to the...

**Locație:** `2138-create-linear-tickets-from-notion-content`

- **Noduri:** 24
- **Conexiuni:** 17
- **Declanșare:** 🌐 Webhook
- **Integrări:** GraphQL, HTTP API, Notion, OpenAI, Răspuns Webhook, linear

### 2140-add-product-ideas-to-notion-via-a-slack-command

> Se declanșează prin webhook HTTP. folosește Webhook, folosește Notion, folosește HTTP API. Detalii: Needed pre-work: Add a Slack App
1. Visit https://api.slack.com/apps, click on `New App` and choose a name and workspace.
2. Click on `OAuth & Permissions` and scroll down to Scopes -> Bot token Scopes
3. Add the `chat:write` scope
4. Head over to...

**Locație:** `2140-add-product-ideas-to-notion-via-a-slack-command`

- **Noduri:** 8
- **Conexiuni:** 3
- **Declanșare:** 🌐 Webhook
- **Integrări:** HTTP API, Notion, Webhook

### 2150-report-n8n-workflow-errors-to-slack

> Se declanșează de On Error. folosește Slack. Detalii: 👨‍🎤 Setup
1. Add Slack creds
2. Add this error workflow to other workflows
https://docs.n8n.io/flow-logic/error-handling/create-and-set-an-error-workflow

**Locație:** `2150-report-n8n-workflow-errors-to-slack`

- **Noduri:** 5
- **Conexiuni:** 2
- **Integrări:** Slack

### 2153-add-a-bug-to-linear-via-slack-command

> Se declanșează prin webhook HTTP. folosește Webhook, folosește HTTP API. Detalii: Needed pre-work: Add a Slack App
1. Visit https://api.slack.com/apps, click on `New App` and choose a name and workspace.
2. Click on `OAuth & Permissions` and scroll down to Scopes -> Bot token Scopes
3. Add the `chat:write` scope
4. Head over to...

**Locație:** `2153-add-a-bug-to-linear-via-slack-command`

- **Noduri:** 10
- **Conexiuni:** 4
- **Declanșare:** 🌐 Webhook
- **Integrări:** HTTP API, Webhook

### 2154-classify-new-bugs-in-linear-with-openai-s-gpt-4-and-move-them-to-the-right-team

> Se declanșează de linearTrigger. actualizează date în linear, folosește HTTP API, folosește Slack, folosește OpenAI. Detalii: Setup
1. Add your Linear and OpenAi credentials
2. Change the team in the `Linear Trigger` to match your needs
3. Customize your teams and their areas of responsibility in the `Set me up` node. Please use the format `[Teamname][Description/Areas of...

**Locație:** `2154-classify-new-bugs-in-linear-with-openai-s-gpt-4-and-move-them-to-the-right-team`

- **Noduri:** 12
- **Conexiuni:** 8
- **Integrări:** HTTP API, OpenAI, Slack, linear

### 2157-advanced-slackbot-with-n8n

> Se declanșează prin webhook HTTP. folosește Slack, folosește HTTP API, folosește Sub-workflow, folosește Webhook (+2 altele). Detalii: 👨‍🎤 Setup
1. Add Slack command and point it up to the webhook
2. Add the following to the **Set config** node
- `alerts_channel` with alerts channel to start threads on
- `instance_url` with this instance url to make it easy to debug
- `slack_token`...

**Locație:** `2157-advanced-slackbot-with-n8n`

- **Noduri:** 34
- **Conexiuni:** 19
- **Declanșare:** 🌐 Webhook
- **Integrări:** HTTP API, PostgreSQL, Slack, Sub-workflow, Webhook

### 2159-report-n8n-workflow-errors-to-telegram

> Se declanșează de On Error. folosește Telegram. Detalii: 👨‍🎤 Setup
1. Add Telegram creds
2. Set chat id in **Telegram** node
2. Add this error workflow to other workflows
https://docs.n8n.io/flow-logic/error-handling/create-and-set-an-error-workflow

**Locație:** `2159-report-n8n-workflow-errors-to-telegram`

- **Noduri:** 5
- **Conexiuni:** 2
- **Integrări:** Telegram

### 2160-report-n8n-workflow-errors-directly-to-your-email

> Se declanșează de On Error. folosește Gmail. Detalii: 👨‍🎤 Setup
1. Add your Gmail creds
2. Add your target email
2. Add this error workflow to other workflows
https://docs.n8n.io/flow-logic/error-handling/create-and-set-an-error-workflow

**Locație:** `2160-report-n8n-workflow-errors-directly-to-your-email`

- **Noduri:** 4
- **Conexiuni:** 1
- **Integrări:** Gmail

### 2162-whatsapp-starter-workflow

> Se declanșează prin webhook HTTP. folosește Webhook, folosește Răspuns Webhook, trimite mesaje prin WhatsApp. Detalii: Main flow
* *Respond* webhook receives various POST Requests from Meta regarding WhatsApp messages (user messages + status notifications)
* Check if the incoming JSON contains user message
* Echo back the text message to the user. This is a custom...

**Locație:** `2162-whatsapp-starter-workflow`

- **Noduri:** 8
- **Conexiuni:** 3
- **Declanșare:** 🌐 Webhook
- **Integrări:** Răspuns Webhook, Webhook, WhatsApp

### 2167-chatgpt-automatic-code-review-in-gitlab-mr

> Se declanșează prin webhook HTTP. folosește Webhook, folosește OpenAI Chat, folosește HTTP API, folosește LangChain LLM. Detalii: Filter comments and customize your trigger words ⬇️

**Locație:** `2167-chatgpt-automatic-code-review-in-gitlab-mr`

- **Noduri:** 14
- **Conexiuni:** 9
- **Declanșare:** 🌐 Webhook
- **Integrări:** HTTP API, LangChain LLM, OpenAI Chat, Webhook

### 2192-streamline-your-zoom-meetings-with-secure-automated-stripe-payments

> Se declanșează la trimiterea unui formular n8n. folosește Zoom, folosește HTTP API, folosește Gmail, creează înregistrări în Google Sheets (+1 altele). Detalii: Setup
 1/ Add Your credentials
[Zoom](https://docs.n8n.io/integrations/builtin/credentials/zoom/)
[Google](https://docs.n8n.io/integrations/builtin/credentials/google/)
[Stripe](https://docs.n8n.io/integrations/builtin/credentials/stripe/)

Note:...

**Locație:** `2192-streamline-your-zoom-meetings-with-secure-automated-stripe-payments`

- **Noduri:** 20
- **Conexiuni:** 13
- **Integrări:** Gmail, Google Sheets, HTTP API, Zoom

### 2201-openai-assistant-workflow-upload-file-create-an-assistant-chat-with-it

> Se declanșează manual. descarcă din Google Drive, folosește OpenAI, creează înregistrări în OpenAI. Detalii: STEP 4. Expand the Assistant. Check the tutorials:

[Create a WhatsApp bot](https://blog.n8n.io/whatsapp-bot/)
[Create simple Telegram bot](https://blog.n8n.io/telegram-bots/)
[![Create a Telegram AI...

**Locație:** `2201-openai-assistant-workflow-upload-file-create-an-assistant-chat-with-it`

- **Noduri:** 10
- **Conexiuni:** 2
- **Declanșare:** 👆 Manual
- **Integrări:** Google Drive, OpenAI

### 2223-set-credentials-dynamically-using-expressions

> Se declanșează la trimiterea unui formular n8n. folosește nasa, folosește Răspuns Webhook. Detalii: This workflow shows how to set credentials dynamically using expressions.


First, set up your NASA credential: 

1. Create a new NASA credential.
1. Hover over **API Key**.
1. Toggle **Expression** on.
1. In the **API Key** field, enter `{{...

**Locație:** `2223-set-credentials-dynamically-using-expressions`

- **Noduri:** 7
- **Conexiuni:** 2
- **Declanșare:** 🌐 Webhook
- **Integrări:** Răspuns Webhook, nasa

### 2276-send-http-requests-to-a-list-of-urls

> Rulează programat (schedule). folosește HTTP API.

**Locație:** `2276-send-http-requests-to-a-list-of-urls`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** ⏰ Programat
- **Integrări:** HTTP API

### 2289-restore-backed-up-workflows-from-github-to-n8n

> Se declanșează manual. listează date din GitHub, folosește n8n Sub-workflow, obține date din GitHub, creează înregistrări în n8n Sub-workflow. Detalii: Workflow - Restore Backups
This workflow will restore backed-up workflows from Github. 
It is launch by testing the workflow

 Setup
Open Globals and update the values below
**repo.owner:** This is your Github username
**repo.name:** This is the...

**Locație:** `2289-restore-backed-up-workflows-from-github-to-n8n`

- **Noduri:** 17
- **Conexiuni:** 10
- **Declanșare:** 👆 Manual
- **Integrări:** GitHub, n8n Sub-workflow

### 2295-export-n8n-cloud-execution-data-to-csv

> Se declanșează manual. folosește n8n Sub-workflow, folosește Conversie Fișier. Detalii: Replace this node
**Replace this node with any cloud storage destination**

**Locație:** `2295-export-n8n-cloud-execution-data-to-csv`

- **Noduri:** 7
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** Conversie Fișier, n8n Sub-workflow

### 2312-attach-a-default-error-handler-to-all-active-workflows

> Se declanșează de Error Trigger. folosește n8n Sub-workflow, folosește Gmail, obține date din n8n Sub-workflow, actualizează date în n8n Sub-workflow. Detalii: Default Error Handler

Update this to your preferred notification mechanism

**Locație:** `2312-attach-a-default-error-handler-to-all-active-workflows`

- **Noduri:** 11
- **Conexiuni:** 6
- **Declanșare:** ⏰ Programat
- **Integrări:** Gmail, n8n Sub-workflow

### 2343-introduction-to-the-http-tool

> Se declanșează manual. folosește OpenAI Chat, folosește HTTP Tool, folosește AI Agent. Detalii: Try It Out!

 The HTTP tool is drastically simplifies API-enabled AI agents cutting down the number of workflow nodes by as much as 10!

* Available since v1.47.0
* Recommended for single purpose APIs which don't require much post-fetch...

**Locație:** `2343-introduction-to-the-http-tool`

- **Noduri:** 12
- **Conexiuni:** 7
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, HTTP Tool, OpenAI Chat

### 2348-get-multiple-attachments-from-gmail-and-upload-them-to-gdrive

> Se declanșează de Gmail Trigger. folosește Google Drive.

**Locație:** `2348-get-multiple-attachments-from-gmail-and-upload-them-to-gdrive`

- **Noduri:** 3
- **Conexiuni:** 2
- **Integrări:** Google Drive

### 2358-advanced-ai-demo-presented-at-ai-developers-14-meetup

> Se declanșează prin mesaj de chat. folosește Slack, folosește Text Splitter, folosește OpenAI Embeddings, folosește Document Loader (+12 altele). Detalii: ![h](https://i.imghippo.com/files/d9Bgv1721858679.pngfull-width)
[Open Calendar](https://calendar.google.com/calendar/u/0/r/day/2024/7/26)

**Locație:** `2358-advanced-ai-demo-presented-at-ai-developers-14-meetup`

- **Noduri:** 39
- **Conexiuni:** 19
- **Declanșare:** 🌐 Webhook
- **Integrări:** AI Agent, Anthropic Claude, Buffer Memory, Clasificator Text, Document Loader, Gmail, HTTP API, HTTP Tool, LangChain Retrieval QA, OpenAI Chat (+6 altele)

### 2379-validate-totp-token-without-creating-a-credential

> Se declanșează manual. Detalii: TOTP Validation with Function Node

This template allows you to verify if a 6-digit TOTP code is valid using the corresponding TOTP secret. It can be used in an authentication system.
 Example usage:
- You retrieve the user's TOTP secret from a...

**Locație:** `2379-validate-totp-token-without-creating-a-credential`

- **Noduri:** 5
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual

### 2395-supabase-insertion-upsertion-retrieval

> Se declanșează prin mesaj de chat. descarcă din Google Drive, folosește Document Loader, folosește LangChain Retrieval QA, folosește OpenAI Chat (+5 altele). Detalii: PREPARATION (in Supabase)

- your database needs the extension 'pgvector' enabled -> select Database > Extension > Search for 'vector'
- make sure you have a table that has the following columns (if not, use the query below in the Supabase SQL...

**Locație:** `2395-supabase-insertion-upsertion-retrieval`

- **Noduri:** 21
- **Conexiuni:** 12
- **Integrări:** Document Loader, Google Drive, LangChain Retrieval QA, OpenAI Chat, OpenAI Embeddings, Supabase, Supabase Vector, Text Splitter, Vector Retriever

### 2398-kb-tool-confluence-knowledge-base

> Se declanșează de Execute Workflow Trigger. folosește HTTP API. Detalii: ![n8n](https://i.imgur.com/qXWqiOd.png)
 Enhance Query Resolution with the Knowledge Base Tool!

Our **Knowledge Base Tool** is crafted to seamlessly integrate into the IT Department Q&A Workflow, enhancing the IT support process by enabling...

**Locație:** `2398-kb-tool-confluence-knowledge-base`

- **Noduri:** 7
- **Conexiuni:** 2
- **Integrări:** HTTP API

### 2400-ai-agent-with-charts-capabilities-using-openai-structured-output-and-quickchart

> Se declanșează de Execute "Generate a chart" tool. folosește OpenAI Chat, folosește Buffer Memory, folosește Sub-workflow Tool, folosește HTTP API (+1 altele). Detalii: Workflow: AI Agent with charts capabilities using OpenAI Structured Output

**Overview**
- This workflow is a experiment to integrate charts into an AI Agent
- The AI Agent has normal AI conversation and can invoke a tool to integrate a graph in the...

**Locație:** `2400-ai-agent-with-charts-capabilities-using-openai-structured-output-and-quickchart`

- **Noduri:** 11
- **Conexiuni:** 6
- **Integrări:** AI Agent, Buffer Memory, HTTP API, OpenAI Chat, Sub-workflow Tool

### 2406-telegram-user-registration-workflow

> Se declanșează de Trigger Start. folosește Google Sheets, folosește Telegram.

**Locație:** `2406-telegram-user-registration-workflow`

- **Noduri:** 15
- **Conexiuni:** 7
- **Integrări:** Google Sheets, Telegram

### 2408-user-verification-and-login-using-auth0

> Se declanșează prin webhook HTTP. folosește HTTP API, folosește Răspuns Webhook, folosește Webhook. Detalii: 1. First, go to https://auth0.com and create a Single Page Application. From Dashboard/Applications, click on your new app settings. The first step is to add the following to allowed callback URLs:
http://localhost:5678,...

**Locație:** `2408-user-verification-and-login-using-auth0`

- **Noduri:** 16
- **Conexiuni:** 6
- **Declanșare:** 🌐 Webhook
- **Integrări:** HTTP API, Răspuns Webhook, Webhook

### 2417-flux-ai-image-generator

> Se declanșează la trimiterea unui formular n8n. folosește Răspuns Webhook, încarcă fișiere în s3, folosește HTTP API. Detalii: Run flux model
In `Call huggingface inference api` You can change `black-forest-labs/FLUX.1-schnell` in URL parameter to other models:
- `black-forest-labs/FLUX.1-dev`
- `Shakker-Labs/FLUX.1-dev-LoRA-AntiBlur`
- `XLabs-AI/flux-RealismLora`
-...

**Locație:** `2417-flux-ai-image-generator`

- **Noduri:** 19
- **Conexiuni:** 10
- **Declanșare:** 🌐 Webhook
- **Integrări:** HTTP API, Răspuns Webhook, s3

### 2418-easy-image-captioning-with-gemini-1-5-pro

> Se declanșează manual. folosește Google Gemini, folosește Parser Structurat, folosește Editor Imagine, folosește Editor Imagine (+3 altele). Detalii: 2. Using Vision Model to Generate Caption
[Learn more about the Basic LLM Chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm)

n8n's basic LLM node supports multimodal input by allowing you to...

**Locație:** `2418-easy-image-captioning-with-gemini-1-5-pro`

- **Noduri:** 16
- **Conexiuni:** 10
- **Declanșare:** 👆 Manual
- **Integrări:** Editor Imagine, Google Gemini, HTTP API, LangChain LLM, Parser Structurat

### 2420-automate-image-validation-tasks-using-ai-vision

> Se declanșează manual. folosește Parser Structurat, descarcă din Google Drive, folosește Editor Imagine, folosește LangChain LLM (+1 altele). Detalii: 2. Verify Passport Photo Validity Using AI Vision Model
[Learn more about Basic LLM Chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm)

Verifying if a photo is suitable for a passport photo is a...

**Locație:** `2420-automate-image-validation-tasks-using-ai-vision`

- **Noduri:** 11
- **Conexiuni:** 7
- **Declanșare:** 👆 Manual
- **Integrări:** Editor Imagine, Google Drive, Google Gemini, LangChain LLM, Parser Structurat

### 2436-siri-ai-agent-apple-shortcuts-powered-voice-template

> Se declanșează prin webhook HTTP. folosește OpenAI Chat, folosește Răspuns Webhook, folosește AI Agent, folosește Webhook. Detalii: ![Siri Template Thumbnail](https://uploads.n8n.io/devrel/wf-siri-header.pngfull-width)
 "Hey Siri, Ask Agent" workflow
**Made by [Max Tkacz](https://www.linkedin.com/in/maxtkacz) during the [30 Day AI...

**Locație:** `2436-siri-ai-agent-apple-shortcuts-powered-voice-template`

- **Noduri:** 7
- **Conexiuni:** 3
- **Declanșare:** 🌐 Webhook
- **Integrări:** AI Agent, OpenAI Chat, Răspuns Webhook, Webhook

### 2456-text-automations-using-apple-shortcuts

> Se declanșează prin webhook HTTP. folosește Răspuns Webhook, folosește Webhook, folosește OpenAI. Detalii: Workflow: Text automations using Apple Shortcuts

**Overview**
- This workflow answers user requests sent via Apple Shortcuts
- Several Shortcuts call the same webhook, with a query and a type of query
- Types of query are:
  - translate to english
...

**Locație:** `2456-text-automations-using-apple-shortcuts`

- **Noduri:** 10
- **Conexiuni:** 7
- **Declanșare:** 🌐 Webhook
- **Integrări:** OpenAI, Răspuns Webhook, Webhook

### 2467-narrating-over-a-video-using-multimodal-ai

> Se declanșează manual. folosește OpenAI Chat, folosește HTTP API, folosește Conversie Fișier, folosește Google Drive (+3 altele). Detalii: Try It Out!

 This n8n template takes a video and extracts frames from it which are used with a multimodal LLM to generate a script. The script is then passed to the same multimodal LLM to generate a voiceover clip.

This template was inspired by...

**Locație:** `2467-narrating-over-a-video-using-multimodal-ai`

- **Noduri:** 21
- **Conexiuni:** 13
- **Declanșare:** 👆 Manual
- **Integrări:** Conversie Fișier, Editor Imagine, Google Drive, HTTP API, LangChain LLM, OpenAI, OpenAI Chat

### 2473-generate-seo-seed-keywords-using-ai

> Se declanșează manual. folosește Anthropic Claude, folosește AI Agent. Detalii: Generate SEO Seed Keywords Using AI

This flow uses an AI node to generate Seed Keywords to focus SEO efforts on based on your ideal customer profile

**Outputs:** 
- List of 20 Seed Keywords


**Pre-requisites / Dependencies:**
- You know your...

**Locație:** `2473-generate-seo-seed-keywords-using-ai`

- **Noduri:** 15
- **Conexiuni:** 6
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, Anthropic Claude

### 2485-automate-droplet-snapshots-on-digitalocean

> Rulează programat (cron). folosește HTTP API. Detalii: What this workflow does
1. **`Runs every 48 hours`**: The workflow is triggered by a cron node that runs every 48 hours, ensuring timely snapshot management.
2. **`List all droplets`**: The workflow retrieves all droplets in the DigitalOcean...

**Locație:** `2485-automate-droplet-snapshots-on-digitalocean`

- **Noduri:** 17
- **Conexiuni:** 5
- **Declanșare:** ⏰ Programat
- **Integrări:** HTTP API

### 2490-build-an-endpoint-to-perform-crud-operations-with-multiple-http-methods

> Se declanșează prin webhook HTTP. folosește Răspuns Webhook, creează înregistrări în Airtable, caută în Airtable, actualizează date în Airtable (+2 altele). Detalii: Update
Updates of an existing record

**Locație:** `2490-build-an-endpoint-to-perform-crud-operations-with-multiple-http-methods`

- **Noduri:** 18
- **Conexiuni:** 8
- **Declanșare:** 🌐 Webhook
- **Integrări:** Airtable, Răspuns Webhook, Webhook

### 2504-wordpress-ai-chatbot-to-enhance-user-experience-with-supabase-and-openai

> Se declanșează manual. folosește OpenAI Embeddings, folosește Document Loader, folosește textSplitterTokenSplitter, folosește OpenAI Chat (+10 altele). Detalii: Workflow 3 : Use this workflow to enable chat functionality with your website content. The chat can be embedded into your website to enhance user experience

**Locație:** `2504-wordpress-ai-chatbot-to-enhance-user-experience-with-supabase-and-openai`

- **Noduri:** 53
- **Conexiuni:** 41
- **Declanșare:** 🌐 Webhook, ⏰ Programat, 👆 Manual
- **Integrări:** AI Agent, Document Loader, HTTP API, Markdown, OpenAI Chat, OpenAI Embeddings, PostgreSQL, PostgreSQL Memory, Răspuns Webhook, Supabase (+3 altele)

### 2508-generate-sql-queries-from-schema-only-ai-powered

> Se declanșează prin mesaj de chat. folosește OpenAI Chat, folosește Buffer Memory, folosește mySql, folosește Conversie Fișier (+4 altele). Detalii: LangChain AI Agent's system prompt is modified.
It uses only the database schema to generate SQL queries. The agent creates these queries but does not execute them. Instead, it passes them to subsequent nodes.

**Example:**
"Can you show me the list...

**Locație:** `2508-generate-sql-queries-from-schema-only-ai-powered`

- **Noduri:** 29
- **Conexiuni:** 17
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, Buffer Memory, Conversie Fișier, Extracție Fișier, Fișier Local, OpenAI Chat, mySql

### 2527-sharepoint-list-fetch-with-oauth-token

> Rulează programat (schedule). folosește HTTP API. Detalii: Never expose or hard code below values 
**tenant_id,client_id,client_secret** 

Always save these either in secure vault like hashicorp or GCP Secret Manager.

**Locație:** `2527-sharepoint-list-fetch-with-oauth-token`

- **Noduri:** 5
- **Conexiuni:** 3
- **Declanșare:** ⏰ Programat
- **Integrări:** HTTP API

### 2535-get-long-lived-facebook-user-or-page-access-token

> Se declanșează manual. folosește HTTP API. Detalii: Set Required Facebook Parameter 
- client_id
- client_secret
- user_access_token
- app-scoped-user-id (optional)

 according to this doc
 https://developers.facebook.com/docs/facebook-login/guides/access-tokens/get-long-lived/

**Locație:** `2535-get-long-lived-facebook-user-or-page-access-token`

- **Noduri:** 5
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** HTTP API

### 2536-pattern-for-parallel-sub-workflow-execution-followed-by-wait-for-all-loop

> Se declanșează manual. folosește HTTP API, folosește Răspuns Webhook, folosește Webhook. Detalii: Start Multiple Sub-Workflows Asynchronously
* Note: Callback/Webhook "internal" Base-URL should be configured in the n8n instance to reference the k8s service name and internal port.

**Locație:** `2536-pattern-for-parallel-sub-workflow-execution-followed-by-wait-for-all-loop`

- **Noduri:** 18
- **Conexiuni:** 12
- **Declanșare:** 🌐 Webhook, 👆 Manual
- **Integrări:** HTTP API, Răspuns Webhook, Webhook

### 2538-demo-workflow-how-to-use-workflowstaticdata

> Se declanșează prin webhook HTTP. folosește Webhook, folosește HTTP API. Detalii: StaticData Demo


This workflow demonstrates how to use the [`workflowStaticData()` function](https://docs.n8n.io/code/cookbook/builtin/get-workflow-static-data/
) to set any type of variable that will persist within workflow executions. 

This can...

**Locație:** `2538-demo-workflow-how-to-use-workflowstaticdata`

- **Noduri:** 9
- **Conexiuni:** 6
- **Declanșare:** 🌐 Webhook, ⏰ Programat
- **Integrări:** HTTP API, Webhook

### 2551-add-new-clients-from-notion-to-clockify

> Se declanșează de notionTrigger. folosește Clockify. Detalii: Clockify
 Add new client
**To-dos**:
1. Connect your Clockify account
2. Select your Clockify workspace
3. Map your Notion client name column to the Clockify "Client Name" field

**Locație:** `2551-add-new-clients-from-notion-to-clockify`

- **Noduri:** 4
- **Conexiuni:** 2
- **Integrări:** Clockify

### 2559-visualize-your-sql-agent-queries-with-openai-and-quickchart-io

> Se declanșează de Execute "Generate a chart" tool. folosește OpenAI Chat, folosește Sub-workflow, folosește HTTP API, folosește AI Agent (+2 altele). Detalii: Workflow: SQL Agent with visualisation skills

**Overview**
- This workflow aims at providing data visualization to a native SQL Agent.
- Together, they can help with fostering data analysis and data visualization within a team.
- It uses the native...

**Locație:** `2559-visualize-your-sql-agent-queries-with-openai-and-quickchart-io`

- **Noduri:** 16
- **Conexiuni:** 9
- **Integrări:** AI Agent, Buffer Memory, Clasificator Text, HTTP API, OpenAI Chat, Sub-workflow

### 2566-conversational-interviews-with-ai-agents-and-n8n-forms

> Se declanșează la trimiterea unui formular n8n. folosește Chat Memory, folosește form, folosește Crypto, folosește Redis (+10 altele). Detalii: Try it out! 

 Conducting user interviews have been traditionally difficult due to preparation, timing and execution costs. What if we let an AI/LLM do it instead?

This template enables automated AI/LLM powered user interviews using n8n forms and...

**Locație:** `2566-conversational-interviews-with-ai-agents-and-n8n-forms`

- **Noduri:** 40
- **Conexiuni:** 28
- **Declanșare:** 🌐 Webhook
- **Integrări:** AI Agent, Buffer Memory, Chat Memory, Crypto, Google Sheets, Groq, HTML, Redis, Răspuns Webhook, Webhook (+1 altele)

### 2576-import-productboard-notes-companies-and-features-into-snowflake

> Rulează zilnic la ora 8:00. folosește HTTP API, folosește snowflake, folosește snowflake, folosește Slack. Detalii: Preview Slack Message
:productboard: Weekly Update in :snowflake_logo: Completed
27 new insights added in the last 7 days.
88 insights remain unprocessed.
You can view the updated :metabase: dashboard below:
<link metabase>

**Locație:** `2576-import-productboard-notes-companies-and-features-into-snowflake`

- **Noduri:** 35
- **Conexiuni:** 28
- **Declanșare:** ⏰ Programat
- **Integrări:** HTTP API, Slack, snowflake

### 2604-time-logging-on-clockify-using-slack

> Se declanșează de slackTrigger. folosește OpenAI Chat, folosește Calculator, folosește HTTP Tool, folosește Cod Personalizat (+4 altele).

**Locație:** `2604-time-logging-on-clockify-using-slack`

- **Noduri:** 16
- **Conexiuni:** 14
- **Integrări:** AI Agent, Buffer Memory, Calculator, Cod Personalizat, HTTP Tool, OpenAI Chat, Slack, executionData

### 2612-ai-agent-to-chat-with-supabase-postgresql-db

> Se declanșează prin mesaj de chat. folosește Cod Personalizat, folosește OpenAI Chat, folosește postgresTool, folosește AI Agent. Detalii: ![5min Logo](https://cflobdhpqwnoisuctsoc.supabase.co/storage/v1/object/public/my_storage/banner.png)
 AI Agent to chat with Supabase/PostgreSQL DB
**Made by [Mark Shcherbakov](https://www.linkedin.com/in/marklowcoding/) from community...

**Locație:** `2612-ai-agent-to-chat-with-supabase-postgresql-db`

- **Noduri:** 11
- **Conexiuni:** 5
- **Integrări:** AI Agent, Cod Personalizat, OpenAI Chat, postgresTool

### 2649-prompt-based-object-detection-with-gemini-2-0

> Se declanșează manual. folosește HTTP API, folosește Editor Imagine, folosește Editor Imagine. Detalii: Try it out!
 This n8n template demonstrates how to use Gemini 2.0's new Bounding Box detection capabilities your workflows.

The key difference being this enables prompt-based object detection for images which is pretty powerful for things like...

**Locație:** `2649-prompt-based-object-detection-with-gemini-2-0`

- **Noduri:** 14
- **Conexiuni:** 7
- **Declanșare:** 👆 Manual
- **Integrări:** Editor Imagine, HTTP API

### 2653-ai-data-analyst-agent-for-spreadsheets-with-nocodb

> Se declanșează prin mesaj de chat. folosește Buffer Memory, citește date din nocoDbTool, folosește HTTP API, folosește AI Agent (+1 altele). Detalii: Start here: Step-by Step Youtube Tutorial :star:

[![Multi-Agent Research team ](https://img.youtube.com/vi/eScD4Y7nRBQ/sddefault.jpg)](https://youtu.be/eScD4Y7nRBQ)

**Locație:** `2653-ai-data-analyst-agent-for-spreadsheets-with-nocodb`

- **Noduri:** 10
- **Conexiuni:** 7
- **Integrări:** AI Agent, Buffer Memory, HTTP API, OpenAI Chat, nocoDbTool

### 3-write-http-query-string-on-image

> Se declanșează prin webhook HTTP. folosește Webhook, folosește Editor Imagine, folosește HTTP API.

**Locație:** `3-write-http-query-string-on-image`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** 🌐 Webhook
- **Integrări:** Editor Imagine, HTTP API, Webhook

### 359-sample-error-workflow

> Se declanșează de Error Trigger. folosește Twilio, folosește Mattermost.

**Locație:** `359-sample-error-workflow`

- **Noduri:** 3
- **Conexiuni:** 2
- **Integrări:** Mattermost, Twilio

### 371-notify-a-team-channel-about-new-software-releases-via-slack-and-github

> Se declanșează de githubTrigger. folosește Slack.

**Locație:** `371-notify-a-team-channel-about-new-software-releases-via-slack-and-github`

- **Noduri:** 2
- **Conexiuni:** 1
- **Integrări:** Slack

### 385-send-airtable-data-as-tasks-to-trello

> Se declanșează manual. listează date din Airtable, folosește bannerbear, folosește Trello.

**Locație:** `385-send-airtable-data-as-tasks-to-trello`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** Airtable, Trello, bannerbear

### 4-send-selected-github-events-to-slack

> Se declanșează de githubTrigger. folosește Slack.

**Locație:** `4-send-selected-github-events-to-slack`

- **Noduri:** 4
- **Conexiuni:** 2
- **Integrări:** Slack

### 434-extract-post-titles-from-a-blog

> Se declanșează manual. folosește HTTP API, folosește htmlExtract.

**Locație:** `434-extract-post-titles-from-a-blog`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** HTTP API, htmlExtract

### 437-perform-speech-to-text-on-recorded-audio-clips-using-wit-ai

> Declanșare manuală sau nedeterminată. folosește readBinaryFile, folosește HTTP API.

**Locație:** `437-perform-speech-to-text-on-recorded-audio-clips-using-wit-ai`

- **Noduri:** 2
- **Conexiuni:** 1
- **Integrări:** HTTP API, readBinaryFile

### 442-create-a-url-on-bitly

> Se declanșează manual. folosește bitly.

**Locație:** `442-create-a-url-on-bitly`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** bitly

### 445-send-a-tweet-to-twitter

> Se declanșează manual. folosește Twitter/X.

**Locație:** `445-send-a-tweet-to-twitter`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** Twitter/X

### 454-get-a-pipeline-in-circleci

> Se declanșează manual. folosește circleCi.

**Locație:** `454-get-a-pipeline-in-circleci`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** circleCi

### 458-run-a-sql-query-on-postgres

> Se declanșează manual. folosește PostgreSQL.

**Locație:** `458-run-a-sql-query-on-postgres`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** PostgreSQL

### 459-create-a-new-issue-in-jira

> Se declanșează manual. folosește Jira.

**Locație:** `459-create-a-new-issue-in-jira`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** Jira

### 461-create-a-new-card-in-trello

> Se declanșează manual. folosește Trello.

**Locație:** `461-create-a-new-card-in-trello`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** Trello

### 465-get-details-of-a-gitlab-repository

> Se declanșează manual. obține date din GitLab.

**Locație:** `465-get-details-of-a-gitlab-repository`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** GitLab

### 479-execute-an-sql-query-in-microsoft-sql

> Se declanșează manual. folosește Microsoft SQL.

**Locație:** `479-execute-an-sql-query-in-microsoft-sql`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** Microsoft SQL

### 482-insert-data-into-a-new-row-for-a-table-in-coda

> Se declanșează manual. folosește coda.

**Locație:** `482-insert-data-into-a-new-row-for-a-table-in-coda`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** 👆 Manual
- **Integrări:** coda

### 485-create-a-task-in-clickup

> Se declanșează manual. folosește ClickUp.

**Locație:** `485-create-a-task-in-clickup`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** ClickUp

### 487-receive-updates-for-events-in-clickup

> Se declanșează de clickUpTrigger.

**Locație:** `487-receive-updates-for-events-in-clickup`

- **Noduri:** 1
- **Conexiuni:** 0

### 495-track-an-event-in-segment

> Se declanșează manual. folosește segment.

**Locație:** `495-track-an-event-in-segment`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** segment

### 510-invoke-an-aws-lambda-function

> Se declanșează manual. folosește AWS Lambda.

**Locație:** `510-invoke-an-aws-lambda-function`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** AWS Lambda

### 518-get-entries-from-a-cockpit-collection

> Se declanșează manual. folosește cockpit.

**Locație:** `518-get-entries-from-a-cockpit-collection`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** cockpit

### 524-get-today-s-date-and-day-using-the-function-node

> Se declanșează manual.

**Locație:** `524-get-today-s-date-and-day-using-the-function-node`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual

### 525-get-articles-from-hacker-news

> Se declanșează manual. folosește hackerNews.

**Locație:** `525-get-articles-from-hacker-news`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** hackerNews

### 526-assign-values-to-variables-using-the-set-node

> Se declanșează manual.

**Locație:** `526-assign-values-to-variables-using-the-set-node`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual

### 527-receive-updates-for-github-events

> Se declanșează de githubTrigger.

**Locație:** `527-receive-updates-for-github-events`

- **Noduri:** 1
- **Conexiuni:** 0

### 528-receive-updates-for-gitlab-events

> Se declanșează de gitlabTrigger.

**Locație:** `528-receive-updates-for-gitlab-events`

- **Noduri:** 1
- **Conexiuni:** 0

### 529-receive-updates-for-bitbucket-events

> Se declanșează de bitbucketTrigger.

**Locație:** `529-receive-updates-for-bitbucket-events`

- **Noduri:** 1
- **Conexiuni:** 0

### 544-create-an-image-procedurally-using-bannerbear

> Se declanșează manual. folosește bannerbear.

**Locație:** `544-create-an-image-procedurally-using-bannerbear`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** bannerbear

### 546-get-all-posts-from-wordpress

> Se declanșează manual. citește date din WordPress.

**Locație:** `546-get-all-posts-from-wordpress`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** WordPress

### 548-get-all-orders-in-shopify

> Se declanșează manual. citește date din Shopify.

**Locație:** `548-get-all-orders-in-shopify`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** Shopify

### 556-get-a-board-from-monday-com

> Se declanșează manual. obține date din Monday.com.

**Locație:** `556-get-a-board-from-monday-com`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** Monday.com

### 557-get-the-value-of-a-key-from-redis

> Se declanșează manual. obține date din Redis.

**Locație:** `557-get-the-value-of-a-key-from-redis`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** Redis

### 559-create-a-new-folder-in-box

> Se declanșează manual. folosește Box.

**Locație:** `559-create-a-new-folder-in-box`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** Box

### 563-get-contributors-information-from-github-in-slack

> Se declanșează prin webhook HTTP. folosește Webhook, folosește GraphQL, folosește Slack.

**Locație:** `563-get-contributors-information-from-github-in-slack`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** 🌐 Webhook
- **Integrări:** GraphQL, Slack, Webhook

### 565-create-a-folder-in-onedrive

> Se declanșează manual. creează înregistrări în microsoftOneDrive.

**Locație:** `565-create-a-folder-in-onedrive`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** microsoftOneDrive

### 574-encrypt-some-data-using-the-crypto-node

> Se declanșează manual. folosește Crypto.

**Locație:** `574-encrypt-some-data-using-the-crypto-node`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** Crypto

### 576-get-information-of-an-image

> Se declanșează manual. folosește Editor Imagine, folosește HTTP API.

**Locație:** `576-get-information-of-an-image`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** 👆 Manual
- **Integrări:** Editor Imagine, HTTP API

### 581-execute-set-node-based-on-function-output

> Se declanșează manual.

**Locație:** `581-execute-set-node-based-on-function-output`

- **Noduri:** 5
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual

### 582-rename-a-key-in-n8n

> Se declanșează manual.

**Locație:** `582-rename-a-key-in-n8n`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** 👆 Manual

### 583-read-an-rss-feed

> Se declanșează manual. folosește rssFeedRead.

**Locație:** `583-read-an-rss-feed`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** rssFeedRead

### 588-execute-another-workflow

> Se declanșează manual. folosește Sub-workflow.

**Locație:** `588-execute-another-workflow`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** Sub-workflow

### 592-create-a-table-in-quest-db-and-insert-data

> Se declanșează manual. folosește questDb, folosește questDb.

**Locație:** `592-create-a-table-in-quest-db-and-insert-data`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** questDb

### 597-create-a-table-in-cratedb-and-insert-data

> Se declanșează manual. folosește crateDb, folosește crateDb.

**Locație:** `597-create-a-table-in-cratedb-and-insert-data`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** crateDb

### 598-create-a-table-in-mysql-and-insert-data

> Se declanșează manual. folosește mySql, folosește mySql.

**Locație:** `598-create-a-table-in-mysql-and-insert-data`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** mySql

### 599-create-a-table-in-postgres-and-insert-data

> Se declanșează manual. folosește PostgreSQL, folosește PostgreSQL.

**Locație:** `599-create-a-table-in-postgres-and-insert-data`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** PostgreSQL

### 602-manage-users-automatically-in-reqres-in

> Se declanșează manual. folosește HTTP API.

**Locație:** `602-manage-users-automatically-in-reqres-in`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** HTTP API

### 632-nathan-your-n8n-personal-assistant

> Se declanșează la primirea unui email. folosește Email IMAP, folosește readBinaryFile, folosește Fișier Spreadsheet, folosește Email SMTP (+1 altele).

**Locație:** `632-nathan-your-n8n-personal-assistant`

- **Noduri:** 9
- **Conexiuni:** 6
- **Integrări:** Email IMAP, Email SMTP, Fișier Spreadsheet, Slack, readBinaryFile

### 635-export-wordpress-posts-to-spreadsheet

> Se declanșează manual. citește date din WordPress, folosește Fișier Spreadsheet, folosește writeBinaryFile.

**Locație:** `635-export-wordpress-posts-to-spreadsheet`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** Fișier Spreadsheet, WordPress, writeBinaryFile

### 639-receive-server-sent-events

> Se declanșează de sseTrigger.

**Locație:** `639-receive-server-sent-events`

- **Noduri:** 1
- **Conexiuni:** 0

### 640-get-all-the-entries-from-contentful

> Se declanșează manual. citește date din Contentful.

**Locație:** `640-get-all-the-entries-from-contentful`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** Contentful

### 643-get-all-releases-in-sentry

> Se declanșează manual. creează înregistrări în sentryIo, citește date din sentryIo.

**Locație:** `643-get-all-releases-in-sentry`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** 👆 Manual
- **Integrări:** sentryIo

### 655-merge-greetings-with-the-users-based-on-the-language

> Se declanșează manual.

**Locație:** `655-merge-greetings-with-the-users-based-on-the-language`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual

### 658-trigger-a-build-using-the-travisci-node

> Se declanșează manual. folosește travisCi.

**Locație:** `658-trigger-a-build-using-the-travisci-node`

- **Noduri:** 2
- **Conexiuni:** 2
- **Declanșare:** 👆 Manual
- **Integrări:** travisCi

### 667-send-an-sms-using-the-mocean-node

> Se declanșează manual. folosește mocean.

**Locație:** `667-send-an-sms-using-the-mocean-node`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** mocean

### 668-create-or-update-a-post-in-wordpress

> Se declanșează manual. folosește WordPress, actualizează date în WordPress.

**Locație:** `668-create-or-update-a-post-in-wordpress`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** 👆 Manual
- **Integrări:** WordPress

### 685-create-update-and-get-an-issue-on-taiga

> Se declanșează manual. folosește taiga, actualizează date în taiga, obține date din taiga.

**Locație:** `685-create-update-and-get-an-issue-on-taiga`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** taiga

### 686-receive-updates-when-an-event-occurs-in-taiga

> Se declanșează de taigaTrigger.

**Locație:** `686-receive-updates-when-an-event-occurs-in-taiga`

- **Noduri:** 1
- **Conexiuni:** 0

### 687-read-rss-feed-from-two-different-sources

> Se declanșează manual. folosește rssFeedRead.

**Locație:** `687-read-rss-feed-from-two-different-sources`

- **Noduri:** 4
- **Conexiuni:** 4
- **Declanșare:** 👆 Manual
- **Integrări:** rssFeedRead

### 688-execute-set-node-based-on-function-output

> Se declanșează manual.

**Locație:** `688-execute-set-node-based-on-function-output`

- **Noduri:** 7
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual

### 693-display-project-data-on-a-smashing-dashboard

> Rulează programat (cron). folosește HTTP API, obține date din GitHub.

**Locație:** `693-display-project-data-on-a-smashing-dashboard`

- **Noduri:** 24
- **Conexiuni:** 10
- **Declanșare:** ⏰ Programat
- **Integrări:** GitHub, HTTP API

### 695-get-local-datetime-into-function-node-using-moment-js

> Se declanșează manual.

**Locație:** `695-get-local-datetime-into-function-node-using-moment-js`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual

### 697-archive-spotify-s-discover-weekly-playlist

> Rulează programat (schedule). folosește spotify, folosește spotify, folosește spotify.

**Locație:** `697-archive-spotify-s-discover-weekly-playlist`

- **Noduri:** 7
- **Conexiuni:** 5
- **Declanșare:** ⏰ Programat
- **Integrări:** spotify

### 700-purge-n8n-execution-history-located-in-mysql

> Se declanșează manual. folosește mySql.

**Locație:** `700-purge-n8n-execution-history-located-in-mysql`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** ⏰ Programat, 👆 Manual
- **Integrări:** mySql

### 701-manage-projects-in-clockify

> Se declanșează manual. folosește Clockify, actualizează date în Clockify.

**Locație:** `701-manage-projects-in-clockify`

- **Noduri:** 5
- **Conexiuni:** 4
- **Declanșare:** 👆 Manual
- **Integrări:** Clockify

### 702-extract-information-from-an-image-of-a-receipt

> Se declanșează manual. folosește mindee, folosește HTTP API.

**Locație:** `702-extract-information-from-an-image-of-a-receipt`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** 👆 Manual
- **Integrări:** HTTP API, mindee

### 728-create-a-board-lists-and-a-card-in-wekan

> Se declanșează manual. folosește wekan, actualizează date în wekan.

**Locație:** `728-create-a-board-lists-and-a-card-in-wekan`

- **Noduri:** 6
- **Conexiuni:** 5
- **Declanșare:** 👆 Manual
- **Integrări:** wekan

### 738-store-and-send-information-about-the-weather-for-any-city-via-sms

> Se declanșează prin webhook HTTP. folosește Webhook, adaugă date în Airtable, folosește openWeatherMap, folosește Twilio.

**Locație:** `738-store-and-send-information-about-the-weather-for-any-city-via-sms`

- **Noduri:** 5
- **Conexiuni:** 4
- **Declanșare:** 🌐 Webhook
- **Integrări:** Airtable, Twilio, Webhook, openWeatherMap

### 739-detect-and-store-the-information-about-a-purchase-using-the-image-of-a-receipt

> Se declanșează prin webhook HTTP. folosește Webhook, folosește mindee, adaugă date în Airtable.

**Locație:** `739-detect-and-store-the-information-about-a-purchase-using-the-image-of-a-receipt`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** 🌐 Webhook
- **Integrări:** Airtable, Webhook, mindee

### 741-extract-infromation-from-a-receipt-and-store-it-in-airtable

> Se declanșează la trimiterea unui formular n8n. folosește HTTP API, folosește mindee, adaugă date în Airtable.

**Locație:** `741-extract-infromation-from-a-receipt-and-store-it-in-airtable`

- **Noduri:** 5
- **Conexiuni:** 4
- **Integrări:** Airtable, HTTP API, mindee

### 744-create-update-and-get-activity-in-strava

> Se declanșează manual. folosește strava, actualizează date în strava, obține date din strava.

**Locație:** `744-create-update-and-get-activity-in-strava`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** strava

### 750-send-updates-about-the-position-of-the-iss-every-minute-to-a-topic-in-kafka

> Rulează programat (cron). folosește HTTP API, folosește Kafka.

**Locație:** `750-send-updates-about-the-position-of-the-iss-every-minute-to-a-topic-in-kafka`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** ⏰ Programat
- **Integrări:** HTTP API, Kafka

### 762-send-updates-about-the-position-of-the-iss-every-minute-to-a-topic-in-activemq

> Rulează programat (cron). folosește HTTP API, folosește AMQP.

**Locație:** `762-send-updates-about-the-position-of-the-iss-every-minute-to-a-topic-in-activemq`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** ⏰ Programat
- **Integrări:** AMQP, HTTP API

### 765-create-a-new-member-update-the-infromation-create-a-note-and-post-in-orbit

> Se declanșează manual. actualizează/creează în orbit, actualizează date în orbit, folosește orbit.

**Locație:** `765-create-a-new-member-update-the-infromation-create-a-note-and-post-in-orbit`

- **Noduri:** 5
- **Conexiuni:** 4
- **Declanșare:** 👆 Manual
- **Integrări:** orbit

### 766-create-multiple-json-items-from-an-array

> Declanșare manuală sau nedeterminată.

**Locație:** `766-create-multiple-json-items-from-an-array`

- **Noduri:** 2
- **Conexiuni:** 1

### 767-create-an-array-of-objects

> Declanșare manuală sau nedeterminată.

**Locație:** `767-create-an-array-of-objects`

- **Noduri:** 2
- **Conexiuni:** 1

### 768-get-all-the-stories-and-publish-them-in-storyblok

> Se declanșează manual. citește date din storyblok, folosește storyblok.

**Locație:** `768-get-all-the-stories-and-publish-them-in-storyblok`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** 👆 Manual
- **Integrări:** storyblok

### 787-receive-updates-for-the-position-of-the-iss-and-push-it-to-a-firbase

> Rulează programat (cron). folosește HTTP API, folosește googleFirebaseRealtimeDatabase.

**Locație:** `787-receive-updates-for-the-position-of-the-iss-and-push-it-to-a-firbase`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** ⏰ Programat
- **Integrări:** HTTP API, googleFirebaseRealtimeDatabase

### 797-translate-instructions-using-lingvanex

> Se declanșează manual. folosește lingvaNex, folosește HTTP API.

**Locație:** `797-translate-instructions-using-lingvanex`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** 👆 Manual
- **Integrări:** HTTP API, lingvaNex

### 8-handle-errors-from-a-different-workflow

> Se declanșează de Error Trigger. folosește mailgun.

**Locație:** `8-handle-errors-from-a-different-workflow`

- **Noduri:** 2
- **Conexiuni:** 1
- **Integrări:** mailgun

### 805-create-update-and-get-records-in-quick-base

> Se declanșează manual. folosește quickbase, actualizează date în quickbase, citește date din quickbase.

**Locație:** `805-create-update-and-get-records-in-quick-base`

- **Noduri:** 6
- **Conexiuni:** 5
- **Declanșare:** 👆 Manual
- **Integrări:** quickbase

### 806-get-synonyms-of-a-german-word

> Se declanșează manual. folosește openThesaurus.

**Locație:** `806-get-synonyms-of-a-german-word`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** openThesaurus

### 809-get-the-job-details-using-the-cortex-node

> Se declanșează manual. folosește cortex.

**Locație:** `809-get-the-job-details-using-the-cortex-node`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** 👆 Manual
- **Integrări:** cortex

### 817-save-your-workflows-into-a-github-repository

> Se declanșează manual. folosește HTTP API, obține date din GitHub, folosește GitHub, folosește GitHub.

**Locație:** `817-save-your-workflows-into-a-github-repository`

- **Noduri:** 16
- **Conexiuni:** 16
- **Declanșare:** ⏰ Programat, 👆 Manual
- **Integrări:** GitHub, HTTP API

### 818-insert-and-update-data-in-airtable

> Se declanșează manual. adaugă date în Airtable, listează date din Airtable, actualizează date în Airtable.

**Locație:** `818-insert-and-update-data-in-airtable`

- **Noduri:** 6
- **Conexiuni:** 5
- **Declanșare:** 👆 Manual
- **Integrări:** Airtable

### 823-n8n-workflow-backup-management-with-dropbox-and-airtable

> Se declanșează manual. listează date din Airtable, actualizează date în Airtable, adaugă date în Airtable, folosește HTTP API (+2 altele).

**Locație:** `823-n8n-workflow-backup-management-with-dropbox-and-airtable`

- **Noduri:** 19
- **Conexiuni:** 18
- **Declanșare:** ⏰ Programat, 👆 Manual
- **Integrări:** Airtable, Dropbox, HTTP API, moveBinaryData

### 824-create-a-table-and-insert-and-update-data-in-the-table-in-snowflake

> Se declanșează manual. folosește snowflake, folosește snowflake, actualizează date în snowflake.

**Locație:** `824-create-a-table-and-insert-and-update-data-in-the-table-in-snowflake`

- **Noduri:** 6
- **Conexiuni:** 5
- **Declanșare:** 👆 Manual
- **Integrări:** snowflake

### 825-create-update-and-get-a-post-in-ghost

> Se declanșează manual. creează înregistrări în Ghost CMS, actualizează date în Ghost CMS, folosește Ghost CMS.

**Locație:** `825-create-update-and-get-a-post-in-ghost`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** Ghost CMS

### 828-send-the-astronomy-picture-of-the-day-daily-to-a-telegram-channel

> Rulează programat (cron). folosește nasa, trimite imagini prin Telegram.

**Locație:** `828-send-the-astronomy-picture-of-the-day-daily-to-a-telegram-channel`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** ⏰ Programat
- **Integrări:** Telegram, nasa

### 835-get-company-data-and-store-it-in-airtable

> Se declanșează manual. folosește Brandfetch, folosește Brandfetch, adaugă date în Airtable.

**Locație:** `835-get-company-data-and-store-it-in-airtable`

- **Noduri:** 5
- **Conexiuni:** 4
- **Declanșare:** 👆 Manual
- **Integrări:** Airtable, Brandfetch

### 837-track-changes-of-product-prices

> Rulează programat (cron). folosește htmlExtract, folosește HTTP API, folosește writeBinaryFile, folosește moveBinaryData (+3 altele).

**Locație:** `837-track-changes-of-product-prices`

- **Noduri:** 25
- **Conexiuni:** 24
- **Declanșare:** ⏰ Programat
- **Integrări:** Comandă Shell, Email SMTP, HTTP API, htmlExtract, moveBinaryData, readBinaryFile, writeBinaryFile

### 844-send-updates-about-the-position-of-the-iss-every-minute-to-a-topic-in-rabbitmq

> Rulează programat (cron). folosește RabbitMQ, folosește HTTP API.

**Locație:** `844-send-updates-about-the-position-of-the-iss-every-minute-to-a-topic-in-rabbitmq`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** ⏰ Programat
- **Integrări:** HTTP API, RabbitMQ

### 847-create-update-and-get-a-product-from-woocommerce

> Se declanșează manual. folosește WooCommerce, actualizează date în WooCommerce, obține date din WooCommerce.

**Locație:** `847-create-update-and-get-a-product-from-woocommerce`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** WooCommerce

### 853-weekly-coffee-chat-mattermost-version

> Rulează programat (cron). folosește Mattermost, citește date din Mattermost, folosește Google Calendar.

**Locație:** `853-weekly-coffee-chat-mattermost-version`

- **Noduri:** 6
- **Conexiuni:** 4
- **Declanșare:** ⏰ Programat
- **Integrări:** Google Calendar, Mattermost

### 858-create-a-website-screenshot-and-send-via-telegram-channel

> Se declanșează manual. trimite imagini prin Telegram, folosește uproc.

**Locație:** `858-create-a-website-screenshot-and-send-via-telegram-channel`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** 👆 Manual
- **Integrări:** Telegram, uproc

### 867-create-add-an-attachment-and-send-a-draft-using-microsoft-outlook

> Se declanșează manual. folosește Microsoft Outlook, folosește HTTP API, trimite mesaje prin Microsoft Outlook.

**Locație:** `867-create-add-an-attachment-and-send-a-draft-using-microsoft-outlook`

- **Noduri:** 5
- **Conexiuni:** 4
- **Declanșare:** 👆 Manual
- **Integrări:** HTTP API, Microsoft Outlook

### 869-find-a-new-book-recommendations

> Se declanșează manual. folosește HTTP API, folosește Email SMTP.

**Locație:** `869-find-a-new-book-recommendations`

- **Noduri:** 13
- **Conexiuni:** 11
- **Declanșare:** ⏰ Programat, 👆 Manual
- **Integrări:** Email SMTP, HTTP API

### 870-send-an-sms-to-a-number-whenever-you-go-out

> Se declanșează de pushcutTrigger. folosește Twilio.

**Locație:** `870-send-an-sms-to-a-number-whenever-you-go-out`

- **Noduri:** 2
- **Conexiuni:** 1
- **Integrări:** Twilio

### 875-send-tweets-every-minute-to-mattermost

> Rulează programat (cron). caută în Twitter/X, folosește Mattermost.

**Locație:** `875-send-tweets-every-minute-to-mattermost`

- **Noduri:** 5
- **Conexiuni:** 4
- **Declanșare:** ⏰ Programat
- **Integrări:** Mattermost, Twitter/X

### 879-access-data-from-bubble-application

> Se declanșează manual. folosește HTTP API.

**Locație:** `879-access-data-from-bubble-application`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** HTTP API

### 880-receive-updates-of-the-position-of-the-iss-every-minute

> Rulează programat (cron). folosește HTTP API.

**Locație:** `880-receive-updates-of-the-position-of-the-iss-every-minute`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** ⏰ Programat
- **Integrări:** HTTP API

### 888-get-data-from-hacker-news-and-send-to-airtable-or-via-sms

> Rulează programat (cron). folosește hackerNews, folosește lingvaNex, adaugă date în Airtable, folosește Vonage.

**Locație:** `888-get-data-from-hacker-news-and-send-to-airtable-or-via-sms`

- **Noduri:** 8
- **Conexiuni:** 6
- **Declanșare:** ⏰ Programat
- **Integrări:** Airtable, Vonage, hackerNews, lingvaNex

### 900-add-a-datapoint-to-beeminder-on-strava-activity-update

> Se declanșează de stravaTrigger. folosește beeminder.

**Locație:** `900-add-a-datapoint-to-beeminder-on-strava-activity-update`

- **Noduri:** 2
- **Conexiuni:** 1
- **Integrări:** beeminder

### 930-create-update-and-get-a-post-via-discourse

> Se declanșează manual. folosește discourse, actualizează date în discourse, obține date din discourse.

**Locație:** `930-create-update-and-get-a-post-via-discourse`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** discourse

### 934-insert-and-retrieve-data-from-a-table-in-stackby

> Se declanșează manual. folosește stackby, listează date din stackby.

**Locație:** `934-insert-and-retrieve-data-from-a-table-in-stackby`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** stackby

### 935-check-for-preview-for-a-link

> Se declanșează manual. folosește peekalink, folosește peekalink.

**Locație:** `935-check-for-preview-for-a-link`

- **Noduri:** 5
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** peekalink

### 959-create-a-collection-and-create-update-and-get-a-bookmark-in-raindrop

> Declanșare manuală sau nedeterminată. creează înregistrări în raindrop, actualizează date în raindrop, folosește raindrop.

**Locație:** `959-create-a-collection-and-create-update-and-get-a-bookmark-in-raindrop`

- **Noduri:** 4
- **Conexiuni:** 3
- **Integrări:** raindrop

### 965-analyze-feedback-using-aws-comprehend-and-send-it-to-a-mattermost-channel

> Se declanșează la trimiterea unui formular n8n. folosește Mattermost, folosește awsComprehend.

**Locație:** `965-analyze-feedback-using-aws-comprehend-and-send-it-to-a-mattermost-channel`

- **Noduri:** 5
- **Conexiuni:** 3
- **Integrări:** Mattermost, awsComprehend

### 987-create-asana-ticket-from-terminal-bash-dash

> Se declanșează prin webhook HTTP. folosește Asana, folosește Webhook.

**Locație:** `987-create-asana-ticket-from-terminal-bash-dash`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** 🌐 Webhook
- **Integrări:** Asana, Webhook

### 995-split-in-batches-node-noitemsleft-example

> Se declanșează manual.

**Locație:** `995-split-in-batches-node-noitemsleft-example`

- **Noduri:** 5
- **Conexiuni:** 4
- **Declanșare:** 👆 Manual

### 996-split-in-batches-node-currentrunindex-example

> Se declanșează manual.

**Locație:** `996-split-in-batches-node-currentrunindex-example`

- **Noduri:** 5
- **Conexiuni:** 4
- **Declanșare:** 👆 Manual

### getting-started

> Declanșare manuală sau nedeterminată. folosește interval.

**Locație:** `getting-started`

- **Noduri:** 3
- **Conexiuni:** 2
- **Integrări:** interval

---

## communication

### 1105-check-to-do-on-notion-and-send-message-on-slack

> Rulează programat (cron). citește date din Notion, deschide sesiune în Slack, folosește Slack.

**Locație:** `1105-check-to-do-on-notion-and-send-message-on-slack`

- **Noduri:** 6
- **Conexiuni:** 4
- **Declanșare:** ⏰ Programat
- **Integrări:** Notion, Slack

### 1109-add-positive-feedback-messages-to-a-table-in-notion

> Se declanșează la trimiterea unui formular n8n. folosește googleCloudNaturalLanguage, folosește Notion, folosește Slack, folosește Trello.

**Locație:** `1109-add-positive-feedback-messages-to-a-table-in-notion`

- **Noduri:** 6
- **Conexiuni:** 4
- **Integrări:** Notion, Slack, Trello, googleCloudNaturalLanguage

### 1255-send-notification-when-deployment-fails

> Se declanșează de netlifyTrigger. folosește Slack.

**Locație:** `1255-send-notification-when-deployment-fails`

- **Noduri:** 2
- **Conexiuni:** 1
- **Integrări:** Slack

### 1344-save-email-attachments-to-nextcloud

> Se declanșează la primirea unui email. folosește Email IMAP, folosește nextCloud.

**Locație:** `1344-save-email-attachments-to-nextcloud`

- **Noduri:** 3
- **Conexiuni:** 2
- **Integrări:** Email IMAP, nextCloud

### 1377-extract-url-from-an-email-address

> Se declanșează manual.

**Locație:** `1377-extract-url-from-an-email-address`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** 👆 Manual

### 1416-send-a-message-to-telegram-on-a-new-item-saved-to-reader

> Se declanșează manual. folosește writeBinaryFile, folosește readBinaryFile, folosește HTTP API, folosește Telegram (+1 altele).

**Locație:** `1416-send-a-message-to-telegram-on-a-new-item-saved-to-reader`

- **Noduri:** 11
- **Conexiuni:** 8
- **Declanșare:** ⏰ Programat, 👆 Manual
- **Integrări:** HTTP API, Telegram, moveBinaryData, readBinaryFile, writeBinaryFile

### 1453-parse-email-body-message

> Se declanșează manual.

**Locație:** `1453-parse-email-body-message`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** 👆 Manual

### 1471-message-on-website-content-changed-in-telegram

> Rulează programat (cron). folosește HTTP API, folosește Telegram.

**Locație:** `1471-message-on-website-content-changed-in-telegram`

- **Noduri:** 7
- **Conexiuni:** 5
- **Declanșare:** ⏰ Programat
- **Integrări:** HTTP API, Telegram

### 1507-send-telegram-messages-on-rss-feed-read

> Rulează programat (cron). folosește Telegram, folosește rssFeedRead.

**Locație:** `1507-send-telegram-messages-on-rss-feed-read`

- **Noduri:** 7
- **Conexiuni:** 5
- **Declanșare:** ⏰ Programat
- **Integrări:** Telegram, rssFeedRead

### 1528-send-a-discord-message-when-a-certain-onfleet-event-happens

> Se declanșează de onfleetTrigger. folosește Discord.

**Locație:** `1528-send-a-discord-message-when-a-certain-onfleet-event-happens`

- **Noduri:** 2
- **Conexiuni:** 1
- **Integrări:** Discord

### 1532-send-onfleet-driver-signup-messages-in-slack

> Se declanșează de onfleetTrigger. folosește Slack.

**Locație:** `1532-send-onfleet-driver-signup-messages-in-slack`

- **Noduri:** 2
- **Conexiuni:** 1
- **Integrări:** Slack

### 154-listen-on-new-emails-on-a-imap-mailbox

> Se declanșează la primirea unui email. folosește Email IMAP, folosește moveBinaryData, folosește XML, folosește HTTP API.

**Locație:** `154-listen-on-new-emails-on-a-imap-mailbox`

- **Noduri:** 5
- **Conexiuni:** 4
- **Integrări:** Email IMAP, HTTP API, XML, moveBinaryData

### 1765-get-slack-notifications-when-new-product-published-on-woocommerce

> Se declanșează de wooCommerceTrigger. folosește Slack.

**Locație:** `1765-get-slack-notifications-when-new-product-published-on-woocommerce`

- **Noduri:** 3
- **Conexiuni:** 2
- **Integrări:** Slack

### 1790-generate-dynamic-contents-for-emails-or-html-pages

> Se declanșează manual. folosește n8nTrainingCustomerDatastore, folosește Email SMTP.

**Locație:** `1790-generate-dynamic-contents-for-emails-or-html-pages`

- **Noduri:** 8
- **Conexiuni:** 6
- **Declanșare:** 👆 Manual
- **Integrări:** Email SMTP, n8nTrainingCustomerDatastore

### 2032-poll-emails-using-jmap

> Se declanșează manual. folosește HTTP API. Detalii: ℹ️ Credentials

The JMAP standard does not limit the available authentication options. Fastmail (the sponsor of the standard) supports Bearer authentication as well as OAuth2.

In n8n you can implement the Fastmail Bearer authentication by creating...

**Locație:** `2032-poll-emails-using-jmap`

- **Noduri:** 7
- **Conexiuni:** 4
- **Declanșare:** 👆 Manual
- **Integrări:** HTTP API

### 2034-send-dingtalk-message-on-new-azure-devops-pull-request

> Se declanșează prin webhook HTTP. folosește mySql, folosește Webhook, folosește HTTP API. Detalii: Send DingTalk message on new Azure DevOps Pull Request
This template automates sending a DingTalk message on new Azure Dev Ops Pull Request Created Events. It uses a MySQL database to store mappings between Azure users and DingTalk users; so the...

**Locație:** `2034-send-dingtalk-message-on-new-azure-devops-pull-request`

- **Noduri:** 5
- **Conexiuni:** 3
- **Declanșare:** 🌐 Webhook
- **Integrări:** HTTP API, Webhook, mySql

### 2212-zalando-price-patrol-monitor-price-evolution-with-email-notification

> Rulează programat (schedule). folosește Google Sheets, actualizează date în Google Sheets, folosește Google Sheets, folosește HTTP API (+1 altele). Detalii: Setup
 1/ Add Your credentials
[Google SHeet](https://docs.n8n.io/integrations/builtin/credentials/google/)

 2/ Create a Google Spreadsheet that will be your database.
Copy this template:...

**Locație:** `2212-zalando-price-patrol-monitor-price-evolution-with-email-notification`

- **Noduri:** 14
- **Conexiuni:** 7
- **Declanșare:** ⏰ Programat
- **Integrări:** Gmail, Google Sheets, HTTP API

### 2239-extract-domain-and-verify-email-syntax-on-the-go

> Se declanșează manual. folosește debugHelper. Detalii: Email Validation and extract domain
** This workflow is aimed at making email validation and domain extract using the native functionalities in n8n

** Replace the debugger node with your actual data source to validate your own emails

**Locație:** `2239-extract-domain-and-verify-email-syntax-on-the-go`

- **Noduri:** 5
- **Conexiuni:** 2
- **Declanșare:** 👆 Manual
- **Integrări:** debugHelper

### 2280-send-a-message-with-an-inline-embedded-image-with-gmail

> Se declanșează manual. folosește HTTP API, folosește Extracție Fișier. Detalii: Try me out
1. Make sure you add your Gmail credential in the last node
2. Update the sender and recipient in the 'Message settings' node
3. Click 'test workflow'

**Locație:** `2280-send-a-message-with-an-inline-embedded-image-with-gmail`

- **Noduri:** 10
- **Conexiuni:** 5
- **Declanșare:** 👆 Manual
- **Integrări:** Extracție Fișier, HTTP API

### 2471-create-single-new-masked-email-address-with-fastmail

> Se declanșează prin webhook HTTP. folosește HTTP API, folosește Răspuns Webhook, folosește Webhook. Detalii: Template Description
This n8n workflow template allows you to create a masked email address using the Fastmail API, triggered by a webhook. This is especially useful for generating disposable email addresses for privacy-conscious users or for...

**Locație:** `2471-create-single-new-masked-email-address-with-fastmail`

- **Noduri:** 7
- **Conexiuni:** 5
- **Declanșare:** 🌐 Webhook
- **Integrări:** HTTP API, Răspuns Webhook, Webhook

### 2478-send-a-message-via-a-lark-bot

> Se declanșează manual. folosește HTTP API. Detalii: You can get app_id and app_secret in Lark here: https://open.larksuite.com/

**Locație:** `2478-send-a-message-via-a-lark-bot`

- **Noduri:** 6
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** HTTP API

### 2534-telegram-ai-bot-assistant-ready-made-template-for-voice-text-messages

> Se declanșează la primirea unui mesaj Telegram. folosește OpenAI Chat, folosește Buffer Memory, folosește Telegram, folosește OpenAI (+2 altele). Detalii: 1. Send incoming message to the AI Agent
 2. Deliver agent reply to the user

**Locație:** `2534-telegram-ai-bot-assistant-ready-made-template-for-voice-text-messages`

- **Noduri:** 15
- **Conexiuni:** 9
- **Integrări:** AI Agent, Buffer Memory, OpenAI, OpenAI Chat, Telegram

### 401-send-an-sms-whatsapp-message-with-twilio

> Se declanșează manual. folosește Twilio.

**Locație:** `401-send-an-sms-whatsapp-message-with-twilio`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** Twilio

### 462-post-a-message-to-a-channel-in-rocketchat

> Se declanșează manual. folosește Rocket.Chat.

**Locație:** `462-post-a-message-to-a-channel-in-rocketchat`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** Rocket.Chat

### 501-send-a-message-via-aws-sns

> Se declanșează manual. folosește AWS SNS.

**Locație:** `501-send-a-message-via-aws-sns`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** AWS SNS

### 507-send-an-email-using-aws-ses

> Se declanșează manual. folosește awsSes.

**Locație:** `507-send-an-email-using-aws-ses`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** awsSes

### 519-verify-email-deliverability-with-hunter

> Se declanșează manual. folosește hunter.

**Locație:** `519-verify-email-deliverability-with-hunter`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** hunter

### 520-send-an-email-using-mailjet

> Se declanșează manual. folosește mailjet.

**Locație:** `520-send-an-email-using-mailjet`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** mailjet

### 522-send-an-email-using-mailgun

> Se declanșează manual. folosește mailgun.

**Locație:** `522-send-an-email-using-mailgun`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** mailgun

### 571-send-an-email-template-using-mandrill

> Se declanșează manual. folosește mandrill.

**Locație:** `571-send-an-email-template-using-mandrill`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** mandrill

### 584-send-an-email

> Se declanșează manual. folosește Email SMTP.

**Locație:** `584-send-an-email`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** Email SMTP

### 680-create-update-and-send-a-message-to-a-channel-in-microsoft-teams

> Se declanșează manual. folosește Microsoft Teams, actualizează date în Microsoft Teams.

**Locație:** `680-create-update-and-send-a-message-to-a-channel-in-microsoft-teams`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** Microsoft Teams

### 772-send-bulk-messages-to-chats-in-telegram

> Se declanșează manual. folosește Telegram, folosește Google Sheets.

**Locație:** `772-send-bulk-messages-to-chats-in-telegram`

- **Noduri:** 5
- **Conexiuni:** 5
- **Declanșare:** 👆 Manual
- **Integrări:** Google Sheets, Telegram

### 774-send-daily-weather-updates-via-a-message-using-the-gotify-node

> Rulează programat (cron). folosește openWeatherMap, folosește gotify.

**Locație:** `774-send-daily-weather-updates-via-a-message-using-the-gotify-node`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** ⏰ Programat
- **Integrări:** gotify, openWeatherMap

### 796-send-daily-weather-updates-via-a-push-notification-using-spontit

> Rulează programat (cron). folosește openWeatherMap, folosește spontit.

**Locație:** `796-send-daily-weather-updates-via-a-push-notification-using-spontit`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** ⏰ Programat
- **Integrări:** openWeatherMap, spontit

### 799-receive-a-mattermost-message-when-new-data-gets-added-to-airtable

> Se declanșează de airtableTrigger. folosește Mattermost.

**Locație:** `799-receive-a-mattermost-message-when-new-data-gets-added-to-airtable`

- **Noduri:** 2
- **Conexiuni:** 1
- **Integrări:** Mattermost

### 814-receive-messages-from-a-topic-via-kafka-and-send-an-sms

> Se declanșează de kafkaTrigger. folosește Vonage.

**Locație:** `814-receive-messages-from-a-topic-via-kafka-and-send-an-sms`

- **Noduri:** 4
- **Conexiuni:** 2
- **Integrări:** Vonage

### 832-create-a-channel-add-a-member-and-post-a-message-to-the-channel-on-mattermost

> Se declanșează manual. folosește Mattermost, folosește Mattermost.

**Locație:** `832-create-a-channel-add-a-member-and-post-a-message-to-the-channel-on-mattermost`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** Mattermost

### 845-receive-messages-from-a-queue-via-rabbitmq-and-send-an-sms

> Se declanșează de rabbitmqTrigger. folosește Vonage.

**Locație:** `845-receive-messages-from-a-queue-via-rabbitmq-and-send-an-sms`

- **Noduri:** 4
- **Conexiuni:** 2
- **Integrări:** Vonage

### 857-create-screenshots-with-uproc-save-to-dropbox-and-send-by-email

> Se declanșează manual. folosește awsSes, folosește uproc, folosește HTTP API, folosește Dropbox.

**Locație:** `857-create-screenshots-with-uproc-save-to-dropbox-and-send-by-email`

- **Noduri:** 10
- **Conexiuni:** 9
- **Declanșare:** 👆 Manual
- **Integrări:** Dropbox, HTTP API, awsSes, uproc

### 876-monitor-strava-and-send-email-updates

> Rulează programat (cron). citește date din strava, folosește Email SMTP.

**Locație:** `876-monitor-strava-and-send-email-updates`

- **Noduri:** 6
- **Conexiuni:** 4
- **Declanșare:** ⏰ Programat
- **Integrări:** Email SMTP, strava

---

## data-integration

### 1-insert-excel-data-to-postgres

> Declanșare manuală sau nedeterminată. folosește readBinaryFile, folosește Fișier Spreadsheet, folosește PostgreSQL.

**Locație:** `1-insert-excel-data-to-postgres`

- **Noduri:** 3
- **Conexiuni:** 2
- **Integrări:** Fișier Spreadsheet, PostgreSQL, readBinaryFile

### 11-add-data-from-google-sheet-to-dropbox

> Declanșare manuală sau nedeterminată. folosește Google Sheets, folosește Fișier Spreadsheet, folosește Dropbox, folosește interval.

**Locație:** `11-add-data-from-google-sheet-to-dropbox`

- **Noduri:** 4
- **Conexiuni:** 3
- **Integrări:** Dropbox, Fișier Spreadsheet, Google Sheets, interval

### 1122-database-alerts-with-notion-and-signl4

> Se declanșează de notionTrigger. folosește Webhook, actualizează date în Notion, folosește interval, folosește signl4 (+2 altele).

**Locație:** `1122-database-alerts-with-notion-and-signl4`

- **Noduri:** 13
- **Conexiuni:** 8
- **Declanșare:** 🌐 Webhook
- **Integrări:** Notion, Webhook, interval, signl4

### 1150-backup-n8n-workflows-to-google-drive

> Se declanșează manual. folosește moveBinaryData, folosește HTTP API, folosește Google Drive.

**Locație:** `1150-backup-n8n-workflows-to-google-drive`

- **Noduri:** 9
- **Conexiuni:** 8
- **Declanșare:** ⏰ Programat, 👆 Manual
- **Integrări:** Google Drive, HTTP API, moveBinaryData

### 1277-send-a-daily-summary-of-your-google-calendar-events-to-slack

> Rulează programat (cron). citește date din Google Calendar, folosește Date/Time, folosește Slack.

**Locație:** `1277-send-a-daily-summary-of-your-google-calendar-events-to-slack`

- **Noduri:** 12
- **Conexiuni:** 11
- **Declanșare:** ⏰ Programat
- **Integrări:** Date/Time, Google Calendar, Slack

### 1283-get-email-notifications-for-newly-uploaded-google-drive-files

> Se declanșează de googleDriveTrigger. folosește Email SMTP.

**Locație:** `1283-get-email-notifications-for-newly-uploaded-google-drive-files`

- **Noduri:** 2
- **Conexiuni:** 1
- **Integrări:** Email SMTP

### 1340-create-zoom-meeting-link-from-google-calendar-invite

> Se declanșează manual. folosește Zoom, folosește Date/Time, citește date din Google Calendar.

**Locație:** `1340-create-zoom-meeting-link-from-google-calendar-invite`

- **Noduri:** 6
- **Conexiuni:** 5
- **Declanșare:** ⏰ Programat, 👆 Manual
- **Integrări:** Date/Time, Google Calendar, Zoom

### 1388-save-telegram-daily-messages-to-google-sheets

> Se declanșează la primirea unui mesaj Telegram. adaugă date în Google Sheets.

**Locație:** `1388-save-telegram-daily-messages-to-google-sheets`

- **Noduri:** 3
- **Conexiuni:** 2
- **Integrări:** Google Sheets

### 1395-collects-images-from-web-search-results-and-send-to-google-sheets

> Declanșare manuală sau nedeterminată. folosește AWS Rekognition, folosește HTTP API, adaugă date în Google Sheets.

**Locație:** `1395-collects-images-from-web-search-results-and-send-to-google-sheets`

- **Noduri:** 6
- **Conexiuni:** 4
- **Integrări:** AWS Rekognition, Google Sheets, HTTP API

### 1396-sync-data-between-google-drive-and-aws-s3

> Se declanșează de googleDriveTrigger. citește date din awsS3, încarcă fișiere în awsS3.

**Locație:** `1396-sync-data-between-google-drive-and-aws-s3`

- **Noduri:** 4
- **Conexiuni:** 3
- **Integrări:** awsS3

### 1401-collect-and-label-images-and-send-to-google-sheets

> Declanșare manuală sau nedeterminată. folosește HTTP API, folosește AWS Rekognition, adaugă date în Google Sheets.

**Locație:** `1401-collect-and-label-images-and-send-to-google-sheets`

- **Noduri:** 4
- **Conexiuni:** 3
- **Integrări:** AWS Rekognition, Google Sheets, HTTP API

### 1420-google-calendar-to-slack-status-and-philips-hue

> Se declanșează manual. obține date din Google Calendar, folosește HTTP API, actualizează date în Slack.

**Locație:** `1420-google-calendar-to-slack-status-and-philips-hue`

- **Noduri:** 9
- **Conexiuni:** 5
- **Declanșare:** 👆 Manual
- **Integrări:** Google Calendar, HTTP API, Slack

### 1435-convert-json-to-an-excel-file

> Se declanșează prin webhook HTTP. folosește Webhook, folosește Fișier Spreadsheet, folosește Răspuns Webhook.

**Locație:** `1435-convert-json-to-an-excel-file`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** 🌐 Webhook
- **Integrări:** Fișier Spreadsheet, Răspuns Webhook, Webhook

### 1478-archive-empty-pages-in-notion-database

> Rulează programat (cron). citește date din Notion, folosește Notion.

**Locație:** `1478-archive-empty-pages-in-notion-database`

- **Noduri:** 10
- **Conexiuni:** 9
- **Declanșare:** ⏰ Programat
- **Integrări:** Notion

### 1492-update-time-tracking-projects-based-on-syncro-status-changes

> Se declanșează prin webhook HTTP. folosește Webhook, citește date din Clockify, folosește HTTP API.

**Locație:** `1492-update-time-tracking-projects-based-on-syncro-status-changes`

- **Noduri:** 6
- **Conexiuni:** 4
- **Declanșare:** 🌐 Webhook
- **Integrări:** Clockify, HTTP API, Webhook

### 1736-export-json-file-to-google-sheets

> Declanșare manuală sau nedeterminată. adaugă date în Google Sheets, folosește readBinaryFile, folosește moveBinaryData.

**Locație:** `1736-export-json-file-to-google-sheets`

- **Noduri:** 3
- **Conexiuni:** 2
- **Integrări:** Google Sheets, moveBinaryData, readBinaryFile

### 1737-import-json-data-into-google-sheets-and-csv-file

> Declanșare manuală sau nedeterminată. folosește HTTP API, adaugă date în Google Sheets, folosește Fișier Spreadsheet. Detalii: JSON > Google Sheets

**Locație:** `1737-import-json-data-into-google-sheets-and-csv-file`

- **Noduri:** 6
- **Conexiuni:** 2
- **Integrări:** Fișier Spreadsheet, Google Sheets, HTTP API

### 1752-import-data-from-google-sheets-into-mysql

> Rulează programat (cron). folosește mySql, folosește Google Sheets.

**Locație:** `1752-import-data-from-google-sheets-into-mysql`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** ⏰ Programat
- **Integrări:** Google Sheets, mySql

### 1753-import-data-from-mysql-into-google-sheets

> Rulează programat (cron). folosește mySql, adaugă date în Google Sheets.

**Locație:** `1753-import-data-from-mysql-into-google-sheets`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** ⏰ Programat
- **Integrări:** Google Sheets, mySql

### 1754-identify-new-google-sheets-rows

> Se declanșează manual. actualizează date în Google Sheets, folosește Google Sheets, folosește interval.

**Locație:** `1754-identify-new-google-sheets-rows`

- **Noduri:** 7
- **Conexiuni:** 5
- **Declanșare:** 👆 Manual
- **Integrări:** Google Sheets, interval

### 1756-google-spreadsheet-to-html-variant-with-spreadsheet-file

> Se declanșează prin webhook HTTP. folosește Google Sheets, folosește Fișier Spreadsheet, folosește Webhook.

**Locație:** `1756-google-spreadsheet-to-html-variant-with-spreadsheet-file`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** 🌐 Webhook
- **Integrări:** Fișier Spreadsheet, Google Sheets, Webhook

### 1757-google-spreadsheet-to-html-variant-with-js-function

> Se declanșează prin webhook HTTP. folosește Google Sheets, folosește Răspuns Webhook, folosește Webhook.

**Locație:** `1757-google-spreadsheet-to-html-variant-with-js-function`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** 🌐 Webhook
- **Integrări:** Google Sheets, Răspuns Webhook, Webhook

### 1769-sync-tasks-data-between-notion-and-asana

> Se declanșează de asanaTrigger. actualizează date în Notion, folosește Notion, obține date din Asana, citește date din Notion.

**Locație:** `1769-sync-tasks-data-between-notion-and-asana`

- **Noduri:** 10
- **Conexiuni:** 8
- **Integrări:** Asana, Notion

### 1778-sync-tasks-automatically-from-todoist-to-notion

> Rulează programat (schedule). citește date din Todoist, folosește Notion, actualizează date în Todoist.

**Locație:** `1778-sync-tasks-automatically-from-todoist-to-notion`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** ⏰ Programat
- **Integrări:** Notion, Todoist

### 1804-sync-your-github-issues-to-your-notion-database

> Se declanșează de githubTrigger. folosește Notion, citește date din Notion, actualizează date în Notion, folosește Notion. Detalii: IF & Switch
Depends on what action was taken on an issue in GitHub.

**Locație:** `1804-sync-your-github-issues-to-your-notion-database`

- **Noduri:** 11
- **Conexiuni:** 5
- **Integrări:** Notion

### 1810-read-xml-file-and-store-content-in-google-sheets

> Se declanșează manual. folosește HTTP API, folosește XML, folosește Google Sheets, actualizează date în Google Sheets (+1 altele). Detalii: n8n version

This workflow was created using n8n version 0.197.1 and uses a new [expression syntax](https://docs.n8n.io/code-examples/methods-variables-reference/) as well as a new version of the Merge node. Make sure you're also using n8n version...

**Locație:** `1810-read-xml-file-and-store-content-in-google-sheets`

- **Noduri:** 10
- **Conexiuni:** 8
- **Declanșare:** 👆 Manual
- **Integrări:** Google Sheets, HTTP API, XML

### 1819-send-google-drive-files-to-notion-database

> Se declanșează de googleDriveTrigger. folosește Notion.

**Locație:** `1819-send-google-drive-files-to-notion-database`

- **Noduri:** 2
- **Conexiuni:** 1
- **Integrări:** Notion

### 1826-working-with-excel-spreadsheet-files-xls-xlsx

> Se declanșează manual. folosește readBinaryFile, folosește writeBinaryFile, descarcă din Google Drive, descarcă din microsoftOneDrive (+6 altele). Detalii: Working with Excel files
1. Load the spreadsheet file into the workflow (.xls, .xlsx, .csv).
2. Convert the file with **Spreadsheet File** node. This allows other nodes to access the data.
3. Transform and manipulate the spreadsheet data as...

**Locație:** `1826-working-with-excel-spreadsheet-files-xls-xlsx`

- **Noduri:** 24
- **Conexiuni:** 8
- **Declanșare:** 👆 Manual
- **Integrări:** FTP, Fișier Spreadsheet, Google Drive, HTTP API, microsoftOneDrive, readBinaryFile, writeBinaryFile

### 1831-sync-jira-issues-with-subsequent-comments-to-notion-database

> Se declanșează de jiraTrigger. folosește Notion, citește date din Notion, folosește Notion, actualizează date în Notion. Detalii: `IF` & `Switch` nodes
These conditional nodes (`IF` and `Switch`) determine which Notion [**CRUD**](https://www.sumologic.com/glossary/crud/) operations will be performed.

**Locație:** `1831-sync-jira-issues-with-subsequent-comments-to-notion-database`

- **Noduri:** 10
- **Conexiuni:** 6
- **Integrări:** Notion

### 1832-sync-zendesk-tickets-with-subsequent-comments-to-github-issues

> Se declanșează prin webhook HTTP. obține date din Zendesk, actualizează date în Zendesk, folosește GitHub, folosește GitHub (+1 altele).

**Locație:** `1832-sync-zendesk-tickets-with-subsequent-comments-to-github-issues`

- **Noduri:** 7
- **Conexiuni:** 5
- **Declanșare:** 🌐 Webhook
- **Integrări:** GitHub, Webhook, Zendesk

### 1834-send-new-clockify-invoice-to-notion-database

> Se declanșează prin webhook HTTP. folosește Webhook, folosește Notion. Detalii: Send new Clockify invoice to Notion database
 How it works
1. `On new invoice in Clockify` webhook node will trigger when a new invoice is created in Clockify. Setup is involved.
2. `Create database page` Notion node will create a database page with...

**Locație:** `1834-send-new-clockify-invoice-to-notion-database`

- **Noduri:** 3
- **Conexiuni:** 1
- **Declanșare:** 🌐 Webhook
- **Integrări:** Notion, Webhook

### 1835-sync-notion-database-pages-as-clickup-tasks

> Se declanșează de notionTrigger. actualizează date în ClickUp, citește date din Notion, actualizează date în Notion.

**Locație:** `1835-sync-notion-database-pages-as-clickup-tasks`

- **Noduri:** 5
- **Conexiuni:** 3
- **Integrări:** ClickUp, Notion

### 1872-convert-sql-table-into-excel-spreadsheet

> Se declanșează manual. folosește mySql, folosește Fișier Spreadsheet. Detalii: Save SQL table as a binary XLSX file
 You can send it via e-mail, upload to the file storage or download on your computer.
 Just connect one or two extra n8n Nodes here!

**Locație:** `1872-convert-sql-table-into-excel-spreadsheet`

- **Noduri:** 5
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** Fișier Spreadsheet, mySql

### 1897-send-specific-pdf-attachments-from-gmail-to-google-drive-using-openai

> Se declanșează de Gmail Trigger. folosește readPDF, folosește OpenAI, folosește Google Drive. Detalii: Send specific PDF attachments from Gmail to Google Drive using OpenAI

_**DISCLAIMER**: You may have varying success when using this workflow so be prepared to validate the correctness of OpenAI's results._

This workflow reads PDF textual content...

**Locație:** `1897-send-specific-pdf-attachments-from-gmail-to-google-drive-using-openai`

- **Noduri:** 18
- **Conexiuni:** 11
- **Integrări:** Google Drive, OpenAI, readPDF

### 1898-send-a-chatgpt-email-reply-and-save-responses-to-google-sheets

> Se declanșează de Gmail Trigger. folosește OpenAI, folosește Gmail, folosește Crypto, folosește HTML (+6 altele). Detalii: Send a ChatGPT email reply when email received and save responses to Google Sheets
This workflow sends a OpenAI GPT reply when an email is received from specific email recipients. It then saves the initial email and the GPT response to an...

**Locație:** `1898-send-a-chatgpt-email-reply-and-save-responses-to-google-sheets`

- **Noduri:** 49
- **Conexiuni:** 32
- **Declanșare:** 🌐 Webhook
- **Integrări:** Crypto, Gmail, Google Sheets, HTML, OpenAI, Răspuns Webhook, Webhook

### 1932-send-alert-when-data-is-created-in-app-database

> Se declanșează de linearTrigger. folosește Slack. Detalii: 1. Trigger step listens for new events































We added a `Linear trigger` that starts the workflow every time we have an `Issue` event int the `Product & Design` team. 

**You can replace this node with any trigger you wish,...

**Locație:** `1932-send-alert-when-data-is-created-in-app-database`

- **Noduri:** 10
- **Conexiuni:** 5
- **Declanșare:** 👆 Manual
- **Integrări:** Slack

### 1939-send-labeled-email-to-a-notion-database

> Rulează programat (schedule). folosește Date/Time, citește date din Gmail, folosește Notion, citește date din Notion (+2 altele). Detalii: Send labeled email to a Notion database
This workflow sends the contents of an email to a Notion database. The email must be labeled with a specific label for the workflow to trigger. The email subject will be the title of the Notion page, and a...

**Locație:** `1939-send-labeled-email-to-a-notion-database`

- **Noduri:** 14
- **Conexiuni:** 9
- **Declanșare:** ⏰ Programat
- **Integrări:** Date/Time, Gmail, HTTP API, Notion

### 1940-sync-discord-scheduled-events-to-google-calendar

> Rulează programat (schedule). folosește HTTP API, actualizează date în Google Calendar, folosește Google Calendar, obține date din Google Calendar. Detalii: Sync Discord scheduled events to Google Calendar
This workflow syncs Discord scheduled events to Google Calendar. On a specified schedule, a request to Discord's API is made to get the scheduled events on a particular server. Only the events that...

**Locație:** `1940-sync-discord-scheduled-events-to-google-calendar`

- **Noduri:** 9
- **Conexiuni:** 5
- **Declanșare:** ⏰ Programat
- **Integrări:** Google Calendar, HTTP API

### 1948-xml-to-sql-database-import

> Se declanșează manual. folosește readBinaryFiles, folosește XML, folosește mySql, folosește mySql. Detalii: This is a content of the example XML file.
 Please use it if the file was not already created

<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Products>
  <Product Price="69.26" Code="S24_2360">
    <Name>1982 Ducati 900 Monster</Name>
   ...

**Locație:** `1948-xml-to-sql-database-import`

- **Noduri:** 9
- **Conexiuni:** 5
- **Declanșare:** 👆 Manual
- **Integrări:** XML, mySql, readBinaryFiles

### 1964-sync-google-sheets-data-with-mysql

> Se declanșează manual. folosește Google Sheets, folosește mySql, actualizează/creează în mySql, actualizează date în Google Sheets (+1 altele). Detalii: Create a new Google Form with several variables:

-Email Address
-Your name 
-What event are you organizing? 
-When does the event take place? 
-Where does the event take place? 
-Please tell us more about the event. 

- Timestamp variable is added...

**Locație:** `1964-sync-google-sheets-data-with-mysql`

- **Noduri:** 15
- **Conexiuni:** 9
- **Declanșare:** ⏰ Programat, 👆 Manual
- **Integrări:** Google Sheets, mySql

### 1968-import-multiple-csv-to-google-sheets

> Se declanșează manual. folosește readBinaryFiles, folosește Fișier Spreadsheet, folosește Google Sheets.

**Locație:** `1968-import-multiple-csv-to-google-sheets`

- **Noduri:** 9
- **Conexiuni:** 8
- **Declanșare:** 👆 Manual
- **Integrări:** Fișier Spreadsheet, Google Sheets, readBinaryFiles

### 1969-import-csv-from-url-to-google-sheets

> Se declanșează manual. folosește Google Sheets, folosește Fișier Spreadsheet, folosește HTTP API. Detalii: Google API has rate-limits for read and write operations, that's why we take only a subset of the data

To import the whole dataset please add Split In Batches and a Wait node with a sufficient delay.

**Locație:** `1969-import-csv-from-url-to-google-sheets`

- **Noduri:** 7
- **Conexiuni:** 5
- **Declanșare:** 👆 Manual
- **Integrări:** Fișier Spreadsheet, Google Sheets, HTTP API

### 2-transfer-data-from-postgres-to-excel

> Declanșare manuală sau nedeterminată. folosește PostgreSQL, folosește Fișier Spreadsheet, folosește writeBinaryFile.

**Locație:** `2-transfer-data-from-postgres-to-excel`

- **Noduri:** 3
- **Conexiuni:** 2
- **Integrări:** Fișier Spreadsheet, PostgreSQL, writeBinaryFile

### 2041-get-csv-from-url-and-convert-to-excel

> Se declanșează manual. folosește Fișier Spreadsheet, folosește HTTP API, folosește Fișier Spreadsheet. Detalii: Convert CSV to Excel (.xlsx)
1. Click Execute Workflow to begin
2. Download the data from the Web
3. Import CSV binary data as a JSON
4. Convert JSON to .xlsx...

**Locație:** `2041-get-csv-from-url-and-convert-to-excel`

- **Noduri:** 5
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** Fișier Spreadsheet, HTTP API

### 2046-kv-cloudflare-key-value-database-full-api-integration-workflow

> Se declanșează manual. folosește HTTP API. Detalii: This n8n template provides a seamless and efficient way to manage Key-Value (KV) pairs in Cloudflare's KV storage. all you need just take the part of action you want then use it with your workflow, keep in mind that the **_`Account Path`_** node is...

**Locație:** `2046-kv-cloudflare-key-value-database-full-api-integration-workflow`

- **Noduri:** 47
- **Conexiuni:** 20
- **Declanșare:** 👆 Manual
- **Integrări:** HTTP API

### 2063-google-maps-scraper

> Se declanșează manual. folosește Google Sheets, folosește HTTP API, folosește Google Sheets, actualizează date în Google Sheets. Detalii: Read Me

This workflow allows to scrape Google Maps data in an efficient way using SerpAPI. 

You'll get all data from Gmaps at a cheaper cost than Google Maps API.

Add as input, your Google Maps search URL and you'll get a list of places with many...

**Locație:** `2063-google-maps-scraper`

- **Noduri:** 20
- **Conexiuni:** 13
- **Declanșare:** ⏰ Programat, 👆 Manual
- **Integrări:** Google Sheets, HTTP API

### 2081-synchronize-your-google-sheets-with-postgres

> Rulează programat (schedule). folosește Google Sheets, folosește PostgreSQL, folosește PostgreSQL, actualizează date în PostgreSQL. Detalii: Setup 
In order to make this automation work for you, you need to make a few adjustments:

1. Add your Postgres & Google Sheets Credentials to the respective Nodes

2. Select the Sheet (Google Sheets) and the table (Postgres) you want to sync

3....

**Locație:** `2081-synchronize-your-google-sheets-with-postgres`

- **Noduri:** 10
- **Conexiuni:** 5
- **Declanșare:** ⏰ Programat
- **Integrări:** Google Sheets, PostgreSQL

### 2087-streamline-data-from-an-n8n-form-into-google-sheet-airtable-and-email-sending

> Se declanșează la trimiterea unui formular n8n. creează înregistrări în Airtable, adaugă date în Google Sheets, folosește Gmail. Detalii: Workflow Description:

1. **n8n Form Trigger:**
   - A trigger node that initiates the workflow when a form is submitted.
   - Form fields include Name, City, and Email.

2. **Extracting Date and Time Fields from 'submittedAt' Field:**
   - A code...

**Locație:** `2087-streamline-data-from-an-n8n-form-into-google-sheet-airtable-and-email-sending`

- **Noduri:** 10
- **Conexiuni:** 5
- **Integrări:** Airtable, Gmail, Google Sheets

### 2090-chat-with-a-database-using-ai

> Se declanșează prin mesaj de chat. folosește OpenAI Chat, folosește AI Agent. Detalii: Try me out
Click the 'chat' button at the bottom of the canvas and paste in:

_Which tables are available?_

**Locație:** `2090-chat-with-a-database-using-ai`

- **Noduri:** 5
- **Conexiuni:** 2
- **Integrări:** AI Agent, OpenAI Chat

### 2141-add-product-ideas-to-google-sheets-via-a-slack

> Se declanșează prin webhook HTTP. folosește Webhook, folosește Google Sheets, folosește HTTP API. Detalii: Needed pre-work: Add a Slack App
1. Visit https://api.slack.com/apps, click on `New App` and choose a name and workspace.
2. Click on `OAuth & Permissions` and scroll down to Scopes -> Bot token Scopes
3. Add the `chat:write` scope
4. Head over to...

**Locație:** `2141-add-product-ideas-to-google-sheets-via-a-slack`

- **Noduri:** 8
- **Conexiuni:** 4
- **Declanșare:** 🌐 Webhook
- **Integrări:** Google Sheets, HTTP API, Webhook

### 2148-write-all-linear-tickets-to-google-sheets

> Rulează zilnic la ora 9:00. folosește GraphQL, folosește Google Sheets. Detalii: 👨‍🎤 Setup
1. Add Linear API header key
2. Add Google sheets creds
3. Update which teams to get tickets from in Graphql Nodes
4. Update which Google Sheets page to write all the tickets to. 
 **You only need to add one column, id. Google Sheets node...

**Locație:** `2148-write-all-linear-tickets-to-google-sheets`

- **Noduri:** 14
- **Conexiuni:** 8
- **Declanșare:** ⏰ Programat
- **Integrări:** Google Sheets, GraphQL

### 226-receive-google-sheet-data-via-rest-api

> Se declanșează prin webhook HTTP. folosește Google Sheets, folosește Webhook.

**Locație:** `226-receive-google-sheet-data-via-rest-api`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 🌐 Webhook
- **Integrări:** Google Sheets, Webhook

### 2393-save-n8n-cloud-invoices-received-in-gmail-in-google-drive

> Se declanșează de Gmail Trigger. folosește HTTP API, actualizează date în Google Drive, folosește Google Drive, folosește HTML. Detalii: Setup
1. Setup your **Gmail** and **Google Drive** credentials
1. Create a free account at https://pdflayer.com/
2. Insert your **pdflayer** API key into the `Setup` node
3. Insert the URL to the wanted drive folder into the setup node (make sure to...

**Locație:** `2393-save-n8n-cloud-invoices-received-in-gmail-in-google-drive`

- **Noduri:** 13
- **Conexiuni:** 9
- **Integrări:** Google Drive, HTML, HTTP API

### 2494-generate-seo-keyword-search-volume-data-using-google-api

> Se declanșează manual. folosește HTTP API. Detalii: Generate SEO Keyword Search Volume Data using Google API

 Use Case
Generate accurate search volume data for SEO keyword research:
- You have a list of potential keywords to target for your website SEO but don't know their actual search volume
- You...

**Locație:** `2494-generate-seo-keyword-search-volume-data-using-google-api`

- **Noduri:** 12
- **Conexiuni:** 4
- **Declanșare:** 👆 Manual
- **Integrări:** HTTP API

### 2501-replace-images-in-google-docs-documents-and-download-as-pdf-docx

> Se declanșează manual. folosește HTTP API, folosește Google Drive, folosește Google Drive, descarcă din Google Drive. Detalii: Replace Images in Google Docs Documents and Download as PDF/Docx

 Use Case
Automate image replacement in Google Docs:
- You need to update document images dynamically
- You want to create multiple versions of a template with different images
- You...

**Locație:** `2501-replace-images-in-google-docs-documents-and-download-as-pdf-docx`

- **Noduri:** 18
- **Conexiuni:** 8
- **Declanșare:** 👆 Manual
- **Integrări:** Google Drive, HTTP API

### 2517-send-google-analytics-data-to-a-i-to-analyze-then-save-results-in-baserow

> Rulează programat (schedule). folosește Google Analytics, folosește HTTP API, creează înregistrări în Baserow. Detalii: Send Google analytics to A.I. and save results to baserow

This workflow will check for country views, page engagement and google search console results. It will take this week's data and compare it to last week's data.

[You can read more about...

**Locație:** `2517-send-google-analytics-data-to-a-i-to-analyze-then-save-results-in-baserow`

- **Noduri:** 22
- **Conexiuni:** 17
- **Declanșare:** ⏰ Programat, 👆 Manual
- **Integrări:** Baserow, Google Analytics, HTTP API

### 2549-automate-google-analytics-reporting

> Se declanșează manual. folosește Google Analytics, folosește Gmail. Detalii: Aggregate Google Analytics data and Email the results

This workflow will check for country views, page engagement and google search console results. It will take this week's data and compare it to last week's data.

[Credit to Keith Rumjahn for the...

**Locație:** `2549-automate-google-analytics-reporting`

- **Noduri:** 23
- **Conexiuni:** 17
- **Declanșare:** ⏰ Programat, 👆 Manual
- **Integrări:** Gmail, Google Analytics

### 2550-waitlist-form-stored-in-googlesheet-with-email-verification-step

> Se declanșează la trimiterea unui formular n8n. folosește Google Sheets, folosește Email SMTP, folosește form, folosește Crypto. Detalii: Instructions

This automation streamlines the process of **collecting user information** using a Form Node, enabling individuals to join a **waitlist managed via Google Sheets.**

It also **generates a verification code**, prompting users to input...

**Locație:** `2550-waitlist-form-stored-in-googlesheet-with-email-verification-step`

- **Noduri:** 19
- **Conexiuni:** 13
- **Integrări:** Crypto, Email SMTP, Google Sheets, form

### 2556-exponential-backoff-for-google-apis

> Se declanșează manual. folosește Google Sheets. Detalii: Exponential Backoff for Google APIs 
 Connect these nodes to any Google API node such as the Google Sheets node example in this workflow

**Locație:** `2556-exponential-backoff-for-google-apis`

- **Noduri:** 8
- **Conexiuni:** 6
- **Declanșare:** 👆 Manual
- **Integrări:** Google Sheets

### 356-generate-and-insert-data-into-a-postgres-database

> Rulează programat (cron). folosește PostgreSQL.

**Locație:** `356-generate-and-insert-data-into-a-postgres-database`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** ⏰ Programat
- **Integrări:** PostgreSQL

### 357-send-sms-alerts-based-on-database-queries-twilio-and-postgres

> Rulează programat (cron). folosește PostgreSQL, folosește Twilio, actualizează date în PostgreSQL.

**Locație:** `357-send-sms-alerts-based-on-database-queries-twilio-and-postgres`

- **Noduri:** 5
- **Conexiuni:** 4
- **Declanșare:** ⏰ Programat
- **Integrări:** PostgreSQL, Twilio

### 428-add-a-task-to-google-tasks

> Se declanșează manual. folosește googleTasks.

**Locație:** `428-add-a-task-to-google-tasks`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** googleTasks

### 515-download-a-file-from-google-drive

> Se declanșează manual. descarcă din Google Drive, folosește writeBinaryFile.

**Locație:** `515-download-a-file-from-google-drive`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** 👆 Manual
- **Integrări:** Google Drive, writeBinaryFile

### 566-get-all-excel-workbooks

> Se declanșează manual. citește date din Microsoft Excel.

**Locație:** `566-get-all-excel-workbooks`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** Microsoft Excel

### 6-sync-data-between-multiple-google-spreadsheets

> Rulează programat (cron). folosește Google Sheets, actualizează date în Google Sheets.

**Locație:** `6-sync-data-between-multiple-google-spreadsheets`

- **Noduri:** 4
- **Conexiuni:** 2
- **Declanșare:** ⏰ Programat
- **Integrări:** Google Sheets

### 600-insert-and-read-data-from-google-sheets

> Se declanșează manual. adaugă date în Google Sheets, folosește Google Sheets.

**Locație:** `600-insert-and-read-data-from-google-sheets`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** Google Sheets

### 694-transform-data-in-google-sheets

> Se declanșează manual. actualizează date în Google Sheets, caută în Google Sheets, adaugă date în Google Sheets, folosește Google Sheets.

**Locație:** `694-transform-data-in-google-sheets`

- **Noduri:** 7
- **Conexiuni:** 6
- **Declanșare:** 👆 Manual
- **Integrări:** Google Sheets

### 770-automated-congratulations-with-google-sheets-twilio-and-n8n

> Rulează programat (cron). folosește Google Sheets, folosește Twilio.

**Locație:** `770-automated-congratulations-with-google-sheets-twilio-and-n8n`

- **Noduri:** 8
- **Conexiuni:** 6
- **Declanșare:** ⏰ Programat
- **Integrări:** Google Sheets, Twilio

### 839-create-update-and-get-a-document-in-google-cloud-firestore

> Se declanșează manual. creează înregistrări în googleFirebaseCloudFirestore, actualizează/creează în googleFirebaseCloudFirestore, folosește googleFirebaseCloudFirestore.

**Locație:** `839-create-update-and-get-a-document-in-google-cloud-firestore`

- **Noduri:** 6
- **Conexiuni:** 5
- **Declanșare:** 👆 Manual
- **Integrări:** googleFirebaseCloudFirestore

### 864-monitor-changes-in-google-sheets-every-45-mins

> Declanșare manuală sau nedeterminată. folosește Mattermost, folosește Google Sheets, folosește interval.

**Locație:** `864-monitor-changes-in-google-sheets-every-45-mins`

- **Noduri:** 4
- **Conexiuni:** 3
- **Integrări:** Google Sheets, Mattermost, interval

### 890-read-in-an-excel-spreadsheet-file

> Se declanșează manual. folosește Fișier Spreadsheet, folosește readBinaryFile.

**Locație:** `890-read-in-an-excel-spreadsheet-file`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** 👆 Manual
- **Integrări:** Fișier Spreadsheet, readBinaryFile

### 892-transfer-google-analytics-data-to-airtable-database

> Se declanșează manual. folosește Google Analytics, adaugă date în Airtable.

**Locație:** `892-transfer-google-analytics-data-to-airtable-database`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** Airtable, Google Analytics

### 980-load-data-into-spreadsheet-or-database

> Se declanșează manual.

**Locație:** `980-load-data-into-spreadsheet-or-database`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual

### excel-to-postgres

> Declanșare manuală sau nedeterminată. folosește readBinaryFile, folosește Fișier Spreadsheet, folosește PostgreSQL.

**Locație:** `excel-to-postgres`

- **Noduri:** 3
- **Conexiuni:** 2
- **Integrări:** Fișier Spreadsheet, PostgreSQL, readBinaryFile

### google-sheets-to-dropbox

> Declanșare manuală sau nedeterminată. folosește Google Sheets, folosește Fișier Spreadsheet, folosește Dropbox, folosește interval.

**Locație:** `google-sheets-to-dropbox`

- **Noduri:** 4
- **Conexiuni:** 3
- **Integrări:** Dropbox, Fișier Spreadsheet, Google Sheets, interval

---

## data-transformation

### 1045-etl-pipeline-for-text-processing

> Rulează programat (cron). caută în Twitter/X, folosește PostgreSQL, folosește mongoDb, folosește Slack (+1 altele).

**Locație:** `1045-etl-pipeline-for-text-processing`

- **Noduri:** 9
- **Conexiuni:** 7
- **Declanșare:** ⏰ Programat
- **Integrări:** PostgreSQL, Slack, Twitter/X, googleCloudNaturalLanguage, mongoDb

### 13-transform-xml-data-and-upload-to-dropbox

> Declanșare manuală sau nedeterminată. folosește XML, folosește HTTP API, folosește Dropbox.

**Locație:** `13-transform-xml-data-and-upload-to-dropbox`

- **Noduri:** 5
- **Conexiuni:** 4
- **Integrări:** Dropbox, HTTP API, XML

### 1537-convert-filemaker-data-api-to-flat-file-array

> Declanșare manuală sau nedeterminată.

**Locație:** `1537-convert-filemaker-data-api-to-flat-file-array`

- **Noduri:** 3
- **Conexiuni:** 2

### 160-convert-xml-to-json

> Se declanșează manual. folosește XML.

**Locație:** `160-convert-xml-to-json`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** 👆 Manual
- **Integrări:** XML

### 1902-convert-postgresql-table-to-csv

> Se declanșează manual. folosește Fișier Spreadsheet, folosește PostgreSQL.

**Locație:** `1902-convert-postgresql-table-to-csv`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** Fișier Spreadsheet, PostgreSQL

### 2037-convert-image-urls-to-an-uploaded-attachment-in-airtable

> Se declanșează manual. caută în Airtable, actualizează date în Airtable. Detalii: Read me
Super simple workflow to upload image URLs as attachments in Airtable. [Here's the example Airtable database I used for this workflow.](https://airtable.com/app5TBVbHPs64w5lE/shrcqQJEC56DV3I9b/tblTVTofgqfzqyIZk)

1. Set up your Airtable...

**Locație:** `2037-convert-image-urls-to-an-uploaded-attachment-in-airtable`

- **Noduri:** 4
- **Conexiuni:** 2
- **Declanșare:** 👆 Manual
- **Integrări:** Airtable

### 2222-convert-an-xml-file-to-json-via-webhook-call

> Se declanșează prin webhook HTTP. folosește Extracție Fișier, folosește Răspuns Webhook, folosește Webhook, folosește XML (+1 altele). Detalii: Response
Where possible we will be returning a JSON object.
```
{
  "status": "ok",
  "data": { // JSON DATA }
}
```
If there is an error
```
{
  "status": "error",
  "data": "error message to display"
}
```

**Locație:** `2222-convert-an-xml-file-to-json-via-webhook-call`

- **Noduri:** 12
- **Conexiuni:** 8
- **Declanșare:** 🌐 Webhook
- **Integrări:** Extracție Fișier, Răspuns Webhook, Slack, Webhook, XML

### 2294-convert-docx-to-pdf-using-convertapi

> Se declanșează manual. folosește Fișier Local, folosește HTTP API. Detalii: Authentication
Conversion requests must be authenticated. Please create 
[ConvertAPI account to get authentication secret](https://www.convertapi.com/a/signin)

Create a query auth credential with __secret__ as name and your secret from the...

**Locație:** `2294-convert-docx-to-pdf-using-convertapi`

- **Noduri:** 5
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** Fișier Local, HTTP API

### 2297-convert-docx-from-url-to-pdf-using-convertapi

> Se declanșează manual. folosește HTTP API, folosește Fișier Local. Detalii: Authentication
Conversion requests must be authenticated. Please create 
[ConvertAPI account to get authentication secret](https://www.convertapi.com/a/signin)

Create a query auth credential with `secret` as name and your secret from the convertAPI...

**Locație:** `2297-convert-docx-from-url-to-pdf-using-convertapi`

- **Noduri:** 6
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** Fișier Local, HTTP API

### 2298-merge-pdf-files-using-convertapi

> Se declanșează manual. folosește Fișier Local, folosește HTTP API. Detalii: Authentication
Conversion requests must be authenticated. Please create 
[ConvertAPI account to get authentication secret](https://www.convertapi.com/a/signin)

**Locație:** `2298-merge-pdf-files-using-convertapi`

- **Noduri:** 6
- **Conexiuni:** 4
- **Declanșare:** 👆 Manual
- **Integrări:** Fișier Local, HTTP API

### 2304-convert-xlsx-to-pdf-using-convertapi

> Se declanșează manual. folosește Fișier Local, folosește HTTP API. Detalii: Authentication
Conversion requests must be authenticated. Please create 
[ConvertAPI account to get authentication secret](https://www.convertapi.com/a/signin)

**Locație:** `2304-convert-xlsx-to-pdf-using-convertapi`

- **Noduri:** 5
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** Fișier Local, HTTP API

### 2305-convert-pptx-to-pdf-using-convertapi

> Se declanșează manual. folosește Fișier Local, folosește HTTP API. Detalii: Authentication
Conversion requests must be authenticated. Please create 
[ConvertAPI account to get authentication secret](https://www.convertapi.com/a/signin)

**Locație:** `2305-convert-pptx-to-pdf-using-convertapi`

- **Noduri:** 5
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** Fișier Local, HTTP API

### 2306-protect-pdf-with-the-password-using-convertapi

> Se declanșează manual. folosește Fișier Local, folosește HTTP API, folosește Google Drive. Detalii: Authentication
Conversion requests must be authenticated. Please create 
[ConvertAPI account to get authentication secret](https://www.convertapi.com/a/signin)

**Locație:** `2306-protect-pdf-with-the-password-using-convertapi`

- **Noduri:** 7
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** Fișier Local, Google Drive, HTTP API

### 2308-convert-airtable-rich-text-markdown-field-to-html

> Se declanșează prin webhook HTTP. obține date din Airtable, folosește Markdown, actualizează date în Airtable, caută în Airtable (+1 altele). Detalii: Tutorial
[Youtube video](https://www.youtube.com/watch?v=PAoxZjICd7o)

**Locație:** `2308-convert-airtable-rich-text-markdown-field-to-html`

- **Noduri:** 9
- **Conexiuni:** 6
- **Declanșare:** 🌐 Webhook
- **Integrări:** Airtable, Markdown, Webhook

### 2310-convert-web-page-to-pdf-using-convertapi

> Se declanșează manual. folosește HTTP API, folosește Fișier Local. Detalii: Authentication
Conversion requests must be authenticated. Please create 
[ConvertAPI account to get authentication secret](https://www.convertapi.com/a/signin)

**Locație:** `2310-convert-web-page-to-pdf-using-convertapi`

- **Noduri:** 5
- **Conexiuni:** 2
- **Declanșare:** 👆 Manual
- **Integrări:** Fișier Local, HTTP API

### 2314-convert-html-to-pdf-using-convertapi

> Se declanșează manual. folosește Fișier Local, folosește HTTP API. Detalii: Authentication
Conversion requests must be authenticated. Please create 
[ConvertAPI account to get authentication secret](https://www.convertapi.com/a/signin)

**Locație:** `2314-convert-html-to-pdf-using-convertapi`

- **Noduri:** 6
- **Conexiuni:** 4
- **Declanșare:** 👆 Manual
- **Integrări:** Fișier Local, HTTP API

### 2316-convert-image-to-pdf-using-convertapi

> Se declanșează manual. folosește Fișier Local, folosește HTTP API. Detalii: Authentication
Conversion requests must be authenticated. Please create 
[ConvertAPI account to get authentication secret](https://www.convertapi.com/a/signin)

**Locație:** `2316-convert-image-to-pdf-using-convertapi`

- **Noduri:** 5
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** Fișier Local, HTTP API

### 2317-convert-pdf-to-pdfa-using-convertapi

> Se declanșează manual. folosește Fișier Local, folosește HTTP API. Detalii: Authentication
Conversion requests must be authenticated. Please create 
[ConvertAPI account to get authentication secret](https://www.convertapi.com/a/signin)

**Locație:** `2317-convert-pdf-to-pdfa-using-convertapi`

- **Noduri:** 5
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** Fișier Local, HTTP API

### 2345-convert-baserow-rich-text-markdown-field-to-html

> Se declanșează prin webhook HTTP. obține date din Baserow, actualizează date în Baserow, folosește Baserow, folosește Webhook (+1 altele). Detalii: Tutorial
[Youtube video](https://www.youtube.com/watch?v=PAoxZjICd7o)

**Locație:** `2345-convert-baserow-rich-text-markdown-field-to-html`

- **Noduri:** 9
- **Conexiuni:** 6
- **Declanșare:** 🌐 Webhook
- **Integrări:** Baserow, Markdown, Webhook

### 2513-convert-image-files-jpg-png-jpeg-to-urls-and-reduce-file-size-with-resmush-it-and-imgbb

> Declanșare manuală sau nedeterminată. folosește HTTP API, folosește OpenAI. Detalii: Convert Image Files (JPG, PNG, JPEG) to URLs and Reduce File Size

 Use Case
Transform and optimize images for web use:
- You need to host local images online
- You want to reduce image file sizes automatically
- You need image URLs for web...

**Locație:** `2513-convert-image-files-jpg-png-jpeg-to-urls-and-reduce-file-size-with-resmush-it-and-imgbb`

- **Noduri:** 11
- **Conexiuni:** 5
- **Integrări:** HTTP API, OpenAI

### 575-convert-a-date-from-one-format-to-another

> Se declanșează manual. folosește Date/Time.

**Locație:** `575-convert-a-date-from-one-format-to-another`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** Date/Time

### 661-convert-the-json-data-received-from-the-cocktaildb-api-in-xml

> Se declanșează manual. folosește HTTP API, folosește XML.

**Locație:** `661-convert-the-json-data-received-from-the-cocktaildb-api-in-xml`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** 👆 Manual
- **Integrări:** HTTP API, XML

### 763-convert-an-array-into-an-array-of-objects

> Declanșare manuală sau nedeterminată.

**Locație:** `763-convert-an-array-into-an-array-of-objects`

- **Noduri:** 2
- **Conexiuni:** 1

### xml-to-dropbox

> Declanșare manuală sau nedeterminată. folosește XML, folosește HTTP API, folosește Dropbox.

**Locație:** `xml-to-dropbox`

- **Noduri:** 5
- **Conexiuni:** 4
- **Integrări:** Dropbox, HTTP API, XML

---

## document-processing

### 1083-create-an-event-file-and-send-it-as-an-email-attachment

> Se declanșează manual. folosește iCal, folosește Email SMTP.

**Locație:** `1083-create-an-event-file-and-send-it-as-an-email-attachment`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** 👆 Manual
- **Integrări:** Email SMTP, iCal

### 1282-send-a-file-from-s3-to-aws-textract

> Se declanșează manual. folosește awsTextract, folosește awsS3.

**Locație:** `1282-send-a-file-from-s3-to-aws-textract`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** 👆 Manual
- **Integrări:** awsS3, awsTextract

### 1375-create-a-document-in-outline-for-each-new-gitlab-release

> Se declanșează de gitlabTrigger. folosește HTTP API.

**Locație:** `1375-create-a-document-in-outline-for-each-new-gitlab-release`

- **Noduri:** 3
- **Conexiuni:** 2
- **Integrări:** HTTP API

### 1394-transcribe-audio-files-from-cloud-storage

> Se declanșează de googleDriveTrigger. adaugă date în Google Sheets, obține date din awsTranscribe, folosește awsTranscribe, încarcă fișiere în awsS3 (+1 altele).

**Locație:** `1394-transcribe-audio-files-from-cloud-storage`

- **Noduri:** 8
- **Conexiuni:** 7
- **Integrări:** Google Sheets, awsS3, awsTranscribe

### 1407-simple-file-based-key-value-store-writekey

> Se declanșează manual. folosește writeBinaryFile, folosește readBinaryFiles, folosește moveBinaryData.

**Locație:** `1407-simple-file-based-key-value-store-writekey`

- **Noduri:** 10
- **Conexiuni:** 9
- **Declanșare:** 👆 Manual
- **Integrări:** moveBinaryData, readBinaryFiles, writeBinaryFile

### 1408-simple-file-based-key-value-store-getkey

> Se declanșează manual. folosește readBinaryFile, folosește moveBinaryData.

**Locație:** `1408-simple-file-based-key-value-store-getkey`

- **Noduri:** 5
- **Conexiuni:** 4
- **Declanșare:** 👆 Manual
- **Integrări:** moveBinaryData, readBinaryFile

### 1731-export-csv-file-to-json

> Se declanșează manual. folosește readBinaryFile, folosește Fișier Spreadsheet, folosește moveBinaryData, folosește writeBinaryFile.

**Locație:** `1731-export-csv-file-to-json`

- **Noduri:** 5
- **Conexiuni:** 4
- **Declanșare:** 👆 Manual
- **Integrări:** Fișier Spreadsheet, moveBinaryData, readBinaryFile, writeBinaryFile

### 1734-import-a-json-file-from-gmail-into-a-spreadsheet

> Declanșare manuală sau nedeterminată. citește date din Gmail, folosește Fișier Spreadsheet, folosește moveBinaryData. Detalii: JSON file > Sheets

**Locație:** `1734-import-a-json-file-from-gmail-into-a-spreadsheet`

- **Noduri:** 4
- **Conexiuni:** 2
- **Integrări:** Fișier Spreadsheet, Gmail, moveBinaryData

### 1791-transfer-json-data-to-csv-file

> Declanșare manuală sau nedeterminată. adaugă date în Google Sheets, folosește readBinaryFile, folosește moveBinaryData.

**Locație:** `1791-transfer-json-data-to-csv-file`

- **Noduri:** 3
- **Conexiuni:** 2
- **Integrări:** Google Sheets, moveBinaryData, readBinaryFile

### 1914-export-sql-table-into-csv-file

> Se declanșează manual. folosește Microsoft SQL, folosește Fișier Spreadsheet. Detalii: Save SQL table as a CSV file
 You can send it via e-mail, upload to the file storage or download on your computer.
 Just connect one or two extra n8n Nodes here!

**Locație:** `1914-export-sql-table-into-csv-file`

- **Noduri:** 5
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** Fișier Spreadsheet, Microsoft SQL

### 1920-respond-with-file-download-to-incoming-http-request

> Se declanșează prin webhook HTTP. folosește Webhook, folosește HTTP API, folosește Răspuns Webhook.

**Locație:** `1920-respond-with-file-download-to-incoming-http-request`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** 🌐 Webhook
- **Integrări:** HTTP API, Răspuns Webhook, Webhook

### 1933-push-json-data-into-an-app-or-to-spreadsheet-file

> Se declanșează manual. folosește HTTP API, folosește Fișier Spreadsheet, adaugă date în Google Sheets. Detalii: 👋 How to use this template
This template shows how you can load JSON data from an API and load it into an App (Google Sheets) or convert to a file. Here's how to use it:

1. Open the `Google Sheets` node and add a credential (or disabled the...

**Locație:** `1933-push-json-data-into-an-app-or-to-spreadsheet-file`

- **Noduri:** 8
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** Fișier Spreadsheet, Google Sheets, HTTP API

### 1942-push-and-update-files-in-github

> Se declanșează manual. folosește GitHub, folosește Comandă Shell, folosește git, folosește git (+3 altele). Detalii: Please update the path to the local repository and connect this node to the upper or lower parts of the workflow

**Locație:** `1942-push-and-update-files-in-github`

- **Noduri:** 13
- **Conexiuni:** 7
- **Declanșare:** 👆 Manual
- **Integrări:** Comandă Shell, GitHub, git

### 1949-create-2-xml-files-with-and-without-xml-attributes

> Se declanșează manual. folosește mySql, folosește XML, folosește moveBinaryData, folosește writeBinaryFile. Detalii: Simple conversion to XML

**Locație:** `1949-create-2-xml-files-with-and-without-xml-attributes`

- **Noduri:** 13
- **Conexiuni:** 10
- **Declanșare:** 👆 Manual
- **Integrări:** XML, moveBinaryData, mySql, writeBinaryFile

### 1967-prepare-csv-files-with-gpt-4

> Se declanșează manual. folosește OpenAI, folosește Fișier Spreadsheet, folosește writeBinaryFile, folosește moveBinaryData. Detalii: This is a helper workflow to create 3 CSV files
 Feel free to adapt as needed
 Some mock data from GPT is pinned for convenience

**Locație:** `1967-prepare-csv-files-with-gpt-4`

- **Noduri:** 11
- **Conexiuni:** 9
- **Declanșare:** 👆 Manual
- **Integrări:** Fișier Spreadsheet, OpenAI, moveBinaryData, writeBinaryFile

### 2451-download-and-compress-folder-from-s3-to-zip-file

> Se declanșează manual. citește date din awsS3, folosește awsS3, folosește Compresie. Detalii: Instructions

This workflow downloads all Files from a specific folder in a S3 Bucket and compresses them so you can download it via n8n or do further processings.

Fill in your **Credentials and Settings** in the Nodes marked with...

**Locație:** `2451-download-and-compress-folder-from-s3-to-zip-file`

- **Noduri:** 6
- **Conexiuni:** 4
- **Declanșare:** 👆 Manual
- **Integrări:** Compresie, awsS3

### 2568-upsert-huge-documents-in-a-vector-store-with-supabase-and-notion

> Se declanșează prin mesaj de chat. folosește OpenAI Embeddings, folosește textSplitterTokenSplitter, folosește LangChain Retrieval QA, folosește Vector Retriever (+5 altele). Detalii: Store additional meta data with each embed, especially the Notion ID, which can be later used to find all belonging entries of one page, even if they got split into multiple embeds.

**Locație:** `2568-upsert-huge-documents-in-a-vector-store-with-supabase-and-notion`

- **Noduri:** 34
- **Conexiuni:** 18
- **Declanșare:** ⏰ Programat
- **Integrări:** Document Loader, LangChain Retrieval QA, Notion, OpenAI Chat, OpenAI Embeddings, Supabase, Supabase Vector, Vector Retriever, textSplitterTokenSplitter

### 2621-ai-agent-to-chat-with-files-in-supabase-storage

> Se declanșează manual. folosește HTTP API, folosește Document Loader, folosește Text Splitter, folosește Extracție Fișier (+7 altele). Detalii: Set up steps

1. **Fetch File List from Supabase**:
   - Use Supabase to retrieve the stored file list from a specified bucket.
   - Add logic to manage empty folder placeholders returned by Supabase, avoiding incorrect processing.

2. **Compare and...

**Locație:** `2621-ai-agent-to-chat-with-files-in-supabase-storage`

- **Noduri:** 33
- **Conexiuni:** 21
- **Declanșare:** 👆 Manual
- **Integrări:** AI Agent, Document Loader, Extracție Fișier, HTTP API, OpenAI Chat, OpenAI Embeddings, Supabase, Supabase Vector, Text Splitter, Vector Store Tool

### 450-get-the-community-profile-of-a-repository

> Se declanșează manual. folosește GitHub.

**Locație:** `450-get-the-community-profile-of-a-repository`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** GitHub

### 503-insert-a-document-in-mongodb

> Se declanșează manual. folosește mongoDb.

**Locație:** `503-insert-a-document-in-mongodb`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** 👆 Manual
- **Integrări:** mongoDb

### 577-read-a-file-from-disk

> Se declanșează manual. folosește readBinaryFile.

**Locație:** `577-read-a-file-from-disk`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** readBinaryFile

### 578-read-multiple-files-from-disk

> Se declanșează manual. folosește readBinaryFiles.

**Locație:** `578-read-multiple-files-from-disk`

- **Noduri:** 2
- **Conexiuni:** 1
- **Declanșare:** 👆 Manual
- **Integrări:** readBinaryFiles

### 585-extract-text-from-a-pdf-file

> Se declanșează manual. folosește readBinaryFile, folosește readPDF.

**Locație:** `585-extract-text-from-a-pdf-file`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** 👆 Manual
- **Integrări:** readBinaryFile, readPDF

### 586-read-a-spreadsheet-file

> Se declanșează manual. folosește Fișier Spreadsheet, folosește readBinaryFile.

**Locație:** `586-read-a-spreadsheet-file`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** 👆 Manual
- **Integrări:** Fișier Spreadsheet, readBinaryFile

### 590-write-a-file-to-the-host-machine

> Se declanșează manual. folosește HTTP API, folosește writeBinaryFile.

**Locație:** `590-write-a-file-to-the-host-machine`

- **Noduri:** 3
- **Conexiuni:** 2
- **Declanșare:** 👆 Manual
- **Integrări:** HTTP API, writeBinaryFile

### 663-download-a-file-and-upload-it-to-an-ftp-server

> Se declanșează manual. încarcă fișiere în FTP, listează date din FTP, folosește HTTP API.

**Locație:** `663-download-a-file-and-upload-it-to-an-ftp-server`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** FTP, HTTP API

### 674-manage-files-in-s3

> Se declanșează manual. folosește HTTP API, încarcă fișiere în s3, citește date din s3.

**Locație:** `674-manage-files-in-s3`

- **Noduri:** 4
- **Conexiuni:** 3
- **Declanșare:** 👆 Manual
- **Integrări:** HTTP API, s3

### 908-compress-binary-files-to-zip-format

> Se declanșează manual. folosește Dropbox, folosește Compresie, folosește HTTP API.

**Locație:** `908-compress-binary-files-to-zip-format`

- **Noduri:** 5
- **Conexiuni:** 4
- **Declanșare:** 👆 Manual
- **Integrări:** Compresie, Dropbox, HTTP API

### 913-execute-multiple-command-lines-based-on-text-file-inputs

> Se declanșează manual. folosește readBinaryFile, folosește moveBinaryData, folosește Comandă Shell.

**Locație:** `913-execute-multiple-command-lines-based-on-text-file-inputs`

- **Noduri:** 7
- **Conexiuni:** 6
- **Declanșare:** 👆 Manual
- **Integrări:** Comandă Shell, moveBinaryData, readBinaryFile

### 967-monitor-a-file-for-changes-and-send-an-alert

> Rulează programat (cron). folosește writeBinaryFile, folosește readBinaryFile, folosește moveBinaryData, folosește signl4 (+1 altele).

**Locație:** `967-monitor-a-file-for-changes-and-send-an-alert`

- **Noduri:** 9
- **Conexiuni:** 7
- **Declanșare:** ⏰ Programat
- **Integrări:** moveBinaryData, readBinaryFile, signl4, writeBinaryFile

---
