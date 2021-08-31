// directory parsing해서, 
// forEach 문으로, dir찾아들어가기. 
// map 은 객체이기 때문에, map[key(dir 이름)]으로 다음 레벨의 객체로 접근이 가능하다.
function solution(map, directory) {
    const path = directory.split('/')    
    console.log(path)
    
    var a = map
    path.forEach(v => {
        a= a[v]
    });

       console.log(a)

    return a
}
//     for(var key in map) {
//         if (key == directory){
//             console.log(map[key])
//             return (map[key])
//         }//잘했음. 근데, 
//         else if(Array.isArray(map[key])!=true){
// //            console.log(map[key])
//             solution(map[key],directory)
        // }
    // }
// }

