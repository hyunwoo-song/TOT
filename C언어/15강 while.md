### 15강 while

```c
// 반복문 (while)
#include <stdio.h>

int main() {
	int i = 1;

	while (i <= 10) {
		printf("%d\n", i);
		i++;
	}
}
```

```c
// do-while

#include<stdio.h>

int main(){
	int i = 18;

	do {
		printf("%d\n", i);
		i++;
	} while (i <= 10);
}
```

```c
// 무한 반복(while)

#include <stdio.h>

int main() {
	int i = 1;

	while (true) {
		printf("%d", i);
		i++;
	}
}
```

```c
#include <stdio.h>

int main() {
	int n;
	
	do {
		printf("제발 0을 입력해 주세여 !!\n");
		scanf_s("%d", &n);
	} while (n != 0);
	printf("드디어 0이 나왔군요\n");
}
```



### 16강 for 문

```c
#include <stdio.h>

int main() {
	int i ;

	i = 1;
	while (i <= 10) {
		printf("%d\n", i);
		i++;
	}
	for (i = 1; i <= 10; i++) {
		printf("%d\n", i);
	}
	// 일정하게 증가 or 감소 되는 변수가 필요할 때
	// 배열의 모든 원소에 접근하고 싶을 때 
	// 특정 횟수만큼 작업을 반복하고 싶을 때
}
```

```c
#include <stdio.h>

int main() {
	// 1, 2, 4, 8, 16, 32, 64

	int n;
	scanf_s("%d", &n);

	for (int i = 1; i <= n; i *= 2) {
		printf("%d\n", i);
	// 여기서의 i는 for문 안에서만 사용 가능
	}
}
```

```c
#include <stdio.h>
int main() {
	// 1~n까지 숫자의 합을 출력
	int n;
	scanf_s("%d", &n);
	int sum = 0;
	for (int i = 1; i <= n; i++) {
		sum += i;
	}
	printf("%d\n", sum);
}
```

```c
#include<stdio.h>
int main() {
	int n;
	scanf_s("%d", &n);

	for (int i = 1; i <= n; i++) {
		printf("*");
	}
	printf("\n");
}
```

