# D0422_Workshop

```javascript
JSON.stringify() // Object -> JSON String
    > const jsonData = JSON.stringify(me)
    undefined
    > jsonData
    '{"name":"Jjas","phone number":"01054812452","appleProducts":{"ipad":true,"iphone":"X"}}'
    > typeof jsonData
    'string'
```



```javascript
const concat = (str1, str2) => {
    return `${str1}-${str2}`
} 

const checkLongStr = function(string){
    if (string.length>10){
        return true
    } else{
        return false
    }
}

if (checkLongStr(concat('Happy', 'Hacking'))){
    console.log('LONG STRING')
} else{
    console.log('SHORT STRING')
}

```



