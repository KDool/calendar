# README for the Calendar update robot

This is a robot to auto extract the Schedule from the Excel file, and then update to your Calendar Outlook/Gmail.

## Development guide
To Run the Robot, open and execute the run.bat file.

If local have installed Conda before, skip line 1 in file run.bat and run
Else Run run.bat normally
### Suggested directory structure

The directory structure given by the template:

```
├── devdata
├── keywords
│   └── keywords.robot
├── libraries
│   └── MyLibrary.py
├── variables
│   └── variables.py
├── conda.yaml
├── robot.yaml
└── tasks.robot
```

where

- `devdata`: A place for all data/material related to development, e.g., test data. Do not put any sensitive data here!
- `keywords`: Robot Framework keyword files.
- `libraries`: Python library code.
- `variables`: Define your robot variables in a centralized place. Do not put any sensitive data here!
- `conda.yaml`: Environment configuration file.
- `robot.yaml`: Robot configuration file.
- `tasks.robot`: Robot Framework task suite - high-level process definition.

In addition to these, you can create your own directories (e.g. `bin`, `tmp`). Add these directories to the `PATH` or `PYTHONPATH` section of `robot.yaml` if necessary.

Logs and artifacts are stored in `output` by default - see `robot.yaml` for configuring this.

Learn how to [handle variables and secrets](https://robocorp.com/docs/development-guide/variables-and-secrets/secret-management).

### Configuration
Change the location of the calendar Excel file in FileCalendarLocation.txt

