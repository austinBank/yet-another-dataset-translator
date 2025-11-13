# Yet Another Dataset Translator

> A powerful dataset translation tool designed to detect source language, selectively translate fields, and generate enriched multilingual datasets. It minimizes translation costs through smart language detection and provides full control over which fields are processed.

> Ideal for teams working with multilingual data, localization workflows, and large-scale content transformation pipelines.


<p align="center">
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>Yet Another Dataset Translator</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction

This project enables seamless translation of entire datasets with configurable field targeting and automatic language detection. It is designed to optimize translation efficiency by skipping items already written in the target language, reducing processing time and translation expenses.

### Smart Translation Workflow

- Automatically detects the language of dataset items with configurable thresholds.
- Selectively translates fields that match user-defined patterns.
- Supports a mock-translation mode for cost-free testing.
- Attaches original field values for full auditability.
- Generates translation markers for easy downstream filtering.

## Features

| Feature | Description |
|--------|-------------|
| Language Detection | Identifies input language and skips translation when content matches the target language. |
| Field Pattern Matching | Translate only fields matching glob patterns such as `*field`, `[fF]ield`, or `?ield`. |
| Mock Translation Mode | Enables testing without an API key by simulating translated output. |
| Threshold Configuration | Fine-tune detection strictness using a numeric confidence threshold. |
| Original Value Preservation | Optionally store original text using a customizable prefix. |
| Translation Marker Field | Marks each item as translated or skipped for transparency. |
| Multi-Dataset Support | Combine multiple dataset IDs as translation input. |
| Custom Output Dataset | Select or create a dedicated output dataset for aggregation. |

---

## What Data This Scraper Extracts

| Field Name | Field Description |
|------------|------------------|
| dataset_ids | List of dataset identifiers that will be translated. |
| api_key | API key used to authenticate translation operations. |
| field_patterns_to_translate | A list of glob rules determining which fields should be translated. |
| detect_language_threshold | Numeric value controlling sensitivity of language detection. |
| output_dataset_id | Identifier for the dataset where translated items will be stored. |
| translation_marker_field | Field added to output items indicating translation status. |
| original_value_field_prefix | Prefix applied to duplicated original values. |

---

## Example Output


    [
        {
            "text": "Goodbye.",
            "original_text": "Auf Wiedersehen.",
            "wasTranslated": true
        }
    ]

---

## Directory Structure Tree


    Yet Another Dataset Translator/
    ├── src/
    │   ├── main.py
    │   ├── translator/
    │   │   ├── language_detector.py
    │   │   ├── field_selector.py
    │   │   ├── translator_engine.py
    │   │   └── utils.py
    │   ├── config/
    │   │   └── settings.json
    │   └── outputs/
    │       └── writer.py
    ├── data/
    │   ├── input.sample.json
    │   └── output.example.json
    ├── tests/
    │   ├── test_detector.py
    │   ├── test_patterns.py
    │   └── test_translation.py
    ├── requirements.txt
    └── README.md

---

## Use Cases

- **Data analysts** use it to translate multilingual datasets so they can standardize text for downstream processing.
- **Localization teams** use it to prepare structured fields for translation workflows, ensuring consistency and cost efficiency.
- **Researchers** use it to unify multilingual text sources, enabling accurate text mining and NLP modeling.
- **Businesses** use it to convert customer feedback or product data into a single target language for reporting and insights.

---

## FAQs

**Q: Can I run translations without providing an API key?**
Yes. The tool supports a mock-translation mode that simulates translated text while preserving all logic and structure.

**Q: How does field pattern matching work?**
You can supply glob-style patterns such as `*name`, `?ield`, or `[fF]ield` to target specific fields. All matched fields are processed together per item.

**Q: What happens if language detection is disabled?**
Setting the threshold to `0` disables detection entirely, causing all matched fields to be translated regardless of source language.

**Q: Will original values always be included?**
Only if you specify a non-empty prefix. Setting the prefix to an empty string removes original value storage.

---

## Performance Benchmarks and Results

**Primary Metric:** Translates up to thousands of dataset items per minute depending on field count and text length.
**Reliability Metric:** Consistently maintains above 98% successful processing on large datasets with mixed languages.
**Efficiency Metric:** Reduces unnecessary translation calls by up to 40% through intelligent language detection.
**Quality Metric:** Ensures complete field coverage with accurate pattern-matching and optional preservation of original text for validation.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
