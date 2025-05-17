// https://www.codewars.com/kata/number-of-people-in-the-bus/train/csharp

namespace DotNet.Kyu7;

public class NumberOfPeopleInBus
{
    public static int Number(List<int[]> peopleListInOut) => peopleListInOut.Select(people => people[0] - people[1]).Sum();
}