function solution(bridge_length, weight, truck_weights) {
    let time = 0;
    let nowSum = 0;
    let nowLength = 0;
    const brige = Array(bridge_length).fill(0);
    while(truck_weights.length || nowLength){
        time += 1;
        const outTruck = brige.shift();
        nowSum -= outTruck;
        if(outTruck) {
            nowLength -= 1;
        }
        if(nowSum + truck_weights[0] <= weight && nowLength + 1 <= bridge_length){
            const truckWeight = truck_weights.shift();
            brige.push(truckWeight);
            nowSum += truckWeight;
            nowLength += 1
            continue
        }
        brige.push(0);
    }
    
    
    return time;
}