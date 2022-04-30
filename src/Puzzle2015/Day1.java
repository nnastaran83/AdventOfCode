package Puzzle2015;

public class Day1 {

    /**
     *Day1:part1: get a string as input that represents directions '(' goes up and ')' goes down
     * @param input A string that represents directions
     * @return the floor number at the end of direction
     */
    public long part1(String input){
        return input.chars().filter(c ->c == '(').count() - input.chars().filter(c -> c == ')').count();

    }

    /**
     * Day1:part2
     * @param input A string that represents directions
     * @return the first characters position start from 1 that takes us to floor -1
     */
    public long part2(String input){
        long floor = 0;
        int i = 0;
        while(floor != -1){
           floor = input.charAt(i) == '(' ? floor+1 : floor-1;
            i++;
        }
        return i;
    }
}
