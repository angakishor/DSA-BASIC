function sumtwosorted(arr,target){
    let left=0,right= arr.length - 1;
    while(left<right){
        let sum=arr[left]+arr[right];
        
        if(sum===target) return [arr[left],arr[right]];
        else if(sum<target) left++;
        else right--;
    }
    return [];
}
console.log(sumtwosorted([1,2,3,4,6],6));
