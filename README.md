# Rest Api Server

## Create Virtual Environment

```shell
python3 -m venv venv
```

## Activate Virtual Environment

```shell
source ./venv/bin/activate
```

## Install Local Module

```shell
pip install -e .
```

## Run Flask App :rocket:

```shell
python run.py
```

## Access the App via API
API base url: `http://localhost:5000/api/v1`

### Endpoints

* `/store-file` (method `POST`)
  Input: `filename`, `file`
  
  Output:
  ```json
  {
	"filename": "test.txt",
	"message": "File successfully stored"
  }
  ```
  
* `/retrieve-histogram` (method `GET`)
  Input params: `filename`, `text`
  
  Output:
  ```json
  {
	"filename": "test.txt",
    "message": "Histogram successfully retrieved",
    "occurences": 2,
    "text": "xxx"
  }
  ```

* `/replace-text` (method `POST`)
  Input: `filename`, `text`, `replacement`
  
  Output:
  ```json
  {
	"filename": "test.txt",
    "message": "Text successfully replaced",
    "replacedOccurences": 2,
	"replacement": "yyy",
    "text": "xxx"
  }
  ```

* `/delete-file` (method `POST`)
  Input: `filename`
  
  Output:
  ```json
  {
	"filename": "test.txt",
    "message": "File successfully deleted",
  }
  ```

### Examples
```
curl -i -X POST -F "filename=test.txt" -F "file=@test.txt" 'localhost:5000/api/v1/store-file'
```

```
curl -i -X GET 'localhost:5000/api/v1/retrieve-histogram?filename=test.txt&text=xxx'
```

```
curl -i -X POST -F "filename=test.txt" -F "text=xxx" -F "replacement=yyy" 'localhost:5000/api/v1/replace-text'
```

```
curl -i -X POST -F "filename=test.txt" 'localhost:5000/api/v1/delete-file'
```

### Testing

```
pytest
```
