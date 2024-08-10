# salatsync
SalatSync is a simple yet powerful script that generates .ics (iCalendar) files for Islamic prayer times. With PrayCal, you can easily integrate daily prayer times into your digital calendar, ensuring you never miss a prayer.

## Table of content
- [Motivation](#motivation)
- [Development](#development)
- [Installation & Usage](#installation--usage)
    - [Installation](#installation)
    - [Usage](#usage)
- [Contributing](#contributing)
- [History](#history)
- [Credits](#credits)
- [License](#license)

## Motivation
The motivation behind this project stemmed from a desire to streamline daily routines by having everything in one place—Google Calendar. Instead of relying on multiple apps or manual tracking for prayer times, I wanted a seamless integration that would automatically add prayer times to my existing calendar. This ensures that I never miss a prayer, while also keeping my schedule organized and consolidated in a single, convenient location.

## Development
### First time
1. Fire up a github codespace.
2. python -m pip install --user virtualenv
3. virtualenv .venv
4. source .venv/bin/activate
5. ctrl+shift+p in vscode python select intrepreter and point it to python3 in .venv/bin/

### Regular development
1. Fire up a github codespace.
2. source .venv/bin/activate

### Useful commands
- Update requirements.txt: pip freeze > requirements.txt


## Installation & Usage

### Installation
1. Download the script

### Usage
1. Update the location and timezone in the script in your favorite text editor.
2. Run the scipt via
```
python salatsync.py
```

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -m 'Added some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History
10/08/24: Project created.  

## Credits
TODO: Write credits as below and delete this line
- Created by <a href="https://iamzain.com">Zain Khan</a>.
- Template for this README is <a href="https://github.com/gitzain/template-README">template-readme</a> created by <a href="https://iamzain.com">Zain Khan</a>.

## License
See the LICENSE file in this project's directory.
