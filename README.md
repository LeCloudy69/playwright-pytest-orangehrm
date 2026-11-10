**1. Create and activate a virtual environment**
 
```bash
python -m venv .venv
source .venv/bin/activate        # Mac / Linux
.venv\Scripts\activate           # Windows
```
 
**2. Install dependencies**
 
```bash
pip install -r requirements.txt
```
 
**3. Install the browsers** (one time per machine)
 
```bash
playwright install chromium firefox
```
 
**4. Optional: set credentials**
 
The OrangeHRM demo login is public and used by default. To override it, copy the template and edit the values:
 
```bash
cp .env.example .env
```
 
**5. Run the tests**
 
```bash
pytest
```
 
## ▶️ Useful commands
 
| Goal | Command |
|---|---|
| Run everything (parallel, headless) | `pytest` |
| Watch the browser | `pytest --headed --slowmo 500 -n 0` |
| Run in Firefox | `pytest --browser firefox` |
| Run both browsers | `pytest --browser chromium --browser firefox` |
| Run one test by name | `pytest -k test_valid_login -n 0` |
| Open a failure trace | `playwright show-trace test-results/<test-folder>/trace.zip` |