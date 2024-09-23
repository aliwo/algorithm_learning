def solution(diffs, times, limit):
    """
    https://school.programmers.co.kr/learn/courses/30/lessons/340212?language=python3
    
    diffs 의 중간값에서 탐색을 시작한다면...?
        -> 이 경우도 limit 이 말도안되게 높을 경우에는 한참을 내려가야 된다.

    중앙값을 limit / len(diffs) 의 시간 안에 풀 수 있는 level 에서 시작한다면?

    3456789012 / 4 = 864197253

    99995 를 864197253 안에 풀 수 있는 level 은?

    잠깐... 식에 "과거의 diff" 가 들어가고, 이 "과거의 diff" 는 랜덤하다. 이거 그냥 완전탐색 아닌가?


    (cur_time + prev_time) * cur_diff + cur_time 이 중간값인 애를 찾아야 되나...?



    """
    answer = 0
    return answer