### Endpoints 개요

##### Endpoints란?

모델링한 Action과 Business Logic을 연결해주는 역할

Bixby Language로 구현

##### Endpoints의 종류

- Local Endpoint
- Remote Endpoint


### Endpoints 종류

##### Loacl Endpoint 

ex) "수원 날씨 알려줘" 

캡슐 내부의 리소스나 코드 사용

```
endpoints {
  // action과 그에 맞는 자바스크립트를 매핑
  action-endpoints {
  // 연결하고자 하는 Action 파일 명
    action-endpoint (ArithmeticOperation) {
    // 연산 수행에 필요한 Input 리스트
      accepted-inputs (leftOperand, rightOperand, operator)
      // 연결하고자 하는 JavaScript 파일명
      local-endpoint (arithmeticOperation.js)
    }
  }
}
```





##### Remote Endpoint

ex) "아침 뉴스 보여줘"

직접 Api를 호출해서 사용



### Bixby Capsule로 외부 서버 연동하기

##### Remote Endpoint

직접 외부서버를 호출, 비지니스 로직 필요는 없지만 API를 호출해서 받아올 수 있는 Oupconcept은 필요 

##### JavaScript HTTP

 