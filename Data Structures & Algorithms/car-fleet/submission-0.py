class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_and_times = {}
        fleets = []
        for i in range(len(position)):
            car_and_times[position[i]] = (target - position[i]) / speed[i]

        position.sort(reverse=True)

        for car in position:
            if not fleets:
                fleets.append(car_and_times[car])
            elif car_and_times[car] > fleets[-1]:
                fleets.append(car_and_times[car])
        return len(fleets)

