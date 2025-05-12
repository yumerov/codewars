// https://www.codewars.com/kata/did-she-say-hallo/train/csharp

namespace DotNet.Kyu8;

using System.Linq;

public class DidSayHello
{

    public static bool Validate_hello(string greetings)
    {
        string[] greetingList = ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"];
        return greetingList.Any(greeting => greetings.ToLower().Contains(greeting));
    }

}