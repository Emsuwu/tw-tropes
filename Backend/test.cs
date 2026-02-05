using System;

class Program 
{
    static void Main(string[] args)
    {
        Console.WriteLine(Silly.GetWhatAmI());
        
        Silly silly = new Silly();
        Console.WriteLine(silly.GetWhatAmINotStatic());
    }
}

public class Silly
{
    public static string WhatAmI = "frog";

    public string GetWhatAmINotStatic(){
        return WhatAmI;
    }

    public static string GetWhatAmI()
    {
        return WhatAmI;
    }
}