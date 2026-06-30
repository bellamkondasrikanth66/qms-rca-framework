# Quality Management System (QMS): Root Cause Analysis (RCA) Framework

This repository provides a standardized and practical framework for conducting **Root Cause Analysis (RCA)** and integrating the results with a digital defect logging workflow.

It includes:

* A structured **5 Whys Root Cause Analysis template** populated with a realistic manufacturing non-conformity scenario.
* An interactive **Python-based mock issue tracker** that simulates linking RCA documents to quality issues within a Quality Management System (QMS).

---

# 📁 Repository Structure

```
.
├── issue_tracker.py      # Interactive Python CLI issue tracker
├── rca_template.md       # Sample 5 Whys RCA document
└── README.md             # Project documentation
```

### Files

* **`rca_template.md`**

  * A comprehensive Markdown template implementing the **5 Whys** methodology.
  * Includes a realistic engineering failure scenario, immediate containment actions, identified root causes, and corrective/preventive actions (CAPA).

* **`issue_tracker.py`**

  * A standalone Python command-line application that simulates a quality issue tracking system.
  * Users can create issues and link completed RCA documents to issue records.

* **`README.md`**

  * Project documentation, setup instructions, and usage guide.

---

# ⚙️ Prerequisites

No external libraries or databases are required.

Requirements:

* **Python 3.x**
* **VS Code** (recommended)
* Integrated terminal (recommended)

---

# 🚀 Running the Project (VS Code)

## Step 1: Open the Project

1. Open **VS Code**.
2. Select **File → Open Folder...**
3. Open (or create) your project folder.
4. Place the following files inside it:

```
issue_tracker.py
rca_template.md
README.md
```

---

## Step 2: Open the Terminal

Open the integrated terminal:

* **Terminal → New Terminal**

or press:

```
Ctrl + `
```

Verify that the terminal is currently inside your project directory.

---

## Step 3: Run the Application

Execute:

```bash
python issue_tracker.py
```

If your system uses multiple Python installations, use:

```bash
python3 issue_tracker.py
```

---

# 📋 Demonstration Workflow

## Step 1: View Existing Issues

When the application starts, you'll see the current quality issues:

```text
=== CURRENT QUALITY ISSUES ===
ID     | Issue Title                                   | RCA Linked?
----------------------------------------------------------------------
101    | Raw material variance on dock 2               | ❌ No
102    | Component-X Tensile Strength Failure          | ❌ No
103    | Label printer calibration error               | ❌ No
======================================================================
```

---

## Step 2: Create a New Issue

1. Enter:

```text
1
```

2. Press **Enter**.

3. When prompted, enter a new issue title:

```text
Line 4 Packaging Seal Failure
```

4. Press **Enter**.

The issue tracker automatically creates a new record:

```text
104 | Line 4 Packaging Seal Failure | ❌ No
```

---

## Step 3: Link an RCA Document

1. Enter:

```text
2
```

2. Press **Enter**.

3. For the Issue ID, enter:

```text
102
```

4. When prompted for the RCA document path, enter:

```text
rca_template.md
```

5. Press **Enter**.

---

## Step 4: Verify Successful Linking

If the file exists, the application validates it and updates the issue:

```text
102    | Component-X Tensile Strength Failure          | ✅ Yes (rca_template.md)
```

This simulates associating an RCA document with a quality issue inside a QMS workflow.

---

# 🔬 Methodology Overview: 5 Whys Analysis

This project demonstrates the **5 Whys** problem-solving methodology, a widely used Root Cause Analysis technique in quality management.

Rather than stopping at the immediate symptom, the method repeatedly asks **"Why?"** until the underlying systemic cause is identified.

In the provided example, the investigation progresses beyond the observed component failure and ultimately identifies deficiencies in automated tool tracking and software deployment processes. This illustrates how effective Root Cause Analysis focuses on improving systems and processes rather than assigning blame to individuals.

---

# ✅ Features

* Interactive command-line issue tracker
* Create new quality issues
* Link RCA documents to issues
* File existence validation
* Sample 5 Whys RCA template
* No external dependencies
* Beginner-friendly Python implementation

---

# 🛠 Technologies Used

* Python 3
* Markdown
* Command-Line Interface (CLI)

---

# 📄 License

This project is intended for educational and demonstration purposes.
