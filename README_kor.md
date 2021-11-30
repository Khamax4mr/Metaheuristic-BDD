# 메타휴리스틱 모델 검증

## 목표

모델 검증의 상태 폭발 문제의 해결 방법으로 메타휴리스틱을 적용해서 모델에서 속성을 위반하는 조합을 좀 더 효율적으로 찾아본다.

- [ ] 모델 구조 만들기.
- [ ] 메타 휴리스틱 적용하기.
- [ ] 예제 탐색 및 변환.


## 함수 디자인

* **Initialisation**
모델을 한번 실행하는 동안 일어난 전이 Element를 가지는 전이 리스트 Individual을 생성한다. Individual은 다양한 크기를 가지나 최대 크기는 지정한 값으로 제한된다.

* **Stopping criteria**
일정 횟수만큼 진전이 없을 경우 중단한다.

* **Fitness**
정상적인 모델에서 전이가 불가능한 Individual은 제외한다. (모델 검증 결과는 대부분 부울 형식을 가지므로 좀 더 좋은 방법이 있는지 생각해볼 것!)

* **Selection**
부모가 될 Individual은 Stochastic처럼 다양한 표본을 후보로 고를 수 있는 알고리즘으로 고른다.

* **Crossover**
부모로 고른 Individual에 대하여 같은 상태를 가진 Element를 고르고 교차하여 새로운 Individual을 만든다. 단 최대 크기를 넘지 않아야 한다.

* **Mutation**
선택한 Element의 상태가 가질 수 있는 전이로 변이하고 그 이후는 랜덤하게 유효한 Element를 선택하여 새로운 Individual을 만든다.