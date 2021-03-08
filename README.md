# PyReadings

Allows you to send your electricity readings to former EDP Distribuição, now E-Redes. This program is specially useful if you have multiple people or homes whose readings you send out. It will keep the necessary data to submit the readings (CPE and NIF) and also the last given reading as well as the date of when it was given. It has language support for English and Portuguese

## Getting it up and Running

### Prerequisites

A standalone version for 64 bit Linux and Windows is made available in the Releases section of the repository, if you do not want to install python3 and the required library on your machine.

You will need Python3 and the pyautogui installed to use this.

To install pyautogui on Python3 open a terminal and type:
```
pip3 install pyautogui
```

## Running it

### For Windows:
In the standalone version in Windows all you have to do is double click the downloaded .exe file,

### For Linux:
For the standalone Linux version you will have to use a terminal to navigate the directory where the file was saved and then ./readings

### For the non-standalone version (Should be OS independent):
``` 
python3 ./readings.py
```

## What can it do?

* Keep all the necessary data needed to communicate energy readings for multiple energy contracts
* List all the registered contracts
* Delete registered contracts
* Show the last registered reading and date for each contract
* Send readings to the electricity distribuitor (E-REDES) independently of whoever is your electricity supplier

## Authors

* **Diogo Paulico** - *Initial work*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
