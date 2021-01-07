# Overview 

Adapted from:

* [yoavram/client.py](https://gist.github.com/yoavram/4351498)
* [Flask file uploads](https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/)

## Usage 

```bash
test=/tmp/upload.txt
echo "upload $(date)" >> ${test}

curl -X POST -F "file=@${test}" localhost:5000
```