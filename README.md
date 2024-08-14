# cloud-events-slack-notification

This is an application to listen to Google Cloud Build events (through pub/sub `cloud-builds`) and send Slack notifications, indicating whether the build is successful or failed.  

## Services involved

- Google Cloud Build
- Google Cloud Pub/Sub (topic `cloud-builds`)
- Google Cloud Functions (this)
- Google Secret Manager (id `slack-webhook-url`)
- Slack API

## Used Python packages

- `Jinja2` for Slack message template
- `Http` for calling Slack API
- `re` for extracting pub/sub payload
- `human_readable` for formating date time to human-readable format

## Sample Slack messages

### A build is successful

### A build is unsuccessful

## Diagram

![diagram](resources/img/diagram.png)
<details>
<summary>mermaid.js code</summary>

```mermaid
sequenceDiagram
    participant gcb as Google<br>Cloud Build
    participant psb as Google<br>Cloud Pub/Sub
    participant gcf as Google<br>Cloud Functions
    participant gsm as Google<br>Secret Manager
    participant swh as Slack<br>Webhook
    participant sch as Slack<br>Channel
    autonumber

    gcb->>psb: send build events
    psb->>gcf: trigger eventarc
    gcf->>+gsm: get slack url
    gsm->>-gcf: return slack url 
    gcf->>swh: post Slack messages
    swh->>sch: display messages
```

</details>
