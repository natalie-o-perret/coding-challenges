static int FindBasementPosition(string source)
{
    var floor = 0;
    for (var position = 0; position < source.Length; position++)
    {
        var character = source[position];
        
        if (character == '(')
            floor++;
        else if (character == ')')
            floor--;
        
        if (floor == -1)
            return position + 1; // 1-indexed
    }
    return 0;
}

// Test cases with assertions
System.Diagnostics.Debug.Assert(FindBasementPosition(")") == 1);
System.Diagnostics.Debug.Assert(FindBasementPosition("()())") == 5);

var scriptDir = Directory.GetCurrentDirectory();
var inputPath = Path.Combine(scriptDir, "..", "input.txt");
Console.WriteLine($"C#: {FindBasementPosition(File.ReadAllText(inputPath))}");
