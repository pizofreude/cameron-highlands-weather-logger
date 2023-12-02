# Cameron Highlands Weather Logger

This is a Python project that logs the weather data in Cameron Highlands, Tanah Rata, Pahang, Malaysia every six hours daily. The project uses the [Talk Python Weather API](https://weather.talkpython.fm/) to get the current temperature and saves it to a status.log file.

## Requirements

- Python 3.8 or higher
- requests library
- logging library
- CHWL_SECRET environment variable

## Usage

To run the project, you need to set the CHWL_SECRET environment variable to Cameron Highland Weather Logger repository. You can set it from:
 - Repository settings
 - Under **Security**
 - Under **Secrets and Variable**
 - Under **Actions** and create **New Repository Secret**
 - Create **CHWL_SECRET** and enter your own arbitrarily chosen token value


Then, you can run the main.py file as follows:

```python
python main.py
```

The project will log the current temperature in Cameron Highlands to the status.log file, along with the date, time, and level of the message. The status.log file will rotate when it reaches 1 MB in size, and keep one backup file.

## Example Output

Here is an example of the output in the status.log file:

```
2023-12-02 22:41:41,123 - __main__ - INFO - Token value: 1234567890
2023-12-02 22:41:42,456 - __main__ - INFO - Weather in Cameron Highlands: 18
```

## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](https://github.com/pizofreude/cameron-highlands-weather-logger/blob/master/LICENSE) file for details.