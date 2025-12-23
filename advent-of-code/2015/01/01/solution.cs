using System.Diagnostics;

static int CalculateFloor(string source)
{
    return source.Aggregate(0, (floor, character) => character switch
    {
        '(' => floor + 1,
        ')' => floor - 1,
        _ => floor
    });
}

// Test cases with assertions
Debug.Assert(CalculateFloor("(())") == 0);
Debug.Assert(CalculateFloor("()()") == 0);
Debug.Assert(CalculateFloor("(((") == 3);
Debug.Assert(CalculateFloor("(()(()(") == 3);
Debug.Assert(CalculateFloor("))(((((") == 3);
Debug.Assert(CalculateFloor("())") == -1);
Debug.Assert(CalculateFloor("))(") == -1);
Debug.Assert(CalculateFloor(")))") == -3);
Debug.Assert(CalculateFloor(")())())") == -3);


var scriptDir = Directory.GetCurrentDirectory();
var inputPath = Path.Combine(scriptDir, "..", "input.txt");
Console.WriteLine($"C#: {CalculateFloor(File.ReadAllText(inputPath))}");
