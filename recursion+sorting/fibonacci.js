function fibonacci(num){
    let fib_array = [0, 1];

    for (let  i =0; i < num; i++) {
        fib_array.push(fib_array.at(-1)+fib_array.at(-2));
    }

    return fib_array;
}

function fibsrec(num) { //0, 1, 1, 2, 3, 5, 8, 13, 21
    if (num == 0){
        return 0;
    } else if (num == 1) {
        return 1;
    }

    return fibsrec(num-1) + fibsrec(num-2)
}

function mergesort(arr){
    let n = arr.length
    if (n <= 1){
        return arr
    }

    let arr1 = mergesort(arr.slice(0, Math.floor(n/2)))
    let arr2 = mergesort(arr.slice(Math.floor(n/2), n))

    return merge(arr1, arr2)
}

function merge(arr1, arr2){
    return_arr = []

    let i = 0;
    let j = 0 ;
    arr1.push(Number.POSITIVE_INFINITY);
    arr2.push(Number.POSITIVE_INFINITY);

    while (true) {
        if (arr1[i] < arr2[j]){
            return_arr.push(arr1[i]);
            i += 1;
        }
        else {
            return_arr.push(arr2[j])
            j += 1
        }

        if (arr1[i] == Number.POSITIVE_INFINITY && arr2[j] == Number.POSITIVE_INFINITY){
            break
        }
    }

    return return_arr
}

console.log(mergesort([42, 17, 93, 8, 56, 23, 77, 11, 65, 39, 88, 14, 99, 4, 50, 31, 72, 6, 81, 27]))

function mult35sumrec(num){
    sum = 0
    if (num == 1){
        return 0
    }
    if (num % 3 == 0 || num % 5 == 0){
        sum += num
    }

    return sum + mult35(num-1)
}

console.log(mult35sumrec(1000-1))