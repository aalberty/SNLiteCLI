SNLite


More responsive and time efficient experience for navigating records on platform
- schema view with sample record values
- Multi-instance record compare/retrieval
	- Ex: List of mid servers combined from all three instances
	- "sudo" requirement to perform Create, Update, and Delete operations on prod records. Single command, or sudo session
- threading to prevent freeze while a command is running
- Ability to run a script on platform and retrieve results
	- Script library


CLI commands
- search : search with specified criteria
    - --for <artifact_type> : specify what is being searched for. Accepted values:
        - table
        - record, rec
    - --with <query_params> : friendly-ish encoded params. Separate the pieces of your query with ` and ` and ` or `. Use of ServiceNow query keywords is also supported (`LIKE`, `STARTS WITH`, etc).
    - --sort <direction> on <field_name> : Order results in specified direction on specified field.  

- list <table_name> : show list of recs from specified table. If table isn't found, `search --for table --with name:<table_name>`

- sample <table_name> : show sample rec from specified table. If table isn't found, `search --for table --with name:<table_name>`
