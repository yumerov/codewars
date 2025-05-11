// https://www.codewars.com/kata/56efc695740d30f963000557/train/csharp

namespace DotNet.Kyu8;

using System;
using System.Linq;

public static class StringExt
{
    public static string ToAlternatingCase (this string s) => string
        .Concat(s.ToCharArray().Select(c => Char.IsLower(c) ? Char.ToUpper(c) : Char.ToLower(c)).ToArray());

    public static void Main() => Console.WriteLine("aBcD 1 2 _".ToAlternatingCase());
}