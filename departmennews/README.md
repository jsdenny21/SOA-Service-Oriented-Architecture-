
# Department News Board:
1.  Regis 
2.  Login
3.  Upload
4.  Download
5.  News by Id
6. All News
7. Edit(Rename,Deleted)



### Request: Regis
![POST](https://badgen.net/badge/Method/POST/yellow)<span style="padding:10px">**/regis**</span>
````json
    {
        "Username":"name",
        "Password":"password"
    }
````
### Response:
#### Regis done!
![created](https://badgen.net/badge/created/201/green)
```json
nama password registered
```
#### Username Occupied!
![Not Found](https://badgen.net/badge/NotFound/404/red)
```json
username occupied
```
#### Regis Error!
![Not Found](https://badgen.net/badge/NotFound/404/red)
```json
Failed to registered
```


### Request: Login
![GET](https://badgen.net/badge/Method/GET/yellow)<span style="padding:10px">**/login**</span>
```json
    {
        "Username":"name",
        "Password":"password"
    }
```
### Response:
#### Success
![ok](https://badgen.net/badge/Method/OK/green)
```json
    {
        "Username":"name",
        "Password":"password"
    }
```
#### Already Login
![Not Found](https://badgen.net/badge/NotFound/404/red)
```json
already login
```
#### Username Not Found
![Not Found](https://badgen.net/badge/NotFound/404/red)
```json
already login
```

### Request: All news
![GET](https://badgen.net/badge/Method/GET/yellow)<span style="padding:10px">**/allnews**</span>
### Response:
#### Success
![ok](https://badgen.net/badge/Method/OK/green)
```json
    {
        "name news":"name",
        "status":0,
        "date":"2022-1-1"
    },
    {"..."},"..."
```


### Request: News by Id
![GET](https://badgen.net/badge/Method/GET/yellow)<span style="padding:10px">**/news/'<int:file_id>'**</span>
### Response:
#### Success
![ok](https://badgen.net/badge/Method/OK/green)
```json
    {
        "name news":"name",
        "status":0,
        "date":"2022-1-1"
    }
```
#### Id not found
![Not Found](https://badgen.net/badge/NotFound/404/red)
```json
    {
        "Messsage":"id not found"
    }
```


### Request: edit,deleted
![PUT](https://badgen.net/badge/Method/PUT/blue)<span style="padding:10px">**/(edit/deleted)/'<int:file_id>'**</span>
### Response:
#### Success edit or deleted
![ok](https://badgen.net/badge/Method/OK/green)
```json
    {
        "name news":"name",
        "status":1,
        "date":"2022-1-1"
    }
```
#### Not Login
![Not Found](https://badgen.net/badge/NotFound/404/red)
```json
MUST LOGIN
```
#### Not Found
![Not Found](https://badgen.net/badge/NotFound/404/red)
```json
    {
        "Error":"file not found!"
    }
```
#### Already deleted
![Not Found](https://badgen.net/badge/NotFound/404/red)
```json
    {
        "Error":"Already deleted"
    }
```
#### Already Archived
![Not Found](https://badgen.net/badge/NotFound/404/red)
```json
    {
        "Error":"Already archived"
    }
```


### Request: Upload
![GET](https://badgen.net/badge/Method/GET/yellow)<span style="padding:10px">**/file**</span>
```json
input->file
````

### Response:
#### Success 
![ok](https://badgen.net/badge/Method/OK/green)
```json
    success uploaded
```
#### Not Login
![Not Found](https://badgen.net/badge/NotFound/404/red)
```json
Must Login
```

### Request: Download
![GET](https://badgen.net/badge/Method/GET/yellow)<span style="padding:10px">**/download/'<int:id>'**</span>

### Response:
#### Success 
![ok](https://badgen.net/badge/Method/OK/green)
```json
output -> file
```

### Request: Logout
![GET](https://badgen.net/badge/Method/GET/yellow)<span style="padding:10px">**/logout'**</span>

### Response:
#### Success 
![ok](https://badgen.net/badge/Method/OK/green)
```json
logout success
```
#### Not Login
![Not Found](https://badgen.net/badge/NotFound/404/red)
```json
Not Login Yet

```