```javascript
// get 방식

response = http.getUrl('http:....', {format:"json", cacheTime: 0, returnHeaders:true});

// error 처리
if(response.status == 404){
      throw fail.checkedError("No Result", "NoResult");  
    }
```



```javascript
// post 방식
var headers = {
  
}
var body = {
  
}
var data = http.postUrl("https://....", body, headers);
```

