// https://www.codewars.com/kata/5a5f9f80f5dc3f942b002309/train/csharp

using System;

namespace DotNet.Kyu6;

public class SchrodingerBoolean
{
    private static bool _omnibool = true;
    public static bool omnibool
    {
        get {
            var result = _omnibool;
            _omnibool = !_omnibool;
            return result;
        }
    }

    public static void Main() => Console.WriteLine($"{omnibool} -> {omnibool} -> {omnibool} -> {omnibool}");
}