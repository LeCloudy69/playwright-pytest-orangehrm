   
   Make a python enviroment in the root directory and activate it (Mac)
   python -m venv .venv
   source .venv/bin/activate

   Install requirements (In the activated enviroment)
   pip install -r requirements.txt

   One time install
   playwright install
   incase of error run (incase of missing browser)
   playwright firefox

   after this playwright will be downloaded gloabally so any activated enviroment can access 'playwright'

   run the test.
   pytest