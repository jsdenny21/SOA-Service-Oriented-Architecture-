# Simple Cloud Storage:
1.  Regis 
2.  Login
3.  Upload
4.  Download

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
### Request: Upload
![POST](https://badgen.net/badge/Method/GET/yellow)<span style="padding:10px">**/file**</span>
```json
input ->file
```
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
#### Not Login
![Not Found](https://badgen.net/badge/NotFound/404/red)
```json
Must Login
```
#### Not owner file
![Not Found](https://badgen.net/badge/NotFound/404/red)
```json
{
    "status":"not",
    "Messsage":"USER NOT SAME"
}
```
#### File not found
![Not Found](https://badgen.net/badge/NotFound/404/red)
```json
{
    "status":"not",
    "Messsage":"id not found"
}
```