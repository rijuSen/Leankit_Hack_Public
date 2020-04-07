# Leankit_Hack_Public
Simple project to create timesheet from LeanKit task cards.
Use LeanKit API with HTTPS Basic auth to fetch Leankit task cards. Use the task cards to create an entry into a timesheet file. Entries made when the card is moved to DONE. Has to be manually trigered to populate new entries.
Instructions to run the script:
1. Download the script
2. Run main from the script
3. Input your name
4. Input your board number
5. Input your DONE Lane number (toggle to API on Leankit to view Lane Number)
6. Input your Leankit registered mail id and password 
7. Check for status code 0 
8. If a CSV file exists, the scripts updated only new entries. Otherwise the script creates a new CSV file and appends entries.
8. Find in the script folder a csv named - cardList.csv
