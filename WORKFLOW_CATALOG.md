# n8n Workflow Catalog

**Total Workflows:** 448
**Categories:** 7

## Table of Contents

- [analytics](#analytics) (6 workflows)
- [api-webhooks](#api-webhooks) (20 workflows)
- [automation](#automation) (252 workflows)
- [communication](#communication) (41 workflows)
- [data-integration](#data-integration) (75 workflows)
- [data-transformation](#data-transformation) (24 workflows)
- [document-processing](#document-processing) (30 workflows)

---

## analytics

### Unnamed Workflow

**Location:** `1690-markdown-report-generation`

- **Nodes:** 10
- **Connections:** 9
- **Trigger:** 👆 Manual
- **Integrations:** emailSend, httpRequest, itemLists, manualTrigger, markdown, moveBinaryData

### Unnamed Workflow

**Location:** `1692-markdown-timesheet-report-generation`

- **Nodes:** 10
- **Connections:** 9
- **Trigger:** 👆 Manual
- **Integrations:** emailSend, httpRequest, itemLists, manualTrigger, markdown, moveBinaryData

### Unnamed Workflow

**Location:** `1931-report-number-of-weekly-created-records-in-an-app`

- **Nodes:** 11
- **Connections:** 5
- **Trigger:** ⏰ Scheduled
- **Integrations:** filter, itemLists, notion, scheduleTrigger, slack, stickyNote

### Unnamed Workflow

**Location:** `1996-ai-customer-feedback-sentiment-analysis`

- **Nodes:** 9
- **Connections:** 3
- **Integrations:** formTrigger, googleSheets, openAi, stickyNote

### Unnamed Workflow

**Location:** `812-send-instagram-statistics-to-mattermost`

- **Nodes:** 5
- **Connections:** 4
- **Trigger:** ⏰ Scheduled
- **Integrations:** cron, dateTime, googleSheets, mattermost

### Unnamed Workflow

**Location:** `815-create-a-short-url-and-get-the-statistics-of-the-url`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, yourls

---

## api-webhooks

### Unnamed Workflow

**Location:** `119-webhook-returning-xml`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** 🌐 Webhook
- **Integrations:** respondToWebhook, webhook, xml

### Unnamed Workflow

**Location:** `1236-use-redis-to-rate-limit-your-low-code-api`

- **Nodes:** 11
- **Connections:** 8
- **Trigger:** 🌐 Webhook
- **Integrations:** airtable, redis, webhook

### Unnamed Workflow

**Location:** `1440-handle-verification-for-twitter-webhook`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** 🌐 Webhook
- **Integrations:** crypto, webhook

### Unnamed Workflow

**Location:** `1535-automate-testimonials-in-strapi-with-n8n`

- **Nodes:** 14
- **Connections:** 12
- **Trigger:** 🌐 Webhook
- **Integrations:** googleCloudNaturalLanguage, interval, strapi, twitter, webhook

### Unnamed Workflow

**Location:** `1588-manage-adobe-acrobat-e-signatures-with-webhooks`

- **Nodes:** 5
- **Connections:** 4
- **Trigger:** 🌐 Webhook
- **Integrations:** respondToWebhook, webhook

### Unnamed Workflow

**Location:** `159-send-rss-feed-data-to-webhook`

- **Nodes:** 18
- **Connections:** 17
- **Trigger:** ⏰ Scheduled, 👆 Manual
- **Integrations:** cron, httpRequest, manualTrigger, mongoDb, noOp, rssFeedRead, splitInBatches

### Unnamed Workflow

**Location:** `1748-pulling-data-from-services-that-n8n-doesnt-have-a-pre-built-integration-for`

- **Nodes:** 14
- **Connections:** 8
- **Trigger:** 👆 Manual
- **Integrations:** htmlExtract, httpRequest, itemLists, manualTrigger, stickyNote

### Unnamed Workflow

**Location:** `1750-creating-an-api-endpoint`

- **Nodes:** 5
- **Connections:** 2
- **Trigger:** 🌐 Webhook
- **Integrations:** respondToWebhook, stickyNote, webhook

### Unnamed Workflow

**Location:** `216-api-queries-data-from-graphql`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** 🌐 Webhook
- **Integrations:** graphql, webhook

### Unnamed Workflow

**Location:** `2274-low-code-api-for-flutterflow-apps`

- **Nodes:** 9
- **Connections:** 4
- **Trigger:** 🌐 Webhook
- **Integrations:** aggregate, n8nTrainingCustomerDatastore, respondToWebhook, stickyNote, webhook

### Unnamed Workflow

**Location:** `2419-visual-regression-testing-with-apify-and-ai-vision-model`

- **Nodes:** 34
- **Connections:** 22
- **Trigger:** ⏰ Scheduled, 👆 Manual
- **Integrations:** aggregate, filter, googleDrive, googleSheets, httpRequest, linear, manualTrigger, scheduleTrigger, splitInBatches, stickyNote (+1 more)

### Unnamed Workflow

**Location:** `2424-manipulate-pdf-with-adobe-developer-api`

- **Nodes:** 20
- **Connections:** 13
- **Trigger:** 👆 Manual
- **Integrations:** dropbox, executeWorkflowTrigger, httpRequest, manualTrigger, stickyNote, wait

### Unnamed Workflow

**Location:** `2435-monitor-multiple-github-repos-via-webhook`

- **Nodes:** 19
- **Connections:** 9
- **Trigger:** 🌐 Webhook, 👆 Manual
- **Integrations:** httpRequest, manualTrigger, slack, splitOut, stickyNote, telegram, webhook

### Unnamed Workflow

**Location:** `2658-api-schema-extractor`

- **Nodes:** 88
- **Connections:** 75
- **Trigger:** 👆 Manual
- **Integrations:** aggregate, executeWorkflow, executeWorkflowTrigger, executionData, filter, googleDrive, googleSheets, httpRequest, manualTrigger, removeDuplicates (+4 more)

### Unnamed Workflow

**Location:** `351-webhooks-with-mattermost`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** 🌐 Webhook
- **Integrations:** httpRequest, mattermost, webhook

### Unnamed Workflow

**Location:** `471-send-github-notifications-to-discord-webhook`

- **Nodes:** 6
- **Connections:** 5
- **Trigger:** ⏰ Scheduled
- **Integrations:** cron, discord, httpRequest

### Unnamed Workflow

**Location:** `558-get-the-last-five-spacex-launches-from-the-spacex-land-api-using-graphql`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** graphql, manualTrigger

### Unnamed Workflow

**Location:** `652-store-data-received-from-webhook-in-json`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** httpRequest, manualTrigger, moveBinaryData, writeBinaryFile

### Unnamed Workflow

**Location:** `779-create-update-and-get-an-entry-in-strapi`

- **Nodes:** 6
- **Connections:** 5
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, strapi

### Unnamed Workflow

**Location:** `968-create-an-event-in-posthog-when-a-request-is-made-to-a-webhook-url`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 🌐 Webhook
- **Integrations:** postHog, webhook

---

## automation

### Unnamed Workflow

**Location:** `100-using-the-merge-node-merge-by-key`

- **Nodes:** 5
- **Connections:** 4

### Unnamed Workflow

**Location:** `101-write-json-to-disk-binary`

- **Nodes:** 3
- **Connections:** 2
- **Integrations:** writeBinaryFile

### Unnamed Workflow

**Location:** `1041-create-update-and-get-an-object-from-bubble`

- **Nodes:** 3
- **Connections:** 2
- **Integrations:** bubble

### Unnamed Workflow

**Location:** `1047-send-location-updates-of-the-iss-every-minute-to-a-queue-in-aws-sqs`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** ⏰ Scheduled
- **Integrations:** awsSqs, cron, httpRequest

### Unnamed Workflow

**Location:** `1048-create-update-and-get-an-item-from-webflow`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, webflow

### Unnamed Workflow

**Location:** `1053-git-backup-of-workflows-and-credentials`

- **Nodes:** 7
- **Connections:** 6
- **Trigger:** ⏰ Scheduled, 👆 Manual
- **Integrations:** cron, executeCommand, manualTrigger

### Unnamed Workflow

**Location:** `1073-scrape-and-store-data-from-multiple-website-pages`

- **Nodes:** 23
- **Connections:** 23
- **Trigger:** 👆 Manual
- **Integrations:** executeCommand, functionItem, htmlExtract, httpRequest, manualTrigger, mongoDb, readBinaryFile, splitInBatches, uproc, writeBinaryFile

### Unnamed Workflow

**Location:** `1074-add-liked-songs-to-a-spotify-monthly-playlist`

- **Nodes:** 30
- **Connections:** 26
- **Trigger:** ⏰ Scheduled
- **Integrations:** filter, noOp, nocoDb, scheduleTrigger, splitInBatches, spotify, stickyNote

### Unnamed Workflow

**Location:** `1093-build-a-self-hosted-url-shortener-with-a-dashboard`

- **Nodes:** 26
- **Connections:** 19
- **Trigger:** 🌐 Webhook
- **Integrations:** airtable, crypto, webhook

### Unnamed Workflow

**Location:** `1110-add-articles-to-a-notion-list-by-accessing-a-discord-slash-command`

- **Nodes:** 7
- **Connections:** 5
- **Trigger:** 🌐 Webhook
- **Integrations:** htmlExtract, httpRequest, notion, webhook

### Unnamed Workflow

**Location:** `1111-create-transcription-jobs-using-aws-transcribe`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** 👆 Manual
- **Integrations:** awsS3, awsTranscribe, manualTrigger

### Unnamed Workflow

**Location:** `1114-create-update-and-get-a-task-in-microsoft-to-do`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, microsoftToDo

### Unnamed Workflow

**Location:** `1115-manage-changes-using-the-git-node`

- **Nodes:** 5
- **Connections:** 4
- **Trigger:** 👆 Manual
- **Integrations:** git, manualTrigger

### Unnamed Workflow

**Location:** `1130-add-a-check-condition-for-a-loop-in-n8n`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, noOp, twitter

### Unnamed Workflow

**Location:** `1132-trigger-a-build-in-travis-ci-when-code-changes-are-push-to-a-github-repo`

- **Nodes:** 4
- **Connections:** 2
- **Integrations:** githubTrigger, noOp, travisCi

### Unnamed Workflow

**Location:** `1160-merge-data-for-multiple-executions`

- **Nodes:** 6
- **Connections:** 5
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, rssFeedRead, splitInBatches

### Unnamed Workflow

**Location:** `1222-backup-workflows-to-github`

- **Nodes:** 11
- **Connections:** 9
- **Trigger:** ⏰ Scheduled
- **Integrations:** cron, github, httpRequest

### Unnamed Workflow

**Location:** `1243-avoid-rate-limiting-by-batching-http-requests`

- **Nodes:** 6
- **Connections:** 5
- **Trigger:** 👆 Manual
- **Integrations:** httpRequest, manualTrigger, n8nTrainingCustomerDatastore, noOp, splitInBatches, wait

### Unnamed Workflow

**Location:** `1254-deploy-site-when-new-content-gets-added`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 🌐 Webhook
- **Integrations:** netlify, webhook

### Unnamed Workflow

**Location:** `1274-assign-issues-to-interested-contributors`

- **Nodes:** 11
- **Connections:** 5
- **Integrations:** github, githubTrigger, noOp

### Unnamed Workflow

**Location:** `1298-get-top-5-products-on-product-hunt-every-hour`

- **Nodes:** 5
- **Connections:** 4
- **Trigger:** ⏰ Scheduled
- **Integrations:** cron, discord, graphql, itemLists

### Unnamed Workflow

**Location:** `1306-serve-a-static-html-page-when-a-link-is-accessed`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 🌐 Webhook
- **Integrations:** respondToWebhook, webhook

### Unnamed Workflow

**Location:** `1309-get-only-new-rss-with-photo`

- **Nodes:** 5
- **Connections:** 5
- **Trigger:** ⏰ Scheduled
- **Integrations:** cron, htmlExtract, rssFeedRead

### Unnamed Workflow

**Location:** `1325-transf-meeting-booking-into-notion-s-task-with-verified-information`

- **Nodes:** 3
- **Connections:** 2
- **Integrations:** calendlyTrigger, dropcontact, notion

### Unnamed Workflow

**Location:** `1328-use-regex-to-select-date`

- **Nodes:** 6
- **Connections:** 5
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, noOp

### Unnamed Workflow

**Location:** `1330-demonstrates-the-use-of-the-item-index-method`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** httpRequest, manualTrigger, n8nTrainingCustomerDatastore

### Unnamed Workflow

**Location:** `1349-create-an-issue-on-gitlab-on-every-github-release`

- **Nodes:** 6
- **Connections:** 6
- **Trigger:** ⏰ Scheduled
- **Integrations:** cron, github, gitlab

### Unnamed Workflow

**Location:** `1363-join-data-from-postgres-and-mysql`

- **Nodes:** 6
- **Connections:** 5
- **Trigger:** 🌐 Webhook
- **Integrations:** httpRequest, mySql, postgres, webhook

### Unnamed Workflow

**Location:** `1364-cron-routines-with-telegram`

- **Nodes:** 7
- **Connections:** 5
- **Trigger:** 🌐 Webhook, ⏰ Scheduled, 👆 Manual
- **Integrations:** cron, manualTrigger, mySql, telegram, webhook

### Unnamed Workflow

**Location:** `1373-create-a-new-user-in-notion-based-on-the-signup-form-submission`

- **Nodes:** 12
- **Connections:** 11
- **Trigger:** 🌐 Webhook
- **Integrations:** notion, webhook

### Unnamed Workflow

**Location:** `1374-create-a-new-team-for-a-project-in-notion`

- **Nodes:** 23
- **Connections:** 21
- **Trigger:** 🌐 Webhook
- **Integrations:** notion, webhook

### Unnamed Workflow

**Location:** `1376-share-jokes-on-twitter-automatically`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** ⏰ Scheduled
- **Integrations:** cron, httpRequest, twitter

### Unnamed Workflow

**Location:** `1381-search-and-download-torrents-using-transmission-daemon`

- **Nodes:** 8
- **Connections:** 6
- **Trigger:** 🌐 Webhook
- **Integrations:** functionItem, httpRequest, telegram, webhook

### Unnamed Workflow

**Location:** `1387-send-automated-daily-reminders-on-telegram`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** ⏰ Scheduled
- **Integrations:** cron, functionItem, telegram

### Unnamed Workflow

**Location:** `1393-extract-and-store-text-from-chat-images-using-aws-s3`

- **Nodes:** 4
- **Connections:** 2
- **Integrations:** airtable, awsS3, awsTextract, telegramTrigger

### Unnamed Workflow

**Location:** `1415-plex-automatic-qbittorent-throttler`

- **Nodes:** 21
- **Connections:** 16
- **Trigger:** 🌐 Webhook
- **Integrations:** httpRequest, noOp, webhook

### Unnamed Workflow

**Location:** `1418-create-an-rss-feed-based-on-a-website-s-content`

- **Nodes:** 12
- **Connections:** 11
- **Trigger:** 🌐 Webhook, 👆 Manual
- **Integrations:** dateTime, functionItem, htmlExtract, httpRequest, itemLists, manualTrigger, respondToWebhook, webhook

### Unnamed Workflow

**Location:** `1423-tiny-tiny-rss-new-stared-article-saved-to-wallabag`

- **Nodes:** 10
- **Connections:** 8
- **Trigger:** ⏰ Scheduled, 👆 Manual
- **Integrations:** cron, httpRequest, manualTrigger, noOp

### Unnamed Workflow

**Location:** `1425-send-a-random-recipe-once-a-day-to-telegram`

- **Nodes:** 15
- **Connections:** 12
- **Trigger:** ⏰ Scheduled
- **Integrations:** airtable, cron, httpRequest, telegram, telegramTrigger

### Unnamed Workflow

**Location:** `1442-automate-assigning-github-issues`

- **Nodes:** 10
- **Connections:** 5
- **Integrations:** github, githubTrigger, noOp

### Unnamed Workflow

**Location:** `1469-post-rss-feed-items-from-yesterday-to-slack`

- **Nodes:** 6
- **Connections:** 5
- **Trigger:** ⏰ Scheduled
- **Integrations:** cron, dateTime, rssFeedRead, slack

### Unnamed Workflow

**Location:** `1472-standup-bot-1-4-initialize`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, moveBinaryData, writeBinaryFile

### Unnamed Workflow

**Location:** `1473-standup-bot-2-4-read-config`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, moveBinaryData, readBinaryFile

### Unnamed Workflow

**Location:** `1474-standup-bot-3-4-override-config`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, moveBinaryData, writeBinaryFile

### Unnamed Workflow

**Location:** `1475-standup-bot-4-4-worker`

- **Nodes:** 29
- **Connections:** 23
- **Trigger:** 🌐 Webhook, ⏰ Scheduled
- **Integrations:** cron, executeWorkflow, httpRequest, mattermost, noOp, webhook

### Unnamed Workflow

**Location:** `1497-sum-or-aggregate-a-column-of-spreadsheet-or-table-data`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger

### Unnamed Workflow

**Location:** `1534-back-up-your-n8n-workflows-to-github`

- **Nodes:** 26
- **Connections:** 21
- **Trigger:** ⏰ Scheduled, 👆 Manual
- **Integrations:** executeWorkflow, executeWorkflowTrigger, github, httpRequest, manualTrigger, n8n, noOp, scheduleTrigger, slack, splitInBatches (+1 more)

### Unnamed Workflow

**Location:** `1554-get-data-from-multiple-rss-feeds-to-telegram`

- **Nodes:** 11
- **Connections:** 7
- **Trigger:** ⏰ Scheduled
- **Integrations:** cron, rssFeedRead, splitInBatches, telegram

### Unnamed Workflow

**Location:** `156-get-execute-command-data-and-transfer-to-json`

- **Nodes:** 3
- **Connections:** 1
- **Integrations:** executeCommand, functionItem

### Unnamed Workflow

**Location:** `1576-push-your-public-ip-to-namecheaps-dynamic-dns`

- **Nodes:** 7
- **Connections:** 6
- **Trigger:** ⏰ Scheduled
- **Integrations:** cron, httpRequest

### Unnamed Workflow

**Location:** `1599-send-new-youtube-channel-videos-to-telegram`

- **Nodes:** 5
- **Connections:** 4
- **Integrations:** interval, telegram, youTube

### Unnamed Workflow

**Location:** `1605-extend-n8n-with-additional-tools`

- **Nodes:** 21
- **Connections:** 16
- **Integrations:** executeCommand, httpRequest, readBinaryFile, spreadsheetFile, telegram, telegramTrigger, writeBinaryFile

### Unnamed Workflow

**Location:** `1621-split-out-binary-data`

- **Nodes:** 6
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** compression, httpRequest, manualTrigger, stickyNote

### Unnamed Workflow

**Location:** `1700-very-quick-quickstart`

- **Nodes:** 6
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, n8nTrainingCustomerDatastore, stickyNote

### Unnamed Workflow

**Location:** `1739-move-data-between-json-and-spreadsheets`

- **Nodes:** 14
- **Connections:** 8
- **Integrations:** gmail, googleSheets, httpRequest, moveBinaryData, spreadsheetFile, stickyNote, writeBinaryFile

### Unnamed Workflow

**Location:** `1744-working-with-dates-and-times`

- **Nodes:** 9
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** dateTime, manualTrigger, stickyNote

### Unnamed Workflow

**Location:** `1746-filtering-and-branching-data`

- **Nodes:** 9
- **Connections:** 2
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, n8nTrainingCustomerDatastore, stickyNote

### Unnamed Workflow

**Location:** `1747-joining-different-datasets`

- **Nodes:** 17
- **Connections:** 7
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, stickyNote

### Unnamed Workflow

**Location:** `1749-rate-limiting-and-waiting-for-external-events`

- **Nodes:** 13
- **Connections:** 9
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, n8nTrainingCustomerDatastore, n8nTrainingCustomerMessenger, noOp, splitInBatches, stickyNote, wait

### Unnamed Workflow

**Location:** `1751-preparing-data-to-be-sent-to-a-service`

- **Nodes:** 6
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** googleSheets, manualTrigger, n8nTrainingCustomerDatastore, stickyNote

### Unnamed Workflow

**Location:** `1799-rss-feed-for-ard-audiothek-podcasts`

- **Nodes:** 11
- **Connections:** 10
- **Trigger:** 🌐 Webhook, 👆 Manual
- **Integrations:** htmlExtract, httpRequest, itemLists, manualTrigger, respondToWebhook, webhook

### Unnamed Workflow

**Location:** `18-n8n-nodemation-basic-getting-started-on-the-workflow-canvas-1-3`

- **Nodes:** 3
- **Connections:** 2
- **Integrations:** functionItem, interval

### Unnamed Workflow

**Location:** `1814-merge-multiple-runs-into-one`

- **Nodes:** 7
- **Connections:** 6
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, n8nTrainingCustomerDatastore, noOp, splitInBatches, wait

### Unnamed Workflow

**Location:** `1839-import-csv-into-mysql`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, mySql, readBinaryFile, spreadsheetFile

### Unnamed Workflow

**Location:** `1856-turn-on-a-light-to-a-specific-color-on-any-update-in-github-repository`

- **Nodes:** 4
- **Connections:** 1
- **Integrations:** githubTrigger, homeAssistant, stickyNote

### Unnamed Workflow

**Location:** `1892-get-workflows-affected-by-0-214-3-migration`

- **Nodes:** 9
- **Connections:** 4
- **Trigger:** 🌐 Webhook
- **Integrations:** html, n8n, respondToWebhook, stickyNote, webhook

### Unnamed Workflow

**Location:** `1895-reddit-ai-digest`

- **Nodes:** 15
- **Connections:** 9
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, openAi, reddit, stickyNote

### Unnamed Workflow

**Location:** `19-n8n-nodemation-basic-creating-your-first-simple-workflow-2-3`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** 🌐 Webhook
- **Integrations:** functionItem, httpRequest, webhook

### Unnamed Workflow

**Location:** `1900-openai-examples-chatgpt-dalle-2-whisper-1-5-in-1`

- **Nodes:** 27
- **Connections:** 11
- **Trigger:** 👆 Manual
- **Integrations:** html, httpRequest, manualTrigger, openAi, readBinaryFiles, stickyNote

### Unnamed Workflow

**Location:** `1913-count-the-items-returned-by-a-node`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, n8nTrainingCustomerDatastore

### Unnamed Workflow

**Location:** `1916-merge-binary-objects-on-multiple-items-into-a-single-item`

- **Nodes:** 6
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** httpRequest, manualTrigger, stickyNote

### Unnamed Workflow

**Location:** `1918-load-data-into-snowflake`

- **Nodes:** 5
- **Connections:** 4
- **Trigger:** 👆 Manual
- **Integrations:** httpRequest, manualTrigger, snowflake, spreadsheetFile

### Unnamed Workflow

**Location:** `1943-comparing-data-with-the-compare-datasets-node`

- **Nodes:** 6
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** compareDatasets, manualTrigger, stickyNote

### Unnamed Workflow

**Location:** `1944-compare-sql-datasets`

- **Nodes:** 5
- **Connections:** 4
- **Trigger:** 👆 Manual
- **Integrations:** compareDatasets, manualTrigger, mySql

### Unnamed Workflow

**Location:** `1947-sql-to-xml-export-with-xsl-template-formatting`

- **Nodes:** 15
- **Connections:** 9
- **Trigger:** 🌐 Webhook
- **Integrations:** html, httpRequest, itemLists, moveBinaryData, mySql, respondToWebhook, stickyNote, webhook, xml

### Unnamed Workflow

**Location:** `1953-suggest-meeting-slots-using-ai`

- **Nodes:** 21
- **Connections:** 14
- **Integrations:** executeWorkflowTrigger, filter, gmail, gmailTrigger, googleCalendar, itemLists, stickyNote

### Unnamed Workflow

**Location:** `1955-custom-langchain-agent-written-in-javascript`

- **Nodes:** 10
- **Connections:** 6
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, stickyNote

### Unnamed Workflow

**Location:** `1956-ai-summarize-podcast-episode-and-enhance-using-wikipedia`

- **Nodes:** 19
- **Connections:** 14
- **Trigger:** 👆 Manual
- **Integrations:** gmail, itemLists, manualTrigger, stickyNote

### Unnamed Workflow

**Location:** `1957-force-ai-to-use-a-specific-output-format`

- **Nodes:** 11
- **Connections:** 6
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, stickyNote

### Unnamed Workflow

**Location:** `1961-slack-chatbot-powered-by-ai`

- **Nodes:** 14
- **Connections:** 7
- **Trigger:** 🌐 Webhook
- **Integrations:** noOp, slack, stickyNote, webhook

### Unnamed Workflow

**Location:** `1966-itemmatching-usage-example`

- **Nodes:** 8
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, n8nTrainingCustomerDatastore, stickyNote

### Unnamed Workflow

**Location:** `1997-authenticate-a-user-in-a-workflow-with-openid-connect`

- **Nodes:** 15
- **Connections:** 10
- **Trigger:** 🌐 Webhook
- **Integrations:** html, httpRequest, respondToWebhook, stickyNote, webhook

### Unnamed Workflow

**Location:** `1999-de-activate-n8n-workflows-using-telegram-commands`

- **Nodes:** 12
- **Connections:** 5
- **Integrations:** filter, n8n, stickyNote, telegramTrigger

### Unnamed Workflow

**Location:** `2007-telegram-echo-bot`

- **Nodes:** 3
- **Connections:** 1
- **Integrations:** stickyNote, telegram, telegramTrigger

### Unnamed Workflow

**Location:** `2036-domain-extractor`

- **Nodes:** 4
- **Connections:** 2
- **Integrations:** executeWorkflowTrigger, stickyNote

### Unnamed Workflow

**Location:** `2038-bookmarking-urls-in-your-browser-and-save-them-to-notion`

- **Nodes:** 4
- **Connections:** 1
- **Trigger:** 🌐 Webhook
- **Integrations:** notion, stickyNote, webhook

### Unnamed Workflow

**Location:** `2070-airtable-automate-recurring-tasks`

- **Nodes:** 14
- **Connections:** 9
- **Integrations:** airtable, airtableTrigger, httpRequest, slack, stickyNote

### Unnamed Workflow

**Location:** `2071-upload-bulk-records-from-csv-airtable-interfaces`

- **Nodes:** 17
- **Connections:** 10
- **Integrations:** airtable, airtableTrigger, httpRequest, spreadsheetFile, stickyNote

### Unnamed Workflow

**Location:** `2073-monday-com-useful-utilities`

- **Nodes:** 14
- **Connections:** 9
- **Trigger:** 👆 Manual
- **Integrations:** convertToFile, httpRequest, manualTrigger, mondayCom, splitOut

### Unnamed Workflow

**Location:** `2074-send-n8n-automation-errors-to-a-monday-com-board`

- **Nodes:** 5
- **Connections:** 4
- **Integrations:** dateTime, errorTrigger, mondayCom

### Unnamed Workflow

**Location:** `2086-retrieve-a-monday-com-row-and-all-data-in-a-single-node`

- **Nodes:** 26
- **Connections:** 19
- **Integrations:** aggregate, executeWorkflow, executeWorkflowTrigger, mondayCom, splitOut, stickyNote

### Unnamed Workflow

**Location:** `2105-get-all-members-of-a-discord-server-with-a-specific-role`

- **Nodes:** 16
- **Connections:** 12
- **Trigger:** 🌐 Webhook, 👆 Manual
- **Integrations:** discord, filter, googleSheets, manualTrigger, noOp, respondToWebhook, stickyNote, webhook

### Unnamed Workflow

**Location:** `2138-create-linear-tickets-from-notion-content`

- **Nodes:** 24
- **Connections:** 17
- **Trigger:** 🌐 Webhook
- **Integrations:** aggregate, filter, formTrigger, graphql, httpRequest, linear, notion, respondToWebhook, splitInBatches, stickyNote

### Unnamed Workflow

**Location:** `2140-add-product-ideas-to-notion-via-a-slack-command`

- **Nodes:** 8
- **Connections:** 3
- **Trigger:** 🌐 Webhook
- **Integrations:** httpRequest, notion, stickyNote, webhook

### Unnamed Workflow

**Location:** `2150-report-n8n-workflow-errors-to-slack`

- **Nodes:** 5
- **Connections:** 2
- **Integrations:** errorTrigger, slack, stickyNote

### Unnamed Workflow

**Location:** `2153-add-a-bug-to-linear-via-slack-command`

- **Nodes:** 10
- **Connections:** 4
- **Trigger:** 🌐 Webhook
- **Integrations:** httpRequest, stickyNote, webhook

### Unnamed Workflow

**Location:** `2154-classify-new-bugs-in-linear-with-openai-s-gpt-4-and-move-them-to-the-right-team`

- **Nodes:** 12
- **Connections:** 8
- **Integrations:** filter, httpRequest, linear, linearTrigger, slack, stickyNote

### Unnamed Workflow

**Location:** `2157-advanced-slackbot-with-n8n`

- **Nodes:** 34
- **Connections:** 19
- **Trigger:** 🌐 Webhook
- **Integrations:** executeWorkflow, executeWorkflowTrigger, httpRequest, postgres, slack, stickyNote, webhook

### Unnamed Workflow

**Location:** `2159-report-n8n-workflow-errors-to-telegram`

- **Nodes:** 5
- **Connections:** 2
- **Integrations:** errorTrigger, stickyNote, telegram

### Unnamed Workflow

**Location:** `2160-report-n8n-workflow-errors-directly-to-your-email`

- **Nodes:** 4
- **Connections:** 1
- **Integrations:** errorTrigger, gmail, stickyNote

### Unnamed Workflow

**Location:** `2162-whatsapp-starter-workflow`

- **Nodes:** 8
- **Connections:** 3
- **Trigger:** 🌐 Webhook
- **Integrations:** respondToWebhook, stickyNote, webhook, whatsApp

### Unnamed Workflow

**Location:** `2167-chatgpt-automatic-code-review-in-gitlab-mr`

- **Nodes:** 14
- **Connections:** 9
- **Trigger:** 🌐 Webhook
- **Integrations:** httpRequest, splitOut, stickyNote, webhook

### Unnamed Workflow

**Location:** `2192-streamline-your-zoom-meetings-with-secure-automated-stripe-payments`

- **Nodes:** 20
- **Connections:** 13
- **Integrations:** formTrigger, gmail, googleSheets, httpRequest, noOp, stickyNote, stripeTrigger, zoom

### Unnamed Workflow

**Location:** `2201-openai-assistant-workflow-upload-file-create-an-assistant-chat-with-it`

- **Nodes:** 10
- **Connections:** 2
- **Trigger:** 👆 Manual
- **Integrations:** googleDrive, manualTrigger, stickyNote

### Unnamed Workflow

**Location:** `2223-set-credentials-dynamically-using-expressions`

- **Nodes:** 7
- **Connections:** 2
- **Trigger:** 🌐 Webhook
- **Integrations:** formTrigger, nasa, respondToWebhook, stickyNote

### Unnamed Workflow

**Location:** `2276-send-http-requests-to-a-list-of-urls`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** ⏰ Scheduled
- **Integrations:** httpRequest, scheduleTrigger, splitOut

### Unnamed Workflow

**Location:** `2289-restore-backed-up-workflows-from-github-to-n8n`

- **Nodes:** 17
- **Connections:** 10
- **Trigger:** 👆 Manual
- **Integrations:** github, manualTrigger, n8n, noOp, stickyNote

### Unnamed Workflow

**Location:** `2295-export-n8n-cloud-execution-data-to-csv`

- **Nodes:** 7
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** convertToFile, manualTrigger, n8n, noOp, stickyNote

### Unnamed Workflow

**Location:** `2312-attach-a-default-error-handler-to-all-active-workflows`

- **Nodes:** 11
- **Connections:** 6
- **Trigger:** ⏰ Scheduled
- **Integrations:** errorTrigger, gmail, n8n, scheduleTrigger, stickyNote

### Unnamed Workflow

**Location:** `2343-introduction-to-the-http-tool`

- **Nodes:** 12
- **Connections:** 7
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, stickyNote

### Unnamed Workflow

**Location:** `2348-get-multiple-attachments-from-gmail-and-upload-them-to-gdrive`

- **Nodes:** 3
- **Connections:** 2
- **Integrations:** gmailTrigger, googleDrive

### Unnamed Workflow

**Location:** `2358-advanced-ai-demo-presented-at-ai-developers-14-meetup`

- **Nodes:** 39
- **Connections:** 19
- **Trigger:** 🌐 Webhook
- **Integrations:** gmail, gmailTrigger, httpRequest, noOp, slack, stickyNote, webhook

### Unnamed Workflow

**Location:** `2379-validate-totp-token-without-creating-a-credential`

- **Nodes:** 5
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, stickyNote

### Unnamed Workflow

**Location:** `2395-supabase-insertion-upsertion-retrieval`

- **Nodes:** 21
- **Connections:** 12
- **Integrations:** googleDrive, stickyNote, supabase

### Unnamed Workflow

**Location:** `2398-kb-tool-confluence-knowledge-base`

- **Nodes:** 7
- **Connections:** 2
- **Integrations:** executeWorkflowTrigger, httpRequest, stickyNote

### Unnamed Workflow

**Location:** `2400-ai-agent-with-charts-capabilities-using-openai-structured-output-and-quickchart`

- **Nodes:** 11
- **Connections:** 6
- **Integrations:** executeWorkflowTrigger, httpRequest, stickyNote

### Unnamed Workflow

**Location:** `2406-telegram-user-registration-workflow`

- **Nodes:** 15
- **Connections:** 7
- **Integrations:** executeWorkflowTrigger, googleSheets, stickyNote, telegram

### Unnamed Workflow

**Location:** `2408-user-verification-and-login-using-auth0`

- **Nodes:** 16
- **Connections:** 6
- **Trigger:** 🌐 Webhook
- **Integrations:** httpRequest, respondToWebhook, stickyNote, stopAndError, webhook

### Unnamed Workflow

**Location:** `2417-flux-ai-image-generator`

- **Nodes:** 19
- **Connections:** 10
- **Trigger:** 🌐 Webhook
- **Integrations:** formTrigger, httpRequest, respondToWebhook, s3, stickyNote

### Unnamed Workflow

**Location:** `2418-easy-image-captioning-with-gemini-1-5-pro`

- **Nodes:** 16
- **Connections:** 10
- **Trigger:** 👆 Manual
- **Integrations:** editImage, httpRequest, manualTrigger, stickyNote

### Unnamed Workflow

**Location:** `2420-automate-image-validation-tasks-using-ai-vision`

- **Nodes:** 11
- **Connections:** 7
- **Trigger:** 👆 Manual
- **Integrations:** editImage, googleDrive, manualTrigger, splitOut, stickyNote

### Unnamed Workflow

**Location:** `2436-siri-ai-agent-apple-shortcuts-powered-voice-template`

- **Nodes:** 7
- **Connections:** 3
- **Trigger:** 🌐 Webhook
- **Integrations:** respondToWebhook, stickyNote, webhook

### Unnamed Workflow

**Location:** `2456-text-automations-using-apple-shortcuts`

- **Nodes:** 10
- **Connections:** 7
- **Trigger:** 🌐 Webhook
- **Integrations:** respondToWebhook, stickyNote, webhook

### Unnamed Workflow

**Location:** `2467-narrating-over-a-video-using-multimodal-ai`

- **Nodes:** 21
- **Connections:** 13
- **Trigger:** 👆 Manual
- **Integrations:** aggregate, convertToFile, editImage, googleDrive, httpRequest, manualTrigger, splitInBatches, splitOut, stickyNote, wait

### Unnamed Workflow

**Location:** `2473-generate-seo-seed-keywords-using-ai`

- **Nodes:** 15
- **Connections:** 6
- **Trigger:** 👆 Manual
- **Integrations:** aggregate, manualTrigger, noOp, splitOut, stickyNote

### Unnamed Workflow

**Location:** `2485-automate-droplet-snapshots-on-digitalocean`

- **Nodes:** 17
- **Connections:** 5
- **Trigger:** ⏰ Scheduled
- **Integrations:** cron, filter, httpRequest, stickyNote

### Unnamed Workflow

**Location:** `2490-build-an-endpoint-to-perform-crud-operations-with-multiple-http-methods`

- **Nodes:** 18
- **Connections:** 8
- **Trigger:** 🌐 Webhook
- **Integrations:** airtable, respondToWebhook, stickyNote, webhook

### Unnamed Workflow

**Location:** `2504-wordpress-ai-chatbot-to-enhance-user-experience-with-supabase-and-openai`

- **Nodes:** 53
- **Connections:** 41
- **Trigger:** 🌐 Webhook, ⏰ Scheduled, 👆 Manual
- **Integrations:** aggregate, filter, httpRequest, manualTrigger, markdown, postgres, respondToWebhook, scheduleTrigger, splitInBatches, stickyNote (+2 more)

### Unnamed Workflow

**Location:** `2508-generate-sql-queries-from-schema-only-ai-powered`

- **Nodes:** 29
- **Connections:** 17
- **Trigger:** 👆 Manual
- **Integrations:** convertToFile, extractFromFile, manualTrigger, mySql, noOp, readWriteFile, stickyNote

### Unnamed Workflow

**Location:** `2527-sharepoint-list-fetch-with-oauth-token`

- **Nodes:** 5
- **Connections:** 3
- **Trigger:** ⏰ Scheduled
- **Integrations:** httpRequest, scheduleTrigger, stickyNote

### Unnamed Workflow

**Location:** `2535-get-long-lived-facebook-user-or-page-access-token`

- **Nodes:** 5
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** httpRequest, manualTrigger, stickyNote

### Unnamed Workflow

**Location:** `2536-pattern-for-parallel-sub-workflow-execution-followed-by-wait-for-all-loop`

- **Nodes:** 18
- **Connections:** 12
- **Trigger:** 🌐 Webhook, 👆 Manual
- **Integrations:** httpRequest, manualTrigger, noOp, respondToWebhook, splitInBatches, stickyNote, wait, webhook

### Unnamed Workflow

**Location:** `2538-demo-workflow-how-to-use-workflowstaticdata`

- **Nodes:** 9
- **Connections:** 6
- **Trigger:** 🌐 Webhook, ⏰ Scheduled
- **Integrations:** httpRequest, noOp, scheduleTrigger, stickyNote, webhook

### Unnamed Workflow

**Location:** `2551-add-new-clients-from-notion-to-clockify`

- **Nodes:** 4
- **Connections:** 2
- **Integrations:** clockify, notionTrigger, stickyNote

### Unnamed Workflow

**Location:** `2559-visualize-your-sql-agent-queries-with-openai-and-quickchart-io`

- **Nodes:** 16
- **Connections:** 9
- **Integrations:** executeWorkflow, executeWorkflowTrigger, httpRequest, stickyNote

### Unnamed Workflow

**Location:** `2566-conversational-interviews-with-ai-agents-and-n8n-forms`

- **Nodes:** 40
- **Connections:** 28
- **Trigger:** 🌐 Webhook
- **Integrations:** crypto, form, formTrigger, googleSheets, html, redis, respondToWebhook, splitOut, stickyNote, webhook

### Unnamed Workflow

**Location:** `2576-import-productboard-notes-companies-and-features-into-snowflake`

- **Nodes:** 35
- **Connections:** 28
- **Trigger:** ⏰ Scheduled
- **Integrations:** httpRequest, scheduleTrigger, slack, snowflake, splitInBatches, splitOut, stickyNote

### Unnamed Workflow

**Location:** `2604-time-logging-on-clockify-using-slack`

- **Nodes:** 16
- **Connections:** 14
- **Integrations:** executionData, slack, slackTrigger

### Unnamed Workflow

**Location:** `2612-ai-agent-to-chat-with-supabase-postgresql-db`

- **Nodes:** 11
- **Connections:** 5
- **Integrations:** postgresTool, stickyNote

### Unnamed Workflow

**Location:** `2649-prompt-based-object-detection-with-gemini-2-0`

- **Nodes:** 14
- **Connections:** 7
- **Trigger:** 👆 Manual
- **Integrations:** editImage, httpRequest, manualTrigger, stickyNote

### Unnamed Workflow

**Location:** `2653-ai-data-analyst-agent-for-spreadsheets-with-nocodb`

- **Nodes:** 10
- **Connections:** 7
- **Integrations:** httpRequest, nocoDbTool, stickyNote

### Unnamed Workflow

**Location:** `3-write-http-query-string-on-image`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** 🌐 Webhook
- **Integrations:** editImage, httpRequest, webhook

### Unnamed Workflow

**Location:** `359-sample-error-workflow`

- **Nodes:** 3
- **Connections:** 2
- **Integrations:** errorTrigger, mattermost, twilio

### Unnamed Workflow

**Location:** `371-notify-a-team-channel-about-new-software-releases-via-slack-and-github`

- **Nodes:** 2
- **Connections:** 1
- **Integrations:** githubTrigger, slack

### Unnamed Workflow

**Location:** `385-send-airtable-data-as-tasks-to-trello`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** airtable, bannerbear, manualTrigger, trello

### Unnamed Workflow

**Location:** `4-send-selected-github-events-to-slack`

- **Nodes:** 4
- **Connections:** 2
- **Integrations:** githubTrigger, slack

### Unnamed Workflow

**Location:** `434-extract-post-titles-from-a-blog`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** htmlExtract, httpRequest, manualTrigger

### Unnamed Workflow

**Location:** `437-perform-speech-to-text-on-recorded-audio-clips-using-wit-ai`

- **Nodes:** 2
- **Connections:** 1
- **Integrations:** httpRequest, readBinaryFile

### Unnamed Workflow

**Location:** `442-create-a-url-on-bitly`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** bitly, manualTrigger

### Unnamed Workflow

**Location:** `445-send-a-tweet-to-twitter`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, twitter

### Unnamed Workflow

**Location:** `454-get-a-pipeline-in-circleci`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** circleCi, manualTrigger

### Unnamed Workflow

**Location:** `458-run-a-sql-query-on-postgres`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, postgres

### Unnamed Workflow

**Location:** `459-create-a-new-issue-in-jira`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** jira, manualTrigger

### Unnamed Workflow

**Location:** `461-create-a-new-card-in-trello`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, trello

### Unnamed Workflow

**Location:** `465-get-details-of-a-gitlab-repository`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** gitlab, manualTrigger

### Unnamed Workflow

**Location:** `479-execute-an-sql-query-in-microsoft-sql`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, microsoftSql

### Unnamed Workflow

**Location:** `482-insert-data-into-a-new-row-for-a-table-in-coda`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** 👆 Manual
- **Integrations:** coda, manualTrigger

### Unnamed Workflow

**Location:** `485-create-a-task-in-clickup`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** clickUp, manualTrigger

### Unnamed Workflow

**Location:** `487-receive-updates-for-events-in-clickup`

- **Nodes:** 1
- **Connections:** 0
- **Integrations:** clickUpTrigger

### Unnamed Workflow

**Location:** `495-track-an-event-in-segment`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, segment

### Unnamed Workflow

**Location:** `510-invoke-an-aws-lambda-function`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** awsLambda, manualTrigger

### Unnamed Workflow

**Location:** `518-get-entries-from-a-cockpit-collection`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** cockpit, manualTrigger

### Unnamed Workflow

**Location:** `524-get-today-s-date-and-day-using-the-function-node`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger

### Unnamed Workflow

**Location:** `525-get-articles-from-hacker-news`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** hackerNews, manualTrigger

### Unnamed Workflow

**Location:** `526-assign-values-to-variables-using-the-set-node`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger

### Unnamed Workflow

**Location:** `527-receive-updates-for-github-events`

- **Nodes:** 1
- **Connections:** 0
- **Integrations:** githubTrigger

### Unnamed Workflow

**Location:** `528-receive-updates-for-gitlab-events`

- **Nodes:** 1
- **Connections:** 0
- **Integrations:** gitlabTrigger

### Unnamed Workflow

**Location:** `529-receive-updates-for-bitbucket-events`

- **Nodes:** 1
- **Connections:** 0
- **Integrations:** bitbucketTrigger

### Unnamed Workflow

**Location:** `544-create-an-image-procedurally-using-bannerbear`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** bannerbear, manualTrigger

### Unnamed Workflow

**Location:** `546-get-all-posts-from-wordpress`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, wordpress

### Unnamed Workflow

**Location:** `548-get-all-orders-in-shopify`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, shopify

### Unnamed Workflow

**Location:** `556-get-a-board-from-monday-com`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, mondayCom

### Unnamed Workflow

**Location:** `557-get-the-value-of-a-key-from-redis`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, redis

### Unnamed Workflow

**Location:** `559-create-a-new-folder-in-box`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** box, manualTrigger

### Unnamed Workflow

**Location:** `563-get-contributors-information-from-github-in-slack`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** 🌐 Webhook
- **Integrations:** graphql, slack, webhook

### Unnamed Workflow

**Location:** `565-create-a-folder-in-onedrive`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, microsoftOneDrive

### Unnamed Workflow

**Location:** `574-encrypt-some-data-using-the-crypto-node`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** crypto, manualTrigger

### Unnamed Workflow

**Location:** `576-get-information-of-an-image`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** 👆 Manual
- **Integrations:** editImage, httpRequest, manualTrigger

### Unnamed Workflow

**Location:** `581-execute-set-node-based-on-function-output`

- **Nodes:** 5
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger

### Unnamed Workflow

**Location:** `582-rename-a-key-in-n8n`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, renameKeys

### Unnamed Workflow

**Location:** `583-read-an-rss-feed`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, rssFeedRead

### Unnamed Workflow

**Location:** `588-execute-another-workflow`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** executeWorkflow, manualTrigger

### Unnamed Workflow

**Location:** `592-create-a-table-in-quest-db-and-insert-data`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, questDb

### Unnamed Workflow

**Location:** `597-create-a-table-in-cratedb-and-insert-data`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** crateDb, manualTrigger

### Unnamed Workflow

**Location:** `598-create-a-table-in-mysql-and-insert-data`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, mySql

### Unnamed Workflow

**Location:** `599-create-a-table-in-postgres-and-insert-data`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, postgres

### Unnamed Workflow

**Location:** `602-manage-users-automatically-in-reqres-in`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** httpRequest, manualTrigger

### Unnamed Workflow

**Location:** `632-nathan-your-n8n-personal-assistant`

- **Nodes:** 9
- **Connections:** 6
- **Integrations:** emailReadImap, emailSend, readBinaryFile, slack, spreadsheetFile

### Unnamed Workflow

**Location:** `635-export-wordpress-posts-to-spreadsheet`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, spreadsheetFile, wordpress, writeBinaryFile

### Unnamed Workflow

**Location:** `639-receive-server-sent-events`

- **Nodes:** 1
- **Connections:** 0
- **Integrations:** sseTrigger

### Unnamed Workflow

**Location:** `640-get-all-the-entries-from-contentful`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** contentful, manualTrigger

### Unnamed Workflow

**Location:** `643-get-all-releases-in-sentry`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, sentryIo

### Unnamed Workflow

**Location:** `655-merge-greetings-with-the-users-based-on-the-language`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger

### Unnamed Workflow

**Location:** `658-trigger-a-build-using-the-travisci-node`

- **Nodes:** 2
- **Connections:** 2
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, travisCi

### Unnamed Workflow

**Location:** `667-send-an-sms-using-the-mocean-node`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, mocean

### Unnamed Workflow

**Location:** `668-create-or-update-a-post-in-wordpress`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, wordpress

### Unnamed Workflow

**Location:** `685-create-update-and-get-an-issue-on-taiga`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, taiga

### Unnamed Workflow

**Location:** `686-receive-updates-when-an-event-occurs-in-taiga`

- **Nodes:** 1
- **Connections:** 0
- **Integrations:** taigaTrigger

### Unnamed Workflow

**Location:** `687-read-rss-feed-from-two-different-sources`

- **Nodes:** 4
- **Connections:** 4
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, rssFeedRead, splitInBatches

### Unnamed Workflow

**Location:** `688-execute-set-node-based-on-function-output`

- **Nodes:** 7
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, noOp

### Unnamed Workflow

**Location:** `693-display-project-data-on-a-smashing-dashboard`

- **Nodes:** 24
- **Connections:** 10
- **Trigger:** ⏰ Scheduled
- **Integrations:** cron, github, httpRequest

### Unnamed Workflow

**Location:** `695-get-local-datetime-into-function-node-using-moment-js`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger

### Unnamed Workflow

**Location:** `697-archive-spotify-s-discover-weekly-playlist`

- **Nodes:** 7
- **Connections:** 5
- **Trigger:** ⏰ Scheduled
- **Integrations:** scheduleTrigger, spotify

### Unnamed Workflow

**Location:** `700-purge-n8n-execution-history-located-in-mysql`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** ⏰ Scheduled, 👆 Manual
- **Integrations:** cron, manualTrigger, mySql

### Unnamed Workflow

**Location:** `701-manage-projects-in-clockify`

- **Nodes:** 5
- **Connections:** 4
- **Trigger:** 👆 Manual
- **Integrations:** clockify, manualTrigger

### Unnamed Workflow

**Location:** `702-extract-information-from-an-image-of-a-receipt`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** 👆 Manual
- **Integrations:** httpRequest, manualTrigger, mindee

### Unnamed Workflow

**Location:** `728-create-a-board-lists-and-a-card-in-wekan`

- **Nodes:** 6
- **Connections:** 5
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, wekan

### Unnamed Workflow

**Location:** `738-store-and-send-information-about-the-weather-for-any-city-via-sms`

- **Nodes:** 5
- **Connections:** 4
- **Trigger:** 🌐 Webhook
- **Integrations:** airtable, openWeatherMap, twilio, webhook

### Unnamed Workflow

**Location:** `739-detect-and-store-the-information-about-a-purchase-using-the-image-of-a-receipt`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** 🌐 Webhook
- **Integrations:** airtable, mindee, webhook

### Unnamed Workflow

**Location:** `741-extract-infromation-from-a-receipt-and-store-it-in-airtable`

- **Nodes:** 5
- **Connections:** 4
- **Integrations:** airtable, httpRequest, mindee, typeformTrigger

### Unnamed Workflow

**Location:** `744-create-update-and-get-activity-in-strava`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, strava

### Unnamed Workflow

**Location:** `750-send-updates-about-the-position-of-the-iss-every-minute-to-a-topic-in-kafka`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** ⏰ Scheduled
- **Integrations:** cron, httpRequest, kafka

### Unnamed Workflow

**Location:** `762-send-updates-about-the-position-of-the-iss-every-minute-to-a-topic-in-activemq`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** ⏰ Scheduled
- **Integrations:** amqp, cron, httpRequest

### Unnamed Workflow

**Location:** `765-create-a-new-member-update-the-infromation-create-a-note-and-post-in-orbit`

- **Nodes:** 5
- **Connections:** 4
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, orbit

### Unnamed Workflow

**Location:** `766-create-multiple-json-items-from-an-array`

- **Nodes:** 2
- **Connections:** 1

### Unnamed Workflow

**Location:** `767-create-an-array-of-objects`

- **Nodes:** 2
- **Connections:** 1

### Unnamed Workflow

**Location:** `768-get-all-the-stories-and-publish-them-in-storyblok`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, storyblok

### Unnamed Workflow

**Location:** `787-receive-updates-for-the-position-of-the-iss-and-push-it-to-a-firbase`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** ⏰ Scheduled
- **Integrations:** cron, googleFirebaseRealtimeDatabase, httpRequest

### Unnamed Workflow

**Location:** `797-translate-instructions-using-lingvanex`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** 👆 Manual
- **Integrations:** httpRequest, lingvaNex, manualTrigger

### Unnamed Workflow

**Location:** `8-handle-errors-from-a-different-workflow`

- **Nodes:** 2
- **Connections:** 1
- **Integrations:** errorTrigger, mailgun

### Unnamed Workflow

**Location:** `805-create-update-and-get-records-in-quick-base`

- **Nodes:** 6
- **Connections:** 5
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, quickbase

### Unnamed Workflow

**Location:** `806-get-synonyms-of-a-german-word`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, openThesaurus

### Unnamed Workflow

**Location:** `809-get-the-job-details-using-the-cortex-node`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** 👆 Manual
- **Integrations:** cortex, manualTrigger

### Unnamed Workflow

**Location:** `817-save-your-workflows-into-a-github-repository`

- **Nodes:** 16
- **Connections:** 16
- **Trigger:** ⏰ Scheduled, 👆 Manual
- **Integrations:** cron, github, httpRequest, manualTrigger, noOp, splitInBatches

### Unnamed Workflow

**Location:** `818-insert-and-update-data-in-airtable`

- **Nodes:** 6
- **Connections:** 5
- **Trigger:** 👆 Manual
- **Integrations:** airtable, manualTrigger

### Unnamed Workflow

**Location:** `823-n8n-workflow-backup-management-with-dropbox-and-airtable`

- **Nodes:** 19
- **Connections:** 18
- **Trigger:** ⏰ Scheduled, 👆 Manual
- **Integrations:** airtable, cron, dropbox, httpRequest, manualTrigger, moveBinaryData, noOp, splitInBatches

### Unnamed Workflow

**Location:** `824-create-a-table-and-insert-and-update-data-in-the-table-in-snowflake`

- **Nodes:** 6
- **Connections:** 5
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, snowflake

### Unnamed Workflow

**Location:** `825-create-update-and-get-a-post-in-ghost`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** ghost, manualTrigger

### Unnamed Workflow

**Location:** `828-send-the-astronomy-picture-of-the-day-daily-to-a-telegram-channel`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** ⏰ Scheduled
- **Integrations:** cron, nasa, telegram

### Unnamed Workflow

**Location:** `835-get-company-data-and-store-it-in-airtable`

- **Nodes:** 5
- **Connections:** 4
- **Trigger:** 👆 Manual
- **Integrations:** Brandfetch, airtable, manualTrigger

### Unnamed Workflow

**Location:** `837-track-changes-of-product-prices`

- **Nodes:** 25
- **Connections:** 24
- **Trigger:** ⏰ Scheduled
- **Integrations:** cron, emailSend, executeCommand, functionItem, htmlExtract, httpRequest, moveBinaryData, readBinaryFile, writeBinaryFile

### Unnamed Workflow

**Location:** `844-send-updates-about-the-position-of-the-iss-every-minute-to-a-topic-in-rabbitmq`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** ⏰ Scheduled
- **Integrations:** cron, httpRequest, rabbitmq

### Unnamed Workflow

**Location:** `847-create-update-and-get-a-product-from-woocommerce`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, wooCommerce

### Unnamed Workflow

**Location:** `853-weekly-coffee-chat-mattermost-version`

- **Nodes:** 6
- **Connections:** 4
- **Trigger:** ⏰ Scheduled
- **Integrations:** cron, googleCalendar, mattermost

### Unnamed Workflow

**Location:** `858-create-a-website-screenshot-and-send-via-telegram-channel`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, telegram, uproc

### Unnamed Workflow

**Location:** `867-create-add-an-attachment-and-send-a-draft-using-microsoft-outlook`

- **Nodes:** 5
- **Connections:** 4
- **Trigger:** 👆 Manual
- **Integrations:** httpRequest, manualTrigger, microsoftOutlook

### Unnamed Workflow

**Location:** `869-find-a-new-book-recommendations`

- **Nodes:** 13
- **Connections:** 11
- **Trigger:** ⏰ Scheduled, 👆 Manual
- **Integrations:** cron, emailSend, httpRequest, manualTrigger

### Unnamed Workflow

**Location:** `870-send-an-sms-to-a-number-whenever-you-go-out`

- **Nodes:** 2
- **Connections:** 1
- **Integrations:** pushcutTrigger, twilio

### Unnamed Workflow

**Location:** `875-send-tweets-every-minute-to-mattermost`

- **Nodes:** 5
- **Connections:** 4
- **Trigger:** ⏰ Scheduled
- **Integrations:** cron, mattermost, twitter

### Unnamed Workflow

**Location:** `879-access-data-from-bubble-application`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** httpRequest, manualTrigger

### Unnamed Workflow

**Location:** `880-receive-updates-of-the-position-of-the-iss-every-minute`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** ⏰ Scheduled
- **Integrations:** cron, httpRequest

### Unnamed Workflow

**Location:** `888-get-data-from-hacker-news-and-send-to-airtable-or-via-sms`

- **Nodes:** 8
- **Connections:** 6
- **Trigger:** ⏰ Scheduled
- **Integrations:** airtable, cron, hackerNews, lingvaNex, vonage

### Unnamed Workflow

**Location:** `900-add-a-datapoint-to-beeminder-on-strava-activity-update`

- **Nodes:** 2
- **Connections:** 1
- **Integrations:** beeminder, stravaTrigger

### Unnamed Workflow

**Location:** `930-create-update-and-get-a-post-via-discourse`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** discourse, manualTrigger

### Unnamed Workflow

**Location:** `934-insert-and-retrieve-data-from-a-table-in-stackby`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, stackby

### Unnamed Workflow

**Location:** `935-check-for-preview-for-a-link`

- **Nodes:** 5
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, noOp, peekalink

### Unnamed Workflow

**Location:** `959-create-a-collection-and-create-update-and-get-a-bookmark-in-raindrop`

- **Nodes:** 4
- **Connections:** 3
- **Integrations:** raindrop

### Unnamed Workflow

**Location:** `965-analyze-feedback-using-aws-comprehend-and-send-it-to-a-mattermost-channel`

- **Nodes:** 5
- **Connections:** 3
- **Integrations:** awsComprehend, mattermost, noOp, typeformTrigger

### Unnamed Workflow

**Location:** `987-create-asana-ticket-from-terminal-bash-dash`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** 🌐 Webhook
- **Integrations:** asana, webhook

### Unnamed Workflow

**Location:** `995-split-in-batches-node-noitemsleft-example`

- **Nodes:** 5
- **Connections:** 4
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, splitInBatches

### Unnamed Workflow

**Location:** `996-split-in-batches-node-currentrunindex-example`

- **Nodes:** 5
- **Connections:** 4
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, splitInBatches

### Unnamed Workflow

**Location:** `getting-started`

- **Nodes:** 3
- **Connections:** 2
- **Integrations:** functionItem, interval

---

## communication

### Unnamed Workflow

**Location:** `1105-check-to-do-on-notion-and-send-message-on-slack`

- **Nodes:** 6
- **Connections:** 4
- **Trigger:** ⏰ Scheduled
- **Integrations:** cron, noOp, notion, slack

### Unnamed Workflow

**Location:** `1109-add-positive-feedback-messages-to-a-table-in-notion`

- **Nodes:** 6
- **Connections:** 4
- **Integrations:** googleCloudNaturalLanguage, notion, slack, trello, typeformTrigger

### Unnamed Workflow

**Location:** `1255-send-notification-when-deployment-fails`

- **Nodes:** 2
- **Connections:** 1
- **Integrations:** netlifyTrigger, slack

### Unnamed Workflow

**Location:** `1344-save-email-attachments-to-nextcloud`

- **Nodes:** 3
- **Connections:** 2
- **Integrations:** emailReadImap, nextCloud

### Unnamed Workflow

**Location:** `1377-extract-url-from-an-email-address`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger

### Unnamed Workflow

**Location:** `1416-send-a-message-to-telegram-on-a-new-item-saved-to-reader`

- **Nodes:** 11
- **Connections:** 8
- **Trigger:** ⏰ Scheduled, 👆 Manual
- **Integrations:** cron, functionItem, httpRequest, manualTrigger, moveBinaryData, readBinaryFile, telegram, writeBinaryFile

### Unnamed Workflow

**Location:** `1453-parse-email-body-message`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** 👆 Manual
- **Integrations:** functionItem, manualTrigger

### Unnamed Workflow

**Location:** `1471-message-on-website-content-changed-in-telegram`

- **Nodes:** 7
- **Connections:** 5
- **Trigger:** ⏰ Scheduled
- **Integrations:** cron, httpRequest, noOp, telegram, wait

### Unnamed Workflow

**Location:** `1507-send-telegram-messages-on-rss-feed-read`

- **Nodes:** 7
- **Connections:** 5
- **Trigger:** ⏰ Scheduled
- **Integrations:** cron, noOp, rssFeedRead, telegram

### Unnamed Workflow

**Location:** `1528-send-a-discord-message-when-a-certain-onfleet-event-happens`

- **Nodes:** 2
- **Connections:** 1
- **Integrations:** discord, onfleetTrigger

### Unnamed Workflow

**Location:** `1532-send-onfleet-driver-signup-messages-in-slack`

- **Nodes:** 2
- **Connections:** 1
- **Integrations:** onfleetTrigger, slack

### Unnamed Workflow

**Location:** `154-listen-on-new-emails-on-a-imap-mailbox`

- **Nodes:** 5
- **Connections:** 4
- **Integrations:** emailReadImap, httpRequest, moveBinaryData, xml

### Unnamed Workflow

**Location:** `1765-get-slack-notifications-when-new-product-published-on-woocommerce`

- **Nodes:** 3
- **Connections:** 2
- **Integrations:** slack, wooCommerceTrigger

### Unnamed Workflow

**Location:** `1790-generate-dynamic-contents-for-emails-or-html-pages`

- **Nodes:** 8
- **Connections:** 6
- **Trigger:** 👆 Manual
- **Integrations:** emailSend, functionItem, itemLists, manualTrigger, n8nTrainingCustomerDatastore

### Unnamed Workflow

**Location:** `2032-poll-emails-using-jmap`

- **Nodes:** 7
- **Connections:** 4
- **Trigger:** 👆 Manual
- **Integrations:** httpRequest, manualTrigger, stickyNote

### Unnamed Workflow

**Location:** `2034-send-dingtalk-message-on-new-azure-devops-pull-request`

- **Nodes:** 5
- **Connections:** 3
- **Trigger:** 🌐 Webhook
- **Integrations:** httpRequest, mySql, stickyNote, webhook

### Unnamed Workflow

**Location:** `2212-zalando-price-patrol-monitor-price-evolution-with-email-notification`

- **Nodes:** 14
- **Connections:** 7
- **Trigger:** ⏰ Scheduled
- **Integrations:** formTrigger, gmail, googleSheets, httpRequest, scheduleTrigger, stickyNote

### Unnamed Workflow

**Location:** `2239-extract-domain-and-verify-email-syntax-on-the-go`

- **Nodes:** 5
- **Connections:** 2
- **Trigger:** 👆 Manual
- **Integrations:** debugHelper, manualTrigger, stickyNote

### Unnamed Workflow

**Location:** `2280-send-a-message-with-an-inline-embedded-image-with-gmail`

- **Nodes:** 10
- **Connections:** 5
- **Trigger:** 👆 Manual
- **Integrations:** extractFromFile, httpRequest, manualTrigger, stickyNote

### Unnamed Workflow

**Location:** `2471-create-single-new-masked-email-address-with-fastmail`

- **Nodes:** 7
- **Connections:** 5
- **Trigger:** 🌐 Webhook
- **Integrations:** httpRequest, respondToWebhook, stickyNote, webhook

### Unnamed Workflow

**Location:** `2478-send-a-message-via-a-lark-bot`

- **Nodes:** 6
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** httpRequest, manualTrigger, stickyNote

### Unnamed Workflow

**Location:** `2534-telegram-ai-bot-assistant-ready-made-template-for-voice-text-messages`

- **Nodes:** 15
- **Connections:** 9
- **Integrations:** stickyNote, telegram, telegramTrigger

### Unnamed Workflow

**Location:** `401-send-an-sms-whatsapp-message-with-twilio`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, twilio

### Unnamed Workflow

**Location:** `462-post-a-message-to-a-channel-in-rocketchat`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, rocketchat

### Unnamed Workflow

**Location:** `501-send-a-message-via-aws-sns`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** awsSns, manualTrigger

### Unnamed Workflow

**Location:** `507-send-an-email-using-aws-ses`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** awsSes, manualTrigger

### Unnamed Workflow

**Location:** `519-verify-email-deliverability-with-hunter`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** hunter, manualTrigger

### Unnamed Workflow

**Location:** `520-send-an-email-using-mailjet`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** mailjet, manualTrigger

### Unnamed Workflow

**Location:** `522-send-an-email-using-mailgun`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** mailgun, manualTrigger

### Unnamed Workflow

**Location:** `571-send-an-email-template-using-mandrill`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** mandrill, manualTrigger

### Unnamed Workflow

**Location:** `584-send-an-email`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** emailSend, manualTrigger

### Unnamed Workflow

**Location:** `680-create-update-and-send-a-message-to-a-channel-in-microsoft-teams`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, microsoftTeams

### Unnamed Workflow

**Location:** `772-send-bulk-messages-to-chats-in-telegram`

- **Nodes:** 5
- **Connections:** 5
- **Trigger:** 👆 Manual
- **Integrations:** googleSheets, manualTrigger, splitInBatches, telegram, wait

### Unnamed Workflow

**Location:** `774-send-daily-weather-updates-via-a-message-using-the-gotify-node`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** ⏰ Scheduled
- **Integrations:** cron, gotify, openWeatherMap

### Unnamed Workflow

**Location:** `796-send-daily-weather-updates-via-a-push-notification-using-spontit`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** ⏰ Scheduled
- **Integrations:** cron, openWeatherMap, spontit

### Unnamed Workflow

**Location:** `799-receive-a-mattermost-message-when-new-data-gets-added-to-airtable`

- **Nodes:** 2
- **Connections:** 1
- **Integrations:** airtableTrigger, mattermost

### Unnamed Workflow

**Location:** `814-receive-messages-from-a-topic-via-kafka-and-send-an-sms`

- **Nodes:** 4
- **Connections:** 2
- **Integrations:** kafkaTrigger, noOp, vonage

### Unnamed Workflow

**Location:** `832-create-a-channel-add-a-member-and-post-a-message-to-the-channel-on-mattermost`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, mattermost

### Unnamed Workflow

**Location:** `845-receive-messages-from-a-queue-via-rabbitmq-and-send-an-sms`

- **Nodes:** 4
- **Connections:** 2
- **Integrations:** noOp, rabbitmqTrigger, vonage

### Unnamed Workflow

**Location:** `857-create-screenshots-with-uproc-save-to-dropbox-and-send-by-email`

- **Nodes:** 10
- **Connections:** 9
- **Trigger:** 👆 Manual
- **Integrations:** awsSes, dropbox, functionItem, httpRequest, manualTrigger, uproc

### Unnamed Workflow

**Location:** `876-monitor-strava-and-send-email-updates`

- **Nodes:** 6
- **Connections:** 4
- **Trigger:** ⏰ Scheduled
- **Integrations:** cron, emailSend, noOp, strava

---

## data-integration

### Unnamed Workflow

**Location:** `1-insert-excel-data-to-postgres`

- **Nodes:** 3
- **Connections:** 2
- **Integrations:** postgres, readBinaryFile, spreadsheetFile

### Unnamed Workflow

**Location:** `11-add-data-from-google-sheet-to-dropbox`

- **Nodes:** 4
- **Connections:** 3
- **Integrations:** dropbox, googleSheets, interval, spreadsheetFile

### Unnamed Workflow

**Location:** `1122-database-alerts-with-notion-and-signl4`

- **Nodes:** 13
- **Connections:** 8
- **Trigger:** 🌐 Webhook
- **Integrations:** interval, notion, notionTrigger, signl4, webhook

### Unnamed Workflow

**Location:** `1150-backup-n8n-workflows-to-google-drive`

- **Nodes:** 9
- **Connections:** 8
- **Trigger:** ⏰ Scheduled, 👆 Manual
- **Integrations:** cron, functionItem, googleDrive, httpRequest, manualTrigger, moveBinaryData

### Unnamed Workflow

**Location:** `1277-send-a-daily-summary-of-your-google-calendar-events-to-slack`

- **Nodes:** 12
- **Connections:** 11
- **Trigger:** ⏰ Scheduled
- **Integrations:** cron, dateTime, googleCalendar, slack

### Unnamed Workflow

**Location:** `1283-get-email-notifications-for-newly-uploaded-google-drive-files`

- **Nodes:** 2
- **Connections:** 1
- **Integrations:** emailSend, googleDriveTrigger

### Unnamed Workflow

**Location:** `1340-create-zoom-meeting-link-from-google-calendar-invite`

- **Nodes:** 6
- **Connections:** 5
- **Trigger:** ⏰ Scheduled, 👆 Manual
- **Integrations:** cron, dateTime, googleCalendar, manualTrigger, zoom

### Unnamed Workflow

**Location:** `1388-save-telegram-daily-messages-to-google-sheets`

- **Nodes:** 3
- **Connections:** 2
- **Integrations:** functionItem, googleSheets, telegramTrigger

### Unnamed Workflow

**Location:** `1395-collects-images-from-web-search-results-and-send-to-google-sheets`

- **Nodes:** 6
- **Connections:** 4
- **Integrations:** awsRekognition, googleSheets, httpRequest

### Unnamed Workflow

**Location:** `1396-sync-data-between-google-drive-and-aws-s3`

- **Nodes:** 4
- **Connections:** 3
- **Integrations:** awsS3, googleDriveTrigger

### Unnamed Workflow

**Location:** `1401-collect-and-label-images-and-send-to-google-sheets`

- **Nodes:** 4
- **Connections:** 3
- **Integrations:** awsRekognition, googleSheets, httpRequest

### Unnamed Workflow

**Location:** `1420-google-calendar-to-slack-status-and-philips-hue`

- **Nodes:** 9
- **Connections:** 5
- **Trigger:** 👆 Manual
- **Integrations:** googleCalendar, googleCalendarTrigger, httpRequest, manualTrigger, slack

### Unnamed Workflow

**Location:** `1435-convert-json-to-an-excel-file`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** 🌐 Webhook
- **Integrations:** itemLists, respondToWebhook, spreadsheetFile, webhook

### Unnamed Workflow

**Location:** `1478-archive-empty-pages-in-notion-database`

- **Nodes:** 10
- **Connections:** 9
- **Trigger:** ⏰ Scheduled
- **Integrations:** cron, notion, splitInBatches

### Unnamed Workflow

**Location:** `1492-update-time-tracking-projects-based-on-syncro-status-changes`

- **Nodes:** 6
- **Connections:** 4
- **Trigger:** 🌐 Webhook
- **Integrations:** clockify, httpRequest, webhook

### Unnamed Workflow

**Location:** `1736-export-json-file-to-google-sheets`

- **Nodes:** 3
- **Connections:** 2
- **Integrations:** googleSheets, moveBinaryData, readBinaryFile

### Unnamed Workflow

**Location:** `1737-import-json-data-into-google-sheets-and-csv-file`

- **Nodes:** 6
- **Connections:** 2
- **Integrations:** googleSheets, httpRequest, spreadsheetFile, stickyNote

### Unnamed Workflow

**Location:** `1752-import-data-from-google-sheets-into-mysql`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** ⏰ Scheduled
- **Integrations:** cron, googleSheets, mySql

### Unnamed Workflow

**Location:** `1753-import-data-from-mysql-into-google-sheets`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** ⏰ Scheduled
- **Integrations:** cron, googleSheets, mySql

### Unnamed Workflow

**Location:** `1754-identify-new-google-sheets-rows`

- **Nodes:** 7
- **Connections:** 5
- **Trigger:** 👆 Manual
- **Integrations:** googleSheets, interval, manualTrigger, noOp

### Unnamed Workflow

**Location:** `1756-google-spreadsheet-to-html-variant-with-spreadsheet-file`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** 🌐 Webhook
- **Integrations:** googleSheets, spreadsheetFile, webhook

### Unnamed Workflow

**Location:** `1757-google-spreadsheet-to-html-variant-with-js-function`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** 🌐 Webhook
- **Integrations:** googleSheets, respondToWebhook, webhook

### Unnamed Workflow

**Location:** `1769-sync-tasks-data-between-notion-and-asana`

- **Nodes:** 10
- **Connections:** 8
- **Integrations:** asana, asanaTrigger, notion

### Unnamed Workflow

**Location:** `1778-sync-tasks-automatically-from-todoist-to-notion`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** ⏰ Scheduled
- **Integrations:** notion, scheduleTrigger, todoist

### Unnamed Workflow

**Location:** `1804-sync-your-github-issues-to-your-notion-database`

- **Nodes:** 11
- **Connections:** 5
- **Integrations:** githubTrigger, notion, stickyNote

### Unnamed Workflow

**Location:** `1810-read-xml-file-and-store-content-in-google-sheets`

- **Nodes:** 10
- **Connections:** 8
- **Trigger:** 👆 Manual
- **Integrations:** googleSheets, httpRequest, itemLists, manualTrigger, stickyNote, xml

### Unnamed Workflow

**Location:** `1819-send-google-drive-files-to-notion-database`

- **Nodes:** 2
- **Connections:** 1
- **Integrations:** googleDriveTrigger, notion

### Unnamed Workflow

**Location:** `1826-working-with-excel-spreadsheet-files-xls-xlsx`

- **Nodes:** 24
- **Connections:** 8
- **Trigger:** 👆 Manual
- **Integrations:** ftp, googleDrive, httpRequest, manualTrigger, microsoftOneDrive, readBinaryFile, spreadsheetFile, stickyNote, writeBinaryFile

### Unnamed Workflow

**Location:** `1831-sync-jira-issues-with-subsequent-comments-to-notion-database`

- **Nodes:** 10
- **Connections:** 6
- **Integrations:** jiraTrigger, notion, stickyNote

### Unnamed Workflow

**Location:** `1832-sync-zendesk-tickets-with-subsequent-comments-to-github-issues`

- **Nodes:** 7
- **Connections:** 5
- **Trigger:** 🌐 Webhook
- **Integrations:** github, webhook, zendesk

### Unnamed Workflow

**Location:** `1834-send-new-clockify-invoice-to-notion-database`

- **Nodes:** 3
- **Connections:** 1
- **Trigger:** 🌐 Webhook
- **Integrations:** notion, stickyNote, webhook

### Unnamed Workflow

**Location:** `1835-sync-notion-database-pages-as-clickup-tasks`

- **Nodes:** 5
- **Connections:** 3
- **Integrations:** clickUp, clickUpTrigger, notion, notionTrigger

### Unnamed Workflow

**Location:** `1872-convert-sql-table-into-excel-spreadsheet`

- **Nodes:** 5
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, mySql, spreadsheetFile, stickyNote

### Unnamed Workflow

**Location:** `1897-send-specific-pdf-attachments-from-gmail-to-google-drive-using-openai`

- **Nodes:** 18
- **Connections:** 11
- **Integrations:** gmailTrigger, googleDrive, noOp, openAi, readPDF, stickyNote

### Unnamed Workflow

**Location:** `1898-send-a-chatgpt-email-reply-and-save-responses-to-google-sheets`

- **Nodes:** 49
- **Connections:** 32
- **Trigger:** 🌐 Webhook
- **Integrations:** crypto, gmail, gmailTrigger, googleSheets, html, noOp, openAi, respondToWebhook, stickyNote, webhook

### Unnamed Workflow

**Location:** `1932-send-alert-when-data-is-created-in-app-database`

- **Nodes:** 10
- **Connections:** 5
- **Trigger:** 👆 Manual
- **Integrations:** filter, linearTrigger, manualTrigger, slack, stickyNote

### Unnamed Workflow

**Location:** `1939-send-labeled-email-to-a-notion-database`

- **Nodes:** 14
- **Connections:** 9
- **Trigger:** ⏰ Scheduled
- **Integrations:** dateTime, gmail, httpRequest, noOp, notion, notionTrigger, scheduleTrigger, stickyNote

### Unnamed Workflow

**Location:** `1940-sync-discord-scheduled-events-to-google-calendar`

- **Nodes:** 9
- **Connections:** 5
- **Trigger:** ⏰ Scheduled
- **Integrations:** googleCalendar, httpRequest, scheduleTrigger, stickyNote

### Unnamed Workflow

**Location:** `1948-xml-to-sql-database-import`

- **Nodes:** 9
- **Connections:** 5
- **Trigger:** 👆 Manual
- **Integrations:** itemLists, manualTrigger, mySql, readBinaryFiles, stickyNote, xml

### Unnamed Workflow

**Location:** `1964-sync-google-sheets-data-with-mysql`

- **Nodes:** 15
- **Connections:** 9
- **Trigger:** ⏰ Scheduled, 👆 Manual
- **Integrations:** compareDatasets, googleSheets, manualTrigger, mySql, noOp, scheduleTrigger, stickyNote

### Unnamed Workflow

**Location:** `1968-import-multiple-csv-to-google-sheets`

- **Nodes:** 9
- **Connections:** 8
- **Trigger:** 👆 Manual
- **Integrations:** filter, googleSheets, itemLists, manualTrigger, readBinaryFiles, splitInBatches, spreadsheetFile

### Unnamed Workflow

**Location:** `1969-import-csv-from-url-to-google-sheets`

- **Nodes:** 7
- **Connections:** 5
- **Trigger:** 👆 Manual
- **Integrations:** filter, googleSheets, httpRequest, manualTrigger, spreadsheetFile, stickyNote

### Unnamed Workflow

**Location:** `2-transfer-data-from-postgres-to-excel`

- **Nodes:** 3
- **Connections:** 2
- **Integrations:** postgres, spreadsheetFile, writeBinaryFile

### Unnamed Workflow

**Location:** `2041-get-csv-from-url-and-convert-to-excel`

- **Nodes:** 5
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** httpRequest, manualTrigger, spreadsheetFile, stickyNote

### Unnamed Workflow

**Location:** `2046-kv-cloudflare-key-value-database-full-api-integration-workflow`

- **Nodes:** 47
- **Connections:** 20
- **Trigger:** 👆 Manual
- **Integrations:** httpRequest, manualTrigger, stickyNote

### Unnamed Workflow

**Location:** `2063-google-maps-scraper`

- **Nodes:** 20
- **Connections:** 13
- **Trigger:** ⏰ Scheduled, 👆 Manual
- **Integrations:** filter, googleSheets, httpRequest, itemLists, manualTrigger, scheduleTrigger, stickyNote

### Unnamed Workflow

**Location:** `2081-synchronize-your-google-sheets-with-postgres`

- **Nodes:** 10
- **Connections:** 5
- **Trigger:** ⏰ Scheduled
- **Integrations:** compareDatasets, googleSheets, postgres, scheduleTrigger, splitOut, stickyNote

### Unnamed Workflow

**Location:** `2087-streamline-data-from-an-n8n-form-into-google-sheet-airtable-and-email-sending`

- **Nodes:** 10
- **Connections:** 5
- **Integrations:** airtable, formTrigger, gmail, googleSheets, stickyNote

### Unnamed Workflow

**Location:** `2090-chat-with-a-database-using-ai`

- **Nodes:** 5
- **Connections:** 2
- **Integrations:** stickyNote

### Unnamed Workflow

**Location:** `2141-add-product-ideas-to-google-sheets-via-a-slack`

- **Nodes:** 8
- **Connections:** 4
- **Trigger:** 🌐 Webhook
- **Integrations:** googleSheets, httpRequest, stickyNote, webhook

### Unnamed Workflow

**Location:** `2148-write-all-linear-tickets-to-google-sheets`

- **Nodes:** 14
- **Connections:** 8
- **Trigger:** ⏰ Scheduled
- **Integrations:** googleSheets, graphql, scheduleTrigger, splitOut, stickyNote

### Unnamed Workflow

**Location:** `226-receive-google-sheet-data-via-rest-api`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 🌐 Webhook
- **Integrations:** googleSheets, webhook

### Unnamed Workflow

**Location:** `2393-save-n8n-cloud-invoices-received-in-gmail-in-google-drive`

- **Nodes:** 13
- **Connections:** 9
- **Integrations:** filter, gmailTrigger, googleDrive, html, httpRequest, noOp, splitOut, stickyNote

### Unnamed Workflow

**Location:** `2494-generate-seo-keyword-search-volume-data-using-google-api`

- **Nodes:** 12
- **Connections:** 4
- **Trigger:** 👆 Manual
- **Integrations:** httpRequest, manualTrigger, noOp, splitOut, stickyNote

### Unnamed Workflow

**Location:** `2501-replace-images-in-google-docs-documents-and-download-as-pdf-docx`

- **Nodes:** 18
- **Connections:** 8
- **Trigger:** 👆 Manual
- **Integrations:** googleDrive, httpRequest, manualTrigger, noOp, stickyNote

### Unnamed Workflow

**Location:** `2517-send-google-analytics-data-to-a-i-to-analyze-then-save-results-in-baserow`

- **Nodes:** 22
- **Connections:** 17
- **Trigger:** ⏰ Scheduled, 👆 Manual
- **Integrations:** baserow, googleAnalytics, httpRequest, manualTrigger, scheduleTrigger, stickyNote

### Unnamed Workflow

**Location:** `2549-automate-google-analytics-reporting`

- **Nodes:** 23
- **Connections:** 17
- **Trigger:** ⏰ Scheduled, 👆 Manual
- **Integrations:** gmail, googleAnalytics, manualTrigger, scheduleTrigger, stickyNote

### Unnamed Workflow

**Location:** `2550-waitlist-form-stored-in-googlesheet-with-email-verification-step`

- **Nodes:** 19
- **Connections:** 13
- **Integrations:** crypto, emailSend, form, formTrigger, googleSheets, stickyNote

### Unnamed Workflow

**Location:** `2556-exponential-backoff-for-google-apis`

- **Nodes:** 8
- **Connections:** 6
- **Trigger:** 👆 Manual
- **Integrations:** googleSheets, manualTrigger, splitInBatches, stickyNote, stopAndError, wait

### Unnamed Workflow

**Location:** `356-generate-and-insert-data-into-a-postgres-database`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** ⏰ Scheduled
- **Integrations:** cron, postgres

### Unnamed Workflow

**Location:** `357-send-sms-alerts-based-on-database-queries-twilio-and-postgres`

- **Nodes:** 5
- **Connections:** 4
- **Trigger:** ⏰ Scheduled
- **Integrations:** cron, postgres, twilio

### Unnamed Workflow

**Location:** `428-add-a-task-to-google-tasks`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** googleTasks, manualTrigger

### Unnamed Workflow

**Location:** `515-download-a-file-from-google-drive`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** 👆 Manual
- **Integrations:** googleDrive, manualTrigger, writeBinaryFile

### Unnamed Workflow

**Location:** `566-get-all-excel-workbooks`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, microsoftExcel

### Unnamed Workflow

**Location:** `6-sync-data-between-multiple-google-spreadsheets`

- **Nodes:** 4
- **Connections:** 2
- **Trigger:** ⏰ Scheduled
- **Integrations:** cron, googleSheets

### Unnamed Workflow

**Location:** `600-insert-and-read-data-from-google-sheets`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** googleSheets, manualTrigger

### Unnamed Workflow

**Location:** `694-transform-data-in-google-sheets`

- **Nodes:** 7
- **Connections:** 6
- **Trigger:** 👆 Manual
- **Integrations:** googleSheets, manualTrigger

### Unnamed Workflow

**Location:** `770-automated-congratulations-with-google-sheets-twilio-and-n8n`

- **Nodes:** 8
- **Connections:** 6
- **Trigger:** ⏰ Scheduled
- **Integrations:** cron, googleSheets, noOp, twilio

### Unnamed Workflow

**Location:** `839-create-update-and-get-a-document-in-google-cloud-firestore`

- **Nodes:** 6
- **Connections:** 5
- **Trigger:** 👆 Manual
- **Integrations:** googleFirebaseCloudFirestore, manualTrigger

### Unnamed Workflow

**Location:** `864-monitor-changes-in-google-sheets-every-45-mins`

- **Nodes:** 4
- **Connections:** 3
- **Integrations:** googleSheets, interval, mattermost

### Unnamed Workflow

**Location:** `890-read-in-an-excel-spreadsheet-file`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, readBinaryFile, spreadsheetFile

### Unnamed Workflow

**Location:** `892-transfer-google-analytics-data-to-airtable-database`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** airtable, googleAnalytics, manualTrigger

### Unnamed Workflow

**Location:** `980-load-data-into-spreadsheet-or-database`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, noOp

### Unnamed Workflow

**Location:** `excel-to-postgres`

- **Nodes:** 3
- **Connections:** 2
- **Integrations:** postgres, readBinaryFile, spreadsheetFile

### Unnamed Workflow

**Location:** `google-sheets-to-dropbox`

- **Nodes:** 4
- **Connections:** 3
- **Integrations:** dropbox, googleSheets, interval, spreadsheetFile

---

## data-transformation

### Unnamed Workflow

**Location:** `1045-etl-pipeline-for-text-processing`

- **Nodes:** 9
- **Connections:** 7
- **Trigger:** ⏰ Scheduled
- **Integrations:** cron, googleCloudNaturalLanguage, mongoDb, noOp, postgres, slack, twitter

### Unnamed Workflow

**Location:** `13-transform-xml-data-and-upload-to-dropbox`

- **Nodes:** 5
- **Connections:** 4
- **Integrations:** dropbox, httpRequest, xml

### Unnamed Workflow

**Location:** `1537-convert-filemaker-data-api-to-flat-file-array`

- **Nodes:** 3
- **Connections:** 2
- **Integrations:** functionItem, itemLists

### Unnamed Workflow

**Location:** `160-convert-xml-to-json`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, xml

### Unnamed Workflow

**Location:** `1902-convert-postgresql-table-to-csv`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, postgres, spreadsheetFile

### Unnamed Workflow

**Location:** `2037-convert-image-urls-to-an-uploaded-attachment-in-airtable`

- **Nodes:** 4
- **Connections:** 2
- **Trigger:** 👆 Manual
- **Integrations:** airtable, manualTrigger, stickyNote

### Unnamed Workflow

**Location:** `2222-convert-an-xml-file-to-json-via-webhook-call`

- **Nodes:** 12
- **Connections:** 8
- **Trigger:** 🌐 Webhook
- **Integrations:** extractFromFile, respondToWebhook, slack, stickyNote, webhook, xml

### Unnamed Workflow

**Location:** `2294-convert-docx-to-pdf-using-convertapi`

- **Nodes:** 5
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** httpRequest, manualTrigger, readWriteFile, stickyNote

### Unnamed Workflow

**Location:** `2297-convert-docx-from-url-to-pdf-using-convertapi`

- **Nodes:** 6
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** httpRequest, manualTrigger, readWriteFile, stickyNote

### Unnamed Workflow

**Location:** `2298-merge-pdf-files-using-convertapi`

- **Nodes:** 6
- **Connections:** 4
- **Trigger:** 👆 Manual
- **Integrations:** httpRequest, manualTrigger, readWriteFile, stickyNote

### Unnamed Workflow

**Location:** `2304-convert-xlsx-to-pdf-using-convertapi`

- **Nodes:** 5
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** httpRequest, manualTrigger, readWriteFile, stickyNote

### Unnamed Workflow

**Location:** `2305-convert-pptx-to-pdf-using-convertapi`

- **Nodes:** 5
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** httpRequest, manualTrigger, readWriteFile, stickyNote

### Unnamed Workflow

**Location:** `2306-protect-pdf-with-the-password-using-convertapi`

- **Nodes:** 7
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** googleDrive, httpRequest, manualTrigger, readWriteFile, stickyNote

### Unnamed Workflow

**Location:** `2308-convert-airtable-rich-text-markdown-field-to-html`

- **Nodes:** 9
- **Connections:** 6
- **Trigger:** 🌐 Webhook
- **Integrations:** airtable, markdown, stickyNote, webhook

### Unnamed Workflow

**Location:** `2310-convert-web-page-to-pdf-using-convertapi`

- **Nodes:** 5
- **Connections:** 2
- **Trigger:** 👆 Manual
- **Integrations:** httpRequest, manualTrigger, readWriteFile, stickyNote

### Unnamed Workflow

**Location:** `2314-convert-html-to-pdf-using-convertapi`

- **Nodes:** 6
- **Connections:** 4
- **Trigger:** 👆 Manual
- **Integrations:** httpRequest, manualTrigger, readWriteFile, stickyNote

### Unnamed Workflow

**Location:** `2316-convert-image-to-pdf-using-convertapi`

- **Nodes:** 5
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** httpRequest, manualTrigger, readWriteFile, stickyNote

### Unnamed Workflow

**Location:** `2317-convert-pdf-to-pdfa-using-convertapi`

- **Nodes:** 5
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** httpRequest, manualTrigger, readWriteFile, stickyNote

### Unnamed Workflow

**Location:** `2345-convert-baserow-rich-text-markdown-field-to-html`

- **Nodes:** 9
- **Connections:** 6
- **Trigger:** 🌐 Webhook
- **Integrations:** baserow, markdown, stickyNote, webhook

### Unnamed Workflow

**Location:** `2513-convert-image-files-jpg-png-jpeg-to-urls-and-reduce-file-size-with-resmush-it-and-imgbb`

- **Nodes:** 11
- **Connections:** 5
- **Integrations:** httpRequest, noOp, stickyNote

### Unnamed Workflow

**Location:** `575-convert-a-date-from-one-format-to-another`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** dateTime, manualTrigger

### Unnamed Workflow

**Location:** `661-convert-the-json-data-received-from-the-cocktaildb-api-in-xml`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** 👆 Manual
- **Integrations:** httpRequest, manualTrigger, xml

### Unnamed Workflow

**Location:** `763-convert-an-array-into-an-array-of-objects`

- **Nodes:** 2
- **Connections:** 1

### Unnamed Workflow

**Location:** `xml-to-dropbox`

- **Nodes:** 5
- **Connections:** 4
- **Integrations:** dropbox, httpRequest, xml

---

## document-processing

### Unnamed Workflow

**Location:** `1083-create-an-event-file-and-send-it-as-an-email-attachment`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** 👆 Manual
- **Integrations:** emailSend, iCal, manualTrigger

### Unnamed Workflow

**Location:** `1282-send-a-file-from-s3-to-aws-textract`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** 👆 Manual
- **Integrations:** awsS3, awsTextract, manualTrigger

### Unnamed Workflow

**Location:** `1375-create-a-document-in-outline-for-each-new-gitlab-release`

- **Nodes:** 3
- **Connections:** 2
- **Integrations:** gitlabTrigger, httpRequest

### Unnamed Workflow

**Location:** `1394-transcribe-audio-files-from-cloud-storage`

- **Nodes:** 8
- **Connections:** 7
- **Integrations:** awsS3, awsTranscribe, googleDriveTrigger, googleSheets, wait

### Unnamed Workflow

**Location:** `1407-simple-file-based-key-value-store-writekey`

- **Nodes:** 10
- **Connections:** 9
- **Trigger:** 👆 Manual
- **Integrations:** functionItem, manualTrigger, moveBinaryData, readBinaryFiles, splitInBatches, writeBinaryFile

### Unnamed Workflow

**Location:** `1408-simple-file-based-key-value-store-getkey`

- **Nodes:** 5
- **Connections:** 4
- **Trigger:** 👆 Manual
- **Integrations:** functionItem, manualTrigger, moveBinaryData, readBinaryFile

### Unnamed Workflow

**Location:** `1731-export-csv-file-to-json`

- **Nodes:** 5
- **Connections:** 4
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, moveBinaryData, readBinaryFile, spreadsheetFile, writeBinaryFile

### Unnamed Workflow

**Location:** `1734-import-a-json-file-from-gmail-into-a-spreadsheet`

- **Nodes:** 4
- **Connections:** 2
- **Integrations:** gmail, moveBinaryData, spreadsheetFile, stickyNote

### Unnamed Workflow

**Location:** `1791-transfer-json-data-to-csv-file`

- **Nodes:** 3
- **Connections:** 2
- **Integrations:** googleSheets, moveBinaryData, readBinaryFile

### Unnamed Workflow

**Location:** `1914-export-sql-table-into-csv-file`

- **Nodes:** 5
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, microsoftSql, spreadsheetFile, stickyNote

### Unnamed Workflow

**Location:** `1920-respond-with-file-download-to-incoming-http-request`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** 🌐 Webhook
- **Integrations:** httpRequest, respondToWebhook, webhook

### Unnamed Workflow

**Location:** `1933-push-json-data-into-an-app-or-to-spreadsheet-file`

- **Nodes:** 8
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** googleSheets, httpRequest, manualTrigger, spreadsheetFile, stickyNote

### Unnamed Workflow

**Location:** `1942-push-and-update-files-in-github`

- **Nodes:** 13
- **Connections:** 7
- **Trigger:** 👆 Manual
- **Integrations:** executeCommand, git, github, manualTrigger, stickyNote

### Unnamed Workflow

**Location:** `1949-create-2-xml-files-with-and-without-xml-attributes`

- **Nodes:** 13
- **Connections:** 10
- **Trigger:** 👆 Manual
- **Integrations:** itemLists, manualTrigger, moveBinaryData, mySql, stickyNote, writeBinaryFile, xml

### Unnamed Workflow

**Location:** `1967-prepare-csv-files-with-gpt-4`

- **Nodes:** 11
- **Connections:** 9
- **Trigger:** 👆 Manual
- **Integrations:** itemLists, manualTrigger, moveBinaryData, openAi, splitInBatches, spreadsheetFile, stickyNote, writeBinaryFile

### Unnamed Workflow

**Location:** `2451-download-and-compress-folder-from-s3-to-zip-file`

- **Nodes:** 6
- **Connections:** 4
- **Trigger:** 👆 Manual
- **Integrations:** aggregate, awsS3, compression, manualTrigger, stickyNote

### Unnamed Workflow

**Location:** `2568-upsert-huge-documents-in-a-vector-store-with-supabase-and-notion`

- **Nodes:** 34
- **Connections:** 18
- **Trigger:** ⏰ Scheduled
- **Integrations:** limit, noOp, notion, notionTrigger, scheduleTrigger, splitInBatches, stickyNote, summarize, supabase

### Unnamed Workflow

**Location:** `2621-ai-agent-to-chat-with-files-in-supabase-storage`

- **Nodes:** 33
- **Connections:** 21
- **Trigger:** 👆 Manual
- **Integrations:** aggregate, extractFromFile, httpRequest, manualTrigger, splitInBatches, stickyNote, supabase

### Unnamed Workflow

**Location:** `450-get-the-community-profile-of-a-repository`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** github, manualTrigger

### Unnamed Workflow

**Location:** `503-insert-a-document-in-mongodb`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, mongoDb

### Unnamed Workflow

**Location:** `577-read-a-file-from-disk`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, readBinaryFile

### Unnamed Workflow

**Location:** `578-read-multiple-files-from-disk`

- **Nodes:** 2
- **Connections:** 1
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, readBinaryFiles

### Unnamed Workflow

**Location:** `585-extract-text-from-a-pdf-file`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, readBinaryFile, readPDF

### Unnamed Workflow

**Location:** `586-read-a-spreadsheet-file`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** 👆 Manual
- **Integrations:** manualTrigger, readBinaryFile, spreadsheetFile

### Unnamed Workflow

**Location:** `590-write-a-file-to-the-host-machine`

- **Nodes:** 3
- **Connections:** 2
- **Trigger:** 👆 Manual
- **Integrations:** httpRequest, manualTrigger, writeBinaryFile

### Unnamed Workflow

**Location:** `663-download-a-file-and-upload-it-to-an-ftp-server`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** ftp, httpRequest, manualTrigger

### Unnamed Workflow

**Location:** `674-manage-files-in-s3`

- **Nodes:** 4
- **Connections:** 3
- **Trigger:** 👆 Manual
- **Integrations:** httpRequest, manualTrigger, s3

### Unnamed Workflow

**Location:** `908-compress-binary-files-to-zip-format`

- **Nodes:** 5
- **Connections:** 4
- **Trigger:** 👆 Manual
- **Integrations:** compression, dropbox, httpRequest, manualTrigger

### Unnamed Workflow

**Location:** `913-execute-multiple-command-lines-based-on-text-file-inputs`

- **Nodes:** 7
- **Connections:** 6
- **Trigger:** 👆 Manual
- **Integrations:** executeCommand, manualTrigger, moveBinaryData, noOp, readBinaryFile

### Unnamed Workflow

**Location:** `967-monitor-a-file-for-changes-and-send-an-alert`

- **Nodes:** 9
- **Connections:** 7
- **Trigger:** ⏰ Scheduled
- **Integrations:** cron, moveBinaryData, readBinaryFile, signl4, writeBinaryFile

---
