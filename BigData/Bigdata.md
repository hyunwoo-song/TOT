# 빅데이터

### 데이터 마이닝

#### Clustering

* Data를 유사도에 의해서 K개의 그룹으로 나누는 것
* 추천 시스템을 위해서 사용

##### What is Clustering

​	Ex) (1, 1) (1, 2) (2, 1) (5, 5) (5, 6) (6, 5) (7, 7)

​	N 개가 있을 때 2^N 개 가 나온다 (엄청 많다)

​	Clustering이 잘 된지 판단 하기 위해 여러가지 measure?를 사용한다.



#### K-Means Clustering

​	K 개의 평균점

 * 단점

   	* Size가 크거나 작으면 잘 못찾는다
   	* 평균점으로 부터 공처럼 생겨야 잘 찾는다
   	* Outlier가 있으면 정확한 측정 불가

   K-Medoids: 실제로 있는 포인트를 평균점이나 Center로 사용 하겠다.



#### Hierarchical Clustering

​	모든 포인트가 독립적이다(포인트 하나하나가 클러스트). 모든 점에 대해서 젤 가까운점 두개를 merge 해서 하나의 클러스터로 하고 K개가 될 때까지 수행 (Bottom Up 방식) 

* Single-link : 가장 가까운것
* Complete-ling : 가장 먼것
* Average-link : 
* Mean-link
* Centroid-link : 클러스트 마다 평균점을 계산해서 사용



#### DBSCAN Clustering(Density-Based)

* 2가지 파라미터
  * Eps
  * MinPts
* Neps(p)
* Core Point
* Directly density-reachable
  * Density-reachable
  * Density-connected
* Outlier



#### EM Clustering

* Generative model (생성 모델)

  * Probabilistic Modelig

  * (빨 빨 빨 빨) x2 (파 빨 빨 빨)x1

  * 여기서 나온 결과를 바탕으로 모델을 찾아나감

  * Likelihood

    * Red ball:(2/3)*1+(1/3)(3/4) = 11/12
    * Blue ball: (2/3)*0 + (1/3)(1/4) = 1/12
    * Total probability of having the observable data: (11/12)^8 * (1/12) = (11^8)/(12^9)

    Likelihood가 제일 높은 것을 선택 하겠다.

    Likelihood를 미분해서 0 최대값을 찾는다. 

* E -step 에서는 point가 어느 클러스터에서 나왔는지

* M-step 에서는 클러스터의 비중, 평균, 표준편차 (센트로이드를 구하는 과정)

* 결과적으론 Likelihood를 구하기 위함이다. 

#### PLSI







