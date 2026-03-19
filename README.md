![CI](https://github.com/Guwaniee/quality-engineering-platform/actions/workflows/ci.yml/badge.svg)

# Quality Engineering Platform (QEP)

A production-style **QA Automation / Quality Engineering** portfolio project demonstrating real-world test automation practices across **API + UI + E2E** layers.

## What this shows
- **FastAPI** backend with JWT authentication + CRUD endpoints
- **API automation** with Pytest (positive / negative / edge cases)
- **UI automation** with Playwright (real browser)
- **E2E flow testing** against a running service
- **HTML reports** generated for API/UI/E2E suites
- **CI pipeline** (GitHub Actions) runs full test suite and uploads artifacts

## Tech Stack
Python, FastAPI, Pytest, Playwright, GitHub Actions, pytest-html, pytest-cov

## Quickstart

### 1. Install Dependencies
```bash
make install
``` 

### 2. Run & Test
```bash
# This starts your FastAPI server
make run

# These run your Pytest suites
make test-api
make test-ui
make test-e2e
``` 
