// https://www.codewars.com/kata/514a677421607afc99000002/train/csharp

using System.Linq;

namespace DotNet.Kyu7;

public class Person(string name = "John", int age = 21)
{
    public int Age = age;
    public string Name = name;
}

public class FixGetNames
{
    public static string[] GetNames(Person[] data) => data.Select(person => person.Name).ToArray();
}