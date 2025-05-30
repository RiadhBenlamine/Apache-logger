# Apache Log Analyzer with JSON Template Engine

**Author:** Riadh Benlamine  
**Date:** 2025

---

## Overview

This tool analyzes Apache HTTP server logs using customizable JSON templates to detect suspicious activity, attacks, and scanners based on flexible regex patterns. The engine supports multi-threading and multi-processing for scalable performance.

---

## Features

- Template-driven log analysis with JSON format  
- Detect hacking tools, scanners, SQL injections, file enumeration, malware signatures  
- Regex-based matching on log fields: `host`, `user`, `time`, `request`, `status`, `size`, `referrer`, `agent`  
- Multi-threaded template evaluation for performance  
- Multi-processing file parsing for scalability  
- Clean, modular Python codebase  
- CLI interface powered by `typer` for easy usage  
- Easily extendable with new templates

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/apache-log-analyzer.git
cd apache-log-analyzer
pip install typer
```
Usage
Run the analyzer with:

```bash

python log.py TEMPLATE_PATH LOG_PATH```
Example:

bash
```
python log.py templates/wordpress_attack_template.json logs/apache_sample_200.log
```
TEMPLATE_PATH — Path to your JSON detection template

LOG_PATH — Path to the Apache log file to analyze

Output Format
When a log line matches a template, the analyzer prints key-value pairs for that entry, for example:


```host: 192.168.1.100
user: -
time: 15/May/2025:14:12:24 +0000
request: GET /wp-login.php HTTP/1.1
status: 200
size: 1234
referrer: -
agent: Mozilla/5.0 (Nikto/2.1.6)```
Template Structure
Each template JSON file must contain two top-level keys:

description: Meta-information about the template

points: Regex filters for log fields to detect suspicious entries

Example:
```
{
  "description": {
    "template_name": "Wordpress Attack Detector",
    "author": "Riadh Benlamine",
    "description": "Detects common Wordpress attacks like brute force and file enumeration"
  },
  "points": {
    "host": false,
    "user": false,
    "time": false,
    "request": "(wp-login\\.php|xmlrpc\\.php|wp-admin/|wp-content/uploads/)",
    "status": false,
    "size": false,
    "referrer": false,
    "agent": "(nikto|acunetix|nmap|sqlmap|wpscan)"
  }
}
```
Use false for fields you want to ignore.

Use regex strings for fields you want to filter.

Development Notes
JSON regex strings must escape backslashes properly (\\).

The log parser expects standard Apache combined log format.

TemplateEngine uses threading for concurrent evaluation.

FileEngine uses multiprocessing to speed up log parsing.

typer is used for CLI interface and argument parsing.

Extending
Add new templates in JSON format inside the templates/ directory.

Customize regex filters per your environment and threat landscape.

Enhance engine for alerting, logging, or integrating with SIEMs.

Troubleshooting
Invalid JSON errors: Validate your JSON templates with https://jsonlint.com

Regex matching issues: Double-escape backslashes in regex patterns inside JSON.

Encoding errors: Ensure logs and templates are UTF-8 encoded.