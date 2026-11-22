<div align="center">

<!-- CLEAN OPEN-SOURCE HERO BANNER -->
<img src="https://vercel.app" width="100%" />

<br/>

<!-- STATUS & TECH BADGES -->
<a href="https://python.org">
  <img src="https://shields.io" alt="Python" />
</a>
<a href="https://streamlit.io">
  <img src="https://shields.io" alt="Streamlit" />
</a>
<a href="https://pypi.org">
  <img src="https://shields.io" alt="PyPDF" />
</a>
<a href="https://github.com">
  <img src="https://shields.io" alt="License" />
</a>
<a href="https://github.com">
  <img src="https://shields.io" alt="Repo Size" />
</a>

</div>

---

## Overview

**Spidey PDF Tool** is a lightweight, privacy-focused web utility built with **Python**, **Streamlit**, and **PyPDF**. It allows users to merge multiple PDF documents or extract specific page ranges entirely in memory—meaning zero files are saved to disk or uploaded to third-party servers.

---

## Key Features

| Mode | Core Functionality | Description |
| :--- | :--- | :--- |
| **Tobey Mode** | **PDF Merger** | Combines multiple uploaded PDF files into a single document in user-selected order. |
| **Andrew Mode** | **Page Range Splitter** | Extracts a custom page range (`start_page` to `end_page`) with built-in boundary validation. |
| **Tom Mode** | **Session Reset** | Clears active memory state and resets the workspace for a clean session. |

---

## Architecture & Data Flow

```text
[User Uploads PDF(s)] 
        │
        ▼
[Streamlit FileUploader (RAM)]
        │
        ├──► Merge Mode ──► pypdf.PdfWriter.append() ──┐
        │                                              ├──► [io.BytesIO Buffer] ──► [Instant Download]
        └──► Split Mode ──► pypdf.PdfWriter.add_page() ┘
```

* **Zero Disk I/O:** Uses `io.BytesIO()` buffers to process files directly in RAM for speed and privacy.
* **Input Validation:** Prevents out-of-range page slicing before processing begins.

---

## Project Structure

```text
spidey-pdf-tool/
├── yoo.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com.git
cd spidey-pdf-tool
```

### 2. Install Dependencies
```bash
pip install streamlit pypdf
```

### 3. Run the Application
```bash
streamlit run yoo.py
```

---

## Roadmap

- [ ] Add PDF compression support to reduce large file sizes
- [ ] Add drag-and-drop page reordering before merging
- [ ] Add password protection / encryption option for exported PDFs

---

## Author

**Sufyan** — [@Sufyan-m](https://github.com)
