# Gen AI Labs Companion

Welcome to the Gen AI course! This repository contains the hands-on labs you will complete during the workshops.

## Setup Instructions

1. **Clone this repository** to your local machine.
2. **Create a virtual environment**:

   **Mac / Linux:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   **Windows:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up API keys**:
   - Copy `.env.example` to `.env` (or rename the file)
   - Fill in your API keys in the `.env` file.

## Exercise Structure

For each session, you will find two folders:
- `start/`: Contains boilerplate code with `TODO` comments. This is where you will write your code.
- `solution/`: Contains the fully working reference implementation. If you get stuck, you can refer to this code.

## Running the Scripts

Always execute your scripts from the root directory of this repository so that relative paths and `.env` variables load correctly. Make sure your virtual environment is activated.

**Example: Running a Start Script**
```bash
python day2/morning-labs/start/lab2_1_sentiment.py
```

**Example: Running a Solution Script**
```bash
python day2/morning-labs/solution/lab2_1_sentiment.py
```

You can use this same pattern for all other exercises by replacing the file path with the specific script you want to run.

Follow the instructions in the `README.md` file located inside each session's folder.
