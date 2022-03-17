# sunamp-serial
Basic script used to read out some values from Sunamp thermal batteries over serial connection and send them to emoncms

## Install
Recommended: Python 3.9 / 3.10 virtualenv 
```
pip install -r requirements.txt
```

## Example usage
```
python sunamp.py
```

## Example output
```
 # Gen 1
 FTBWZFSS: {"T1": "51.29", "T2": " 51.32", "T3": " 51.08", "T4": " 1.15", "T5": " 1.15", "relay1": " 0", "relay2": " 0", "serial_id": "FTBWZFSS"}
 # Gen 2
 FTBWZH3T:{"ts1": "57", "ts2": "57", "ts3": "56", "err": "0", "SOHT": "0", "ELCD": "1", "extD": "0", "soc": "1", "Charging": "1", "Heater_RLY": "1", "Pump_RLY": "0", "chg_Sig": "1", "link3": "0", "link4": "0", "serial_id": "FTBWZH3T"}
```
