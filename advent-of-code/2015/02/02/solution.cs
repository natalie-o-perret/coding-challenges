using System.Diagnostics;

static int CalculateRibbon(string dimensions)
{
    var dims = dimensions.Split('x').Select(int.Parse).OrderBy(x => x).ToArray();
    
    // Smallest perimeter (using two smallest dimensions)
    var perimeter = 2 * (dims[0] + dims[1]);
    
    // Volume for bow
    var volume = dims[0] * dims[1] * dims[2];
    
    return perimeter + volume;
}

// Test cases with assertions
Debug.Assert(CalculateRibbon("2x3x4") == 34);
Debug.Assert(CalculateRibbon("1x1x10") == 14);

// Read input and calculate total
var scriptDir = Directory.GetCurrentDirectory();
var inputPath = Path.Combine(scriptDir, "..", "input.txt");
var total = File.ReadAllLines(inputPath)
                .Where(line => !string.IsNullOrWhiteSpace(line))
                .Sum(CalculateRibbon);

Console.WriteLine($"C#: {total}");
