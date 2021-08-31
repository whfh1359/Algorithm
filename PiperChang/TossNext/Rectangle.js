function solution(v) {
    var answer = [
        []
    ];
    
    if (v[0][0] == v [1][0]){
        answer[0][0] =v[2][0]
    }
    else if (v[1][0] == v[2][0]) {
        answer[0][0] =v[0][0]        
    }
    else {
        answer[0][0] =v[1][0]                
    }
    
    if (v[0][1] == v [1][1]){
        answer[0][1] =v[2][1]
    }
    else if (v[1][1] == v[2][1]){
        answer[0][1] =v[0][1]        
    }
    else {
        answer[0][1] =v[1][1]                
    }

    return answer[0];
} // 쉬운 문제