# Discord Top.gg Autovoter

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

> **DISCLAIMER**  
> This project is provided strictly for educational and research purposes.  
> Automating votes on top.gg may violate their Terms of Service.  
> You are solely responsible for how you use this software.

---

## Overview

**Discord Top.gg Autovoter** is a Python-based automation tool designed to simulate the voting process for Discord bots listed on top.gg using Discord user tokens.

The tool allows developers to:
- Understand how automated HTTP workflows function
- Learn about authentication headers, cookies, and CSRF tokens
- Explore scheduling and rate-limited task execution in Python

This project is **not intended for misuse** and should only be used on accounts you personally own and control.

---

## Key Features

- Automated voting for a specified top.gg bot ID
- Support for multiple Discord user tokens
- Configurable voting intervals (default: 12 hours)
- Robust error handling and retry logic
- Clear logging for success, failure, and cooldown states
- Lightweight and dependency-minimal design

---

## Important Warnings

Before using this project, read the following carefully:

1. **Terms of Service Violation**  
   top.gg explicitly discourages and may prohibit automated voting. Using this tool could result in vote invalidation, IP bans, or account restrictions.

2. **Account Security**  
   Discord user tokens grant full access to an account.  
   Never:
   - Share tokens publicly
   - Commit tokens to GitHub
   - Use tokens from accounts you do not own

3. **Personal Use Only**  
   This tool is intended for personal experimentation and learning.  
   Using it for commercial, public, or large-scale vote manipulation is strongly discouraged.

4. **Rate Limiting and Detection**  
   Excessive or poorly configured usage may trigger:
   - Discord API rate limits
   - top.gg anti-abuse systems
   - Temporary or permanent account restrictions

---

## Prerequisites

Ensure the following before installation:

- Python **3.11 or higher**
- One or more Discord accounts you personally own
- Valid Discord user token(s)
- The **top.gg bot ID** you want to vote for
- Basic knowledge of Python and command-line usage

---
