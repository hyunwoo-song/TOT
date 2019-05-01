// 반복 1 - while 
let i = 0
while (i < 10){
    console.log(i)
    i++
}

// 반복 2 - for 
for (let j=0; j <10 ; j++){
    console.log(j)
}

// 반복 3 - for of
for (let number of [1,2,3,4,5]){ // const로도 선언 가능
    console.log(number);
}


// Array(배열)
const numbers = [1,2,3,4]

console.log(numbers[0])
console.log(numbers[-1])


// numbers=[1,2,3,4]
// [ 1, 2, 3, 4 ]
// > numbers.reverse()
// [ 4, 3, 2, 1 ]
// > numbers.push('a') :가장 끝에 넣음
// 5 (numbers의 길이가 나옴)
// > numbers.pop()
// 1
// > numbers.unshift('v') : 왼쪽에 넣는다 
// 4
// > numbers.shift()
// 'v'
// > numbers.includes(1)
// false
// > numbers
// [ 4, 3, 2, 'a', 'a' ]
// > numbers.indexOf('a') : 왼쪽에서 부터 찾는다
// 3
// > numbers.indexOf('ㅊ') : 없는 값은 -1
// -1

// > numbers.join() : 기본으로 , 가 들어 가있다
// '4,3,2,a,a'
// > numbers.join('')
// '432aa'
// > numbers.slice(2,4)
// [ 2, 'a' ]
// numbers.filter(function(x){ return x>1 })
// [ 4, 3, 2 ]


// Object(파이썬에서 딕셔너리)
// > const me = {
//     ... name:'Jjas',
//     ... 'phone number':'01054812452',
//     ... appleProducts:{
//     ..... ipad: true,
//     ..... iphone:'X'
//     ..... }
//     ... }
//     undefined
//     > me.name
//     'Jjas'
//     > me.appleProducts.ipad
//     true

// JSON - JavaScript Object Notation(JS 객체 표기법)
JSON.stringify() // Object -> JSON String
    // > const jsonData = JSON.stringify(me)
    // undefined
    // > jsonData
    // '{"name":"Jjas","phone number":"01054812452","appleProducts":{"ipad":true,"iphone":"X"}}'
    // > typeof jsonData
    // 'string'

JSON.parse() // JSON String -> Object
    // > const parseDate = JSON.parse(jsonData)
    // undefined
    // > parseDate
    // { name: 'Jjas',
    //   'phone number': '01054812452',
    //   appleProducts: { ipad: true, iphone: 'X' } }
    // > typeof parseDate
    // 'object'

// 함수 
// 방법 1
function add(num1, num2){
    return num1 + num2
}
console.log('add: ' + add(1,2))

// 방법 2 - 표현식
const sub = function(num1, num2){
    return num1 - num2
}
console.log('sub:' + sub(5,3))

typeof add // function
typeof sub // function

// Arrow Function
// const mul = function (num1, num2){
//     return num1*num2
// }
// Arrow
const mul = (num1, num2) =>{
    return num1*num2
}

let square = (num) => {
    return num**2
}
// return문 단 한줄이면 {} & return 생략 가능
square = (num) => num**2

// () 안의 인자가 하나뿐이면 ()도 생략 가능
square = num => num **2

let noArgs = () => 'No args'

// object를 return 한다면? 괄호가 없으면 {}를 함수의 {}로 인식하기 때문에 ()가 필요!
let returnObject = () => { return {key:'value'}}
let returnObject = () => ({key:'value'})


// 함수의 기본 인자
const sayJjas = (name='noName') => `hiwe ${name}`

sayJjas('john')
sayJjas()

// 익명 함수
function (num) { return num**3 }
(num) => { return num ** 0.5 }

// 익명함수 즉시 호출
(function (num) {return num**3})(3) // 3의 세제곱근
