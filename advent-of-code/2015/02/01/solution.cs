int CalculateWrappingPaper(string dimensions)
{
    var parts = dimensions.Split('x').Select(int.Parse).ToArray();
    var l = parts[0];
    var w = parts[1];
    var h = parts[2];
    
    // Calculate surface area
    var surfaceArea = 2*l*w + 2*w*h + 2*h*l;
    
    // Find smallest side
    var sides = new[] { l*w, w*h, h*l };
    var slack = sides.Min();
    
    return surfaceArea + slack;
}

// Test cases with assertions
System.Diagnostics.Debug.Assert(CalculateWrappingPaper("2x3x4") == 58);
System.Diagnostics.Debug.Assert(CalculateWrappingPaper("1x1x10") == 43);

// Read input and calculate total
var scriptDir = Directory.GetCurrentDirectory();
var inputPath = Path.Combine(scriptDir, "..", "input.txt");
var total = File.ReadAllLines(inputPath)
                .Where(line => !string.IsNullOrWhiteSpace(line))
                .Sum(CalculateWrappingPaper);

Console.WriteLine($"C#: {total}");
